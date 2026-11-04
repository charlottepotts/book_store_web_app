from user import *

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", 
            [user.username, user.password, user.email])
        return None
    
    def find_by_username(self, username):
        user_list = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
        if user_list:
            user_details = user_list[0]
            return User(
                user_details["username"], 
                user_details["password"], 
                user_details["email"], 
                user_details["id"]
                )
        else:
            return None
