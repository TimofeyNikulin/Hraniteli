import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Event(SqlAlchemyBase):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    inventory = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    period = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    