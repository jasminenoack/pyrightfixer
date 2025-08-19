
import os

import typer
from pyrightfixer.lib.process_errors.file_actions import Fix, Target, grep
from pyrightfixer.lib.process_errors.steps.step_base import StepBase
from pyrightfixer.lib.pyright import Diagnostic


class StepDunderAll(StepBase):
    @classmethod
    def choose_fix(cls, error: Diagnostic) -> None: 
        code_snippet= cls.get_actual_code_snipet(error)
        target = code_snippet.exact_target
        object_name = target[1:-1]
        if object_name.upper() == object_name:
            return cls(
                    error=error,
                    code_snippet=code_snippet
                )
        elif object_name[0].upper() == object_name[0]:
            # If the first letter is uppercase, it is probably a class
            return ClassDunderAll(error, code_snippet)
        else:
            return cls(
                error=error,
                code_snippet=code_snippet
            )
            
class ClassDunderAll(StepDunderAll):
    def develop_theory(self, log: bool=True) -> None:
        target = self.code_snippet.exact_target
        object_name = target[1:-1]

        choosen_solution = None

        lines = grep(f'{object_name}')

        if len(lines) == 1:
            choosen_solution = f"# {object_name}"

        lines_with_class_defs = [
            line 
            for line in lines 
            if f"class {object_name}:" in line or f"class {object_name}(" in line
        ]


        from_site_packages = [
            line
            for line in lines_with_class_defs
            if "site-packages" in line
        ]


        if from_site_packages and len(from_site_packages) == 1:
            path = from_site_packages[0].split("site-packages")[1]
            parts = path.split("/")
            usable_parts = parts[1:-1]
            choosen_solution = f"from {'.'.join(usable_parts)} import {object_name}\n"
            self.code_snippet.move_to_imports()



        if choosen_solution:
            self.proposed_fix = Fix(
                file=self.code_snippet.file_name,
                range=self.code_snippet.location,
                new_code=choosen_solution
            )
            
# class AddToTyping(StepReportUndefined):
#     def develop_theory(self, log: bool=True) -> None:
#         target = self.code_snippet.exact_target
#         self.code_snippet.find_typing_import()
#         expanded_target = self.code_snippet.expanded_target
#         if target in expanded_target:
#             self.already_fixed = True
#             return
#         if expanded_target == "":
#             expanded_target = f"from typing import {target}\n"
#         elif "(" in expanded_target:
#             expanded_target = expanded_target.replace(f"(", "(\n {target},")
#         else:
#             expanded_target = expanded_target.strip() + f", {target}\n"
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code=expanded_target
#         )

# class StepAppendAnyAny(StepMissingType):
#     def develop_theory(self, log: bool=True) -> None:
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code=f"{self.code_snippet.exact_target}[Any, Any]"
#         )

# class AppendAny(StepMissingType):
#     def develop_theory(self, log: bool=True) -> None:
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code=f"{self.code_snippet.exact_target}[Any]"
#         )


# class CallableGeneric(StepMissingType):
#     def develop_theory(self, log: bool=True) -> None:
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code="Callable[..., Any]"
#         )




        
        

# class StepOptional(StepDeprecated):
#     def develop_theory(self, log: bool=True) -> None:
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
    
#     def develop_theory(self, log: bool=True):
#         current_code = self.code_snippet.expanded_target
#         assert current_code in ["List", "Dict", "Set", "Tuple", "Type"]
#         self.proposed_fix = Fix(
#             file=self.code_snippet.file_name,
#             range=self.code_snippet.location,
#             new_code=current_code.lower()
#         )

# class StepUnion(StepDeprecated):
#     def develop_theory(self, log: bool=True) -> None:
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
        