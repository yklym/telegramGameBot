from data.keyboards.game import lobby_keyboard
from data.text.game import game_main_message, notify_player_about_start_text


def update_main_message(bot, game):
    bot.edit_message_text(chat_id=game.main_chat_id, message_id=game.main_message_id, text=game_main_message(game),
                          reply_markup=lobby_keyboard(game) if game.state == "lobby" else None, parse_mode="HTML")


def notify_players_about_start(bot, game):
    print("GAME")
    print(game.hitler)
    for player in game.players:
        try:
            bot.send_message(player.id, text=notify_player_about_start_text(game, player, game.hitler[0]), parse_mode="HTML")
        except Exception as e:
            print(e)
            bot.send_message(game.main_chat_id, text="some problems while notifying players")
