from samples.sample_wrapper import SampleWrapper


samples = [
    SampleWrapper(
        sample_name="long_1",
        sample_code="""from typing import Union, Optional, List
from types import NoneType
from pathlib import Path

# deprecated
def bad_union(x: Union[int, str]) -> None:
    ...

def bad_optional(x: Optional[int]) -> None:
    ...

# good new-style
def good_union(x: int | str) -> None:
    ...

def good_optional(x: int | None) -> None:
    ...

# unrelated, still valid
def takes_none(n: NoneType) -> None:
    ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_2",
        sample_code="""from typing import Dict, List, OrderedDict
from collections import defaultdict, deque, Counter
from dataclasses import dataclass

# deprecated
old_map: Dict[str, int] = {}
old_od: OrderedDict[str, int] = OrderedDict()

# new-style good
new_map: dict[str, int] = {}
new_deque: deque[int] = deque()

# real code
@dataclass
class User:
    name: str
    tags: list[str]
    counts: Counter[str]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_3",
        sample_code="""from typing import Tuple, Type
from types import NoneType

# deprecated
pair: Tuple[int, str] = (1, "a")
factory: Type[int]

# good new-style
numbers: tuple[int, ...] = (1, 2, 3)
cls: type[str]

# valid modern typing
none_value: NoneType = None""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_4",
        sample_code="""from __future__ import annotations
from typing import Callable, Annotated, Literal, Dict, List, Optional, Union

# deprecated in args
F: Callable[[List[Optional[int]], Dict[str, Union[int, str]]], None]

# modern / good
G: Callable[[list[int | None], dict[str, int | str]], None]

# other features to ensure no false positives
X = Annotated[int, "meta"]
Y = Literal["a", "b"]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_5",
        sample_code="""from typing import Dict, List, OrderedDict, DefaultDict, Deque, Counter, ChainMap
from collections import defaultdict, deque, Counter as CCounter, ChainMap as CChainMap
from dataclasses import dataclass

# deprecated
old_map: Dict[str, int] = {}
old_list: List[int] = []
old_od: OrderedDict[str, int] = OrderedDict()
old_dd: DefaultDict[str, int] = DefaultDict(int)
old_dq: Deque[int] = Deque()
old_counter: Counter[str] = Counter()
old_cm: ChainMap[str, int] = ChainMap()

# modern / good
new_map: dict[str, int] = {}
new_list: list[int] = []
new_dd = defaultdict(int)              # value-level usage (not a type)
new_dq: deque[int] = deque()
new_counter: CCounter[str] = CCounter()
new_cm: CChainMap[str, int] = CChainMap()

@dataclass
class User:
    name: str
    tags: list[str]
    scores: dict[str, int]""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_6",
        sample_code="""import typing as t
from typing import List as L, Dict as D, Union as U, Optional as O, Type as T
from types import NoneType
from collections import deque, defaultdict

# deprecated via aliasing
a: L[int] = []
m: D[str, int] = {}
u: U[int, str] | None  # Note: this part is already modern for union
o: O[int]
cls: T[int]

# modern / good
b: list[int] = []
n: dict[str, int] = {}
dq: deque[int] = deque()
dd = defaultdict(int)

def takes_none(n: NoneType) -> None: ...""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_7",
        sample_code="""from typing import Protocol, TypedDict, Dict, List

# deprecated inside containers
Data: Dict[str, List[int]] = {}

# modern / good TypedDict + Protocol usage
class Payload(TypedDict):
    id: int
    name: str

class P(Protocol):
    def f(self, x: list[int]) -> None: ...

def use(p: P, payload: Payload) -> None:
    p.f([payload["id"]])""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_8",
        sample_code="""from typing import Tuple, Type, Union
from types import NoneType

# deprecated
pair: Tuple[int, str] = (1, "a")
variadic: Tuple[int, ...] = (1, 2, 3)
cls_t: Type[int]
mixed: Tuple[int, Union[str, bytes]]

# modern / good
pair_ok: tuple[int, str] = (1, "a")
variadic_ok: tuple[int, ...] = (1, 2, 3)
cls_ok: type[str]
none_val: NoneType = None""",
        errors=["reportDeprecated"],
    ),
    SampleWrapper(
        sample_name="long_9",
        sample_code="""from __future__ import annotations
from typing import Union, Optional, List, Dict
from types import NoneType
from pathlib import Path

# deprecated
def bad_union(x: Union[int, str]) -> None: ...
def bad_nested_union(x: Union[int, Union[str, bytes]]) -> None: ...
def bad_optional(x: Optional[int]) -> None: ...
files: Dict[str, Union[Path, str]] = {}

# modern / good
def good_union(x: int | str) -> None: ...
def good_optional(x: int | None) -> None: ...
paths: dict[str, Path | str] = {}

# unrelated correct usage
def takes_none(n: NoneType) -> None: ...
items: list[int] = [1, 2, 3]""",
        errors=["reportDeprecated"],
    ),
]
