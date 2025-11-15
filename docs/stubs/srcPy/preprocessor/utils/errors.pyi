from _typeshed import Incomplete

class OOMRetry(Exception):
    retry_hint: Incomplete
    def __init__(self, message: str = 'OOM: Retry with smaller batch', retry_hint=None) -> None: ...

class UnsupportedAST(Exception): ...

class SchemaMismatch(Exception):
    details: Incomplete
    def __init__(self, message, details=None) -> None: ...
