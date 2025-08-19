from abc import ABC

import typer

from pyrightfixer.lib.process_errors.file_actions import Fix, Target, get_from_file, replace_in_file
from pyrightfixer.lib.pyright import Diagnostic

from typing import TypeVar
Self = TypeVar("Self", bound="StepBase")

class StepBase(ABC):
    def __init__(self, error: Diagnostic, code_snippet: Target) -> None:
        self.error = error 
        self.code_snippet = code_snippet
        self.proposed_fix: Fix | None = None

    @classmethod 
    def choose_fix(cls: type[Self], error: Diagnostic) -> Self:
        return cls(
            error=error,
            code_snippet=cls.get_actual_code_snipet(error)
        )
        
    @classmethod 
    def get_actual_code_snipet(self, error: Diagnostic) -> Target:
        code_snippet = get_from_file(error.file, error.range)
        return code_snippet
    
    def develop_theory(self) -> None:
        typer.echo("No proposed fix available for this error.")

    def process_theory(self) -> None:
        self.develop_theory()

        original_code = self.code_snippet.expanded_target
        typer.echo("Current code:")
        typer.echo('------------------------------')
        typer.echo(original_code)
        typer.echo('------------------------------')
        typer.echo("")
        if self.proposed_fix:
            typer.echo("Proposed fix:")
            typer.echo('------------------------------')
            typer.echo(self.proposed_fix.new_code)
            typer.echo('------------------------------')

    def fix(self) -> None:
        replace_in_file(
            fix=self.proposed_fix
        )
