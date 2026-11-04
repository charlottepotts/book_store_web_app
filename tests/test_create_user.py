import sys
import os
from app import app
from database_connection import *

# def test_create_user_is_saved_to_database():
#     client = app.test_client()

#     connection = DatabaseConnection()
#     connection.connect()

#     # Truncate the users table as it will fail if more than one user / non-unique usernames
#     connection.execute("TRUNCATE TABLE users;")

#     # send the request
#     response = client.post('/users', data={
#         'username': 'testuser',
#         'password': 'password123'
#     })

#     # assert that the redirect happened
#     assert response.status_code == 302

#     result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

#     assert len(result) == 1
#     assert result[0]['username'] == 'testuser'


def test_create_user_is_saved_to_database_with_email():
    client = app.test_client()

    connection = DatabaseConnection()
    connection.connect()

    connection.execute("TRUNCATE TABLE users;")

    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123',
        'email': 'email@email.com'
    })

    assert response.status_code == 302

    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    assert len(result) == 1
    assert result[0]['username'] == 'testuser'
    assert result[0]['email'] == 'email@email.com'