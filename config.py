from peewee import SqliteDatabase


class Config:
    # для работы с базой данных
    DATABASE_NAME = 'cinema.db'
    DATABASE = SqliteDatabase(DATABASE_NAME)
