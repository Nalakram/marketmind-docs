from typing import Any as Incomplete

class OOMRetry(Exception):
    """oom retry class."""
    retry_hint: Incomplete
    def __init__(self, message: str = 'OOM: Retry with smaller batch', retry_hint=None) -> None: ...

class UnsupportedAST(Exception): ...

class SchemaMismatch(Exception):
    """schema mismatch class."""
    details: Incomplete
    def __init__(self, message, details=None) -> None: ...