from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="set_param",
        sample_code="""from typing import Set
def f(s: Set[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_return",
        sample_code="""from typing import Set
def g() -> Set[str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_var",
        sample_code="""from typing import Set
s: Set[bytes] = set()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_set",
        sample_code="""import typing
def f(s: typing.Set[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_set",
        sample_code="""import typing as t
def f(s: t.Set[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_S",
        sample_code="""from typing import Set as S
def f(s: S[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_unions",
        sample_code="""from typing import Set, Union
s: Set[Union[int, str]] = set()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_optionals",
        sample_code="""from typing import Set, Optional
s: Set[Optional[int]] = set()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_sets",
        sample_code="""from typing import Set
nested: Set[Set[int]] = set()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_set_param",
        sample_code="""from typing import Callable, Set
F: Callable[[Set[int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_with_set_value",
        sample_code="""from typing import Dict, Set
D: Dict[str, Set[int]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_sets",
        sample_code="""from typing import Tuple, Set
T: Tuple[Set[int], Set[str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_set",
        sample_code="""from typing import Set
class C:
    seen: Set[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_set",
        sample_code="""from dataclasses import dataclass
from typing import Set
@dataclass
class C:
    seen: Set[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_set",
        sample_code="""from typing import overload, Set
@overload
def f(s: Set[int]) -> int: ...
@overload
def f(s: Set[str]) -> str: ...
def f(s): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_set",
        sample_code="""from typing import Protocol, Set
class P(Protocol):
    def f(self, s: Set[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="typeddict_set",
        sample_code="""from typing import TypedDict, Set
class TD(TypedDict):
    k: Set[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_set",
        sample_code="""from typing import Set
type IntSet = Set[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_set",
        sample_code="""from typing import Set
def f(s: "Set[int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_set",
        sample_code="""from __future__ import annotations
from typing import Set
def f(s: Set[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_set",
        sample_code="""from typing import Set
def f(s: Set[
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_set",
        sample_code="""from typing import Set
s: Set[int]  # numbers""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_set",
        sample_code="""def f(s: set[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_Set",
        sample_code="""from typing import Set
s: Set  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_any",
        sample_code="""from typing import Set, Any
s: Set[Any]""",
        errors=["reportDeprecated"],
    ),
]
