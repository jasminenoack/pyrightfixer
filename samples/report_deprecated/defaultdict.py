from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="defaultdict_param",
        sample_code="""from typing import DefaultDict
def f(d: DefaultDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="defaultdict_return",
        sample_code="""from typing import DefaultDict
def g() -> DefaultDict[str, int]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="defaultdict_var",
        sample_code="""from typing import DefaultDict
d: DefaultDict[str, int] = DefaultDict(int)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_defaultdict",
        sample_code="""import typing
def f(d: typing.DefaultDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_defaultdict",
        sample_code="""import typing as t
def f(d: t.DefaultDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_DD",
        sample_code="""from typing import DefaultDict as DD
def f(d: DD[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="defaultdict_of_lists",
        sample_code="""from typing import DefaultDict, List
d: DefaultDict[str, List[int]] = DefaultDict(list)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="defaultdict_of_unions",
        sample_code="""from typing import DefaultDict, Union
d: DefaultDict[str, Union[int, float]] = DefaultDict(int)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="nested_defaultdicts",
        sample_code="""from typing import DefaultDict
nested: DefaultDict[str, DefaultDict[int, str]] = DefaultDict(dict)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_defaultdict",
        sample_code="""from typing import Callable, DefaultDict
F: Callable[[DefaultDict[str, int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_defaultdicts",
        sample_code="""from typing import Tuple, DefaultDict
T: Tuple[DefaultDict[str, int], DefaultDict[int, str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_defaultdicts",
        sample_code="""from typing import Set, DefaultDict
S: Set[DefaultDict[str, int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_defaultdict",
        sample_code="""from typing import DefaultDict
class C:
    mapping: DefaultDict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_defaultdict",
        sample_code="""from dataclasses import dataclass
from typing import DefaultDict
@dataclass
class C:
    cache: DefaultDict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_defaultdict",
        sample_code="""from typing import overload, DefaultDict
@overload
def f(d: DefaultDict[str, int]) -> int: ...
@overload
def f(d: DefaultDict[int, str]) -> str: ...
def f(d): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_defaultdict",
        sample_code="""from typing import Protocol, DefaultDict
class P(Protocol):
    def f(self, d: DefaultDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_defaultdict",
        sample_code="""from typing import DefaultDict
type StrIntDD = DefaultDict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_defaultdict",
        sample_code="""from typing import DefaultDict
def f(d: "DefaultDict[str, int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_defaultdict",
        sample_code="""from __future__ import annotations
from typing import DefaultDict
def f(d: DefaultDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_defaultdict",
        sample_code="""from typing import DefaultDict
def f(d: DefaultDict[
    str,
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_defaultdict",
        sample_code="""from typing import DefaultDict
d: DefaultDict[str, int]  # mapping""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_defaultdict",
        sample_code="""from collections import defaultdict
def f(d: defaultdict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_DefaultDict",
        sample_code="""from typing import DefaultDict
d: DefaultDict  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="defaultdict_with_any",
        sample_code="""from typing import DefaultDict, Any
d: DefaultDict[str, Any]""",
        errors=["reportDeprecated"],
    ),
]
