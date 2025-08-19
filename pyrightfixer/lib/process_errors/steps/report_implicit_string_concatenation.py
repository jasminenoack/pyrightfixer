
import re
from pyrightfixer.lib.process_errors.file_actions import Fix
from pyrightfixer.lib.process_errors.steps.step_base import StepBase


class ImplicitStringConcatenation(StepBase):
    def develop_theory(self, log: bool=True):
        code_snippet = self.code_snippet
        target = code_snippet.exact_target
        self.proposed_fix = Fix(
            file=code_snippet.file_name,
            range=code_snippet.location,
            new_code=f"({target})",
        )