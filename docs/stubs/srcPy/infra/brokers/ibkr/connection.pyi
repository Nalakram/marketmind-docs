from _typeshed import Incomplete
from contextlib import contextmanager
from ib_insync import IB as IBKR
from pydantic import BaseModel
from typing import Iterator

class IBKR: ...

log: Incomplete

class IBKRConfig(BaseModel):
    host: str
    port: int
    client_id: int

def get_ibkr_config(): ...
@contextmanager
def ibkr_connection() -> Iterator[IBKR]: ...
