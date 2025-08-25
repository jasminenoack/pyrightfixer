from collections import defaultdict
from dataclasses import dataclass
import subprocess

import typer
from pyrightfixer.lib.pyright import Location, Range

dirty_files = set()

@dataclass 
class Target:
    exact_target: str
    file_name: str
    location: Range
    expanded_target: str

    def add_brackets_to_target(self) -> "Target":
        current_end = self.location.end
        with open(self.file_name, "r") as f:
            lines = f.readlines()
        end_line = current_end.line
        end_character = current_end.character
        next_character = lines[end_line][end_character]
        if next_character != "[":
            raise ValueError(
                f"Expected '[' at {self.file_name}:{end_line}:{end_character}, but found '{next_character}'"
            )
        bracket_end_found = False 
        while not bracket_end_found: 
            if end_line >= len(lines):
                raise ValueError(
                    f"Reached end of file {self.file_name} without finding closing bracket for target."
                )
            current_addition = lines[end_line][end_character:]
            if "]" in current_addition:
                end_character += current_addition.index("]") + 1
                self.expanded_target = (
                    self.expanded_target + current_addition[: current_addition.index("]") + 1]
                )
                bracket_end_found = self.expanded_target.count("[") == self.expanded_target.count("]")
            else:
                self.expanded_target += current_addition
                end_character = 0
                end_line += 1
            self.location = Range(
                start=self.location.start,
                end=Location(line=end_line, character=end_character),
            )

    def add_optional_comma_to_target(self) -> "Target":
        current_end = self.location.end
        with open(self.file_name, "r") as f:
            lines = f.readlines()

        next_character = lines[current_end.line][current_end.character]
        if next_character == ",":
            self.expanded_target += ","
            self.location = Range(
                start=self.location.start,
                end=Location(line=current_end.line, character=current_end.character + 1),
            )

    def expand_to_full_import(self) -> "Target":
        with open(self.file_name, "r") as f:
            lines = f.readlines()
        start_line = self.location.start.line
        end_line = self.location.end.line

        while start_line > 0 and not (lines[start_line].startswith("import ") or lines[start_line].startswith("from ")):
            start_line -= 1
        while end_line < len(lines) and lines[end_line].strip().endswith(","):
            end_line += 1

        new_code = "".join(lines[start_line:end_line + 1])
        new_code = new_code
        self.expanded_target = new_code
        self.location = Range(
            start=Location(line=start_line, character=0),
            end=Location(line=end_line, character=len(lines[end_line])),
        )

    def find_typing_import(self) -> None:
        with open(self.file_name, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.startswith("from typing"):
                self.location = Range(
                    start=Location(line=i, character=0),
                    end=Location(line=i, character=len(line)),
                )
                self.expand_to_full_import()
                return
            
        first_non_docstring_line = self.first_non_docstring_line(lines)
        
        self.location = Range(
            start=Location(line=first_non_docstring_line + 1, character=0),
            end=Location(line=first_non_docstring_line + 1, character=0),
        )
        self.exact_target = ""
        self.expanded_target = ""

    def first_non_docstring_line(self, lines: list[str]) -> int:
        first_non_docstring_line = 0
        if lines[0].startswith('"""'):
            first_non_docstring_line = 1
            while not '"""' in lines[first_non_docstring_line]:
                first_non_docstring_line += 1
        return first_non_docstring_line

    def move_to_imports(self) -> "Target":
        with open(self.file_name, "r") as f:
            lines = f.readlines()
        first_non_docstring_line = self.first_non_docstring_line(lines)
        
        self.location = Range(
            start=Location(line=first_non_docstring_line + 1, character=0),
            end=Location(line=first_non_docstring_line + 1, character=0),
        )

    def move_to_top(self) -> "Target":
        self.location = Range(
            start=Location(line=0, character=0),
            end=Location(line=0, character=0),
        )

    def expand_to_full_function(self) -> "Target":
        with open(self.file_name, "r") as f:
            lines = f.readlines()
        start_line = self.location.start.line
        end_line = self.location.end.line

        while start_line > 0 and not lines[start_line].lstrip().startswith("def ") and not lines[start_line].lstrip().startswith("async def "):
            start_line -= 1

        start_indent = len(lines[start_line]) - len(lines[start_line].lstrip())
        end_line = start_line + 1

        while (
            end_line < len(lines) and (
                (
                    lines[end_line].strip() == ""
                or lines[end_line].strip().startswith("):")
                or lines[end_line].strip().startswith(") ->")
                )
             or
              (len(lines[end_line]) - len(lines[end_line].lstrip())) > start_indent 
            )
        ):
            end_line += 1

        new_code = "".join(lines[start_line:end_line])
        self.expanded_target = new_code
        self.location = Range(
            start=Location(line=start_line, character=0),
            end=Location(line=end_line, character=0),
        )


@dataclass
class Fix: 
    file: str 
    range: Range
    new_code: str


def get_from_file(file_path: str, current_range: Range) -> Target:
    with open(file_path, "r") as f:
        lines = f.readlines()

    if current_range.start.line == current_range.end.line:
        exact_str = lines[current_range.start.line][current_range.start.character : current_range.end.character]
        return Target(
            exact_target=exact_str,
            file_name=file_path,
            location=current_range,
            expanded_target=exact_str,
        )
    exact_str = lines[current_range.start.line][current_range.start.character :]
    for line in range(current_range.start.line + 1, current_range.end.line):
        exact_str += lines[line]
    exact_str += lines[current_range.end.line][: current_range.end.character]
    return Target(
        exact_target=exact_str,
        file_name=file_path,
        location=current_range,
        expanded_target=exact_str,
    )







def replace_in_file(fix: Fix) -> None:
    global dirty_files
    file_path = fix.file
    if file_path in dirty_files:
        typer.echo(f"File {file_path} already modified, skipping.")
        return
    current_range = fix.range
    new_text = fix.new_code
    with open(file_path, "r") as f:
        lines = f.readlines()

    line_count = len(lines)

    new_lines = []
    for i, line in enumerate(lines):
        if i < current_range.start.line or i > current_range.end.line:
            new_lines.append(line)
        elif i == current_range.start.line and i == current_range.end.line:
            new_lines.append(
                line[:current_range.start.character] + new_text + line[current_range.end.character:]
            )
        elif i == current_range.start.line:
            new_lines.append(line[:current_range.start.character] + new_text)
        elif i == current_range.end.line:
            new_lines.append(line[current_range.end.character:])
        else:
            new_lines.append("")

    new_lines = "".join(new_lines).splitlines(keepends=True)

    new_line_count = len(new_lines)
    if new_line_count != line_count:
        dirty_files.add(file_path)

    with open(file_path, "w") as f:
        f.writelines(new_lines)


def check_if_file_is_dirty(file_path: str) -> bool:
    return file_path in dirty_files

def grep(pattern: str) -> list[str]:
    p = subprocess.run(
        ["grep", "-r", "-E", pattern, str('.')],
        capture_output=True, text=True
    )
    return p.stdout.splitlines() if p.stdout else []