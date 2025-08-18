from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="list_param",
        sample_code="""from typing import List
def f(xs: List[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_return",
        sample_code="""from typing import List
def g() -> List[str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_var",
        sample_code="""from typing import List
xs: List[bytes] = []""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_list",
        sample_code="""import typing
def f(xs: typing.List[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_list",
        sample_code="""import typing as t
def f(xs: t.List[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_L",
        sample_code="""from typing import List as L
def f(xs: L[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_of_unions",
        sample_code="""from typing import List, Union
xs: List[Union[int, str]] = []""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_of_optionals",
        sample_code="""from typing import List, Optional
xs: List[Optional[int]] = []""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_in_dict",
        sample_code="""from typing import Dict, List
D: Dict[str, List[int]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_of_lists",
        sample_code="""from typing import List
grid: List[List[int]] = []""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_list_param",
        sample_code="""from typing import Callable, List
F: Callable[[List[int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_of_lists",
        sample_code="""from typing import Tuple, List
T: Tuple[List[int], List[str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_list",
        sample_code="""from typing import List
class C:
    items: List[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_list",
        sample_code="""from dataclasses import dataclass
from typing import List
@dataclass
class C:
    items: List[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_list",
        sample_code="""from typing import overload, List
@overload
def f(xs: List[int]) -> int: ...
@overload
def f(xs: List[str]) -> str: ...
def f(xs): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_list",
        sample_code="""from typing import Protocol, List
class P(Protocol):
    def f(self, xs: List[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="typeddict_list",
        sample_code="""from typing import TypedDict, List
class TD(TypedDict):
    k: List[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_list",
        sample_code="""from typing import List
type IntList = List[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_list",
        sample_code="""from typing import List
def f(xs: "List[int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_list",
        sample_code="""from __future__ import annotations
from typing import List
def f(xs: List[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_list",
        sample_code="""from typing import List
def f(xs: List[
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_list",
        sample_code="""from typing import List
xs: List[int]  # numbers""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585",
        sample_code="""def f(xs: list[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_List",
        sample_code="""from typing import List
xs: List  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_of_any",
        sample_code="""from typing import List, Any
xs: List[Any]""",
        errors=["reportDeprecated"],
    ),
]
