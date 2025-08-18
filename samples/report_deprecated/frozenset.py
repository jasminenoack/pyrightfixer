from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="froz_param",
        sample_code="""from typing import FrozenSet
def f(s: FrozenSet[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="froz_return",
        sample_code="""from typing import FrozenSet
def g() -> FrozenSet[str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="froz_var",
        sample_code="""from typing import FrozenSet
s: FrozenSet[bytes] = frozenset()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_froz",
        sample_code="""import typing
def f(s: typing.FrozenSet[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_froz",
        sample_code="""import typing as t
def f(s: t.FrozenSet[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_FS",
        sample_code="""from typing import FrozenSet as FS
def f(s: FS[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="froz_of_union",
        sample_code="""from typing import FrozenSet, Union
s: FrozenSet[Union[int, str]] = frozenset()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="froz_of_optional",
        sample_code="""from typing import FrozenSet, Optional
s: FrozenSet[Optional[int]] = frozenset()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="froz_in_dict",
        sample_code="""from typing import Dict, FrozenSet
D: Dict[str, FrozenSet[int]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_froz",
        sample_code="""from typing import Callable, FrozenSet
F: Callable[[FrozenSet[int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_froz",
        sample_code="""from typing import Tuple, FrozenSet
T: Tuple[FrozenSet[int], FrozenSet[str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_froz",
        sample_code="""from typing import Set, FrozenSet
S: Set[FrozenSet[int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_froz",
        sample_code="""from typing import FrozenSet
class C:
    allowed: FrozenSet[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_froz",
        sample_code="""from dataclasses import dataclass
from typing import FrozenSet
@dataclass
class C:
    tags: FrozenSet[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_froz",
        sample_code="""from typing import overload, FrozenSet
@overload
def f(s: FrozenSet[int]) -> int: ...
@overload
def f(s: FrozenSet[str]) -> str: ...
def f(s): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_froz",
        sample_code="""from typing import Protocol, FrozenSet
class P(Protocol):
    def f(self, s: FrozenSet[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_froz",
        sample_code="""from typing import FrozenSet
type IntFSet = FrozenSet[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_froz",
        sample_code="""from typing import FrozenSet
def f(s: "FrozenSet[int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_froz",
        sample_code="""from __future__ import annotations
from typing import FrozenSet
def f(s: FrozenSet[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_froz",
        sample_code="""from typing import FrozenSet
def f(s: FrozenSet[
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_froz",
        sample_code="""from typing import FrozenSet
s: FrozenSet[int]  # immutable ints""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_froz",
        sample_code="""def f(s: frozenset[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_FrozenSet",
        sample_code="""from typing import FrozenSet
s: FrozenSet  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="froz_of_any",
        sample_code="""from typing import FrozenSet, Any
s: FrozenSet[Any]""",
        errors=["reportDeprecated"],
    ),
]
