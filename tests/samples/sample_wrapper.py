from dataclasses import dataclass, field


@dataclass
class SampleWrapper:
    sample_name: str
    sample_code: str
    errors: list[str] = field(default_factory=list)
