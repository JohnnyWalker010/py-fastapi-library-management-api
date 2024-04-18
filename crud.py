from datetime import date

from sqlalchemy.orm import Session

import schemas
from db.models import Author, Book


def get_all_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).all()


def get_author_by_name(db: Session, name: str):
    return db.query(Author).filter(Author.name == name).all()


def get_all_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).all()


def get_book_by_title(db: Session, title: str):
    return db.query(Book).filter(Book.title == title).all()


def get_books_by_author(db: Session, author_name: str):
    return db.query(Book).join(Author).filter(Author.name == author_name).all()


def create_book(
    db: Session,
    title: str,
    summary: str,
    publication_date: date,
    author_id: int,
):
    db_book = Book(
        title=title,
        summary=summary,
        publication_date=publication_date,
        author_id=author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def create_author(
    db: Session,
    author: schemas.AuthorCreate
):
    db_author = Author(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author
