from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
import json, shutil, subprocess
from pathlib import Path

import typer


class PyrightNotFound(RuntimeError): ...


def _call(cmd: list[str], cwd: Path) -> str:
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if p.returncode not in (0, 1):
        raise RuntimeError(p.stderr or p.stdout)
    return p.stdout

@dataclass 
class Location:
    line: int
    character: int

    @classmethod
    def from_dict(cls, data: dict) -> Location:
        return cls(line=data["line"], character=data["character"])

@dataclass 
class Range: 
    start: Location
    end: Location

    @classmethod
    def from_dict(cls, data: dict) -> Range:
        return cls(
            start=Location.from_dict(data["start"]),
            end=Location.from_dict(data["end"]),
        )

@dataclass 
class Diagnostic:
    file: str
    severity: str
    message: str
    range: Range
    rule: str

    @classmethod
    def from_dict(cls, data: dict) -> Diagnostic:
        return cls(
            file=data["file"],
            severity=data["severity"],
            message=data["message"],
            range=Range.from_dict(data["range"]),
            rule=data["rule"],
        )

@dataclass
class Summary:
    files_analyzed: int
    error_count: int
    warning_count: int
    information_count: int
    time_in_sec: float

    @classmethod
    def from_dict(cls, data: dict) -> Summary:
        return cls(
            files_analyzed=data["filesAnalyzed"],
            error_count=data["errorCount"],
            warning_count=data["warningCount"],
            information_count=data["informationCount"],
            time_in_sec=data["timeInSec"],
        )


@dataclass
class Report:
    version: str
    time: str
    general_diagnostics: list[Diagnostic]
    summary: Summary

    @classmethod
    def from_dict(cls, data: dict) -> Report:
        return cls(
            version=data["version"],
            time=data["time"],
            general_diagnostics=[
                Diagnostic.from_dict(d) for d in data["generalDiagnostics"]
            ],
            summary=Summary.from_dict(data["summary"]),
        )


def _parse_json(s: str) -> Report:
    i, j = s.find("{"), s.rfind("}")
    return Report.from_dict(json.loads(s[i : j + 1]))


def run_pyright(path: str) -> Report:
    if shutil.which("pyright"):
        out = _call(["pyright", "--outputjson", path], cwd=None)
    elif shutil.which("npx"):
        out = _call(["npx", "-y", "pyright", "--outputjson", path], cwd=None)
    else:
        raise PyrightNotFound("Install dev deps: pip install -e '.[dev]'")
    return _parse_json(out)


def print_meta_info(
    report: Report
) -> None:
    total_errors = report.summary.error_count
    total_warnings = report.summary.warning_count
    total_info = report.summary.information_count

    typer.echo(f"Pyright version: {report.version}")
    typer.echo(f"Time: {report.summary.time_in_sec} seconds")
    typer.echo(f"    Files analyzed: {report.summary.files_analyzed}")
    typer.echo(f"    Errors: {total_errors}")
    typer.echo(f"    Warnings: {total_warnings}")
    typer.echo(f"    Information: {total_info}")


def pyright_error_diagnostics(report: Report, detailed: bool=False) -> list[dict]:
    error_counts = defaultdict(lambda: defaultdict(int))
    warning_counts = defaultdict(lambda: defaultdict(int))
    info_counts = defaultdict(lambda: defaultdict(int))

    for diag in report.general_diagnostics:
        if diag.severity == "error":
            error_counts[diag.rule]["total"] += 1
            error_counts[diag.rule][diag.file] += 1
        elif diag.severity == "warning":
            error_counts[diag.rule]["total"] += 1
            warning_counts[diag.rule][diag.file] += 1
        elif diag.severity == "information":
            error_counts[diag.rule]["total"] += 1
            info_counts[diag.rule][diag.file] += 1

    if error_counts:
        typer.echo("\nError counts by rule:")
        for rule, files in sorted(error_counts.items(), key=lambda x: error_counts[x[0]]["total"], reverse=True):
            typer.echo(f"    {rule}:")
            if detailed:
                for file, count in sorted(files.items(), key=lambda x: x[1], reverse=True):
                    typer.echo(f"        {file}: {count}")
            else:
                typer.echo(f"        Total errors: {sum(files.values())}")
    if warning_counts:
        typer.echo("\nWarning counts by rule:")
        for rule, files in sorted(warning_counts.items(), key=lambda x: warning_counts[x[0]]["total"], reverse=True):
            typer.echo(f"    {rule}:")
            if detailed:
                for file, count in sorted(files.items(), key=lambda x: x[1], reverse=True):
                    typer.echo(f"        {file}: {count}")
            else:
                typer.echo(f"        Total warnings: {sum(files.values())}")
    if info_counts:
        typer.echo("\nInformation counts by rule:")
        for rule, files in sorted(info_counts.items(), key=lambda x: info_counts[x[0]]["total"], reverse=True):
            typer.echo(f"    {rule}:")
            if detailed:
                for file, count in sorted(files.items(), key=lambda x: x[1], reverse=True):
                    typer.echo(f"        {file}: {count}")
            else:
                typer.echo(f"        Total information: {sum(files.values())}")


def pyright_file_diagnostics(
    report: Report, detailed: bool=False
) -> list[dict]: 
    error_counts = defaultdict(lambda: defaultdict(int))
    warning_counts = defaultdict(lambda: defaultdict(int))
    info_counts = defaultdict(lambda: defaultdict(int))

    for diag in report.general_diagnostics:
        if diag.severity == "error":
            error_counts[diag.file]["total"] += 1
            error_counts[diag.file][diag.rule] += 1
        elif diag.severity == "warning":
            error_counts[diag.file]["total"] += 1
            warning_counts[diag.file][diag.rule] += 1
        elif diag.severity == "information":
            error_counts[diag.file]["total"] += 1
            info_counts[diag.file][diag.rule] += 1

    if error_counts:
        typer.echo("\nError counts by file and rule:")
        for file, rules in sorted(error_counts.items(), key=lambda x: x[1]["total"], reverse=True):
            typer.echo(f"    {file}:")
            if detailed:
                for rule, count in sorted(rules.items(), key=lambda x: x[1], reverse=True):
                    typer.echo(f"        {rule}: {count}")
            else:
                typer.echo(f"        Total errors: {sum(rules.values())}")
    if warning_counts:
        typer.echo("\nWarning counts by file and rule:")
        for file, rules in sorted(warning_counts.items(), key=lambda x: x[1]["total"], reverse=True):
            typer.echo(f"    {file}:")
            if detailed:
                for rule, count in sorted(rules.items(), key=lambda x: x[1], reverse=True):
                    typer.echo(f"        {rule}: {count}")
            else:
                typer.echo(f"        Total warnings: {sum(rules.values())}")
    if info_counts:
        typer.echo("\nInformation counts by file and rule:")
        for file, rules in sorted(info_counts.items(), key=lambda x: x[1]["total"], reverse=True):
            typer.echo(f"    {file}:")
            if detailed:
                for rule, count in sorted(rules.items(), key=lambda x: x[1], reverse=True):
                    typer.echo(f"        {rule}: {count}")
            else:
                typer.echo(f"        Total information: {sum(rules.values())}")
