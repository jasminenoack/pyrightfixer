from pyrightfixer.lib.process_errors.file_actions import Fix
from pyrightfixer.lib.process_errors.steps.step_base import StepBase


class IncompleteStub(StepBase):
    def develop_theory(self, log: bool=True):
        message = self.error.message
        if message == 'Type stub file is incomplete; "__getattr__" obscures type errors for module':
            self.code_snippet.expand_to_full_function()
            self.proposed_fix = Fix(
                file=self.code_snippet.file_name,
                range=self.code_snippet.location,
                new_code=""
            )
