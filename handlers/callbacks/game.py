from data.keyboards.game import accept_invitation_keyboard
from data.text.game import accept_game, game_accepted
from data.text.warnings import warnings
from loader import bot
from db.dbController import dbController
from ..utils.game import update_main_message

@bot.callback_query_handler(func=lambda call: "lobby_signUp" in call.data)
def test_callback(call):
    # check if user is already signed for this or any game
    game_id = call.data.split("_")[-1]
    try:
        bot.send_message(call.from_user.id, text=accept_game(game_id), reply_markup=accept_invitation_keyboard(game_id))
    except:
        bot.send_message(call.message.chat.id, f"{call.from_user.username}" + warnings["user_not_authorized"])


@bot.callback_query_handler(func=lambda call: "accept_game" in call.data)
def accept_game_func(call):
    # print(call)
    game_id = call.data.split("_")[-1]

    # change it for try/except with manual exceptions
    game = dbController.game_add_player(game_id, call.from_user.id)
    if game:
        bot.send_message(call.from_user.id, game_accepted(game_id))
        update_main_message(bot, game)
    else:
        # get it to warnings
        bot.send_message(call.from_user.id, "error")