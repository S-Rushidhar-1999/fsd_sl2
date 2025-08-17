import cloudscraper

# Create a scraper session
scraper = cloudscraper.create_scraper()

BASE_URL = "https://fsd-sl2.vercel.app"

# ▶️ GET all books
res = scraper.get(f"{BASE_URL}/books")
print("GET /books:", res.json())

# ▶️ GET a single book
res = scraper.get(f"{BASE_URL}/books/2")
print("GET /books/2:", res.json())

# ▶️ POST a new book
new_book = {
    "id": 6,
    "title": "Brave New World",
    "author": "Aldous Huxley"
}
res = scraper.post(f"{BASE_URL}/books", json=new_book)
print("POST /books:", res.json())

# ▶️ PUT (update) the book
updated_book = {
    "id": 6,
    "title": "Brave New World - Updated",
    "author": "Aldous Huxley"
}
res = scraper.put(f"{BASE_URL}/books/6", json=updated_book)
print("PUT /books/6:", res.json())

# ▶️ DELETE the book
res = scraper.delete(f"{BASE_URL}/books/6")
print("DELETE /books/6:", res.json())
