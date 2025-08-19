from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="chainmap_param",
        sample_code="""from typing import ChainMap
def f(cm: ChainMap[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="chainmap_return",
        sample_code="""from typing import ChainMap
def g() -> ChainMap[str, int]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="chainmap_var",
        sample_code="""from typing import ChainMap
cm: ChainMap[str, int] = ChainMap()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_chainmap",
        sample_code="""import typing
def f(cm: typing.ChainMap[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_chainmap",
        sample_code="""import typing as t
def f(cm: t.ChainMap[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_CM",
        sample_code="""from typing import ChainMap as CM
def f(cm: CM[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="chainmap_of_lists",
        sample_code="""from typing import ChainMap, List
cm: ChainMap[str, List[int]] = ChainMap()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="chainmap_of_unions",
        sample_code="""from typing import ChainMap, Union
cm: ChainMap[str, Union[int, float]] = ChainMap()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="nested_chainmaps",
        sample_code="""from typing import ChainMap
nested: ChainMap[str, ChainMap[int, str]] = ChainMap()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_chainmap",
        sample_code="""from typing import Callable, ChainMap
F: Callable[[ChainMap[str, int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_chainmap",
        sample_code="""from typing import Tuple, ChainMap
T: Tuple[ChainMap[str, int], ChainMap[int, str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_chainmaps",
        sample_code="""from typing import Set, ChainMap
S: Set[ChainMap[str, int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_chainmap",
        sample_code="""from typing import ChainMap
class C:
    mapping: ChainMap[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_chainmap",
        sample_code="""from dataclasses import dataclass
from typing import ChainMap
@dataclass
class C:
    cache: ChainMap[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_chainmap",
        sample_code="""from typing import overload, ChainMap
@overload
def f(cm: ChainMap[str, int]) -> int: ...
@overload
def f(cm: ChainMap[int, str]) -> str: ...
def f(cm): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_chainmap",
        sample_code="""from typing import Protocol, ChainMap
class P(Protocol):
    def f(self, cm: ChainMap[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_chainmap",
        sample_code="""from typing import ChainMap
type StrIntCM = ChainMap[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_chainmap",
        sample_code="""from typing import ChainMap
def f(cm: "ChainMap[str, int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_chainmap",
        sample_code="""from __future__ import annotations
from typing import ChainMap
def f(cm: ChainMap[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_chainmap",
        sample_code="""from typing import ChainMap
def f(cm: ChainMap[
    str,
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_chainmap",
        sample_code="""from typing import ChainMap
cm: ChainMap[str, int]  # chain of dicts""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_chainmap",
        sample_code="""from collections import ChainMap
def f(cm: ChainMap[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_ChainMap",
        sample_code="""from typing import ChainMap
cm: ChainMap  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="chainmap_with_any",
        sample_code="""from typing import ChainMap, Any
cm: ChainMap[str, Any]""",
        errors=["reportDeprecated"],
    ),
]
