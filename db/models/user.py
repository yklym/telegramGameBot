from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String, default="")
    username = Column(String)

    curr_game_id = Column(Integer, ForeignKey('games.id'))
    curr_game = relationship("Game", foreign_keys=[curr_game_id], backref="players")

    game_creator_to_id = Column(Integer, ForeignKey('games.id'))
    game_creator_to = relationship("Game", foreign_keys=[game_creator_to_id], backref=backref("creator", uselist=False))

    curr_game_status = Column(String)
    curr_game_role = Column(String)
    curr_game_membership = Column(String)
    curr_game_is_president = Column(Boolean)
    curr_game_is_vice_president = Column(Boolean)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', username='%s', curr_game_id='%s')>" % (
            self.name, self.fullname, self.username, self.curr_game_id)


