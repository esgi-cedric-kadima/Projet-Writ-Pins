from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str
    username: str = None
    bio: str = None
    image: str = None
