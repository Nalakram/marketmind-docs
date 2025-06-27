from _typeshed import Incomplete
from srcPy.utils.logger import get_logger as get_logger

logger: Incomplete

class Backtester:
    df: Incomplete
    strategy_cls: Incomplete
    strat_kwargs: Incomplete
    cash: Incomplete
    commission: Incomplete
    slippage_perc: Incomplete
    riskfreerate: Incomplete
    def __init__(self, df, strategy_cls, strat_kwargs: Incomplete | None = None, cash: int = 100000, commission: float = 0.001, slippage_perc: float = 0.0005, riskfreerate: float = 0.02) -> None: ...
    def run(self): ...
