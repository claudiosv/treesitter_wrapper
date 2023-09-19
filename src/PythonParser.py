from pathlib import Path
import Tree


from tree_sitter import Language, Parser
from tree_sitter_languages import get_language, get_parser


class PythonParser:
   def __init__(self, source: str | bytes) -> None:
      self.language: Language = get_language("python")
      self.parser: Parser = get_parser("python")
      self.source = source.decode("utf8") if isinstance(source, bytes) else source
      self._source = bytes(source, "utf8") if isinstance(source, str) else source
      self.tree = Tree.Tree(self.parser.parse(self._source))
      self.root_node = self.tree.root_node

if __name__ == "__main__":
   print(PythonParser(Path(__file__).read_text()))