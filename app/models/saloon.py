from peewee import Model, PrimaryKeyField, CharField, IntegerField
from config import Config

class Saloon(Model):
     id = PrimaryKeyField(null=False)
     name = CharField(null=False, max_length=25)
     count_place = IntegerField()
     description = CharField(null=False, max_length=255)
     number_of_ros = IntegerField()
     number_of_places = IntegerField()

     class Meta:
        database = Config.DATABASE
