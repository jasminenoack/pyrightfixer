import typer
from pyrightfixer.lib.process_errors.file_actions import check_if_file_is_dirty
from pyrightfixer.lib.process_errors.steps.report_general_type_issues import GeneralTypeIssues
from pyrightfixer.lib.process_errors.steps.report_implicit_string_concatenation import ImplicitStringConcatenation
from pyrightfixer.lib.process_errors.steps.report_incompatible_method_override import IncompatibleMethodOverrideStep
from pyrightfixer.lib.process_errors.steps.report_incompatible_variable_override import IncompatibleVariableOverrideStep
from pyrightfixer.lib.process_errors.steps.report_incomplete_stub import IncompleteStub
from pyrightfixer.lib.process_errors.steps.report_invalid_type_arguments import StepInvalidTypeArguments
from pyrightfixer.lib.process_errors.steps.report_deprecated_errors import StepDeprecated
from pyrightfixer.lib.process_errors.steps.report_missing_type_argument import StepMissingType
from pyrightfixer.lib.process_errors.steps.report_self_cls_paramenter_name import ReportSelfParameterName
from pyrightfixer.lib.process_errors.steps.report_undefined_variable import StepReportUndefined
from pyrightfixer.lib.process_errors.steps.report_unknown_parameter_type import ReportUnknownParameter
from pyrightfixer.lib.process_errors.steps.report_unsupported_dunder_all import StepDunderAll
from pyrightfixer.lib.process_errors.steps.report_unused import StepUnusedImport
from pyrightfixer.lib.process_errors.steps.step_base import StepBase
from pyrightfixer.lib.pyright import Diagnostic


class ProcessorState:
    IDLE = "idle"
    ERROR_STARTED = "error_started"

class Processor:
    step_mapping: dict[str, StepBase] = {
        "reportDeprecated": StepDeprecated,
        "reportUnusedImport": StepUnusedImport,
        "reportMissingTypeArgument": StepMissingType,
        "reportInvalidTypeArguments": StepInvalidTypeArguments,
        "reportInvalidTypeForm": StepInvalidTypeArguments,
        "reportUndefinedVariable": StepReportUndefined,
        "reportImplicitStringConcatenation": ImplicitStringConcatenation,
        "reportUnsupportedDunderAll": StepDunderAll,
        "reportIncompatibleMethodOverride": IncompatibleMethodOverrideStep,
        "reportIncompatibleVariableOverride": IncompatibleVariableOverrideStep,
        "reportIncompleteStub": IncompleteStub,
        "reportUnknownParameterType": ReportUnknownParameter,
        "reportMissingParameterType": ReportUnknownParameter,
        "reportSelfClsParameterName": ReportSelfParameterName,
        "reportGeneralTypeIssues": GeneralTypeIssues,
    }

    def __init__(self, errors: list[Diagnostic]) -> None:
        self.errors = errors
        self.state = ProcessorState.IDLE
        self.current_error: Diagnostic | None = None
        self.finished = False
        self.current_step: StepBase | None = None

    def next(self, log: bool=True) -> StepBase | None:
        if not self.errors:
            self.finished = True
            return None
        self.current_error = self.errors.pop()
        if check_if_file_is_dirty(self.current_error.file):
            if log:
                typer.echo(f"File {self.current_error.file} is modified in unsafe way already, skipping.")
            self.skip()
            return None
        if log:
            typer.echo(f"Processing error:\n    {self.current_error.rule}:{self.current_error.message}")
        self.current_step = self.step_mapping[self.current_error.rule].choose_fix(self.current_error)
        self.current_step.process_theory(log)
        return self.current_step
        
    def skip(self) -> None: 
        self.current_error = None
        self.current_step = None

    def fix(self) -> None:
        self.current_step.fix()
        self.current_error = None
        self.current_step = None