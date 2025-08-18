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
