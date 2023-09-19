from collections import OrderedDict
import json
from pathlib import Path
import re

REG = r"(.*?)_([a-zA-Z])"

def camel(match):
    res: str = (match.group(1) + match.group(2).upper())
    return res.capitalize()

def camel_upper(match: re.Match):
    first_match = ""
    if len(match.group(1)) > 0:
        first_match = match.group(1)
    group_2 = match.group(2).upper()
    res = (first_match + group_2)
    if match.pos == 0:
        res[0] = res[0].capitalize()
    # res = res.capitalize()
    return res

def pep_name(name: str):
    # return re.sub(REG, camel_upper, name, 0)
    match name:
        case "false":
            return "FalseT"
        case "_":
            return "Underscore"
        case "true":
            return "TrueT"
        case "none":
            return "NoneT"
        case "list":
            return "ListT"

    clean_name = ''.join(word.title() for word in name.replace(" ", "_").split('_'))
    internal_class = name.startswith("_")
    if internal_class:
        return "_"+clean_name
    return clean_name

if __name__ == "__main__":
    assert pep_name("list_splat_pattern") == "ListSplatPattern"
    node_types_str = Path("src/node-types.json").read_text()
    node_types: list[dict] = json.loads(node_types_str)
    print(node_types[0])
    python_classes = "from Node import Node\nfrom typing import List, Union"
    visited_types = []
    type_representations = OrderedDict()
    # class name
    # named
    # type
    # parents
    type_representations["Type"] = {
        "name": "Type",
        "named": False,
        "type": None,
        "parents": None,
    }
    for type_ in node_types:
        parent_type_name = pep_name(type_['type'])
        if not parent_type_name.isidentifier():# or parent_type_name in visited_types:
            # if parent_type_name not in visited_types:
                # python_classes += f"\n# TODO: {parent_type_name}"
            continue
        visited_types.append(parent_type_name)
        if parent_type_name not in type_representations:
            type_representations[parent_type_name] = {
            "name": parent_type_name,
            "named": type_['named'],
            "type": type_['type'],
            "parents": [],

                }
            if "children" in type_:
                type_representations[parent_type_name]["children"] = [ pep_name(x["type"]) for x in type_["children"]["types"] ]
        if "subtypes" not in type_:
            continue
        for subtype in type_["subtypes"]:
            subtype_pep = f"{pep_name(subtype['type'])}"
            if not subtype_pep.isidentifier():
                continue
            if subtype_pep in type_representations:
                type_representations[subtype_pep]["parents"].append(parent_type_name)
                if type_representations[subtype_pep]["named"] != subtype["named"]:
                    print("WOW!", subtype_pep)
            else:
                type_representations[subtype_pep] = {
                    "name": subtype_pep,
                    "named": subtype['named'],
                    "type": subtype['type'],
                    "parents": [parent_type_name],
                }
            visited_types.append(subtype_pep)

    def sorter(t):
        if t[1]["parents"] is None:
            return 0
        else:
            return len(t[1]["parents"])
    type_representations = OrderedDict(sorted(type_representations.items(), key=sorter))

    for type_, values in type_representations.items():
        parent_type_name = type_
        if values["parents"] is None:
            parents = ""
        elif values["parents"] == []:
            parents = "Type"
        else:
            parents = ", ".join(values["parents"])
        child_types = ""
        if "children" in values:
            quoted_children = [ '"' + x + '"' for x in values["children"]]
            child_types = ", ".join(quoted_children)
            if len(quoted_children) > 1:
                child_types = "Union["+child_types+"]"
        python_classes += f"\n\nclass {parent_type_name}({parents}):"
        python_classes += f"\n    named: bool = {values['named']}"
        python_classes += f"\n    _type: str = \"{values['type']}\""
        if "children" in values:
            python_classes += f"\n    children: list[{child_types}]"
        print(f"case \"{values['type']}\":\n    return {type_}")
    Path("src/python_types1.py").write_text(python_classes)
