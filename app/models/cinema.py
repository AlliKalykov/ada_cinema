from peewee import Model, SqliteDatabase, PrimaryKeyField, CharField, IntegerField, ForeignKeyField,FloatField, DateTimeField, ManyToManyField

cinema_db = SqliteDatabase('cinema.db')

class Movies(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False, max_length=25)
    duration = FloatField(null=False) 
    rentail_start_date = DateTimeField(null=False)
    rental_finish_date = DateTimeField(null=False)
    sales_company = CharField(null=False, max_length=25)

    class Meta:
        database = cinema_db


class Saloon(Model):
     id = PrimaryKeyField(null=False)
     name = CharField(null=False, max_length=25)
     count_place = IntegerField()
     description = CharField(null=False, max_length=255)
     number_of_ros = IntegerField()
     number_of_places = IntegerField()

     class Meta:
        database = cinema_db


class SectorSaloon(Model):
    id_sector = PrimaryKeyField(null=False)
    saloon = ForeignKeyField(Saloon, related_name='sector_saloon')
    name = CharField(null=False, max_length=25)
    description = CharField(null=False, max_length=25)

    class Meta:
        database = cinema_db  


class Seanses(Model):
    id = PrimaryKeyField(null=False)
    date =  DateTimeField(null=False)
    time = DateTimeField(null=False)
    movie = ForeignKeyField(Movies, backref='seanses')

    class Meta:
        database = cinema_db


class PriceForTickets(Model):
    id = PrimaryKeyField(null=False)
    seanses = ForeignKeyField(Seanses, related_name='price_for_tickets')
    sector = ForeignKeyField(SectorSaloon, related_name='price_for_tickets')
    price = IntegerField() 

    class Meta:
        database = cinema_db


class Places(Model):
    id = PrimaryKeyField(null=False)
    saloon = ForeignKeyField(Saloon, related_name='places')
    row_number = IntegerField()
    row_place = IntegerField()

    class Meta:
        database = cinema_db


class Tickets(Model):
    ticket_number = PrimaryKeyField()
    date_created = DateTimeField()
    seanses = ForeignKeyField(Seanses)
    places =  ForeignKeyField(Places)
    payed = IntegerField()
    booking = IntegerField()
    creashed = IntegerField()

    class Meta:
        database = cinema_db


class JobTitle(Model):
    id = PrimaryKeyField()
    title = CharField(null=False, max_length=25)

    class Meta:
        database = cinema_db


class Employee(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False, max_length=25)
    title = ForeignKeyField(JobTitle)
    passord = CharField(null=False, max_length=25)

    class Meta:
        database = cinema_db


class MovingTickets(Model):
    id  = PrimaryKeyField()
    ticket = ManyToManyField(Tickets)
    date = DateTimeField(null=False)
    operation = IntegerField()
    employee = ForeignKeyField(Employee)

    class Meta:
        database = cinema_db

Movies.create_table()
Saloon.create_table()
SectorSaloon.create_table()
Seanses.create_table()
PriceForTickets.create_table()
Places.create_table()
Tickets.create_table()
JobTitle.create_table()
Employee.create_table()
MovingTickets.create_table()

Saloon.create(name='1', count_place=10, description='1', number_of_ros=1, number_of_places=1)
SectorSaloon.create(saloon=1, name='1', description='1')