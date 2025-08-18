from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="counter_param",
        sample_code="""from typing import Counter
def f(c: Counter[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="counter_return",
        sample_code="""from typing import Counter
def g() -> Counter[int]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="counter_var",
        sample_code="""from typing import Counter
c: Counter[str] = Counter()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_counter",
        sample_code="""import typing
def f(c: typing.Counter[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_counter",
        sample_code="""import typing as t
def f(c: t.Counter[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_C",
        sample_code="""from typing import Counter as C
def f(c: C[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="counter_of_unions",
        sample_code="""from typing import Counter, Union
c: Counter[Union[str, int]] = Counter()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="counter_in_dict",
        sample_code="""from typing import Dict, Counter
d: Dict[str, Counter[int]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="list_of_counters",
        sample_code="""from typing import List, Counter
l: List[Counter[str]] = []""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_counter",
        sample_code="""from typing import Callable, Counter
F: Callable[[Counter[str]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_counter",
        sample_code="""from typing import Tuple, Counter
T: Tuple[Counter[str], Counter[int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_counters",
        sample_code="""from typing import Set, Counter
S: Set[Counter[str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_counter",
        sample_code="""from typing import Counter
class C:
    freq: Counter[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_counter",
        sample_code="""from dataclasses import dataclass
from typing import Counter
@dataclass
class C:
    freq: Counter[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_counter",
        sample_code="""from typing import overload, Counter
@overload
def f(c: Counter[str]) -> int: ...
@overload
def f(c: Counter[int]) -> str: ...
def f(c): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_counter",
        sample_code="""from typing import Protocol, Counter
class P(Protocol):
    def f(self, c: Counter[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_counter",
        sample_code="""from typing import Counter
type StrCounter = Counter[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_counter",
        sample_code="""from typing import Counter
def f(c: "Counter[str]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_counter",
        sample_code="""from __future__ import annotations
from typing import Counter
def f(c: Counter[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_counter",
        sample_code="""from typing import Counter
def f(c: Counter[
    str
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_counter",
        sample_code="""from typing import Counter
c: Counter[str]  # frequency map""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_counter",
        sample_code="""from collections import Counter
def f(c: Counter[str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_Counter",
        sample_code="""from typing import Counter
c: Counter  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="counter_of_any",
        sample_code="""from typing import Counter, Any
c: Counter[Any]""",
        errors=["reportDeprecated"],
    ),
]
