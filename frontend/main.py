from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from models import User, Book, BorrowRequest
import redis

app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "postgresql://samakins:Samakins0111@frontend_db/frontend_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Redis setup for communication
r = redis.Redis(host='message_broker', port=6379)

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)

class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    category = Column(String)
    available = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

@app.post("/users/enroll")
def enroll_user(user: User):
    db = SessionLocal()
    db_user = UserDB(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/books")
def list_books():
    db = SessionLocal()
    books = db.query(BookDB).filter(BookDB.available == True).all()
    return books

@app.get("/books/{id}")
def get_book(id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/borrow/{id}")
def borrow_book(id: int, borrow_request: BorrowRequest):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.id == id, BookDB.available == True).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not available")
    book.available = False
    db.commit()
    r.publish('book_borrowed', f'Book {id} borrowed for {borrow_request.days} days')
    return {"message": "Book borrowed successfully"}
