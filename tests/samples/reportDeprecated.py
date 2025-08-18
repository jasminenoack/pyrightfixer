"""
Samples for fixing the reportDeprecated rule
"""

simple_union = """
def save(self, file_path: Union[Path, str]) -> None:
    ...
"""

long_union = """
def save(self, file_path: Union[Path, str, bytes, int]) -> None:
    ...
"""

nested_in_unions = """
def save(self, file_path: Union[Path, Union[str, bytes]]) -> None:
    ...
"""

dict_nested_in_unions = """
def save(self, file_path: Union[Path, Dict[str, Union[str, bytes]]) -> None:
    ...
"""

list_nested_in_unions = """
def save(self, file_path: Union[Path, List[Union[str, bytes]]]) -> None:
    ...
"""


