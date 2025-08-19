from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="deque_param",
        sample_code="""from typing import Deque
def f(d: Deque[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="deque_return",
        sample_code="""from typing import Deque
def g() -> Deque[str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="deque_var",
        sample_code="""from typing import Deque
dq: Deque[bytes] = Deque()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_deque",
        sample_code="""import typing
def f(d: typing.Deque[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_deque",
        sample_code="""import typing as t
def f(d: t.Deque[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_DQ",
        sample_code="""from typing import Deque as DQ
def f(d: DQ[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="deque_of_unions",
        sample_code="""from typing import Deque, Union
d: Deque[Union[int, str]] = Deque()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="deque_of_optionals",
        sample_code="""from typing import Deque, Optional
d: Deque[Optional[int]] = Deque()""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_with_deque_value",
        sample_code="""from typing import Dict, Deque
D: Dict[str, Deque[int]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_deque",
        sample_code="""from typing import Callable, Deque
F: Callable[[Deque[int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_deque",
        sample_code="""from typing import Tuple, Deque
T: Tuple[Deque[int], Deque[str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_deques",
        sample_code="""from typing import Set, Deque
S: Set[Deque[int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_deque",
        sample_code="""from typing import Deque
class C:
    buffer: Deque[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_deque",
        sample_code="""from dataclasses import dataclass
from typing import Deque
@dataclass
class C:
    buffer: Deque[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_deque",
        sample_code="""from typing import overload, Deque
@overload
def f(d: Deque[int]) -> int: ...
@overload
def f(d: Deque[str]) -> str: ...
def f(d): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_deque",
        sample_code="""from typing import Protocol, Deque
class P(Protocol):
    def f(self, d: Deque[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_deque",
        sample_code="""from typing import Deque
type IntDeque = Deque[int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_deque",
        sample_code="""from typing import Deque
def f(d: "Deque[int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_deque",
        sample_code="""from __future__ import annotations
from typing import Deque
def f(d: Deque[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_deque",
        sample_code="""from typing import Deque
def f(d: Deque[
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_deque",
        sample_code="""from typing import Deque
dq: Deque[int]  # int buffer""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_deque",
        sample_code="""from collections import deque
def f(d: deque[int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_Deque",
        sample_code="""from typing import Deque
dq: Deque  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="deque_of_any",
        sample_code="""from typing import Deque, Any
dq: Deque[Any]""",
        errors=["reportDeprecated"],
    ),
]
