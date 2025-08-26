
import re
from pyrightfixer.lib.process_errors.file_actions import Fix
from pyrightfixer.lib.process_errors.steps.step_base import StepBase


class ReportUnknownParameter(StepBase):
    def develop_theory(self, log: bool=True):
        self.code_snippet.expand_to_full_function()

        fix = None

        arguments_start = self.code_snippet.expanded_target.index("(") + 1
        arguments_end = self.code_snippet.expanded_target.index(")")
        arguments = self.code_snippet.expanded_target[arguments_start:arguments_end]
        

        if "Return type is unknown" in self.error.message:
            if ":  # -> " in self.code_snippet.expanded_target:
                fix = self.code_snippet.expanded_target.replace(":  # -> ", " -> ")
            else: 
                fix = self.code_snippet.expanded_target.replace("):", ") -> Any :")
        elif "Type of parameter" in self.error.message or "Type annotation is missing for parameter" in self.error.message:
            if f"{self.code_snippet.exact_target}," in arguments:
                fix = self.code_snippet.expanded_target.replace(f"{self.code_snippet.exact_target},", f"{self.code_snippet.exact_target}: Any,")
            elif f"{self.code_snippet.exact_target})" in arguments:
                fix = self.code_snippet.expanded_target.replace(f"{self.code_snippet.exact_target})", f"{self.code_snippet.exact_target}: Any)")
            elif f"{self.code_snippet.exact_target}=" in arguments:
                new_arguments = arguments.replace(f"{self.code_snippet.exact_target}=", f"{self.code_snippet.exact_target}: Any =")
                if arguments != new_arguments:
                    fix = self.code_snippet.expanded_target[:arguments_start] + new_arguments + self.code_snippet.expanded_target[arguments_end:]
            elif f"{self.code_snippet.exact_target}\n" in arguments:
                new_arguments = arguments.replace(f"{self.code_snippet.exact_target}\n", f"{self.code_snippet.exact_target}: Any\n")
                if arguments != new_arguments:
                    fix = self.code_snippet.expanded_target[:arguments_start] + new_arguments + self.code_snippet.expanded_target[arguments_end:]
                
        if fix: 
            self.proposed_fix = Fix(
                    file=self.code_snippet.file_name,
                    range=self.code_snippet.location,
                    new_code=fix,
                )