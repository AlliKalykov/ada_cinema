from flask import Blueprint, render_template
from app.models.movie import Movies
from app.models.seanse import Seanses

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies')
def movies():
    return render_template('movies/movies.html', movies=Movies.select(Movies, Seanses).join(Seanses))

@movies_bp.route('/movies/<int:id>')
def movie(id):
    return render_template('movies/movie.html', movie=Movies.get_by_id(id))
