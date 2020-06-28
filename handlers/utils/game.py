from data.keyboards.game import lobby_keyboard
from data.text.game import game_main_message


def update_main_message(bot, game):
    bot.edit_message_text(chat_id=game.main_chat_id, message_id=game.main_message_id, text=game_main_message(game),
                          reply_markup=lobby_keyboard(game), parse_mode="HTML")
