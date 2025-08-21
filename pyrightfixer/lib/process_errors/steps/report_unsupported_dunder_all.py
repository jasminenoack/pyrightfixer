
import os

import typer
from pyrightfixer.lib.process_errors.file_actions import Fix, Target, grep
from pyrightfixer.lib.process_errors.steps.step_base import StepBase
from pyrightfixer.lib.pyright import Diagnostic
from rich import print 


def convert_to_import_path(path: str) -> str:
    path = path.split("site-packages")[1]
    path = path.split(".")[0]
    parts = path.split("/")
    usable_parts = parts[1:]
    return '.'.join(usable_parts)


class StepDunderAll(StepBase):
    @classmethod
    def choose_fix(cls, error: Diagnostic) -> None: 
        code_snippet= cls.get_actual_code_snipet(error)
        return cls(error, code_snippet)
            
    def develop_theory(self, log: bool=True) -> None:
        target = self.code_snippet.exact_target
        object_name = target[1:-1]

        choosen_solution = None

        lines = grep(f'{object_name}')

        _lines_with_class_defs = [
            line 
            for line in lines 
            if f"class {object_name}:" in line or f"class {object_name}(" in line
        ]

        class_from_site_packages = [
            line
            for line in _lines_with_class_defs
            if "site-packages" in line
        ]

        _variable_defs = [
            line for line in lines
            if f":{object_name} = " in line
        ]

        variable_defs_in_site_packages = [
            line for line in _variable_defs
            if "site-packages" in line
        ]

        _function_defs = [
            line for line in lines
            if f":def {object_name}(" in line
        ]

        function_defs_in_site_packages = [
            line for line in _function_defs
            if "site-packages" in line
        ]

        if len(lines) == 1:
            choosen_solution = f"# {object_name}"
        elif class_from_site_packages and len(class_from_site_packages) == 1:
            choosen_solution = f"from {convert_to_import_path(class_from_site_packages[0])} import {object_name}\n"
            self.code_snippet.move_to_imports()
        elif len(class_from_site_packages) > 1 and log:
            choices = [
                convert_to_import_path(path)
                for path in class_from_site_packages
            ]
            for i, choice in enumerate(choices):
                typer.echo(f"{i}: {choice}")
            typer.echo("Multiple locations found, please select one:")
            selected = typer.prompt("Enter the number of your choice", type=int)
            if 0 <= selected < len(choices):
                choosen_solution = f"from {choices[selected]} import {object_name}\n"
                self.code_snippet.move_to_imports()
        elif function_defs_in_site_packages and len(function_defs_in_site_packages) == 1:
            choosen_solution = f"from {convert_to_import_path(function_defs_in_site_packages[0])} import {object_name}\n"
            self.code_snippet.move_to_imports()
        elif function_defs_in_site_packages and len(function_defs_in_site_packages) > 1 and log:
            choices = [
                convert_to_import_path(path)
                for path in function_defs_in_site_packages
            ]
            for i, choice in enumerate(choices):
                typer.echo(f"{i}: {choice}")
            typer.echo("Multiple locations found, please select one:")
            selected = typer.prompt("Enter the number of your choice", type=int)
            if 0 <= selected < len(choices):
                choosen_solution = f"from {choices[selected]} import {object_name}\n"
                self.code_snippet.move_to_imports()
        elif variable_defs_in_site_packages and len(variable_defs_in_site_packages) == 1:
            choosen_solution = f"from {convert_to_import_path(variable_defs_in_site_packages[0])} import {object_name}\n"
            self.code_snippet.move_to_imports()
        elif variable_defs_in_site_packages and len(variable_defs_in_site_packages) > 1 and log:
            choices = [
                convert_to_import_path(path)
                for path in variable_defs_in_site_packages
            ]
            for i, choice in enumerate(choices):
                typer.echo(f"{i}: {choice}")
            typer.echo("Multiple locations found, please select one:")
            selected = typer.prompt("Enter the number of your choice", type=int)
            if 0 <= selected < len(choices):
                choosen_solution = f"from {choices[selected]} import {object_name}\n"
                self.code_snippet.move_to_imports()

        if choosen_solution:
            self.proposed_fix = Fix(
                file=self.code_snippet.file_name,
                range=self.code_snippet.location,
                new_code=choosen_solution
            )
