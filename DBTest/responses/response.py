from pydantic import BaseModel
from typing import List, Optional

class Response(BaseModel):
    status: int
    msg: str

class User(BaseModel):
    id: int
    user_name: str
    password: Optional[str]

    class Config:
        orm_mode = True

class UserResponse(Response):
    data: List[User]
