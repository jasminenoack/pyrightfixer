union = """
x = Union[Path, str, bytes, int]
"""

simple_union_function = """
def save(self, file_path: Union[Path, str]) -> None:
    ...
"""

long_union = """
def save(self, file_path: Union[Path, str, bytes, int]) -> None:
    ...
"""

nested_in_unions = """
def save(self, file_path: Union[Path, Union[str, bytes]]) -> None:
    ...
"""

dict_nested_in_unions = """
def save(self, file_path: Union[Path, Dict[str, Union[str, bytes]]) -> None:
    ...
"""

list_nested_in_unions = """
def save(self, file_path: Union[Path, List[Union[str, bytes]]]) -> None:
    ...
"""

multi_line_union = """
def save(self, file_path: Union[
    Path,
    str,
    bytes,
    int
]) -> None:
    ...
"""

multi_line_union_with_comments = """
def save(self, file_path: Union[
    Path,  # Path to the file
    str,   # File name as a string
    bytes, # File content in bytes
    int    # File descriptor
]) -> None:
    ...
"""

multi_line_union_with_nested = """
def save(self, file_path: Union[
    Path,
    Union[str, bytes],  # File name or content
    int
]) -> None:
    ...
"""

union_in_return_type = """
def get_file_path() -> Union[Path, str]:
    return Path("example.txt")
"""

complex_union_in_return_type = """
def get_file_path() -> Union[Path, str, bytes, int]:
    return Path("example.txt")
"""

qualified_union = """
import typing
def f(x: typing.Union[int, str]) -> None: ...
"""

aliased_union = """
import typing as t
def f(x: t.Union[int, str]) -> None: ...
"""

imported_as_union = """
from typing import Union as U
def f(x: U[int, str]) -> None: ...
"""

optional_as_union = """
def f(x: Union[int, None]) -> None: ...
"""

type_none = """
from types import NoneType
def f(x: Union[int, NoneType]) -> None: ...
"""

nested_optional_union = """
def f(x: Optional[Union[int, str]]) -> None: ...
"""

already_pep604 = """
def f(x: int | str) -> None: ...
"""

union_in_var_annot = """
x: Union[int, Union[str, bytes]] = 0
"""

union_in_class_attr = """
class C:
    field: Union[int, str]
"""

union_in_dataclass = """
from dataclasses import dataclass
@dataclass
class C:
    a: Union[int, str]
"""

union_in_dict_value = """
from typing import Dict
D: Dict[str, Union[int, str]] = {}
"""

union_in_list = """
from typing import List
L: List[Union[int, str]] = []
"""

union_in_callable = """
from typing import Callable
Func: Callable[[Union[int, str]], None]
"""

union_in_tuple = """
T: tuple[Union[int, str], int]
"""

union_with_literal = """
from typing import Literal
def f(x: Union[Literal["a", "b"], int]) -> None: ...
"""

union_inside_annotated = """
from typing import Annotated
def f(x: Annotated[Union[int, str], "meta"]) -> None: ...
"""

union_with_newtype = """
from typing import NewType
UserId = NewType("UserId", int)
def f(x: Union[UserId, int]) -> None: ...
"""

alias_assignment = """
PathLike = Union[str, bytes]
"""

pep695_alias = """
type Num = Union[int, float]
"""

overloads_with_union = """
from typing import overload
@overload
def f(x: Union[int, str]) -> int: ...
@overload
def f(x: bytes) -> bytes: ...
def f(x): ...
"""

return_union_multiline = """
def g() -> Union[
    int,
    str | bytes,  # mixed style inside
]:
    ...
"""

forward_ref_union = """
def f(x: "Union[A, B]") -> None: ...
class A: ...
class B: ...
"""

future_annotations = """
from __future__ import annotations
def f(x: Union['A', 'B']) -> None: ...
class A: ...
class B: ...
"""

typed_dict_union = """
from typing import TypedDict
class TD(TypedDict):
    k: Union[int, str]
"""

protocol_union = """
from typing import Protocol
class P(Protocol):
    def f(self, x: Union[int, str]) -> None: ...
"""

typevar_constraints = """
from typing import TypeVar
T = TypeVar("T", int, str)
U = TypeVar("U", bound=Union[int, float])
"""

multi_line_trailing_commas = """
def f(x: Union[
    int,
    str,
]) -> None: ...
"""

inline_comment_spacing = """
def f(x: Union[int,  # inline comment
                str]) -> None: ...
"""

union_with_any = """
from typing import Any
def f(x: Union[int, Any]) -> None: ...
"""

union_with_never = """
from typing_extensions import Never
def f(x: Union[int, Never]) -> None: ...
"""
