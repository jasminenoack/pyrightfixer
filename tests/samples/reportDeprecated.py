"""
Samples for fixing the reportDeprecated rule
"""

"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Union
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

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

"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Optional
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

simple_optional_param = """
def f(x: Optional[int]) -> None: ...
"""

multi_optional_param = """
def f(x: Optional[int], y: Optional[str]) -> None: ...
"""

nested_optional_param = """
def f(x: Optional[Union[int, str]]) -> None: ...
"""

### Return types
simple_optional_return = """
def g() -> Optional[int]:
    return 1
"""

nested_optional_return = """
def g() -> Optional[Union[int, str]]:
    return "hi"
"""

### Variables / annotations
var_optional = """
x: Optional[int] = None
"""

class_attr_optional = """
class C:
    field: Optional[str]
"""

### Collections / generics
list_of_optional = """
from typing import List
L: List[Optional[int]] = []
"""

dict_with_optional_value = """
from typing import Dict
D: Dict[str, Optional[int]] = {}
"""

callable_with_optional_arg = """
from typing import Callable
F: Callable[[Optional[int]], None]
"""

### Aliasing / imports
qualified_optional = """
import typing
x: typing.Optional[int] = None
"""

aliased_optional = """
import typing as t
x: t.Optional[int] = None
"""

imported_as_o = """
from typing import Optional as O
x: O[int] = None
"""

### Already PEP 604
already_pep604_optional = """
def f(x: int | None) -> None: ...
"""

### Inside Annotated / Literal
annotated_optional = """
from typing import Annotated
def f(x: Annotated[Optional[int], "meta"]) -> None: ...
"""

literal_optional = """
from typing import Literal
def f(x: Optional[Literal["a", "b"]]) -> None: ...
"""

### Type alias / PEP 695
alias_optional = """
PathLike = Optional[str]
"""

pep695_alias_optional = """
type MaybeInt = Optional[int]
"""

### Multiline / comments
multi_line_optional = """
def f(
    x: Optional[
        int
    ]
) -> None: ...
"""

multi_line_optional_with_comment = """
def f(x: Optional[
    int,  # integer or None
]) -> None: ...
"""

### Protocols / TypedDicts
typed_dict_optional = """
from typing import TypedDict
class TD(TypedDict):
    k: Optional[int]
"""

protocol_optional = """
from typing import Protocol
class P(Protocol):
    def f(self, x: Optional[int]) -> None: ...
"""

### Weird / edge cases
optional_none = """
def f(x: Optional[None]) -> None: ...
"""

optional_any = """
from typing import Any
def f(x: Optional[Any]) -> None: ...
"""

optional_never = """
from typing_extensions import Never
def f(x: Optional[Never]) -> None: ...
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Type -> type
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""
simple_type_param = """
from typing import Type
def f(cls: Type[int]) -> None: ...
"""

simple_type_return = """
from typing import Type
def g() -> Type[str]: ...
"""


### Variables & attributes

var_type = """
from typing import Type
x: Type[int]
"""

class_attr_type = """
from typing import Type
class C:
    attr: Type[C]
"""


### Qualified & aliased

qualified_type = """
import typing
def f(cls: typing.Type[int]) -> None: ...
"""

aliased_type = """
import typing as t
def f(cls: t.Type[int]) -> None: ...
"""

imported_as_t = """
from typing import Type as T
def f(cls: T[int]) -> None: ...
"""


### With generics / collections

list_of_type = """
from typing import List, Type
L: List[Type[int]]
"""

dict_with_type_value = """
from typing import Dict, Type
D: Dict[str, Type[int]]
"""

callable_with_type_arg = """
from typing import Callable, Type
F: Callable[[Type[int]], None]
"""


### Subclass bounds

subclass_type = """
from typing import Type
class A: ...
class B(A): ...
x: Type[A] = B
"""


### Nested / Annotated / Union

annotated_type = """
from typing import Annotated, Type
def f(x: Annotated[Type[int], "meta"]) -> None: ...
"""

union_with_type = """
from typing import Union, Type
def f(x: Union[Type[int], Type[str]]) -> None: ...
"""


### Already new-style

already_newstyle_type = """
def f(cls: type[int]) -> None: ...
"""


### Type alias / PEP 695

alias_type = """
from typing import Type
MyType = Type[int]
"""

pep695_alias_type = """
type MyCls = Type[str]
"""


### Multiline / comments

multi_line_type = """
from typing import Type
def f(
    cls: Type[
        int
    ]
) -> None: ...
"""

multi_line_type_with_comment = """
from typing import Type
def f(cls: Type[
    int,  # must be an int subclass
]) -> None: ...
"""


### Protocol / TypedDict context

protocol_type = """
from typing import Protocol, Type
class P(Protocol):
    def f(self, cls: Type[int]) -> None: ...
