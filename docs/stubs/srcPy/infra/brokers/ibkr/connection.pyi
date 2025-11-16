from typing import Any as Incomplete
from contextlib import contextmanager
from ib_insync import IB as IBKR
from pydantic import BaseModel
from srcPy.ops.mm_logkit import configure_logger as configure_logger, get_logger as get_logger
from srcPy.utils.config import get_config as get_config
from srcPy.utils.exceptions import IBKRConnectionError as IBKRConnectionError
from typing import Iterator

class IBKR: ...

log: Incomplete

class IBKRConfig(BaseModel):
    """Configuration for ibkr."""
    host: str
    port: int
    client_id: int

def get_ibkr_config(): ...
@contextmanager
def ibkr_connection() -> Iterator[IBKR]: ...