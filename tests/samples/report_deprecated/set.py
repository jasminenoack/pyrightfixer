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