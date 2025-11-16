import polars as pl
from dataclasses import dataclass, field
from typing import Any

__all__ = ['Bar', 'Tick', 'MarketDataFrameSchema']

@dataclass(frozen=True)
class Bar:
    """bar class."""
    timestamp: pl.Datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    metadata: dict[str, Any] | None = field(default_factory=dict)

@dataclass(frozen=True)
class Tick:
    """tick class."""
    timestamp: pl.Datetime
    price: float
    size: float
    side: str
    metadata: dict[str, Any] | None = field(default_factory=dict)

@dataclass
class MarketDataFrameSchema:
    """market data frame schema class."""
    required_columns: dict[str, pl.DataType] = field(default_factory=dict)
    optional_columns: dict[str, pl.DataType] = field(default_factory=dict)
    strict: bool = ...
    unknown_ok: bool = ...
    def validate(self, df, strict: bool | None = None) -> tuple[bool, list[str]]: ...