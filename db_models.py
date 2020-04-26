# -*- coding: utf-8 -*-
from peewee import SqliteDatabase, Model, TextField, UUIDField, DateTimeField, OperationalError
from datetime import datetime as dt
from log import log
from uuid import uuid4


DATABASE = 'storage/data/files.db'

sqlite_db = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class File(BaseModel):
    id = UUIDField(default=uuid4(), unique=True, primary_key=True)
    f_name = TextField()
    fc_datetime = DateTimeField(default=dt.now)


def init_db():
    try:
        # File.drop_table(File)
        File.create_table()
        log("INFO", "Создание БД")
    except OperationalError:
        log("ERROR", "БД уже существует")
        print("File table already exists!")