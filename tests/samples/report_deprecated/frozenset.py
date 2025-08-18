
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
