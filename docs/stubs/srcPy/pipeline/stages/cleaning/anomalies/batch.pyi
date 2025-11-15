from . import BaseAnomalyNormalizerStep as BaseAnomalyNormalizerStep
from _typeshed import Incomplete

logger: Incomplete

class AnomalyNormalizerStep(BaseAnomalyNormalizerStep):
    contamination: Incomplete
    refit_every_rows: Incomplete
    sample_size: Incomplete
    method: Incomplete
    model: Incomplete
    executor: Incomplete
    counter: int
    fit_future: Incomplete
    def __init__(self, mlflow_logger, **cfg) -> None: ...
    def close(self) -> None: ...
    def __del__(self) -> None: ...
