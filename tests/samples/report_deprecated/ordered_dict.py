
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
