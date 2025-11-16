from typing import Any as Incomplete
from srcPy.domain.interfaces import MarketDataProvider as MarketDataProvider, Order as Order, OrderExecutor as OrderExecutor, PositionSizer as PositionSizer, RiskManager as RiskManager

class TradingService:
    """trading service implementation."""
    executor: Incomplete
    mkt: Incomplete
    risk: Incomplete
    sizer: Incomplete
    def __init__(self, executor: OrderExecutor, mkt: MarketDataProvider, risk: RiskManager, sizer: PositionSizer) -> None: ...
    def trade_signal(self, symbol: str, signal: float): ...