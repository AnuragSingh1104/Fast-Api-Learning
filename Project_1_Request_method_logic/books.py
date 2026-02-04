from fastapi import FastAPI

app=FastAPI()

Books=[
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "category": "Programming"
    },
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "Programming"
    },
    {
        "title": "Code Complete",
        "author": "Steve McConnell",
        "category": "Programming"
    },
    {
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        "category": "Algorithms"
    },
    {
        "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "category": "Software Engineering"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "Classic Fiction"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "category": "Dystopian Fiction"
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "category": "Classic Romance"
    },
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "category": "Magic Realism"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Classic Fiction"
    }


]

@app.get("/books")
def read_books():
    return Books

@app.get("/books/{book_title}")
def read_all_books(book_title:str):
    for book in Books:
        title=book.get("title")
        if title.lower()==book_title.lower():
            return book
        

@app.get("/books/")
async def books_by_category(category:str):
    books=[]
    for book in Books:
        if book.get("category").lower()==category.lower():
            books.append(book)
    return books

@app.get("/books/{author_name}")
def books_by_author_and_category(author_name,category):
    for book in Books:
        title=book.get("author")
        if title.lower()==book.lower() and book.get("category").lower()==category.lower():
            return book


