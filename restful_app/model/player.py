#encoding=utf-8
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from restful_app import db


class Player(db.Model):
    __tablename__ = 'Player'
    PlayerName = Column('player_name', String(50), primary_key=True)
    Score = Column("score", Integer)
    Server=Column("server",String(10),default="restful")
