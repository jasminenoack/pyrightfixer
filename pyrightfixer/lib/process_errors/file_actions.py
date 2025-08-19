from dataclasses import dataclass
import logging
from pyrightfixer.lib.pyright import Location, Range


@dataclass 
class Target:
    exact_target: str
    file_name: str
    location: Range
    expanded_target: str

    def expand_target(self, add_brackets=False) -> "Target":
        current_end = self.location.end
        with open(self.file_name, "r") as f:
            lines = f.readlines()
        if add_brackets:
            end_line = current_end.line
            end_character = current_end.character
            next_character = lines[end_line][end_character]
            if next_character != "[":
                logging.warning(
                    f"Next character after range end is not a bracket: {next_character}"
                )
            bracket_end_found = False 
            while not bracket_end_found: 
                if end_line >= len(lines):
                    logging.warning("Reached end of file while expanding target.")
                    break
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
