"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

# Functions start here!

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_all_users():
    """Get a list of all users."""

    return User.query.all()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date,
                  poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_all_movies():
    """Read and return a list of all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return a movie from the given movie id."""

    return Movie.query.get(movie_id)



def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


