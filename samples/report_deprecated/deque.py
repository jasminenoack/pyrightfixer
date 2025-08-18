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
