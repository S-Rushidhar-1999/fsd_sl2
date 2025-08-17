from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory "database"
books = [
  {
    "id": 1,
    "title": "1984",
    "author": "George Orwell"
  },
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee"
  },
  {
    "id": 3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
  },
  {
    "id": 4,
    "title": "Pride and Prejudice",
    "author": "Jane Austen"
  },
  {
    "id": 5,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger"
  }
]


# Book model
class Book(BaseModel):
    id: int
    title: str
    author: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}

# Get all books
@app.get("/books")
def get_books():
    return books

# Get a book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        print(book)
        if book.get("id") == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Add a new book
@app.post("/books", status_code=201)
def create_book(book: Book):
    for b in books:
        if b.get("id") == book.get("id"):
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return book

# Update a book
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.get("id") == book_id:
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.get("id") == book_id:
            deleted = books.pop(i)
            return {"message": "Book deleted", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")
