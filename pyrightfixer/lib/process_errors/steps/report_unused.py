
import re
from pyrightfixer.lib.process_errors.file_actions import Fix
from pyrightfixer.lib.process_errors.steps.step_base import StepBase


class StepUnusedImport(StepBase):
    def develop_theory(self, log: bool=True):
        self.code_snippet.expand_to_full_import()
        unused_import = self.code_snippet.exact_target
        line = self.code_snippet.expanded_target
        line: str = line.replace("\n", " ").replace("(", "").replace(")", "")
        if line.strip().endswith(","):
            line = line.strip()[:-1]
        line: str = re.sub(r"\s+", " ", line)
        line += "\n"

        new_line = (
            line.replace(", " + unused_import, "")
            .replace(unused_import + ", ", "")
            .replace(unused_import, "")
        )

        if new_line.strip().endswith("import"):
            new_line = ""

        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code=new_line
        )