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
