from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str
    id: int


class UserAge(BaseModel):
    name: str
    age: int


class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(ge=0)
    is_subscribed: bool = False
