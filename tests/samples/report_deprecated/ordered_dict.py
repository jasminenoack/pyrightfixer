from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="ordereddict_param",
        sample_code="""from typing import OrderedDict
def f(d: OrderedDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="ordereddict_return",
        sample_code="""from typing import OrderedDict
def g() -> OrderedDict[int, str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="ordereddict_var",
        sample_code="""from typing import OrderedDict
d: OrderedDict[str, int] = OrderedDict()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_ordereddict",
        sample_code="""import typing
def f(d: typing.OrderedDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_ordereddict",
        sample_code="""import typing as t
def f(d: t.OrderedDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_OD",
        sample_code="""from typing import OrderedDict as OD
def f(d: OD[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="ordereddict_of_lists",
        sample_code="""from typing import OrderedDict, List
d: OrderedDict[str, List[int]] = OrderedDict()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="ordereddict_of_unions",
        sample_code="""from typing import OrderedDict, Union
d: OrderedDict[str, Union[int, float]] = OrderedDict()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="nested_ordereddicts",
        sample_code="""from typing import OrderedDict
nested: OrderedDict[str, OrderedDict[int, str]] = OrderedDict()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_ordereddict",
        sample_code="""from typing import Callable, OrderedDict
F: Callable[[OrderedDict[str, int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_ordereddict",
        sample_code="""from typing import Tuple, OrderedDict
T: Tuple[OrderedDict[str, int], OrderedDict[int, str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_ordereddicts",
        sample_code="""from typing import Set, OrderedDict
S: Set[OrderedDict[str, int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_ordereddict",
        sample_code="""from typing import OrderedDict
class C:
    mapping: OrderedDict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_ordereddict",
        sample_code="""from dataclasses import dataclass
from typing import OrderedDict
@dataclass
class C:
    cache: OrderedDict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_ordereddict",
        sample_code="""from typing import overload, OrderedDict
@overload
def f(d: OrderedDict[str, int]) -> int: ...
@overload
def f(d: OrderedDict[int, str]) -> str: ...
def f(d): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_ordereddict",
        sample_code="""from typing import Protocol, OrderedDict
class P(Protocol):
    def f(self, d: OrderedDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_ordereddict",
        sample_code="""from typing import OrderedDict
type StrIntOD = OrderedDict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_ordereddict",
        sample_code="""from typing import OrderedDict
def f(d: "OrderedDict[str, int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_ordereddict",
        sample_code="""from __future__ import annotations
from typing import OrderedDict
def f(d: OrderedDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_ordereddict",
        sample_code="""from typing import OrderedDict
def f(d: OrderedDict[
    str,
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_ordereddict",
        sample_code="""from typing import OrderedDict
d: OrderedDict[str, int]  # ordered mapping""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_ordereddict",
        sample_code="""from collections import OrderedDict
def f(d: OrderedDict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_OrderedDict",
        sample_code="""from typing import OrderedDict
d: OrderedDict  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="ordereddict_with_any",
        sample_code="""from typing import OrderedDict, Any
d: OrderedDict[str, Any]""",
        errors=["reportDeprecated"],
    ),
]
