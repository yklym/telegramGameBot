import random

from data.config import GAME_INIT_SETTINGS
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
                        fullname=user.first_name + " " + (user.last_name if user.last_name else ""),
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

    def init_game(self, game_id):
        # TODO finish this
        game = self.get_game_by_id(game_id)
        game.state = "play"
        game.acts = create_acts_str()
        init_players_roles(game)
        session.commit()
        return game


dbController = DbController(session)


# todo that it in new utils
def create_acts_str():
    acts_str = list(GAME_INIT_SETTINGS["acts"]["fascist"] * "f" + GAME_INIT_SETTINGS["acts"]["liberal"] * "l")
    random.shuffle(acts_str)
    return acts_str


def init_players_roles(game):
    players_list = game.players
    liberal_amount = len(players_list) // 2 + 1
    if len(players_list) <= 2:
        liberal_amount = 1
    fascists_amount = len(players_list) - liberal_amount

    hitler_index = random.randint(0, fascists_amount-1)
    print("ddd", liberal_amount, fascists_amount, hitler_index)

    roles_index_list = {index: {"is_hitler": False, "membership": "liberal"} for index in
                        [i for i in range(len(players_list))]}

    random.shuffle(roles_index_list)

    for i in range(fascists_amount):
        roles_index_list[i]["membership"] = "fascist"
        if i == hitler_index:
            roles_index_list[i]["is_hitler"] = True

    for i in range(len(players_list)):
        print("i\n")

        player = players_list[i]
        player.curr_game_status = "prevote"
        player.curr_game_is_hitler = True if roles_index_list[i]["is_hitler"] else False
        player.curr_game_membership = roles_index_list[i]["membership"]
        player.curr_game_is_president = False
        player.curr_game_is_vice_president = False
