from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="simple_optional_param",
        sample_code="""def f(x: Optional[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_optional_param",
        sample_code="""def f(x: Optional[int], y: Optional[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="nested_optional_param",
        sample_code="""def f(x: Optional[Union[int, str]]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="simple_optional_return",
        sample_code="""def g() -> Optional[int]:
    return 1""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="nested_optional_return",
        sample_code="""def g() -> Optional[Union[int, str]]:
    return "hi\"""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="var_optional",
        sample_code="""x: Optional[int] = None""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_optional",
        sample_code="""class C:
    field: Optional[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_of_optional",
        sample_code="""from typing import List
L: List[Optional[int]] = []""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_with_optional_value",
        sample_code="""from typing import Dict
D: Dict[str, Optional[int]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_optional_arg",
        sample_code="""from typing import Callable
F: Callable[[Optional[int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_optional",
        sample_code="""import typing
x: typing.Optional[int] = None""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_optional",
        sample_code="""import typing as t
x: t.Optional[int] = None""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_o",
        sample_code="""from typing import Optional as O
x: O[int] = None""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep604_optional",
        sample_code="""def f(x: int | None) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="annotated_optional",
        sample_code="""from typing import Annotated
def f(x: Annotated[Optional[int], "meta"]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="literal_optional",
        sample_code="""from typing import Literal
def f(x: Optional[Literal["a", "b"]]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="alias_optional",
        sample_code="""PathLike = Optional[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_optional",
        sample_code="""type MaybeInt = Optional[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_optional",
        sample_code="""def f(
    x: Optional[
        int
    ]
) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multi_line_optional_with_comment",
        sample_code="""def f(x: Optional[
    int,  # integer or None
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="typed_dict_optional",
        sample_code="""from typing import TypedDict
class TD(TypedDict):
    k: Optional[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_optional",
        sample_code="""from typing import Protocol
class P(Protocol):
    def f(self, x: Optional[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="optional_none",
        sample_code="""def f(x: Optional[None]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="optional_any",
        sample_code="""from typing import Any
def f(x: Optional[Any]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="optional_never",
        sample_code="""from typing_extensions import Never
def f(x: Optional[Never]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
]
