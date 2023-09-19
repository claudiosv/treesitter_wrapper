from Node import Node
from typing import Union


class Type(Node):
    named: bool = False
    _type: str = "None"


class _CompoundStatement(Type):
    named: bool = True
    _type: str = "_compound_statement"


class _SimpleStatement(Type):
    named: bool = True
    _type: str = "_simple_statement"


class Expression(Type):
    named: bool = True
    _type: str = "expression"


class Parameter(Type):
    named: bool = True
    _type: str = "parameter"


class Pattern(Type):
    named: bool = True
    _type: str = "pattern"


class AliasedImport(Type):
    named: bool = True
    _type: str = "aliased_import"


class ArgumentList(Type):
    named: bool = True
    _type: str = "argument_list"
    children: list[
        Union[
            "DictionarySplat",
            "Expression",
            "KeywordArgument",
            "ListSplat",
            "ParenthesizedExpression",
        ]
    ]


class Assignment(Type):
    named: bool = True
    _type: str = "assignment"


class AugmentedAssignment(Type):
    named: bool = True
    _type: str = "augmented_assignment"


class Block(Type):
    named: bool = True
    _type: str = "block"
    children: list[Union["_CompoundStatement", "_SimpleStatement"]]


class CaseClause(Type):
    named: bool = True
    _type: str = "case_clause"
    children: list["CasePattern"]


class CasePattern(Type):
    named: bool = True
    _type: str = "case_pattern"
    children: list[
        Union[
            "AsPattern",
            "ClassPattern",
            "ComplexPattern",
            "ConcatenatedString",
            "DictPattern",
            "DottedName",
            "FalseT",
            "Float",
            "Integer",
            "KeywordPattern",
            "ListPattern",
            "NoneT",
            "SplatPattern",
            "String",
            "TrueT",
            "TuplePattern",
            "UnionPattern",
        ]
    ]


class Chevron(Type):
    named: bool = True
    _type: str = "chevron"
    children: list["Expression"]


class ClassPattern(Type):
    named: bool = True
    _type: str = "class_pattern"
    children: list[Union["CasePattern", "DottedName"]]


class ComplexPattern(Type):
    named: bool = True
    _type: str = "complex_pattern"
    children: list[Union["Float", "Integer"]]


class ConstrainedType(Type):
    named: bool = True
    _type: str = "constrained_type"
    children: list["Type"]


class Decorator(Type):
    named: bool = True
    _type: str = "decorator"
    children: list["Expression"]


class DictPattern(Type):
    named: bool = True
    _type: str = "dict_pattern"
    children: list["SplatPattern"]


class DictionarySplat(Type):
    named: bool = True
    _type: str = "dictionary_splat"
    children: list["Expression"]


class DottedName(Type):
    named: bool = True
    _type: str = "dotted_name"
    children: list["Identifier"]


class ElifClause(Type):
    named: bool = True
    _type: str = "elif_clause"


class ElseClause(Type):
    named: bool = True
    _type: str = "else_clause"


class ExceptClause(Type):
    named: bool = True
    _type: str = "except_clause"
    children: list[Union["Block", "Expression"]]


class ExceptGroupClause(Type):
    named: bool = True
    _type: str = "except_group_clause"
    children: list[Union["Block", "Expression"]]


class ExpressionList(Type):
    named: bool = True
    _type: str = "expression_list"
    children: list["Expression"]


class FinallyClause(Type):
    named: bool = True
    _type: str = "finally_clause"
    children: list["Block"]


class ForInClause(Type):
    named: bool = True
    _type: str = "for_in_clause"


class FormatExpression(Type):
    named: bool = True
    _type: str = "format_expression"


class FormatSpecifier(Type):
    named: bool = True
    _type: str = "format_specifier"
    children: list["FormatExpression"]


class GenericType(Type):
    named: bool = True
    _type: str = "generic_type"
    children: list[Union["Identifier", "TypeParameter"]]


class IfClause(Type):
    named: bool = True
    _type: str = "if_clause"
    children: list["Expression"]


class ImportPrefix(Type):
    named: bool = True
    _type: str = "import_prefix"


class Interpolation(Type):
    named: bool = True
    _type: str = "interpolation"


class KeywordArgument(Type):
    named: bool = True
    _type: str = "keyword_argument"


