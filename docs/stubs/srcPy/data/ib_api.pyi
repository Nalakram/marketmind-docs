from _typeshed import Incomplete
from contextlib import contextmanager
from ib_insync import IB
from pydantic import BaseModel
from srcPy.utils.config import get_config as get_config
from srcPy.utils.exceptions import IBConnectionError as IBConnectionError
from srcPy.utils.logger import configure_logger as configure_logger, get_logger as get_logger
from typing import Iterator

log: Incomplete

class IBConfig(BaseModel):
    host: str
    port: int
    client_id: int

def get_ib_config(): ...
@contextmanager
def ib_connection() -> Iterator[IB]: ...
