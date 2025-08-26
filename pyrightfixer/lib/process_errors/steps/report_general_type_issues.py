
from pyrightfixer.lib.process_errors.file_actions import Fix
from pyrightfixer.lib.process_errors.steps.step_base import StepBase


class GeneralTypeIssues(StepBase):
    def develop_theory(self, log: bool=True):
        message = self.error.message
        if "overrides a field of the same name but is missing" in message:
            self.code_snippet.move_to_top()
            self.proposed_fix = Fix(
                file=self.code_snippet.file_name,
                range=self.code_snippet.location,
                new_code=f"# pyright: reportGeneralTypeIssues=false\n",
            )
        