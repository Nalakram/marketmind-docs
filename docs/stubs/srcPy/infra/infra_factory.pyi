from typing import Any as Incomplete
from typing import Any

__all__ = ['register_source', 'unregister_source', 'get_creator', 'list_sources', 'DataSourceFactory', 'creator']

def register_source(name: str, creator: _Source) -> None: ...
def unregister_source(name: str) -> None: ...
def get_creator(source_type: str) -> _Source | None: ...
def list_sources() -> list[str]: ...

class DataSourceFactory:
    """Factory for creating data source instances."""
    @staticmethod
    def create(source_type: str, /, **kwargs: Any) -> Any: ...

class _LegacyCreatorProxy:
    """legacy creator proxy class."""
    def __call__(self, source_type: str, /, **kwargs: Any): ...

creator: Incomplete