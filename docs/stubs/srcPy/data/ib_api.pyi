from typing import Any as Incomplete
from collections.abc import Generator
from contextlib import contextmanager

class IBKRConnectionError(Exception): ...

class IBAPI:
    """ibapi class."""
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def close(self) -> None: ...

@contextmanager
def ib_connection(*args, **kwargs) -> Generator[Incomplete]: ...

class IBKRConnectionError(RuntimeError): ...