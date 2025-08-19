from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="tuple_param",
        sample_code="""from typing import Tuple
def f(t: Tuple[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_return",
        sample_code="""from typing import Tuple
def g() -> Tuple[int, str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_var",
        sample_code="""from typing import Tuple
t: Tuple[int, str] = (1, "a")""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_variadic_param",
        sample_code="""from typing import Tuple
def f(t: Tuple[int, ...]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_variadic_return",
        sample_code="""from typing import Tuple
def g() -> Tuple[str, ...]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_variadic_var",
        sample_code="""from typing import Tuple
t: Tuple[bytes, ...] = (b"a", b"b")""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_tuple",
        sample_code="""import typing
def f(t: typing.Tuple[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_tuple",
        sample_code="""import typing as t
def f(t: t.Tuple[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_T",
        sample_code="""from typing import Tuple as T
def f(t: T[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_union",
        sample_code="""from typing import Tuple, Union
def f(t: Tuple[int, Union[str, bytes]]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_of_lists",
        sample_code="""from typing import Tuple, List
t: Tuple[List[int], List[str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_variadic_of_optionals",
        sample_code="""from typing import Tuple, Optional
t: Tuple[Optional[int], ...]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_tuple_param",
        sample_code="""from typing import Callable, Tuple
F: Callable[[Tuple[int, str]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_with_tuple_value",
        sample_code="""from typing import Dict, Tuple
D: Dict[str, Tuple[int, str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_tuples",
        sample_code="""from typing import Set, Tuple
S: Set[Tuple[int, str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_tuple",
        sample_code="""from typing import Tuple
class C:
    pair: Tuple[int, str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_tuple",
        sample_code="""from dataclasses import dataclass
from typing import Tuple
@dataclass
class C:
    data: Tuple[int, str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_tuple",
        sample_code="""from typing import overload, Tuple
@overload
def f(t: Tuple[int, str]) -> int: ...
@overload
def f(t: Tuple[str, int]) -> str: ...
def f(t): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_tuple",
        sample_code="""from typing import Protocol, Tuple
class P(Protocol):
    def f(self, t: Tuple[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_tuple",
        sample_code="""from typing import Tuple
type Pair = Tuple[int, str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_tuple",
        sample_code="""from typing import Tuple
def f(t: "Tuple[int, str]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_tuple",
        sample_code="""from __future__ import annotations
from typing import Tuple
def f(t: Tuple[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_tuple",
        sample_code="""from typing import Tuple
def f(t: Tuple[
    int,
    str
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_variadic_multiline",
        sample_code="""from typing import Tuple
def f(t: Tuple[
    int,
    ...
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_tuple",
        sample_code="""from typing import Tuple
t: Tuple[int, str]  # a pair""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_tuple",
        sample_code="""def f(t: tuple[int, str]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_tuple_variadic",
        sample_code="""def f(t: tuple[int, ...]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_Tuple",
        sample_code="""from typing import Tuple
t: Tuple  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_any",
        sample_code="""from typing import Tuple, Any
t: Tuple[Any, Any]""",
        errors=["reportDeprecated"],
    ),
]
