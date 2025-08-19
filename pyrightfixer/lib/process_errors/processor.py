from pyrightfixer.lib.process_errors.step import StepBase, StepDeprecated
from pyrightfixer.lib.pyright import Diagnostic


class ProcessorState:
    IDLE = "idle"
    ERROR_STARTED = "error_started"

class Processor:
    step_mapping: dict[str, StepBase] = {
        "reportDeprecated": StepDeprecated,
    }

    def __init__(self, errors: list[Diagnostic]) -> None:
        self.errors = errors
        self.state = ProcessorState.IDLE
        self.current_error: Diagnostic | None = None
        self.finished = False
        self.current_step: StepBase | None = None

    def next(self, fix=False) -> StepBase | None:
        if not self.errors:
            self.finished = True
            return None
        self.current_error = self.errors.pop()
        self.current_step = self.step_mapping[self.current_error.rule].choose_fix(self.current_error)
        self.current_step.process_theory()
        return self.current_step
        
    def skip(self) -> None: 
        self.current_error = None
        self.current_step = None

    def fix(self) -> None:
        self.current_step.fix()
        self.current_error = None
        self.current_step = None