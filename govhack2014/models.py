from govhack2014 import database
from peewee import *  # noqa


class BaseModel(Model):
    class Meta:
        database = database
