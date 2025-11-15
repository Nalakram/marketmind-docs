import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from enum import Enum
from functools import cached_property
from typing import Any

__all__ = ['OpKind', 'Op', 'ElementwiseOp', 'RollingOp', 'SequenceOp', 'ScalingOp', 'ExternalOp']

class OpKind(str, Enum):
    elementwise = 'elementwise'
    rolling = 'rolling'
    sequence = 'sequence'
    scaling = 'scaling'
    external = 'external'

class Op(ABC, metaclass=abc.ABCMeta):
    NAME: str | None
    KIND: OpKind
    params: dict[str, Any]
    def __init__(self, **params: Any) -> None: ...
    @property
    def name(self) -> str: ...
    def validate_params(self) -> None: ...
    @cached_property
    def requires(self) -> set[str]: ...
    @cached_property
    def provides(self) -> set[str]: ...
    def is_fittable(self) -> bool: ...
    def state_dict(self) -> dict[str, Any]: ...
    def load_state_dict(self, state: dict[str, Any]) -> Op: ...
    def clone(self): ...
    @abstractmethod
    def to_ir(self) -> dict[str, Any]: ...

class ElementwiseOp(Op):
    KIND: Incomplete
    def to_ir(self) -> dict[str, Any]: ...

class RollingOp(Op):
    KIND: Incomplete
    def to_ir(self) -> dict[str, Any]: ...

class SequenceOp(Op):
    KIND: Incomplete
    def to_ir(self) -> dict[str, Any]: ...

class ScalingOp(Op):
    KIND: Incomplete
    def is_fittable(self) -> bool: ...
    def to_ir(self) -> dict[str, Any]: ...

class ExternalOp(Op):
    KIND: Incomplete
    def to_ir(self) -> dict[str, Any]: ...
