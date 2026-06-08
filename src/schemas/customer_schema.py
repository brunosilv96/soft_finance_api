from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class CustomerRequestSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr


class CustomerUpdateRequestSchema(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=50)
    email: EmailStr | None = None


class CustomerResponseSchema(BaseModel):
    id: str
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime | None = None
