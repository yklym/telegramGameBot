from telebot import types


def lobby_keyboard(game):
    lobby_kb = types.InlineKeyboardMarkup()
    lobby_kb.add(types.InlineKeyboardButton("Sign up for the game!", callback_data="lobby_signUp_" + str(game.id)))
    return lobby_kb


def accept_invitation_keyboard(game_id):
    accept_kb = types.InlineKeyboardMarkup()
    accept_kb.add(types.InlineKeyboardButton("Accept game!", callback_data="accept_game_" + str(game_id)))
    return accept_kb
