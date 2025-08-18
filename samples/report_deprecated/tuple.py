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
