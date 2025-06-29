"""
srcPy.utils.exceptions
======================

Defines MarketMind’s full custom exception hierarchy for data, config, modeling, and trading failures.

Purpose
-------
To make failures **semantic, catchable, and machine-readable** across the entire platform.

Each exception targets a specific operational failure mode:  
**data ingestion**, **preprocessing**, **config validation**, **model training**, **broker execution**, or **statistical analysis**.

Every exception includes:
- A human-readable message for logs.
- A structured `details` dictionary for monitoring systems, dashboards, and error tracking.

Design Goals
------------
- **Recoverability:** Callers can catch specific exceptions they know how to handle.
- **Context-first:** Diagnostic metadata lives in `details`, not buried in strings.
- **Minimal inheritance:** Only shared where recovery patterns dictate.

Usage Patterns
--------------
Raise these exceptions inside internal pipelines, API layers, or streaming workers  
anywhere a failure needs to propagate with context.

External consumers (notebooks, services, etc.) should catch by type—not string-matching error messages.

"""

from __future__ import annotations

from typing import Any, Mapping

__all__ = [
    "IBConnectionError",
    "DataFetchError",
    "NoDataError",
    "DataValidationError",
    "ConfigValidationError",
    "PreprocessingError",
    "ModelTrainingError",
    "TradingExecutionError",
    "APIConnectionError",
    "InvalidInputError",
    "StatisticalTestError",
]

_Details = Mapping[str, Any]


class IBConnectionError(Exception):
    """
    Connection to **:term:`Interactive Brokers (IBKR)`** failed.

    Parameters
    ----------
    message : str, optional
        Human-readable summary.  Default is
        ``"Failed to connect to Interactive Brokers"``.
    details : mapping[str, Any], optional
        Structured metadata such as ``{"host": "127.0.0.1", "port": 7497}``.

    Attributes
    ----------
    details : dict[str, Any]
        A *mutable* copy of *details* (empty dict if *None* given).

    Examples
    --------
    >>> raise IBConnectionError(details={"host": "localhost", "port": 7497})
    Traceback (most recent call last):
        ...
    srcPy.utils.exceptions.IBConnectionError: Failed to connect to Interactive Brokers

    See Also
    --------
    :term:`Interactive Brokers (IBKR)`
    """

    details: dict[str, Any]

    def __init__(
        self,
        message: str = "Failed to connect to Interactive Brokers",
        *,
        details: _Details | None = None,
    ) -> None: ...


class DataFetchError(Exception):
    """
    Generic parent for **data-acquisition** failures.

    Parameters
    ----------
    message : str, optional
        Summary of the failure.  Default ``"Error fetching data"``.
    details : mapping[str, Any], optional
        Provider name, :term:`HTTP status`, :term:`retry count`, etc.

    Attributes
    ----------
    details : dict[str, Any]
        Structured diagnostic information.

    See Also
    --------
    NoDataError
    """

    details: dict[str, Any]

    def __init__(
        self,
        message: str = "Error fetching data",
        *,
        details: _Details | None = None,
    ) -> None: ...


class NoDataError(DataFetchError):
    """
    Request succeeded but returned **zero rows**.

    Parameters
    ----------
    symbol : str
        :term:`Ticker` / identifier for which no data was returned.
    details : mapping[str, Any], optional
        Extra context.  If *None*, a mapping ``{"symbol": symbol}`` is created.

    Attributes
    ----------
    details : dict[str, Any]
        Must contain at least ``"symbol"``.
    """

    def __init__(
        self,
        symbol: str,
        *,
        details: _Details | None = None,
    ) -> None: ...


class DataValidationError(Exception):
    """
    Fetched data failed :term:`schema <Schema>` or sanity checks during :term:`Validation`.

    Parameters
    ----------
    message : str
        Explanation of the validation failure.
    details : mapping[str, Any], optional
        Offending column, expected :term:`dtype`, etc.

    Attributes
    ----------
    details : dict[str, Any]
    """

    details: dict[str, Any]

    def __init__(self, message: str, *, details: _Details | None = None) -> None: ...


class ConfigValidationError(Exception):
    """
    ``config.yaml`` violates its :term:`JSON-Schema` / :term:`Pydantic` model.

    Parameters
    ----------
    message : str
        Human-readable summary.
    validation_errors : list[Any], optional
        Raw errors emitted by the validator.

    Attributes
    ----------
    validation_errors : list[Any]
    """

    validation_errors: list[Any]

    def __init__(
        self,
        message: str,
        *,
        validation_errors: list[Any] | None = None,
    ) -> None: ...


class PreprocessingError(Exception):
    """
    Failure during :term:`feature engineering <Feature Engineering>` / preprocessing.

    Same signature pattern as other *details*-carrying exceptions.
    """

    details: dict[str, Any]

    def __init__(self, message: str, *, details: _Details | None = None) -> None: ...


class ModelTrainingError(Exception):
    """Model training or :term:`fine-tuning <Fine-tuning>` failed."""

    details: dict[str, Any]

    def __init__(self, message: str, *, details: _Details | None = None) -> None: ...


class TradingExecutionError(Exception):
    """Order rejected or failed to execute."""

    details: dict[str, Any]

    def __init__(self, message: str, *, details: _Details | None = None) -> None: ...


class APIConnectionError(Exception):
    """External :term:`REST <REST API>` / :term:`streaming API <Streaming API>` :term:`API Endpoint` unreachable."""

    details: dict[str, Any]

    def __init__(self, message: str, *, details: _Details | None = None) -> None: ...


class InvalidInputError(Exception):
    """
    Input data or parameters invalid **before** running a statistical test. See :term:`InvalidInputError`.

    Parameters
    ----------
    message : str, optional
        Default ``"Invalid input provided"``.
    details : mapping[str, Any], optional
        Array shapes, parameter values, etc.
    """

    details: dict[str, Any]

    def __init__(
        self,
        message: str = "Invalid input provided",
        *,
        details: _Details | None = None,
    ) -> None: ...


class StatisticalTestError(Exception):
    """
    Statistical test failed to execute or returned invalid results.

    Parameters
    ----------
    message : str, optional
        Default ``"Statistical test execution failed"``.
    details : mapping[str, Any], optional
        Test name, :term:`\`*p*\`-value <p-value>`, etc.

    See Also
    --------
    :term:`ADF Test`
    :term:`KPSS Test`
    :term:`Granger Causality Test`
    :term:`Ljung-Box Test`
    """

    details: dict[str, Any]

    def __init__(
        self,
        message: str = "Statistical test execution failed",
        *,
        details: _Details | None = None,
    ) -> None: ...