import sqlalchemy
from .db_session import SqlAlchemyBase


class Goods(SqlAlchemyBase):
    __tablename__ = 'goods'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String)
    coast = sqlalchemy.Column(sqlalchemy.Integer)
    value = sqlalchemy.Column(sqlalchemy.Integer)
