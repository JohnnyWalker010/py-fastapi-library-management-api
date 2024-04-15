from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from db.engine import SessionLocal

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/authors/", response_model=list[schemas.AuthorBase])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_all_authors(db)


@app.get("/books/}", response_model=schemas.BookBase)
def read_book(db: Session = Depends(get_db)):
    return crud.get_all_books(db)


@app.post("/authors/", response_model=schemas.AuthorCreate)
def create_author(
        author: schemas.AuthorCreate,
        db: Session = Depends(get_db)
):
    return crud.create_author(db, author)


@app.post("/books/", response_model=schemas.BookCreate)
def create_book(
        book: schemas.BookCreate,
        db: Session = Depends(get_db)
):
    return crud.create_book(db, book)
