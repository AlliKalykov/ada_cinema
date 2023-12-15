from flask import Flask, render_template
from config import Config

from app.models.movie import Movies
from app.models.seanse import Seanses
from app.models.saloon import Saloon

app = Flask(__name__)
app.template_folder = 'app/templates' # папка с шаблонами
app.static_folder = 'app/static' # папка со статикой
app.config.from_object(Config) # подключаем конфигурацию

database = app.config['DATABASE'] # получаем объект базы данных
with database: # подключаемся к базе данных
    database.create_tables([Movies, Seanses, Saloon]) # создаем таблицы
    # Movies.create(name='Титаник', duration=120, rentail_start_date='1997-11-18', rental_finish_date='1998-03-18', sales_company='Paramount Pictures') # создаем фильм
    # Seanses.create(date='2023-12-15', time='12:00', movie=1) # создаем сеанс

@app.route('/')
def index():
    return render_template('home.html')    

@app.route('/alli')
def alli():
    return '<h1 style="font-size: 300px;">Alli</h1>'

@app.route('/movies')
def movies():
    return render_template('movies/movies.html', movies=Movies.select(Movies, Seanses).join(Seanses))

@app.route('/movies/<int:id>')
def movie(id):
    return render_template('movies/movie.html', movie=Movies.get_by_id(id))

@app.route('/seanses')
def seanses():
    return render_template('seanses/seanses.html', seanses=Seanses
         .select(Seanses, Movies).join(Movies).order_by(Seanses.date))

@app.route('/seanses/<int:id>')
def seanse(id):
    return render_template('seanses/seanse.html', seanses=Seanses.filter(movie=id))

if __name__ == '__main__':
    app.run(debug=True)
