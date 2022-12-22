from datetime import datetime

from pydantic import BaseModel, EmailStr  # a class for creating Schema


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # setting default to True


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str
    content: str


# Response Model Schema - schema used to define what field should be returned.
class Post(PostBase):
    id: int
    created_on: datetime

    class Config:
        orm_mode = True


"""
Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
This way, instead of only trying to get the id value from a dict, as in:
id = data["id"]

it will also try to get it from an attribute, as in:
id = data.id

And with this, the Pydantic model is compatible with ORMs, and you can just declare it in the response_model argument in your path operations.
You will be able to return a database model and it will read the data from it.
"""


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Response Model Schema
class User(BaseModel):
    id: int
    email: EmailStr
    created_on: datetime

    class Config:
        orm_mode = True