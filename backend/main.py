from fastapi import FastAPI
from models import Book, UserBorrowedBooks
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

client = MongoClient("mongodb://backend_db:27017/")
db = client.library

@app.post("/admin/books")
def add_book(book: Book):
    db.books.insert_one(book.dict())
    return {"message": "Book added successfully"}

@app.delete("/admin/books/{id}")
def remove_book(id: int):
    db.books.delete_one({"id": id})
    return {"message": "Book removed successfully"}

@app.get("/admin/users")
def list_users():
    users = db.users.find()
    return list(users)

@app.get("/admin/users/borrowed")
def list_users_borrowed_books():
    users = db.users_borrowed_books.find()
    return list(users)

@app.get("/admin/books/unavailable")
def unavailable_books():
    borrowed_books = db.books.find({"available": False})
    return list(borrowed_books)
