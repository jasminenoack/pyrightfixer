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
