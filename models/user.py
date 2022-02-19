from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    user_name: str
    password: Optional[str]