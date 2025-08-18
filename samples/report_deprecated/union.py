from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="simple_union",
        sample_code="""x = Union[Path, str, bytes, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="simple_union_function",
        sample_code="""def save(self, file_path: Union[Path, str]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_union",
        sample_code="""def save(self, file_path: Union[Path, str, bytes, int]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="nested_in_unions",
        sample_code="""def save(self, file_path: Union[Path, Union[str, bytes]]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_nested_in_unions",
        sample_code="""def save(self, file_path: Union[Path, Dict[str, Union[str, bytes]]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_nested_in_unions",
        sample_code="""def save(self, file_path: Union[Path, List[Union[str, bytes]]]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_union",
        sample_code="""def save(self, file_path: Union[
    Path,
    str,
    bytes,
    int
]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_union_with_comments",
        sample_code="""def save(self, file_path: Union[
    Path,  # Path to the file
    str,   # File name as a string
    bytes, # File content in bytes
    int    # File descriptor
]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_union_with_nested",
        sample_code="""def save(self, file_path: Union[
    Path,
    Union[str, bytes],  # File name or content
    int
]) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_return_type",
        sample_code="""def get_file_path() -> Union[Path, str]:
    return Path("example.txt")""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="complex_union_in_return_type",
        sample_code="""def get_file_path() -> Union[Path, str, bytes, int]:
    return Path("example.txt")""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_union",
        sample_code="""import typing
def f(x: typing.Union[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_union",
        sample_code="""import typing as t
def f(x: t.Union[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_union",
        sample_code="""from typing import Union as U
def f(x: U[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="optional_as_union",
        sample_code="""def f(x: Union[int, None]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="type_none",
        sample_code="""from types import NoneType
def f(x: Union[int, NoneType]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="nested_optional_union",
        sample_code="""def f(x: Optional[Union[int, str]]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep604",
        sample_code="""def f(x: int | str) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_var_annot",
        sample_code="""x: Union[int, Union[str, bytes]] = 0""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_class_attr",
        sample_code="""class C:
    field: Union[int, str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_dataclass",
        sample_code="""from dataclasses import dataclass
@dataclass
class C:
    a: Union[int, str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_dict_value",
        sample_code="""from typing import Dict
D: Dict[str, Union[int, str]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_list",
        sample_code="""from typing import List
L: List[Union[int, str]] = []""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_callable",
        sample_code="""from typing import Callable
Func: Callable[[Union[int, str]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_in_tuple",
        sample_code="""T: tuple[Union[int, str], int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_with_literal",
        sample_code="""from typing import Literal
def f(x: Union[Literal["a", "b"], int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_inside_annotated",
        sample_code="""from typing import Annotated
def f(x: Annotated[Union[int, str], "meta"]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_with_newtype",
        sample_code="""from typing import NewType
UserId = NewType("UserId", int)
def f(x: Union[UserId, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="alias_assignment",
        sample_code="""PathLike = Union[str, bytes]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias",
        sample_code="""type Num = Union[int, float]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overloads_with_union",
        sample_code="""from typing import overload
@overload
def f(x: Union[int, str]) -> int: ...
@overload
def f(x: bytes) -> bytes: ...
def f(x): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="return_union_multiline",
        sample_code="""def g() -> Union[
    int,
    str | bytes,  # mixed style inside
]:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_union",
        sample_code="""def f(x: "Union[A, B]") -> None: ...
class A: ...
class B: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations",
        sample_code="""from __future__ import annotations
def f(x: Union['A', 'B']) -> None: ...
class A: ...
class B: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="typed_dict_union",
        sample_code="""from typing import TypedDict
class TD(TypedDict):
    k: Union[int, str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_union",
        sample_code="""from typing import Protocol
class P(Protocol):
    def f(self, x: Union[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="typevar_constraints",
        sample_code="""from typing import TypeVar
T = TypeVar("T", int, str)
U = TypeVar("U", bound=Union[int, float])""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_trailing_commas",
        sample_code="""def f(x: Union[
    int,
    str,
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_spacing",
        sample_code="""def f(x: Union[int,  # inline comment
                str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_with_any",
        sample_code="""from typing import Any
def f(x: Union[int, Any]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_with_never",
        sample_code="""from typing_extensions import Never
def f(x: Union[int, Never]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
]
