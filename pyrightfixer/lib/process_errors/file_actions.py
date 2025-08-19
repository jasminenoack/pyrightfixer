from dataclasses import dataclass
import logging
from pyrightfixer.lib.pyright import Location, Range


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
                end_character += 0
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

@dataclass
class Fix: 
    file: str 
    range: Range
    new_code: str


def get_from_file(file_path: str, range: Range) -> Target:
    with open(file_path, "r") as f:
        lines = f.readlines()

    if range.start.line == range.end.line:
        exact_str = lines[range.start.line][range.start.character : range.end.character]
        return Target(
            exact_target=exact_str,
            file_name=file_path,
            location=range,
            expanded_target=exact_str,
        )
    exact_str = lines[range.start.line][range.start.character :]
    for line in range(range.start.line + 1, range.end.line):
        exact_str += lines[line]
    exact_str += lines[range.end.line][: range.end.character]
    return Target(
        exact_target=exact_str,
        file_name=file_path,
        location=range,
        expanded_target=exact_str,
    )







def replace_in_file(fix: Fix) -> None:
    file_path = fix.file
    range = fix.range
    new_text = fix.new_code
    with open(file_path, "r") as f:
        lines = f.readlines()
    if range.start.line == range.end.line:
        lines[range.start.line] = (
            lines[range.start.line][: range.start.character]
            + new_text
            + lines[range.start.line][range.end.character :]
        )
    else:
        lines[range.start.line] = lines[range.start.line][: range.start.character] + new_text + lines[range.end.line][range.end.character :]
        for line in range(range.start.line + 1, range.end.line):
            lines[line] = ""

    with open(file_path, "w") as f:
        f.writelines(lines)
