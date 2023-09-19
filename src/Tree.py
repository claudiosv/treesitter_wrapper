from tree_sitter import Tree as TsTree, TreeCursor
from NodeFactory import NodeFactory

class Range:
    @property
    def start_byte(self) -> int: ...
    @property
    def end_byte(self) -> int: ...
    @property
    def start_point(self) -> tuple[int, int]: ...
    @property
    def end_point(self) -> tuple[int, int]: ...


class Tree:
    def __init__(self, _tree: TsTree):
        self._tree = _tree
        self.root_node = NodeFactory.get_node(_tree.root_node)

    # @property
    # def root_node(self) -> Node:
    #     return self.root_node

    # @property
    # def text(self) -> bytes | Any:  # technically ReadableBuffer | Any
    #     return self._tree.text

    def edit(
        self,
        start_byte: int,
        old_end_byte: int,
        new_end_byte: int,
        start_point: tuple[int, int],
        old_end_point: tuple[int, int],
        new_end_point: tuple[int, int],
    ) -> None:
        return self._tree.edit(
            start_byte,
            old_end_byte,
            new_end_byte,
            start_point,
            old_end_point,
            new_end_point,
        )

    def get_changed_ranges(self, new_tree: TsTree) -> list[Range]:
        return self._tree.get_changed_ranges(new_tree)

    def walk(self) -> TreeCursor:
        return self._tree.walk()