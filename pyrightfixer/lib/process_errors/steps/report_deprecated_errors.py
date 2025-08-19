
from pyrightfixer.lib.process_errors.file_actions import Fix
from pyrightfixer.lib.process_errors.steps.step_base import StepBase
from pyrightfixer.lib.pyright import Diagnostic


class StepDeprecated(StepBase):
    @classmethod
    def choose_fix(cls, error: Diagnostic) -> None: 
        code_snippet= cls.get_actual_code_snipet(error)
        match code_snippet.exact_target:
            case "Optional":
                return StepOptional(
                    error=error,
                    code_snippet=code_snippet
                )
            case "List":
                return StepDowncase(
                    error=error,
                    code_snippet=code_snippet
                )
            case "Dict":
                return StepDowncase(
                    error=error,
                    code_snippet=code_snippet
                )
            case "Set":
                return StepDowncase(
                    error=error,
                    code_snippet=code_snippet
                )
            case "Tuple":
                return StepDowncase(
                    error=error,
                    code_snippet=code_snippet
                )
            case "Union":
                return StepUnion(
                    error=error,
                    code_snippet=code_snippet
                )
            case _: 
                return StepDeprecated(
                    error=error,
                    code_snippet=code_snippet
                )

        

class StepOptional(StepDeprecated):
    def develop_theory(self) -> None:
        self.code_snippet.expand_target(add_brackets=True)
        current_code = self.code_snippet.expanded_target
        assert current_code.startswith("Optional[")
        assert current_code.endswith("]")
        new_code = current_code[9:-1]
        new_string = f"{new_code} | None"
        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code=new_string
        )

    

class StepDowncase(StepDeprecated):
    def develop_theory(self):
        current_code = self.code_snippet.expanded_target
        assert current_code in ["List", "Dict", "Set", "Tuple"]
        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code=current_code.lower()
        )

class StepUnion(StepDeprecated):
    def develop_theory(self) -> None:
        self.code_snippet.expand_target(add_brackets=True)
        current_code = self.code_snippet.expanded_target
        assert current_code.startswith("Union[")
        assert current_code.endswith("]")
        current_code = current_code[6:-1]
        new_code = ""
        level = 0
        for char in current_code:
            next = char
            if char == "[":
                level += 1
            elif char == "]":
                level -= 1
            if char == "," and level == 0:
                next = " |"
            new_code += next
        self.proposed_fix = Fix(
            file=self.code_snippet.file_name,
            range=self.code_snippet.location,
            new_code=new_code.strip()
        )
        