"""

typed_dict_type = """
from typing import TypedDict, Type
class TD(TypedDict):
    k: Type[int]
"""


### Weird / edge

type_of_any = """
from typing import Type, Any
x: Type[Any]
"""

type_of_never = """
from typing_extensions import Never
from typing import Type
x: Type[Never]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
List
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

### Basics (params / returns / vars)


list_param = """
from typing import List
def f(xs: List[int]) -> None: ...
"""

list_return = """
from typing import List
def g() -> List[str]: ...
"""

list_var = """
from typing import List
xs: List[bytes] = []
"""


### Qualified / aliased imports


qualified_list = """
import typing
def f(xs: typing.List[int]) -> None: ...
"""

aliased_list = """
import typing as t
def f(xs: t.List[int]) -> None: ...
"""

imported_as_L = """
from typing import List as L
def f(xs: L[int]) -> None: ...
"""


### Nested / mixed generics


list_of_unions = """
from typing import List, Union
xs: List[Union[int, str]] = []
"""

list_of_optionals = """
from typing import List, Optional
xs: List[Optional[int]] = []
"""

list_in_dict = """
from typing import Dict, List
D: Dict[str, List[int]] = {}
"""

list_of_lists = """
from typing import List
grid: List[List[int]] = []
"""


### Callable / Tuple interactions


callable_with_list_param = """
from typing import Callable, List
F: Callable[[List[int]], None]
"""

tuple_of_lists = """
from typing import Tuple, List
T: Tuple[List[int], List[str]]
"""


### Class attributes / dataclass


class_attr_list = """
from typing import List
class C:
    items: List[int]
"""

dataclass_list = """
from dataclasses import dataclass
from typing import List
@dataclass
class C:
    items: List[str]
"""


### Overloads / Protocol / TypedDict contexts


overload_list = """
from typing import overload, List
@overload
def f(xs: List[int]) -> int: ...
@overload
def f(xs: List[str]) -> str: ...
def f(xs): ...
"""

protocol_list = """
from typing import Protocol, List
class P(Protocol):
    def f(self, xs: List[int]) -> None: ...
"""

typeddict_list = """
from typing import TypedDict, List
class TD(TypedDict):
    k: List[int]
"""


### PEP 695 type alias / forward ref / future annotations


pep695_alias_list = """
from typing import List
type IntList = List[int]
"""

forward_ref_list = """
from typing import List
def f(xs: "List[int]") -> None: ...
"""

future_annotations_list = """
from __future__ import annotations
from typing import List
def f(xs: List[int]) -> None: ...
"""


### Multiline / comments / spacing


multiline_list = """
from typing import List
def f(xs: List[
    int
]) -> None: ...
"""

inline_comment_list = """
from typing import List
xs: List[int]  # numbers
"""


### Already new-style (should be unchanged)


already_pep585 = """
def f(xs: list[int]) -> None: ...
"""


### Edge-ish


bare_List = """
from typing import List
xs: List  # no parameters (deprecated)
"""

list_of_any = """
from typing import List, Any
xs: List[Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Dict 
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


### Basics (params / returns / vars)


dict_param = """
from typing import Dict
def f(d: Dict[str, int]) -> None: ...
"""

dict_return = """
from typing import Dict
def g() -> Dict[int, str]: ...
"""

dict_var = """
from typing import Dict
d: Dict[str, float] = {}
"""


### Qualified / aliased imports


qualified_dict = """
import typing
def f(d: typing.Dict[str, int]) -> None: ...
"""

aliased_dict = """
import typing as t
def f(d: t.Dict[str, int]) -> None: ...
"""

imported_as_D = """
from typing import Dict as D
def f(d: D[str, int]) -> None: ...
"""


### Nested / mixed generics


dict_of_lists = """
from typing import Dict, List
d: Dict[str, List[int]] = {}
"""

dict_of_unions = """
from typing import Dict, Union
d: Dict[str, Union[int, float]] = {}
"""

dict_of_dicts = """
from typing import Dict
nested: Dict[str, Dict[int, str]] = {}
"""


### Callable / Tuple / Set interactions


callable_with_dict_param = """
from typing import Callable, Dict
F: Callable[[Dict[str, int]], None]
"""

tuple_with_dicts = """
from typing import Tuple, Dict
T: Tuple[Dict[str, int], Dict[str, str]]
"""

set_of_dicts = """
from typing import Set, Dict
S: Set[Dict[str, int]]
"""


### Class attributes / dataclass


class_attr_dict = """
from typing import Dict
class C:
    mapping: Dict[str, int]
