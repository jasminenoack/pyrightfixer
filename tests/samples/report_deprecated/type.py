simple_type_param = """
from typing import Type
def f(cls: Type[int]) -> None: ...
"""

simple_type_return = """
from typing import Type
def g() -> Type[str]: ...
"""


### Variables & attributes

var_type = """
from typing import Type
x: Type[int]
"""

class_attr_type = """
from typing import Type
class C:
    attr: Type[C]
"""


### Qualified & aliased

qualified_type = """
import typing
def f(cls: typing.Type[int]) -> None: ...
"""

aliased_type = """
import typing as t
def f(cls: t.Type[int]) -> None: ...
"""

imported_as_t = """
from typing import Type as T
def f(cls: T[int]) -> None: ...
"""


### With generics / collections

list_of_type = """
from typing import List, Type
L: List[Type[int]]
"""

dict_with_type_value = """
from typing import Dict, Type
D: Dict[str, Type[int]]
"""

callable_with_type_arg = """
from typing import Callable, Type
F: Callable[[Type[int]], None]
"""


### Subclass bounds

subclass_type = """
from typing import Type
class A: ...
class B(A): ...
x: Type[A] = B
"""


### Nested / Annotated / Union

annotated_type = """
from typing import Annotated, Type
def f(x: Annotated[Type[int], "meta"]) -> None: ...
"""

union_with_type = """
from typing import Union, Type
def f(x: Union[Type[int], Type[str]]) -> None: ...
"""


### Already new-style

already_newstyle_type = """
def f(cls: type[int]) -> None: ...
"""


### Type alias / PEP 695

alias_type = """
from typing import Type
MyType = Type[int]
"""

pep695_alias_type = """
type MyCls = Type[str]
"""


### Multiline / comments

multi_line_type = """
from typing import Type
def f(
    cls: Type[
        int
    ]
) -> None: ...
"""

multi_line_type_with_comment = """
from typing import Type
def f(cls: Type[
    int,  # must be an int subclass
]) -> None: ...
"""


### Protocol / TypedDict context

protocol_type = """
from typing import Protocol, Type
class P(Protocol):
    def f(self, cls: Type[int]) -> None: ...
"""

typed_dict_type = """
from typing import TypedDict, Type
class TD(TypedDict):
    k: Type[int]
"""


### Weird / edge

type_of_any = """
from typing import Type, Any
x: Type[Any]
"""

type_of_never = """
from typing_extensions import Never
from typing import Type
x: Type[Never]
"""