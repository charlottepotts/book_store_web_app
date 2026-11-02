import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_get_books_returns_200():
    # make the test client
    client = app.test_client()
    # make the request
    response = client.get("/books")
    # assert that the response status code is 200
    assert response.status_code == 200

# def test_get_books_returns_all_books():
#     client = app.test_client()
#     response = client.get("/books")
#     assert response.json == [
#       {
#         "title": "The Gruffalo",
#         "author": "Julia Donaldson"
#       },
#       {
#         "title": "Ada Twist, Scientist",
#         "author": "Andrea Beaty"
#       },
#       {
#         "title": "The Girl Who Drank the Moon",
#         "author": "Kelly Barnhill"
#       },
#       {
#         "title": "Dragons in a Bag",
#         "author": "Zetta Elliott"
#       }
#     ]

def test_get_authors_returns_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200

def test_get_authors_returns_all_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
  {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
]

def test_get_quotes_returns_200():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.status_code == 200

def test_get_quotes_returns_all_quotes():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.json == [
        {
            "quote": "Be yourself; everyone else is already taken.",
            "author": "Oscar Wilde"
         }, 
         {
             "quote": "So many books, so little time.",
             "author": "Frank Zappa"
         }, 
         {
             "quote": "A room without books is like a body without a soul.",
             "author": "Marcus Tullius Cicero"
             
         }
    ]