from playwright.sync_api import Page, expect
from database_connection import *

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Bunny's Books")

def test_has_list_of_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/book_store.sql")
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator('li')
    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott'
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

# Test the form to create a new book

def test_creates_a_new_bok(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/book_store.sql")
    page.goto("http://127.0.0.1:5001/books")
    # Grab and fill the first field, title
    page.get_by_label("Title").fill("Normal People")
    # Grab and fill the second field, author
    page.get_by_label("Author").fill("Sally Rooney")
    # Press the submit button
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott',
        'Normal People by Sally Rooney'
    ]
    assert expected_books == books.all_inner_texts()