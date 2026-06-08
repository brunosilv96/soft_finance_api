from dataclasses import dataclass
from datetime import datetime


@dataclass
class CustomerModel:
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime | None = None
