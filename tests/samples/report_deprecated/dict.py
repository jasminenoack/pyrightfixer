
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