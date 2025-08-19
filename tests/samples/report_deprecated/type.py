from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="simple_type_param",
        sample_code="""from typing import Type
def f(cls: Type[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="simple_type_return",
        sample_code="""from typing import Type
def g() -> Type[str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="var_type",
        sample_code="""from typing import Type
x: Type[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_type",
        sample_code="""from typing import Type
class C:
    attr: Type[C]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_type",
        sample_code="""import typing
def f(cls: typing.Type[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_type",
        sample_code="""import typing as t
def f(cls: t.Type[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_t",
        sample_code="""from typing import Type as T
def f(cls: T[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_of_type",
        sample_code="""from typing import List, Type
L: List[Type[int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_with_type_value",
        sample_code="""from typing import Dict, Type
D: Dict[str, Type[int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_type_arg",
        sample_code="""from typing import Callable, Type
F: Callable[[Type[int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="subclass_type",
        sample_code="""from typing import Type
class A: ...
class B(A): ...
x: Type[A] = B""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="annotated_type",
        sample_code="""from typing import Annotated, Type
def f(x: Annotated[Type[int], "meta"]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="union_with_type",
        sample_code="""from typing import Union, Type
def f(x: Union[Type[int], Type[str]]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_newstyle_type",
        sample_code="""def f(cls: type[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="alias_type",
        sample_code="""from typing import Type
MyType = Type[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_type",
        sample_code="""type MyCls = Type[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_type",
        sample_code="""from typing import Type
def f(
    cls: Type[
        int
    ]
) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_type_with_comment",
        sample_code="""from typing import Type
def f(cls: Type[
    int,  # must be an int subclass
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_type",
        sample_code="""from typing import Protocol, Type
class P(Protocol):
    def f(self, cls: Type[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="typed_dict_type",
        sample_code="""from typing import TypedDict, Type
class TD(TypedDict):
    k: Type[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="type_of_any",
        sample_code="""from typing import Type, Any
x: Type[Any]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="type_of_never",
        sample_code="""from typing_extensions import Never
from typing import Type
x: Type[Never]""",
        errors=["reportDeprecated"],
    ),
]
