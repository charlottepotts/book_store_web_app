from book import *

class BookRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            book = Book(row['title'], row['author'], row['id'])
            books.append(book)
        return books

    def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author) VALUES (%s, %s)',
            [book.title, book.author]
            )
