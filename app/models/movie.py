from peewee import Model, PrimaryKeyField, CharField, FloatField, DateTimeField
from config import Config

class Movies(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False, max_length=25)
    duration = FloatField(null=False) 
    rentail_start_date = DateTimeField(null=False)
    rental_finish_date = DateTimeField(null=False)
    sales_company = CharField(null=False, max_length=25)

    class Meta:
        database = Config.DATABASE
