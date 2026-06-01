from datetime import datetime

from pydantic import (BaseModel, EmailStr, Field)

class UserRequestSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
class UserResponseSchema(BaseModel):
    id: str
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True