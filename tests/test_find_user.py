import sys
import os
from app import app
from database_connection import *
from user_repository import * 

def test_find_user():
    client = app.test_client()
    
    connection = DatabaseConnection()
    connection.connect()
    
    connection.execute("TRUNCATE TABLE users;")
    
    client.post('/users', data={
        'username': 'testuser',
        'password': 'password123',
        'email': 'email@email.com'
    })


