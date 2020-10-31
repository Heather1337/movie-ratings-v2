"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def movies_page():
    """View all movies on movies page."""

    movies = crud.get_all_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def display_movie(movie_id):
    """Display information about a movie."""
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def users_page():
    """View a list of all users."""

    users = crud.get_all_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def display_user(user_id):
    """Display user profile for given user id."""

    user = crud.get_user_by_id(user_id)

    return render_template('/user_profile.html', user=user)

@app.route('/users', methods=['POST'])
def user_login():
    """Create a new user or login an existing user."""
    print('===================',request.form['email'])
    email = request.form['email']
    password = request.form['password']

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