class KeywordPattern(Type):
    named: bool = True
    _type: str = "keyword_pattern"
    children: list[
        Union[
            "ClassPattern",
            "ComplexPattern",
            "ConcatenatedString",
            "DictPattern",
            "DottedName",
            "FalseT",
            "Float",
            "Identifier",
            "Integer",
            "ListPattern",
            "NoneT",
            "SplatPattern",
            "String",
            "TrueT",
            "TuplePattern",
            "UnionPattern",
        ]
    ]


class LambdaParameters(Type):
    named: bool = True
    _type: str = "lambda_parameters"
    children: list["Parameter"]


class MemberType(Type):
    named: bool = True
    _type: str = "member_type"
    children: list[Union["Identifier", "Type"]]


class Module(Type):
    named: bool = True
    _type: str = "module"
    children: list[Union["_CompoundStatement", "_SimpleStatement"]]


class Pair(Type):
    named: bool = True
    _type: str = "pair"


class Parameters(Type):
    named: bool = True
    _type: str = "parameters"
    children: list["Parameter"]


class ParenthesizedListSplat(Type):
    named: bool = True
    _type: str = "parenthesized_list_splat"
    children: list[Union["ListSplat", "ParenthesizedExpression"]]


class PatternList(Type):
    named: bool = True
    _type: str = "pattern_list"
    children: list["Pattern"]


class RelativeImport(Type):
    named: bool = True
    _type: str = "relative_import"
    children: list[Union["DottedName", "ImportPrefix"]]


class Slice(Type):
    named: bool = True
    _type: str = "slice"
    children: list["Expression"]


class SplatPattern(Type):
    named: bool = True
    _type: str = "splat_pattern"
    children: list["Identifier"]


class SplatType(Type):
    named: bool = True
    _type: str = "splat_type"
    children: list["Identifier"]


class StringContent(Type):
    named: bool = True
    _type: str = "string_content"
    children: list[Union["EscapeInterpolation", "EscapeSequence"]]


class TypeParameter(Type):
    named: bool = True
    _type: str = "type_parameter"
    children: list["Type"]


class UnionPattern(Type):
    named: bool = True
    _type: str = "union_pattern"
    children: list[
        Union[
            "ClassPattern",
            "ComplexPattern",
            "ConcatenatedString",
            "DictPattern",
            "DottedName",
            "FalseT",
            "Float",
            "Integer",
            "ListPattern",
            "NoneT",
            "SplatPattern",
            "String",
            "TrueT",
            "TuplePattern",
            "UnionPattern",
        ]
    ]


class UnionType(Type):
    named: bool = True
    _type: str = "union_type"
    children: list["Type"]


class WildcardImport(Type):
    named: bool = True
    _type: str = "wildcard_import"


class WithClause(Type):
    named: bool = True
    _type: str = "with_clause"
    children: list["WithItem"]


class WithItem(Type):
    named: bool = True
    _type: str = "with_item"


class Yield(Type):
    named: bool = True
    _type: str = "yield"
    children: list[Union["Expression", "ExpressionList"]]


class Underscore(Type):
    named: bool = False
    _type: str = "_"


class _Future(Type):
    named: bool = False
    _type: str = "__future__"


class And(Type):
    named: bool = False
    _type: str = "and"


class As(Type):
    named: bool = False
    _type: str = "as"


class Assert(Type):
    named: bool = False
    _type: str = "assert"


class Async(Type):
    named: bool = False
    _type: str = "async"


class Break(Type):
    named: bool = False
    _type: str = "break"


class Case(Type):
    named: bool = False
    _type: str = "case"


class Class(Type):
    named: bool = False
    _type: str = "class"


class Comment(Type):
    named: bool = True
    _type: str = "comment"


class Continue(Type):
    named: bool = False
    _type: str = "continue"


class Def(Type):
    named: bool = False
    _type: str = "def"


class Del(Type):
    named: bool = False
    _type: str = "del"


class Elif(Type):
    named: bool = False
    _type: str = "elif"


class Else(Type):
    named: bool = False
    _type: str = "else"


class EscapeInterpolation(Type):
    named: bool = True
    _type: str = "escape_interpolation"


class EscapeSequence(Type):
    named: bool = True
    _type: str = "escape_sequence"


