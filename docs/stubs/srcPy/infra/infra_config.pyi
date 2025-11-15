from _typeshed import Incomplete
from pydantic import BaseModel

logger: Incomplete

class BrokerConfig(BaseModel):
    host: str
    port: int
    client_id: int
    account: str | None
    timeout: float
    retries: int
    def validate_port(cls, v: int) -> int: ...
    def validate_account(cls, v: str | None) -> str | None: ...

def load_broker_config(config_path: str = 'pipeline_config.yaml', section: str = 'ibkr') -> BrokerConfig: ...
