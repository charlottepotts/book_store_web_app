from user import * 

def test_user_instance_created():
    user = User('testuser','password123','email@email.com', 1)
    assert user.username == 'testuser'
    assert user.password == 'password123'
    assert user.email == 'email@email.com'
    assert user.id == 1