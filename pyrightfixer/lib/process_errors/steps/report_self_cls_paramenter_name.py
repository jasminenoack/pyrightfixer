
import re
from pyrightfixer.lib.process_errors.file_actions import Fix
from pyrightfixer.lib.process_errors.steps.step_base import StepBase


class ReportSelfParameterName(StepBase):
    def develop_theory(self, log: bool=True):
        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code='cls'
        )
        