import databases
import sqlalchemy
from decouple import config


class DatabaseConnection:
    DB_NAME = config('DB_NAME')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_HOST = config('DB_HOST')
    DB_USER = config('DB_USER')
    DB_PORT = config('DB_PORT')
    DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    database = None
    metadata = sqlalchemy.MetaData()

    def __init__(self):
        self.database = databases.Database(self.DB_URL)


db = DatabaseConnection()
