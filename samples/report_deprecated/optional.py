simple_optional_param = """
def f(x: Optional[int]) -> None: ...
"""

multi_optional_param = """
def f(x: Optional[int], y: Optional[str]) -> None: ...
"""

nested_optional_param = """
def f(x: Optional[Union[int, str]]) -> None: ...
"""

### Return types
simple_optional_return = """
def g() -> Optional[int]:
    return 1
"""

nested_optional_return = """
def g() -> Optional[Union[int, str]]:
    return "hi"
"""

### Variables / annotations
var_optional = """
x: Optional[int] = None
"""

class_attr_optional = """
class C:
    field: Optional[str]
"""

### Collections / generics
list_of_optional = """
from typing import List
L: List[Optional[int]] = []
"""

dict_with_optional_value = """
from typing import Dict
D: Dict[str, Optional[int]] = {}
"""

callable_with_optional_arg = """
from typing import Callable
F: Callable[[Optional[int]], None]
"""

### Aliasing / imports
qualified_optional = """
import typing
x: typing.Optional[int] = None
"""

aliased_optional = """
import typing as t
x: t.Optional[int] = None
"""

imported_as_o = """
from typing import Optional as O
x: O[int] = None
"""

### Already PEP 604
already_pep604_optional = """
def f(x: int | None) -> None: ...
"""

### Inside Annotated / Literal
annotated_optional = """
from typing import Annotated
def f(x: Annotated[Optional[int], "meta"]) -> None: ...
"""

literal_optional = """
from typing import Literal
def f(x: Optional[Literal["a", "b"]]) -> None: ...
"""

### Type alias / PEP 695
alias_optional = """
PathLike = Optional[str]
"""

pep695_alias_optional = """
type MaybeInt = Optional[int]
"""

### Multiline / comments
multi_line_optional = """
def f(
    x: Optional[
        int
    ]
) -> None: ...
"""

multi_line_optional_with_comment = """
def f(x: Optional[
    int,  # integer or None
]) -> None: ...
"""

### Protocols / TypedDicts
typed_dict_optional = """
from typing import TypedDict
class TD(TypedDict):
    k: Optional[int]
"""

protocol_optional = """
from typing import Protocol
class P(Protocol):
    def f(self, x: Optional[int]) -> None: ...
"""

### Weird / edge cases
optional_none = """
def f(x: Optional[None]) -> None: ...
"""

optional_any = """
from typing import Any
def f(x: Optional[Any]) -> None: ...
"""

optional_never = """
from typing_extensions import Never
def f(x: Optional[Never]) -> None: ...
"""
