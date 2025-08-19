
import os
from pyrightfixer.lib.process_errors.file_actions import Fix, Target
from pyrightfixer.lib.process_errors.steps.step_base import StepBase
from pyrightfixer.lib.pyright import Diagnostic


class StepMissingType(StepBase):
    @classmethod
    def choose_fix(cls, error: Diagnostic) -> None: 
        code_snippet= cls.get_actual_code_snipet(error)
        match code_snippet.exact_target:
            case "dict":
                return StepAppendAnyAny(
                    error=error,
                    code_snippet=code_snippet
                )
            case "Callable":
                return CallableGeneric(
                    error=error,
                    code_snippet=code_snippet
                )
            case _: 
                return AppendAny(
                    error=error,
                    code_snippet=code_snippet
                )


class StepAppendAnyAny(StepMissingType):
    def develop_theory(self) -> None:
        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code=f"{self.code_snippet.exact_target}[Any, Any]"
        )

class AppendAny(StepMissingType):
    def develop_theory(self) -> None:
        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code=f"{self.code_snippet.exact_target}[Any]"
        )


class CallableGeneric(StepMissingType):
    def develop_theory(self) -> None:
        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code="Callable[..., Any]"
        )




        
        

# class StepOptional(StepDeprecated):
#     def develop_theory(self) -> None:
#         self.code_snippet.add_brackets_to_target()
#         current_code = self.code_snippet.expanded_target
#         assert current_code.startswith("Optional[")
#         assert current_code.endswith("]")
#         new_code = current_code[9:-1]
#         new_string = f"{new_code} | None"
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code=new_string
#         )

    

# class StepDowncase(StepDeprecated):
#     def __init__(self, error: Diagnostic, code_snippet: Target) -> None:
#         super().__init__(error, code_snippet)
#         self.auto_fix = os.environ.get("PYRIGHTFIXER_AUTO_DOWNCASE") == "1"
    
#     def develop_theory(self):
#         current_code = self.code_snippet.expanded_target
#         assert current_code in ["List", "Dict", "Set", "Tuple", "Type"]
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code=current_code.lower()
#         )

# class StepUnion(StepDeprecated):
#     def develop_theory(self) -> None:
#         self.code_snippet.add_brackets_to_target()
#         current_code = self.code_snippet.expanded_target
#         assert current_code.startswith("Union[")
#         assert current_code.endswith("]")
#         current_code = current_code[6:-1]
#         current_code = current_code.replace("\n", " ").strip()
#         if current_code.endswith(","):
#             current_code = current_code[:-1].strip()
#         new_code = ""
#         level = 0
#         for char in current_code:
#             next = char
#             if char == "[":
#                 level += 1
#             elif char == "]":
#                 level -= 1
#             elif char == " " and new_code.endswith(" "):
#                 next = ""
#             elif char == "," and level == 0:
#                 next = " |"
#             new_code += next
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code=new_code.strip()
#         )
        