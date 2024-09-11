from pydantic import BaseModel

class User(BaseModel):
    email: str
    firstname: str
    lastname: str

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    category: str

class BorrowRequest(BaseModel):
    days: int