class Except(Type):
    named: bool = False
    _type: str = "except"


class Exec(Type):
    named: bool = False
    _type: str = "exec"


class Finally(Type):
    named: bool = False
    _type: str = "finally"


class For(Type):
    named: bool = False
    _type: str = "for"


class From(Type):
    named: bool = False
    _type: str = "from"


class Global(Type):
    named: bool = False
    _type: str = "global"


class If(Type):
    named: bool = False
    _type: str = "if"


class Import(Type):
    named: bool = False
    _type: str = "import"


class In(Type):
    named: bool = False
    _type: str = "in"


class Is(Type):
    named: bool = False
    _type: str = "is"


class IsNot(Type):
    named: bool = False
    _type: str = "is not"


class LineContinuation(Type):
    named: bool = True
    _type: str = "line_continuation"


class Match(Type):
    named: bool = False
    _type: str = "match"


class Nonlocal(Type):
    named: bool = False
    _type: str = "nonlocal"


class Not(Type):
    named: bool = False
    _type: str = "not"


class NotIn(Type):
    named: bool = False
    _type: str = "not in"


class Or(Type):
    named: bool = False
    _type: str = "or"


class Pass(Type):
    named: bool = False
    _type: str = "pass"


class Print(Type):
    named: bool = False
    _type: str = "print"


class Raise(Type):
    named: bool = False
    _type: str = "raise"


class Return(Type):
    named: bool = False
    _type: str = "return"


class StringEnd(Type):
    named: bool = True
    _type: str = "string_end"


class StringStart(Type):
    named: bool = True
    _type: str = "string_start"


class Try(Type):
    named: bool = False
    _type: str = "try"


class TypeConversion(Type):
    named: bool = True
    _type: str = "type_conversion"


class While(Type):
    named: bool = False
    _type: str = "while"


class With(Type):
    named: bool = False
    _type: str = "with"


class ClassDefinition(_CompoundStatement):
    named: bool = True
    _type: str = "class_definition"


class DecoratedDefinition(_CompoundStatement):
    named: bool = True
    _type: str = "decorated_definition"


class ForStatement(_CompoundStatement):
    named: bool = True
    _type: str = "for_statement"


class FunctionDefinition(_CompoundStatement):
    named: bool = True
    _type: str = "function_definition"


class IfStatement(_CompoundStatement):
    named: bool = True
    _type: str = "if_statement"


class MatchStatement(_CompoundStatement):
    named: bool = True
    _type: str = "match_statement"


class TryStatement(_CompoundStatement):
    named: bool = True
    _type: str = "try_statement"


class WhileStatement(_CompoundStatement):
    named: bool = True
    _type: str = "while_statement"


class WithStatement(_CompoundStatement):
    named: bool = True
    _type: str = "with_statement"


class AssertStatement(_SimpleStatement):
    named: bool = True
    _type: str = "assert_statement"


class BreakStatement(_SimpleStatement):
    named: bool = True
    _type: str = "break_statement"


class ContinueStatement(_SimpleStatement):
    named: bool = True
    _type: str = "continue_statement"


class DeleteStatement(_SimpleStatement):
    named: bool = True
    _type: str = "delete_statement"


class ExecStatement(_SimpleStatement):
    named: bool = True
    _type: str = "exec_statement"


class ExpressionStatement(_SimpleStatement):
    named: bool = True
    _type: str = "expression_statement"


class FutureImportStatement(_SimpleStatement):
    named: bool = True
    _type: str = "future_import_statement"


class GlobalStatement(_SimpleStatement):
    named: bool = True
    _type: str = "global_statement"


class ImportFromStatement(_SimpleStatement):
    named: bool = True
    _type: str = "import_from_statement"


class ImportStatement(_SimpleStatement):
    named: bool = True
    _type: str = "import_statement"


class NonlocalStatement(_SimpleStatement):
    named: bool = True
    _type: str = "nonlocal_statement"


class PassStatement(_SimpleStatement):
    named: bool = True
    _type: str = "pass_statement"


class PrintStatement(_SimpleStatement):
    named: bool = True
    _type: str = "print_statement"


class RaiseStatement(_SimpleStatement):
    named: bool = True
    _type: str = "raise_statement"


