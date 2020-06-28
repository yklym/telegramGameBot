from db.dbController import dbController
from loader import bot
from ..utils.filters import is_group
from data.text.game import game_info_text, no_game_info_text


# function=isGroup
@bot.message_handler(commands=['game_create'])
def create_game(message):
    # print(message.db_user)
    if message.db_user.curr_game:
        bot.reply_to(message, "You can't create new game before finishing your previous one ")
        return
    # notify_admin_chat(bot, f"User @{message.from_user.username} created new game")
    new_game = dbController.create_game(message.db_user, message.chat.id)
    bot.reply_to(message, f"game created successfully, game id:{new_game.id}\ncreator: {new_game.creator}")

@bot.message_handler(commands=['game_info'])
def game_info(message):
    game = message.db_user.curr_game
    if not game:
        bot.reply_to(message, no_game_info_text())
        return
    bot.send_message(message.chat.id, game_info_text(game), parse_mode="HTML")
