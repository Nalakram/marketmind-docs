import torch
import torch.nn as nn
from _typeshed import Incomplete
from dataclasses import dataclass
from srcPy.models.LSTM_model import LSTMBlock as LSTMBlock, LSTMConfig as LSTMConfig
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.utils.config import get_config as get_config
from srcPy.utils.exceptions import DataValidationError as DataValidationError, InvalidInputError as InvalidInputError, ModelCheckpointError as ModelCheckpointError, ModelInferenceError as ModelInferenceError
from srcPy.utils.torch_utils import init_weights as init_weights, seed_everything as seed_everything
from srcPy.utils.validators import validate_tensor as validate_tensor
from typing import Any, Mapping

log: Incomplete

@dataclass
class ClassifierConfig(LSTMConfig):
    num_classes: int = ...
    projection_dim: int | None = ...
    pooling_type: str | None = ...
    @classmethod
    def from_marketmind(cls, overrides: Mapping[str, Any] | None = None) -> ClassifierConfig: ...

class LSTMClassifier(nn.Module):
    config: Incomplete
    lstm_block: Incomplete
    projection: Incomplete
    classifier: Incomplete
    def __init__(self, config: ClassifierConfig | None = None) -> None: ...
    def num_parameters(self, trainable_only: bool = True) -> int: ...
    def forward(self, x: torch.Tensor, lengths: torch.Tensor | None = None) -> torch.Tensor: ...
    def predict_proba(self, x: torch.Tensor, lengths: torch.Tensor | None = None) -> torch.Tensor: ...
    def save(self, path: str) -> None: ...
    @classmethod
    def from_pretrained(cls, path: str, map_location: str | torch.device = 'cpu') -> LSTMClassifier: ...
