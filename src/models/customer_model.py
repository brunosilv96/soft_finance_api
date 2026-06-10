from datetime import datetime

from sqlmodel import Field, SQLModel


class CustomerModel(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True)
    created_at: datetime
    updated_at: datetime | None = None
