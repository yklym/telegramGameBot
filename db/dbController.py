from db.loader import session
from db.models import User, Game


class DbController:

    def __init__(self, session):
        self._session = session

    def get_user(self, user):
        qr_res = self._session.query(User).filter(User.id == user.id).first()
        return qr_res

    def get_user_by_id(self, user_id):
        qr_res = self._session.query(User).filter(User.id == user_id).first()
        return qr_res

    def get_game(self, game):
        qr_res = self._session.query(Game).filter(Game.id == game.id).first()
        return qr_res

    def get_game_by_id(self, game_id):
        qr_res = self._session.query(Game).filter(Game.id == game_id).first()
        return qr_res

    def add_user(self, user):
        new_user = User(id=user.id, name=user.first_name,
                        fullname=user.first_name + " " + user.last_name if user.last_name else "",
                        username=user.username, curr_game=None)
        session.add(new_user)
        session.commit()

    def create_game(self, creator, main_chat_id, main_message_id):
        creator_info = creator
        new_game = Game(main_chat_id=main_chat_id, main_message_id=main_message_id)
        new_game.creator = creator_info
        new_game.players.append(creator_info)
        session.add(new_game)
        session.commit()
        return new_game

    def game_add_player(self, game_id, user_id):
        game = self.get_game_by_id(game_id)
        user = self.get_user_by_id(user_id)

        if not game or not user:
            # throw smth
            return False
        # check if player isn't already in this or any other games
        game.players.append(user)
        session.commit()
        return game
    # def get_game_by_user(self, user):


dbController = DbController(session)
