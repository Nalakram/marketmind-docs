from _typeshed import Incomplete
from srcPy.utils.config import get_config as get_config
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from srcPy.utils.logger import configure_logger as configure_logger, get_logger as get_logger

logger: Incomplete

def get_runtime_config(): ...

class Preprocessor:
    sequence_length: Incomplete
    horizon: Incomplete
    normalization: Incomplete
    technical_indicators: Incomplete
    custom_features: Incomplete
    scaler: Incomplete
    required_columns: Incomplete
    def __init__(self) -> None: ...
    def transform(self, data): ...
