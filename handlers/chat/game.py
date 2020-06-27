from db.dbController import dbController
from loader import bot


# @todo Check if user has no more active games
@bot.message_handler(commands=['create_game'])
def create_game(message):
    new_game = dbController.create_game(message.from_user)
    # notify_admin_chat(bot, f"User @{message.from_user.username} created new game")
    bot.reply_to(message, f"game created successfully, game id:{new_game.id}\ncreator: {new_game.creator}")

