from playwright.sync_api import Page, expect
from app import app
from database_connection import *

def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) VALUES ('testuser', 'password123', 'email@email.com');")
    response = client.post('/sessions', data={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 302
    assert response.headers['Location'].endswith('/books')

def test_auth_playwright(page: Page):
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) VALUES ('testuser', 'password123', 'email@email.com');")
    page.goto('http://127.0.0.1:5001//sessions/new')
    page.get_by_label("Username").fill("testuser")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Submit").click()
    assert page.url =="http://127.0.0.1:5001/books"

def test_auth_integration_fails():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) VALUES ('testuser', 'password123', 'email@email.com');")
    response = client.post('/sessions', data={
        'username': 'nottestuser',
        'password': 'notpassword123'
    })
    assert response.status_code == 302
    assert response.headers['Location'].endswith('/sessions/new')

def test_auth_playwright_fails(page: Page):
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) VALUES ('testuser', 'password123', 'email@email.com');")
    page.goto('http://127.0.0.1:5001/sessions/new')
    page.get_by_label("Username").fill("nottestuser")
    page.get_by_label("Password").fill("notpassword123")
    page.get_by_role("button", name="Submit").click()
    assert page.url =="http://127.0.0.1:5001/sessions/new"

def test_unauth_user_creates_book(page: Page):
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) VALUES ('testuser', 'password123', 'email@email.com');")
    page.goto('http://127.0.0.1:5001/books')
    page.get_by_label("Title").fill("test1")
    page.get_by_label("Author").fill("test1")
    page.get_by_role("button", name="Submit").click()
    assert page.url =="http://127.0.0.1:5001/books"