class ReturnStatement(_SimpleStatement):
    named: bool = True
    _type: str = "return_statement"


class TypeAliasStatement(_SimpleStatement):
    named: bool = True
    _type: str = "type_alias_statement"


class AsPattern(Expression):
    named: bool = True
    _type: str = "as_pattern"


class BooleanOperator(Expression):
    named: bool = True
    _type: str = "boolean_operator"


class ComparisonOperator(Expression):
    named: bool = True
    _type: str = "comparison_operator"


class ConditionalExpression(Expression):
    named: bool = True
    _type: str = "conditional_expression"


class Lambda(Expression):
    named: bool = True
    _type: str = "lambda"


class NamedExpression(Expression):
    named: bool = True
    _type: str = "named_expression"


class NotOperator(Expression):
    named: bool = True
    _type: str = "not_operator"


class PrimaryExpression(Expression):
    named: bool = True
    _type: str = "primary_expression"


class DefaultParameter(Parameter):
    named: bool = True
    _type: str = "default_parameter"


class DictionarySplatPattern(Parameter):
    named: bool = True
    _type: str = "dictionary_splat_pattern"


class KeywordSeparator(Parameter):
    named: bool = True
    _type: str = "keyword_separator"


class PositionalSeparator(Parameter):
    named: bool = True
    _type: str = "positional_separator"


class TypedDefaultParameter(Parameter):
    named: bool = True
    _type: str = "typed_default_parameter"


class TypedParameter(Parameter):
    named: bool = True
    _type: str = "typed_parameter"


class ListPattern(Pattern):
    named: bool = True
    _type: str = "list_pattern"


class Await(PrimaryExpression):
    named: bool = True
    _type: str = "await"


class BinaryOperator(PrimaryExpression):
    named: bool = True
    _type: str = "binary_operator"


class Call(PrimaryExpression):
    named: bool = True
    _type: str = "call"


class ConcatenatedString(PrimaryExpression):
    named: bool = True
    _type: str = "concatenated_string"


class Dictionary(PrimaryExpression):
    named: bool = True
    _type: str = "dictionary"


class DictionaryComprehension(PrimaryExpression):
    named: bool = True
    _type: str = "dictionary_comprehension"


class Ellipsis(PrimaryExpression):
    named: bool = True
    _type: str = "ellipsis"


class FalseT(PrimaryExpression):
    named: bool = True
    _type: str = "false"


class Float(PrimaryExpression):
    named: bool = True
    _type: str = "float"


class GeneratorExpression(PrimaryExpression):
    named: bool = True
    _type: str = "generator_expression"


class Integer(PrimaryExpression):
    named: bool = True
    _type: str = "integer"


class ListT(PrimaryExpression):
    named: bool = True
    _type: str = "list"


class ListComprehension(PrimaryExpression):
    named: bool = True
    _type: str = "list_comprehension"


class ListSplat(PrimaryExpression):
    named: bool = True
    _type: str = "list_splat"


class NoneT(PrimaryExpression):
    named: bool = True
    _type: str = "none"


class ParenthesizedExpression(PrimaryExpression):
    named: bool = True
    _type: str = "parenthesized_expression"


class Set(PrimaryExpression):
    named: bool = True
    _type: str = "set"


class SetComprehension(PrimaryExpression):
    named: bool = True
    _type: str = "set_comprehension"


class String(PrimaryExpression):
    named: bool = True
    _type: str = "string"


class TrueT(PrimaryExpression):
    named: bool = True
    _type: str = "true"


class Tuple(PrimaryExpression):
    named: bool = True
    _type: str = "tuple"


class UnaryOperator(PrimaryExpression):
    named: bool = True
    _type: str = "unary_operator"


class ListSplatPattern(Parameter, Pattern):
    named: bool = True
    _type: str = "list_splat_pattern"


class TuplePattern(Parameter, Pattern):
    named: bool = True
    _type: str = "tuple_pattern"


class Attribute(Pattern, PrimaryExpression):
    named: bool = True
    _type: str = "attribute"


class Subscript(Pattern, PrimaryExpression):
    named: bool = True
    _type: str = "subscript"


class Identifier(Parameter, Pattern, PrimaryExpression):
    named: bool = True
    _type: str = "identifier"