"""

dataclass_dict = """
from dataclasses import dataclass
from typing import Dict
@dataclass
class C:
    mapping: Dict[str, int]
"""


### Overloads / Protocol / TypedDict contexts


overload_dict = """
from typing import overload, Dict
@overload
def f(d: Dict[str, int]) -> int: ...
@overload
def f(d: Dict[int, str]) -> str: ...
def f(d): ...
"""

protocol_dict = """
from typing import Protocol, Dict
class P(Protocol):
    def f(self, d: Dict[str, int]) -> None: ...
"""

typeddict_dict = """
from typing import TypedDict, Dict
class TD(TypedDict):
    k: Dict[str, int]
"""


### PEP 695 type alias / forward ref / future annotations


pep695_alias_dict = """
from typing import Dict
type StrIntMap = Dict[str, int]
"""

forward_ref_dict = """
from typing import Dict
def f(d: "Dict[str, int]") -> None: ...
"""

future_annotations_dict = """
from __future__ import annotations
from typing import Dict
def f(d: Dict[str, int]) -> None: ...
"""


### Multiline / comments / spacing


multiline_dict = """
from typing import Dict
def f(d: Dict[
    str,
    int
]) -> None: ...
"""

inline_comment_dict = """
from typing import Dict
d: Dict[str, int]  # mapping
"""


### Already new-style (should be unchanged)


already_pep585_dict = """
def f(d: dict[str, int]) -> None: ...
"""


### Edge-ish


bare_Dict = """
from typing import Dict
d: Dict  # no parameters (deprecated)
"""

dict_with_any = """
from typing import Dict, Any
d: Dict[str, Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Set 
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


### Basics (params / returns / vars)


set_param = """
from typing import Set
def f(s: Set[int]) -> None: ...
"""

set_return = """
from typing import Set
def g() -> Set[str]: ...
"""

set_var = """
from typing import Set
s: Set[bytes] = set()
"""


### Qualified / aliased imports


qualified_set = """
import typing
def f(s: typing.Set[int]) -> None: ...
"""

aliased_set = """
import typing as t
def f(s: t.Set[int]) -> None: ...
"""

imported_as_S = """
from typing import Set as S
def f(s: S[int]) -> None: ...
"""


### Nested / mixed generics


set_of_unions = """
from typing import Set, Union
s: Set[Union[int, str]] = set()
"""

set_of_optionals = """
from typing import Set, Optional
s: Set[Optional[int]] = set()
"""

set_of_sets = """
from typing import Set
nested: Set[Set[int]] = set()
"""


### Callable / Dict / Tuple interactions


callable_with_set_param = """
from typing import Callable, Set
F: Callable[[Set[int]], None]
"""

dict_with_set_value = """
from typing import Dict, Set
D: Dict[str, Set[int]] = {}
"""

tuple_with_sets = """
from typing import Tuple, Set
T: Tuple[Set[int], Set[str]]
"""


### Class attributes / dataclass


class_attr_set = """
from typing import Set
class C:
    seen: Set[int]
"""

dataclass_set = """
from dataclasses import dataclass
from typing import Set
@dataclass
class C:
    seen: Set[str]
"""


### Overloads / Protocol / TypedDict contexts


overload_set = """
from typing import overload, Set
@overload
def f(s: Set[int]) -> int: ...
@overload
def f(s: Set[str]) -> str: ...
def f(s): ...
"""

protocol_set = """
from typing import Protocol, Set
class P(Protocol):
    def f(self, s: Set[int]) -> None: ...
"""

typeddict_set = """
from typing import TypedDict, Set
class TD(TypedDict):
    k: Set[int]
"""


### PEP 695 type alias / forward ref / future annotations


pep695_alias_set = """
from typing import Set
type IntSet = Set[int]
"""

forward_ref_set = """
from typing import Set
def f(s: "Set[int]") -> None: ...
"""

future_annotations_set = """
from __future__ import annotations
from typing import Set
def f(s: Set[int]) -> None: ...
"""


### Multiline / comments / spacing


multiline_set = """
from typing import Set
def f(s: Set[
    int
]) -> None: ...
"""

inline_comment_set = """
from typing import Set
s: Set[int]  # numbers
"""


### Already new-style (should be unchanged)


already_pep585_set = """
def f(s: set[int]) -> None: ...
"""


### Edge-ish


bare_Set = """
from typing import Set
s: Set  # no parameters (deprecated)
"""

set_of_any = """
from typing import Set, Any
s: Set[Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Tuple 
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


### Basics (params / returns / vars)


tuple_param = """
from typing import Tuple
def f(t: Tuple[int, str]) -> None: ...
"""

tuple_return = """
from typing import Tuple
def g() -> Tuple[int, str]: ...
"""

tuple_var = """
from typing import Tuple
t: Tuple[int, str] = (1, "a")
"""


### Variadic (`...`)


tuple_variadic_param = """
from typing import Tuple
def f(t: Tuple[int, ...]) -> None: ...
"""

tuple_variadic_return = """
from typing import Tuple
def g() -> Tuple[str, ...]: ...
"""

tuple_variadic_var = """
from typing import Tuple
t: Tuple[bytes, ...] = (b"a", b"b")
"""


### Qualified / aliased imports


qualified_tuple = """
import typing
def f(t: typing.Tuple[int, str]) -> None: ...
"""

aliased_tuple = """
import typing as t
def f(t: t.Tuple[int, str]) -> None: ...
"""

imported_as_T = """
from typing import Tuple as T
def f(t: T[int, str]) -> None: ...
"""


### Nested / mixed generics


tuple_with_union = """
from typing import Tuple, Union
def f(t: Tuple[int, Union[str, bytes]]) -> None: ...
"""

tuple_of_lists = """
from typing import Tuple, List
t: Tuple[List[int], List[str]]
"""

tuple_variadic_of_optionals = """
from typing import Tuple, Optional
t: Tuple[Optional[int], ...]
"""


### Callable / Dict / Set interactions


callable_with_tuple_param = """
from typing import Callable, Tuple
F: Callable[[Tuple[int, str]], None]
"""

dict_with_tuple_value = """
from typing import Dict, Tuple
D: Dict[str, Tuple[int, str]]
"""

set_of_tuples = """
from typing import Set, Tuple
S: Set[Tuple[int, str]]
"""


### Class attributes / dataclass


class_attr_tuple = """
from typing import Tuple
class C:
    pair: Tuple[int, str]
"""

dataclass_tuple = """
from dataclasses import dataclass
from typing import Tuple
@dataclass
class C:
    data: Tuple[int, str]
"""


### Overloads / Protocol


overload_tuple = """
from typing import overload, Tuple
@overload
def f(t: Tuple[int, str]) -> int: ...
@overload
def f(t: Tuple[str, int]) -> str: ...
def f(t): ...
"""

protocol_tuple = """
from typing import Protocol, Tuple
class P(Protocol):
    def f(self, t: Tuple[int, str]) -> None: ...
"""


### PEP 695 type alias / forward ref / future annotations


pep695_alias_tuple = """
from typing import Tuple
type Pair = Tuple[int, str]
"""

forward_ref_tuple = """
from typing import Tuple
def f(t: "Tuple[int, str]") -> None: ...
"""

future_annotations_tuple = """
from __future__ import annotations
from typing import Tuple
def f(t: Tuple[int, str]) -> None: ...
"""


### Multiline / comments / spacing


multiline_tuple = """
from typing import Tuple
def f(t: Tuple[
    int,
    str
]) -> None: ...
"""

tuple_variadic_multiline = """
from typing import Tuple
def f(t: Tuple[
    int,
    ...
]) -> None: ...
"""

inline_comment_tuple = """
from typing import Tuple
t: Tuple[int, str]  # a pair
"""


### Already new-style (should be unchanged)


already_pep585_tuple = """
def f(t: tuple[int, str]) -> None: ...
"""

already_pep585_tuple_variadic = """
def f(t: tuple[int, ...]) -> None: ...
"""


### Edge-ish


bare_Tuple = """
from typing import Tuple
t: Tuple  # no parameters (deprecated)
"""

tuple_with_any = """
from typing import Tuple, Any
t: Tuple[Any, Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
FrozenSet
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

### Basics (params / returns / vars)


froz_param = """
from typing import FrozenSet
def f(s: FrozenSet[int]) -> None: ...
"""

froz_return = """
from typing import FrozenSet
def g() -> FrozenSet[str]: ...
"""

froz_var = """
from typing import FrozenSet
s: FrozenSet[bytes] = frozenset()
"""


### Qualified / aliased imports


qualified_froz = """
import typing
def f(s: typing.FrozenSet[int]) -> None: ...
"""

aliased_froz = """
import typing as t
def f(s: t.FrozenSet[int]) -> None: ...
"""

imported_as_FS = """
from typing import FrozenSet as FS
def f(s: FS[int]) -> None: ...
"""


### Nested / mixed generics


froz_of_union = """
from typing import FrozenSet, Union
s: FrozenSet[Union[int, str]] = frozenset()
"""

froz_of_optional = """
from typing import FrozenSet, Optional
s: FrozenSet[Optional[int]] = frozenset()
"""

froz_in_dict = """
from typing import Dict, FrozenSet
D: Dict[str, FrozenSet[int]] = {}
"""


### Callable / Tuple / Set interactions


callable_with_froz = """
from typing import Callable, FrozenSet
F: Callable[[FrozenSet[int]], None]
"""

tuple_with_froz = """
from typing import Tuple, FrozenSet
T: Tuple[FrozenSet[int], FrozenSet[str]]
"""

set_of_froz = """
from typing import Set, FrozenSet
S: Set[FrozenSet[int]]
"""


### Class attributes / dataclass


class_attr_froz = """
from typing import FrozenSet
class C:
    allowed: FrozenSet[int]
"""

dataclass_froz = """
from dataclasses import dataclass
from typing import FrozenSet
@dataclass
class C:
    tags: FrozenSet[str]
"""


### Overloads / Protocol


overload_froz = """
from typing import overload, FrozenSet
@overload
def f(s: FrozenSet[int]) -> int: ...
@overload
def f(s: FrozenSet[str]) -> str: ...
def f(s): ...
"""

protocol_froz = """
from typing import Protocol, FrozenSet
class P(Protocol):
    def f(self, s: FrozenSet[int]) -> None: ...
"""


### Type alias / forward ref / future annotations


pep695_alias_froz = """
from typing import FrozenSet
type IntFSet = FrozenSet[int]
"""

forward_ref_froz = """
from typing import FrozenSet
def f(s: "FrozenSet[int]") -> None: ...
"""

future_annotations_froz = """
from __future__ import annotations
from typing import FrozenSet
def f(s: FrozenSet[int]) -> None: ...
"""


### Multiline / comments


multiline_froz = """
from typing import FrozenSet
def f(s: FrozenSet[
    int
]) -> None: ...
"""

inline_comment_froz = """
from typing import FrozenSet
s: FrozenSet[int]  # immutable ints
"""


### Already new-style (should be unchanged)


already_pep585_froz = """
def f(s: frozenset[int]) -> None: ...
"""


### Edge-ish


bare_FrozenSet = """
from typing import FrozenSet
s: FrozenSet  # no parameters (deprecated)
"""

froz_of_any = """
from typing import FrozenSet, Any
s: FrozenSet[Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Deque
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


### Basics (params / returns / vars)


deque_param = """
from typing import Deque
def f(d: Deque[int]) -> None: ...
"""

deque_return = """
from typing import Deque
def g() -> Deque[str]: ...
"""

deque_var = """
from typing import Deque
dq: Deque[bytes] = Deque()
"""


### Qualified / aliased imports


qualified_deque = """
import typing
def f(d: typing.Deque[int]) -> None: ...
"""

aliased_deque = """
import typing as t
def f(d: t.Deque[int]) -> None: ...
"""

imported_as_DQ = """
from typing import Deque as DQ
def f(d: DQ[int]) -> None: ...
"""


### Nested / mixed generics


deque_of_unions = """
from typing import Deque, Union
d: Deque[Union[int, str]] = Deque()
"""

deque_of_optionals = """
from typing import Deque, Optional
d: Deque[Optional[int]] = Deque()
"""

dict_with_deque_value = """
from typing import Dict, Deque
D: Dict[str, Deque[int]] = {}
"""


### Callable / Tuple / Set interactions


callable_with_deque = """
from typing import Callable, Deque
F: Callable[[Deque[int]], None]
"""

tuple_with_deque = """
from typing import Tuple, Deque
T: Tuple[Deque[int], Deque[str]]
"""

set_of_deques = """
from typing import Set, Deque
S: Set[Deque[int]]
"""


### Class attributes / dataclass


class_attr_deque = """
from typing import Deque
class C:
    buffer: Deque[int]
"""

dataclass_deque = """
from dataclasses import dataclass
from typing import Deque
@dataclass
class C:
    buffer: Deque[str]
"""


### Overloads / Protocol


overload_deque = """
from typing import overload, Deque
@overload
def f(d: Deque[int]) -> int: ...
@overload
def f(d: Deque[str]) -> str: ...
def f(d): ...
"""

protocol_deque = """
from typing import Protocol, Deque
class P(Protocol):
    def f(self, d: Deque[int]) -> None: ...
"""


### Type alias / forward ref / future annotations


pep695_alias_deque = """
from typing import Deque
type IntDeque = Deque[int]
"""

forward_ref_deque = """
from typing import Deque
def f(d: "Deque[int]") -> None: ...
"""

future_annotations_deque = """
from __future__ import annotations
from typing import Deque
def f(d: Deque[int]) -> None: ...
"""


### Multiline / comments


multiline_deque = """
from typing import Deque
def f(d: Deque[
    int
]) -> None: ...
"""

inline_comment_deque = """
from typing import Deque
dq: Deque[int]  # int buffer
"""


### Already new-style (should be unchanged)


already_pep585_deque = """
from collections import deque
def f(d: deque[int]) -> None: ...
"""


### Edge-ish


bare_Deque = """
from typing import Deque
dq: Deque  # no parameters (deprecated)
"""

deque_of_any = """
from typing import Deque, Any
dq: Deque[Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
DefaultDict
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


### Basics (params / returns / vars)


defaultdict_param = """
from typing import DefaultDict
def f(d: DefaultDict[str, int]) -> None: ...
"""

defaultdict_return = """
from typing import DefaultDict
def g() -> DefaultDict[str, int]: ...
"""

defaultdict_var = """
from typing import DefaultDict
d: DefaultDict[str, int] = DefaultDict(int)
"""


### Qualified / aliased imports


qualified_defaultdict = """
import typing
def f(d: typing.DefaultDict[str, int]) -> None: ...
"""

aliased_defaultdict = """
import typing as t
def f(d: t.DefaultDict[str, int]) -> None: ...
"""

imported_as_DD = """
from typing import DefaultDict as DD
def f(d: DD[str, int]) -> None: ...
"""


### Nested / mixed generics


defaultdict_of_lists = """
from typing import DefaultDict, List
d: DefaultDict[str, List[int]] = DefaultDict(list)
"""

defaultdict_of_unions = """
from typing import DefaultDict, Union
d: DefaultDict[str, Union[int, float]] = DefaultDict(int)
"""

nested_defaultdicts = """
from typing import DefaultDict
nested: DefaultDict[str, DefaultDict[int, str]] = DefaultDict(dict)
"""


### Callable / Tuple / Set interactions


callable_with_defaultdict = """
from typing import Callable, DefaultDict
F: Callable[[DefaultDict[str, int]], None]
"""

tuple_with_defaultdicts = """
from typing import Tuple, DefaultDict
T: Tuple[DefaultDict[str, int], DefaultDict[int, str]]
"""

set_of_defaultdicts = """
from typing import Set, DefaultDict
S: Set[DefaultDict[str, int]]
"""


### Class attributes / dataclass


class_attr_defaultdict = """
from typing import DefaultDict
class C:
    mapping: DefaultDict[str, int]
"""

dataclass_defaultdict = """
from dataclasses import dataclass
from typing import DefaultDict
@dataclass
class C:
    cache: DefaultDict[str, int]
"""


### Overloads / Protocol


overload_defaultdict = """
from typing import overload, DefaultDict
@overload
def f(d: DefaultDict[str, int]) -> int: ...
@overload
def f(d: DefaultDict[int, str]) -> str: ...
def f(d): ...
"""

protocol_defaultdict = """
from typing import Protocol, DefaultDict
class P(Protocol):
    def f(self, d: DefaultDict[str, int]) -> None: ...
"""


### Type alias / forward ref / future annotations


pep695_alias_defaultdict = """
from typing import DefaultDict
type StrIntDD = DefaultDict[str, int]
"""

forward_ref_defaultdict = """
from typing import DefaultDict
def f(d: "DefaultDict[str, int]") -> None: ...
"""

future_annotations_defaultdict = """
from __future__ import annotations
from typing import DefaultDict
def f(d: DefaultDict[str, int]) -> None: ...
"""


### Multiline / comments


multiline_defaultdict = """
from typing import DefaultDict
def f(d: DefaultDict[
    str,
    int
]) -> None: ...
"""

inline_comment_defaultdict = """
from typing import DefaultDict
d: DefaultDict[str, int]  # mapping
"""


### Already new-style (should be unchanged)


already_pep585_defaultdict = """
from collections import defaultdict
def f(d: defaultdict[str, int]) -> None: ...
"""


### Edge-ish


bare_DefaultDict = """
from typing import DefaultDict
d: DefaultDict  # no parameters (deprecated)
"""

defaultdict_with_any = """
from typing import DefaultDict, Any
d: DefaultDict[str, Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
Counter
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

### Basics (params / returns / vars)


counter_param = """
from typing import Counter
def f(c: Counter[str]) -> None: ...
"""

counter_return = """
from typing import Counter
def g() -> Counter[int]: ...
"""

counter_var = """
from typing import Counter
c: Counter[str] = Counter()
"""


### Qualified / aliased imports


qualified_counter = """
import typing
def f(c: typing.Counter[str]) -> None: ...
"""

aliased_counter = """
import typing as t
def f(c: t.Counter[str]) -> None: ...
"""

imported_as_C = """
from typing import Counter as C
def f(c: C[str]) -> None: ...
"""


### Nested / mixed generics


counter_of_unions = """
from typing import Counter, Union
c: Counter[Union[str, int]] = Counter()
"""

counter_in_dict = """
from typing import Dict, Counter
d: Dict[str, Counter[int]] = {}
"""

list_of_counters = """
from typing import List, Counter
l: List[Counter[str]] = []
"""


### Callable / Tuple / Set interactions


callable_with_counter = """
from typing import Callable, Counter
F: Callable[[Counter[str]], None]
"""

tuple_with_counter = """
from typing import Tuple, Counter
T: Tuple[Counter[str], Counter[int]]
"""

set_of_counters = """
from typing import Set, Counter
S: Set[Counter[str]]
"""


### Class attributes / dataclass


class_attr_counter = """
from typing import Counter
class C:
    freq: Counter[str]
"""

dataclass_counter = """
from dataclasses import dataclass
from typing import Counter
@dataclass
class C:
    freq: Counter[int]
"""


### Overloads / Protocol


overload_counter = """
from typing import overload, Counter
@overload
def f(c: Counter[str]) -> int: ...
@overload
def f(c: Counter[int]) -> str: ...
def f(c): ...
"""

protocol_counter = """
from typing import Protocol, Counter
class P(Protocol):
    def f(self, c: Counter[str]) -> None: ...
"""


### Type alias / forward ref / future annotations


pep695_alias_counter = """
from typing import Counter
type StrCounter = Counter[str]
"""

forward_ref_counter = """
from typing import Counter
def f(c: "Counter[str]") -> None: ...
"""

future_annotations_counter = """
from __future__ import annotations
from typing import Counter
def f(c: Counter[str]) -> None: ...
"""


### Multiline / comments


multiline_counter = """
from typing import Counter
def f(c: Counter[
    str
]) -> None: ...
"""

inline_comment_counter = """
from typing import Counter
c: Counter[str]  # frequency map
"""


### Already new-style (should be unchanged)


already_pep585_counter = """
from collections import Counter
def f(c: Counter[str]) -> None: ...
"""


### Edge-ish


bare_Counter = """
from typing import Counter
c: Counter  # no parameters (deprecated)
"""

counter_of_any = """
from typing import Counter, Any
c: Counter[Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
OrderedDict
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


### Basics (params / returns / vars)


ordereddict_param = """
from typing import OrderedDict
def f(d: OrderedDict[str, int]) -> None: ...
"""

ordereddict_return = """
from typing import OrderedDict
def g() -> OrderedDict[int, str]: ...
"""

ordereddict_var = """
from typing import OrderedDict
d: OrderedDict[str, int] = OrderedDict()
"""


### Qualified / aliased imports


qualified_ordereddict = """
import typing
def f(d: typing.OrderedDict[str, int]) -> None: ...
"""

aliased_ordereddict = """
import typing as t
def f(d: t.OrderedDict[str, int]) -> None: ...
"""

imported_as_OD = """
from typing import OrderedDict as OD
def f(d: OD[str, int]) -> None: ...
"""


### Nested / mixed generics


ordereddict_of_lists = """
from typing import OrderedDict, List
d: OrderedDict[str, List[int]] = OrderedDict()
"""

ordereddict_of_unions = """
from typing import OrderedDict, Union
d: OrderedDict[str, Union[int, float]] = OrderedDict()
"""

nested_ordereddicts = """
from typing import OrderedDict
nested: OrderedDict[str, OrderedDict[int, str]] = OrderedDict()
"""


### Callable / Tuple / Set interactions


callable_with_ordereddict = """
from typing import Callable, OrderedDict
F: Callable[[OrderedDict[str, int]], None]
"""

tuple_with_ordereddict = """
from typing import Tuple, OrderedDict
T: Tuple[OrderedDict[str, int], OrderedDict[int, str]]
"""

set_of_ordereddicts = """
from typing import Set, OrderedDict
S: Set[OrderedDict[str, int]]
"""


### Class attributes / dataclass


class_attr_ordereddict = """
from typing import OrderedDict
class C:
    mapping: OrderedDict[str, int]
"""

dataclass_ordereddict = """
from dataclasses import dataclass
from typing import OrderedDict
@dataclass
class C:
    cache: OrderedDict[str, int]
"""


### Overloads / Protocol


overload_ordereddict = """
from typing import overload, OrderedDict
@overload
def f(d: OrderedDict[str, int]) -> int: ...
@overload
def f(d: OrderedDict[int, str]) -> str: ...
def f(d): ...
"""

protocol_ordereddict = """
from typing import Protocol, OrderedDict
class P(Protocol):
    def f(self, d: OrderedDict[str, int]) -> None: ...
"""


### Type alias / forward ref / future annotations


pep695_alias_ordereddict = """
from typing import OrderedDict
type StrIntOD = OrderedDict[str, int]
"""

forward_ref_ordereddict = """
from typing import OrderedDict
def f(d: "OrderedDict[str, int]") -> None: ...
"""

future_annotations_ordereddict = """
from __future__ import annotations
from typing import OrderedDict
def f(d: OrderedDict[str, int]) -> None: ...
"""


### Multiline / comments


multiline_ordereddict = """
from typing import OrderedDict
def f(d: OrderedDict[
    str,
    int
]) -> None: ...
"""

inline_comment_ordereddict = """
from typing import OrderedDict
d: OrderedDict[str, int]  # ordered mapping
"""


### Already new-style (should be unchanged)


already_pep585_ordereddict = """
from collections import OrderedDict
def f(d: OrderedDict[str, int]) -> None: ...
"""


### Edge-ish


bare_OrderedDict = """
from typing import OrderedDict
d: OrderedDict  # no parameters (deprecated)
"""

ordereddict_with_any = """
from typing import OrderedDict, Any
d: OrderedDict[str, Any]
"""


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
ChainMap
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


### Basics (params / returns / vars)


chainmap_param = """
from typing import ChainMap
def f(cm: ChainMap[str, int]) -> None: ...
"""

chainmap_return = """
from typing import ChainMap
def g() -> ChainMap[str, int]: ...
"""

chainmap_var = """
from typing import ChainMap
cm: ChainMap[str, int] = ChainMap()
"""


### Qualified / aliased imports


qualified_chainmap = """
import typing
def f(cm: typing.ChainMap[str, int]) -> None: ...
"""

aliased_chainmap = """
import typing as t
def f(cm: t.ChainMap[str, int]) -> None: ...
"""

imported_as_CM = """
from typing import ChainMap as CM
def f(cm: CM[str, int]) -> None: ...
"""


### Nested / mixed generics


chainmap_of_lists = """
from typing import ChainMap, List
cm: ChainMap[str, List[int]] = ChainMap()
"""

chainmap_of_unions = """
from typing import ChainMap, Union
cm: ChainMap[str, Union[int, float]] = ChainMap()
"""

nested_chainmaps = """
from typing import ChainMap
nested: ChainMap[str, ChainMap[int, str]] = ChainMap()
"""


### Callable / Tuple / Set interactions


callable_with_chainmap = """
from typing import Callable, ChainMap
F: Callable[[ChainMap[str, int]], None]
"""

tuple_with_chainmap = """
from typing import Tuple, ChainMap
T: Tuple[ChainMap[str, int], ChainMap[int, str]]
"""

set_of_chainmaps = """
from typing import Set, ChainMap
S: Set[ChainMap[str, int]]
"""


### Class attributes / dataclass


class_attr_chainmap = """
from typing import ChainMap
class C:
    mapping: ChainMap[str, int]
"""

dataclass_chainmap = """
from dataclasses import dataclass
from typing import ChainMap
@dataclass
class C:
    cache: ChainMap[str, int]
"""


### Overloads / Protocol


overload_chainmap = """
from typing import overload, ChainMap
@overload
def f(cm: ChainMap[str, int]) -> int: ...
@overload
def f(cm: ChainMap[int, str]) -> str: ...
def f(cm): ...
"""

protocol_chainmap = """
from typing import Protocol, ChainMap
class P(Protocol):
    def f(self, cm: ChainMap[str, int]) -> None: ...
"""


### Type alias / forward ref / future annotations


pep695_alias_chainmap = """
from typing import ChainMap
type StrIntCM = ChainMap[str, int]
"""

forward_ref_chainmap = """
from typing import ChainMap
def f(cm: "ChainMap[str, int]") -> None: ...
"""

future_annotations_chainmap = """
from __future__ import annotations
from typing import ChainMap
def f(cm: ChainMap[str, int]) -> None: ...
"""


### Multiline / comments


multiline_chainmap = """
from typing import ChainMap
def f(cm: ChainMap[
    str,
    int
]) -> None: ...
"""

inline_comment_chainmap = """
from typing import ChainMap
cm: ChainMap[str, int]  # chain of dicts
"""


### Already new-style (should be unchanged)


already_pep585_chainmap = """
from collections import ChainMap
def f(cm: ChainMap[str, int]) -> None: ...
"""


### Edge-ish


bare_ChainMap = """
from typing import ChainMap
cm: ChainMap  # no parameters (deprecated)
"""

chainmap_with_any = """
from typing import ChainMap, Any
cm: ChainMap[str, Any]
"""
