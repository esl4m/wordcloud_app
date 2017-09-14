from .database import database
from .wordcount import *


def init_db():
    database.connect()
    database.create_tables([WordCount], True)
    database.close()
