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
