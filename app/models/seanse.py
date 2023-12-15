from peewee import Model, PrimaryKeyField, DateTimeField, ForeignKeyField
from .movie import Movies
from config import Config

class Seanses(Model):
    id = PrimaryKeyField(null=False)
    date =  DateTimeField(null=False)
    time = DateTimeField(null=False)
    movie = ForeignKeyField(Movies, backref='seanses')

    class Meta:
        database = Config.DATABASE
    