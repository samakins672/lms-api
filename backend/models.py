from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    category: str
    available: bool = True

class UserBorrowedBooks(BaseModel):
    user_email: str
    borrowed_books: List[Dict[str, datetime]]  # book id and return date
