from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="dict_param",
        sample_code="""from typing import Dict
def f(d: Dict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_return",
        sample_code="""from typing import Dict
def g() -> Dict[int, str]: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_var",
        sample_code="""from typing import Dict
d: Dict[str, float] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="qualified_dict",
        sample_code="""import typing
def f(d: typing.Dict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="aliased_dict",
        sample_code="""import typing as t
def f(d: t.Dict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="imported_as_D",
        sample_code="""from typing import Dict as D
def f(d: D[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_of_lists",
        sample_code="""from typing import Dict, List
d: Dict[str, List[int]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_of_unions",
        sample_code="""from typing import Dict, Union
d: Dict[str, Union[int, float]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_of_dicts",
        sample_code="""from typing import Dict
nested: Dict[str, Dict[int, str]] = {}""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="callable_with_dict_param",
        sample_code="""from typing import Callable, Dict
F: Callable[[Dict[str, int]], None]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="tuple_with_dicts",
        sample_code="""from typing import Tuple, Dict
T: Tuple[Dict[str, int], Dict[str, str]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="set_of_dicts",
        sample_code="""from typing import Set, Dict
S: Set[Dict[str, int]]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="class_attr_dict",
        sample_code="""from typing import Dict
class C:
    mapping: Dict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dataclass_dict",
        sample_code="""from dataclasses import dataclass
from typing import Dict
@dataclass
class C:
    mapping: Dict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="overload_dict",
        sample_code="""from typing import overload, Dict
@overload
def f(d: Dict[str, int]) -> int: ...
@overload
def f(d: Dict[int, str]) -> str: ...
def f(d): ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="protocol_dict",
        sample_code="""from typing import Protocol, Dict
class P(Protocol):
    def f(self, d: Dict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="typeddict_dict",
        sample_code="""from typing import TypedDict, Dict
class TD(TypedDict):
    k: Dict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="pep695_alias_dict",
        sample_code="""from typing import Dict
type StrIntMap = Dict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="forward_ref_dict",
        sample_code="""from typing import Dict
def f(d: "Dict[str, int]") -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="future_annotations_dict",
        sample_code="""from __future__ import annotations
from typing import Dict
def f(d: Dict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="multiline_dict",
        sample_code="""from typing import Dict
def f(d: Dict[
    str,
    int
]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="inline_comment_dict",
        sample_code="""from typing import Dict
d: Dict[str, int]  # mapping""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="already_pep585_dict",
        sample_code="""def f(d: dict[str, int]) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="bare_Dict",
        sample_code="""from typing import Dict
d: Dict  # no parameters (deprecated)""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="dict_with_any",
        sample_code="""from typing import Dict, Any
d: Dict[str, Any]""",
        errors=["reportDeprecated"],
    ),
]
