import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from functools import singledispatch
from srcPy.utils.optional_imports import pl
from typing import Any

logger: Incomplete
COMPLIANCE_CHECKS: dict[str, type['ComplianceCheck']]

def register_compliance_check(check_type: str): ...

class ComplianceCheck(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def apply(self, df: pl.DataFrame | pl.LazyFrame, sample_size: int | None = None) -> pl.DataFrame | pl.LazyFrame: ...

class ComplianceManager:
    config: Incomplete
    checks: list[ComplianceCheck]
    max_workers: Incomplete
    def __init__(self, config, max_workers: int = 8) -> None: ...
    def add_check(self, check: ComplianceCheck): ...
    @singledispatch
    def enforce(self, data: Any, eager: bool = False, sample_size: int | None = None) -> Any: ...
    @enforce.register
    def _(self, df: pl.LazyFrame, eager: bool = False, sample_size: int | None = None) -> pl.LazyFrame: ...
    @enforce.register
    def _(self, df: pl.DataFrame, eager: bool = False, sample_size: int | None = None) -> pl.DataFrame: ...
    @enforce.register
    def _(self, dfs: dict, eager: bool = False, sample_size: int | None = None) -> dict: ...

class SchemaCompliance(ComplianceCheck):
    required_cols: Incomplete
    required_dtypes: Incomplete
    def __init__(self, config: dict | None = None) -> None: ...
    def apply(self, df: pl.DataFrame | pl.LazyFrame, sample_size: int | None = None) -> pl.DataFrame | pl.LazyFrame: ...

class GDPRCompliance(ComplianceCheck):
    pii_cols: Incomplete
    def __init__(self, config: dict | None = None) -> None: ...
    def apply(self, df: pl.DataFrame | pl.LazyFrame, sample_size: int | None = None) -> pl.DataFrame | pl.LazyFrame: ...

class DriftCompliance(ComplianceCheck):
    detector: Incomplete
    reference: Incomplete
    def __init__(self, config: dict | None = None) -> None: ...
    def apply(self, df: pl.DataFrame | pl.LazyFrame, sample_size: int | None = None) -> pl.DataFrame | pl.LazyFrame: ...
