from _typeshed import Incomplete

class IBConnectionError(Exception):
    details: Incomplete
    def __init__(self, message: str = 'Failed to connect to Interactive Brokers', details: Incomplete | None = None) -> None: ...

class DataFetchError(Exception):
    details: Incomplete
    def __init__(self, message: str = 'Error fetching data', details: Incomplete | None = None) -> None: ...

class NoDataError(DataFetchError):
    def __init__(self, symbol: str, details: Incomplete | None = None) -> None: ...

class DataValidationError(Exception):
    details: Incomplete
    def __init__(self, message: str, details: Incomplete | None = None) -> None: ...

class ConfigValidationError(Exception):
    validation_errors: Incomplete
    def __init__(self, message: str, validation_errors: Incomplete | None = None) -> None: ...

class PreprocessingError(Exception):
    details: Incomplete
    def __init__(self, message: str, details: Incomplete | None = None) -> None: ...

class ModelTrainingError(Exception):
    details: Incomplete
    def __init__(self, message: str, details: Incomplete | None = None) -> None: ...

class TradingExecutionError(Exception):
    details: Incomplete
    def __init__(self, message: str, details: Incomplete | None = None) -> None: ...

class APIConnectionError(Exception):
    details: Incomplete
    def __init__(self, message: str, details: Incomplete | None = None) -> None: ...

class InvalidInputError(Exception):
    details: Incomplete
    def __init__(self, message: str = 'Invalid input provided', details: Incomplete | None = None) -> None: ...

class StatisticalTestError(Exception):
    details: Incomplete
    def __init__(self, message: str = 'Statistical test execution failed', details: Incomplete | None = None) -> None: ...
