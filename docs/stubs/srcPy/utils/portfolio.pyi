import numpy as np
from _typeshed import Incomplete
from typing import Any, Literal

__all__ = ['PortfolioOptimizer', 'optimise_portfolio']

class PortfolioOptimizer:
    expected_returns: Incomplete
    cov_matrix: Incomplete
    capital: Incomplete
    objective: Incomplete
    constraints: Incomplete
    solver: Incomplete
    risk_free_rate: Incomplete
    random_state: Incomplete
    def __init__(self, expected_returns: np.ndarray | list[float], cov_matrix: np.ndarray | list[list[float]] | None, capital: float, *, objective: Literal['mean_variance', 'cvar', 'kelly', 'risk_parity'] = 'mean_variance', constraints: dict[str, Any] | None = None, solver: Literal['cvxpy', 'scipy', 'pyportfolioopt'] = 'cvxpy', risk_free_rate: float = 0.0, random_state: int | None = None) -> None: ...
    def optimise(self) -> dict[str, float]: ...

def optimise_portfolio(expected_returns: np.ndarray | list[float], cov_matrix: np.ndarray | list[list[float]] | None, capital: float, **kwargs) -> dict[str, float]: ...
