from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String,Date
from config.db import meta, engine

users = Table(
 'users', meta,
 Column('id',Integer,primary_key=True),
 Column('name',String(50)),
 Column('age',Integer),
 Column('message',String(50)),
 Column('createDate',Date)
)

meta.create_all(engine)