from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(gt=0)


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Little Prince", author="Antoine de Saint-Exupery", year=1943),
    2: Book(id=2, title="Frankenstein", author="Mary Shelley", year=1818),
}


@app.get("/books")
def list_books() -> list[Book]:
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    # TODO: Return the book or raise HTTPException with status code 404.
    pass


@app.post("/books", status_code=201)
def create_book(book_input: BookInput) -> Book:
    # TODO: Assign an ID, save the book, and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book_input: BookInput) -> Book:
    # TODO: Replace the book data or raise HTTPException with status code 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    # TODO: Remove the book or raise HTTPException with status code 404.
    pass