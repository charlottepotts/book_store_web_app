from user import *

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    # Not sure if we should save the pword in this way
    # def all(self):
    #     rows = self._connection.execute("SELECT * FROM users")
    #     users = []
    #     for row in rows:
    #         user = User(row['username'], row['password'], row['id'])
    #         users.append(user)
    #     return users

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)", 
            [user.username, user.password])
        return None
