from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserModel():
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime | None = None