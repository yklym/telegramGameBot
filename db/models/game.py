from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from .base import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    state = Column(String, default="lobby")
    main_chat_id = Column(Integer)

    president = relationship("User", primaryjoin="and_(Game.id==User.curr_game_id, "
                                                 "User.curr_game_is_president==True)",
                             backref=backref("president_to", uselist=False))

    vice_president = relationship("User", primaryjoin="and_(Game.id==User.curr_game_id, "
                                                      "User.curr_game_is_vice_president==True)",
                                  backref=backref("vice_president_to", uselist=False))

    def __repr__(self):
        return "<Game(id='%s' state='%s' all_players='%s' president='%s' vice_president='%s' creator='%s')>" % (
            self.id, self.state, self.players, self.president, self.vice_president, self.creator)
