
from collections import defaultdict
import numpy as np
import torch

# Load model directly
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.PythonParser import PythonParser


def to_tokens_and_logprobs(model, tokenizer, input_texts):
    input_ids = tokenizer(
        [tokenizer.bos_token + i for i in input_texts],
        padding=True,
        return_tensors="pt",
    ).input_ids
    outputs = model(input_ids)
    probs = torch.log_softmax(outputs.logits, dim=-1).detach()

    # collect the probability of the generated token -- probability at index 0 corresponds to the token at index 1
    probs = probs[:, :-1, :]
    input_ids = input_ids[:, 1:]
    gen_probs = torch.gather(probs, 2, input_ids[:, :, None]).squeeze(-1)

    batch = []
    for input_sentence, input_probs in zip(input_ids, gen_probs, strict=True):
        text_sequence = []
        for token, p in zip(input_sentence, input_probs, strict=True):
            if token not in tokenizer.all_special_ids:
                text_sequence.append((tokenizer.decode(token), p.item()))
        batch.append(text_sequence)

    return batch


def test_nll():
    # nll = GPT2PPL("mps", "microsoft/CodeGPT-small-py")
    sentence = """def xmlstring(self, pretty_print=False):
    \"\"\"
    Serialises this FoLiA element and all its contents to XML.

    Returns:
        str: a string with XML representation for this element and all its children
    \"\"\"
    s = ElementTree.tostring(
        self.xml(),
        xml_declaration=False,
        pretty_print=pretty_print,
        encoding="utf-8",
    )
    if sys.version < "3":
        if isinstance(s, str):
            s = unicode(s, "utf-8")
        else:
            if isinstance(s, bytes):
                s = str(s, "utf-8")
                s = s.replace("ns0:", "")
                s = s.replace(":ns0", "")
    return s"""
    # ppl = nll.getPPL(sentence)
    # print(ppl)
    # encoding, nll = nll.getLL(sentence)
    # assert ppl
    parser = PythonParser(sentence)
    tokenizer = AutoTokenizer.from_pretrained(
        "microsoft/CodeGPT-small-py", padding_side="left",
    )
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained("microsoft/CodeGPT-small-py")
    model.config.pad_token_id = model.config.eos_token_id

    input_texts = [sentence]

    batch = to_tokens_and_logprobs(model, tokenizer, input_texts)

    from rich.color import Color
    from rich.console import Console
    from rich.style import Style
    from rich.syntax import Syntax

    console = Console()
    console.print("")
    syntax = Syntax(sentence, "python")
    # pprint(batch)
    color_map = defaultdict(lambda: defaultdict())
    for item in batch:
        line_no = 1
        col_no = 0

        for tok, score in item:
            lines = tok.count('\n')
            last_line_len = tok.rfind('\n')
            last_line_len = len(tok) - last_line_len - 1 if last_line_len != -1 else len(tok)

            color = Color.from_rgb(int(np.exp(score) * 255), 0, 0)
            style = Style.from_color(bgcolor=color)

            end_line = line_no + lines
            end_col = last_line_len if lines else col_no + len(tok)

            syntax.stylize_range(style=style, start=(line_no, col_no), end=(end_line, end_col))

            # Update line and column numbers
            if lines:
                line_no += lines
                col_no = last_line_len  # 1 for the space after the token
            else:
                col_no += len(tok)  # 1 for the space after the token
        # curr_i = 0
        # line_no = 1
        # col_no = 0
        # for tok, score in item:
        #     print(f"| {tok:8s} | {score:.3f} | {np.exp(score):.2%}")
        #     lines = str(tok).count("\n")
        #     color = Color.from_rgb(np.exp(score)*255, 0, 0)
        #     style = Style.from_color(bgcolor=color)
        #     end = (line_no + lines, col_no + len(tok))
        #     syntax.stylize_range(style=style, start=(line_no, col_no), end=end)
        #     col_no += len(tok)
        #     line_no += lines

    console.print(syntax)
