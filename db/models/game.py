from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from .base import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    all_players = relationship("User", back_populates="curr_game")

    def __repr__(self):
        return "<Game(name='%s')>" % self.id
