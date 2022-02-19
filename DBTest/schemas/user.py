from pydantic import BaseModel


class User(BaseModel):
    id: int
    user_name: str

    class Config:
        orm_mode = True


class UserRegister(BaseModel):
    id: int
    user_name: str
    password: str


class UserLogin(BaseModel):
    user_name: str
    password: str
