import numpy as np
from . import BaseAnomalyNormalizerStep as BaseAnomalyNormalizerStep
from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_metrics import streaming_step_latency as streaming_step_latency

logger: Incomplete

class StreamingIsolationForest:
    contamination: Incomplete
    refit_every: Incomplete
    window_size: Incomplete
    buffer: Incomplete
    counter: int
    model: Incomplete
    def __init__(self, contamination: float, refit_every: int, window_size: int = 1000) -> None: ...
    def predict(self, df) -> np.ndarray: ...

class StreamingAnomalyNormalizerStep(BaseAnomalyNormalizerStep):
    contamination: Incomplete
    refit_every: Incomplete
    window_size: Incomplete
    detector: Incomplete
    def __init__(self, mlflow_logger, **cfg) -> None: ...
