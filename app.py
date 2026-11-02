from flask import Flask, render_template, request, redirect
from database_connection import *
from book_repository import *
from user_repository import *
from user import *

# instantiate a flask app object
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in 
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# A new route for a GET method for the path /books
# The response will include a list of hard coded books

@app.route('/books', methods=['GET'])
def books():
    connection = DatabaseConnection()
    connection.connect()
    repository = BookRepository(connection)
    books = repository.all()
    print(books)
    return render_template("books.html", books=books)

# A new route for a GET method for the path /authors
# The response will include a list of hard coded books

@app.route('/authors', methods=['GET'])
def authors():
    return [
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

# A new route for a GET method for the path /quotes
# The response will include a list of hard coded quotes

@app.route('/quotes', methods=['GET'])
def quotes():
    return [
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

# A new route for /team

@app.route('/team', methods=['GET'])
def get_team():
    team = ['Miffy', 'Peter', 'Bugs', 'Thumper']
    return render_template("team.html", team=team)

# Grab request body data in the POST route

@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details['title'], author=book_details['author'])
    repository.create(book)
    return redirect("/books")

# A new route for the users sign up form
@app.route('/users', methods=['GET'])
def get_sign_up_form():
    render_template('signup_form.html')

# Handle submission of the signup form, to create a new entry in users table
@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details['username'], password=user_details['password'])
    repository.create(user)
    return redirect("/")

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

