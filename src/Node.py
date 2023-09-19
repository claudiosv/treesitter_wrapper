from tree_sitter import Node as TsNode, TreeCursor
from typing import Self, Any

import NodeFactory

class Node:
    start_byte: int
    start_point: tuple[int, int]
    end_byte: int
    end_point: tuple[int, int]
    has_changes: bool
    has_error: bool
    id: int
    is_missing: bool
    is_named: bool
    child_count: int
    named_child_count: bool
    children: list[Self]
    named_children: list[Self]
    next_named_sibling: Self | None
    next_sibling: Self | None
    parent: Self | None
    prev_named_sibling: Self | None
    prev_sibling: Self | None
    text: bytes | Any
    type: str

    def __init__(self, _node: TsNode):
        self._node = _node
        self.start_byte = _node.start_byte
        self.start_point = _node.start_point
        self.end_byte = _node.end_byte
        self.end_point = _node.end_point
        self.has_changes = _node.has_changes
        self.has_error = _node.has_error
        self.id = _node.id
        self.is_missing = _node.is_missing
        self.is_named = _node.is_named
        self.child_count = _node.child_count
        self.named_child_count = _node.named_child_count
        self.children = [ NodeFactory.NodeFactory.get_node(child) for child in _node.children ]
        self.named_children = [ NodeFactory.NodeFactory.get_node(child) for child in _node.named_children ]
        self.next_named_sibling = _node.next_named_sibling
        self.next_sibling = _node.next_sibling
        self.parent = _node.parent
        self.prev_named_sibling = _node.prev_named_sibling
        self.prev_sibling = _node.prev_sibling
        self.text = _node.text
        self.type = _node.type

    # @property
    # def start_byte(self) -> int:
    #     return self.start_byte

    # @property
    # def start_point(self) -> tuple[int, int]:
    #     return self.start_point

    # @property
    # def end_byte(self) -> int:
    #     return self.end_byte

    # @property
    # def end_point(self) -> tuple[int, int]:
    #     return self.end_point

    # @property
    # def has_changes(self) -> bool:
    #     return self.has_changes

    # @property
    # def has_error(self) -> bool:
    #     return self.has_error

    # @property
    # def id(self) -> int:
    #     return self.id

    # @property
    # def is_missing(self) -> bool:
    #     return self.is_missing

    # @property
    # def is_named(self) -> bool:
    #     return self.is_named

    # @property
    # def child_count(self) -> int:
    #     return self.child_count

    # @property
    # def named_child_count(self) -> bool:
    #     return self.named_child_count

    # @property
    # def children(self) -> list[Self]:
    #     return self.children

    # @property
    # def named_children(self) -> list[Self]:
    #     return self.named_children

    # @property
    # def next_named_sibling(self) -> Self | None:
    #     return self.next_named_sibling

    # @property
    # def next_sibling(self) -> Self | None:
    #     return self.next_sibling

    # @property
    # def parent(self) -> Self | None:
    #     return self.parent

    # @property
    # def prev_named_sibling(self) -> Self | None:
    #     return self.prev_named_sibling

    # @property
    # def prev_sibling(self) -> Self | None:
    #     return self.prev_sibling

    # @property
    # def text(self) -> bytes | Any:
    #     self.text  # can be None, but annoying to check

    # @property
    # def type(self) -> str:
    #     return self.type

    def children_by_field_name(self, name: str) -> list[Self]:
        return self._node.child_by_field_name(name)

    def children_by_field_id(self, __id: int) -> list[Self]:
        return self._node.children_by_field_id(__id)

    def field_name_for_child(self, __child_index: int) -> str:
        return self._node.field_name_for_child(__child_index)

    def child_by_field_id(self, __id: int) -> Self | None:
        return self._node.child_by_field_id(__id)

    def child_by_field_name(self, __name: str) -> Self | None:
        return self._node.child_by_field_name(__name)

    def sexp(self) -> str:
        return self._node.sexp()

    def walk(self) -> TreeCursor:
        return self._node.walk()

    def __eq__(self, other: object) -> bool:
        return self._node.__eq__()

    def __ne__(self, other: object) -> bool:
        return self._node.__ne__()
