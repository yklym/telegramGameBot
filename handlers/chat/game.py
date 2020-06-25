from db.dbController import dbController
from handlers.utils.admin_notify import notify_admin_chat
from loader import bot
from ..utils.filters import isGroup

# @todo Check if user has no more active games
@bot.message_handler(commands=['create_game'])
def create_game(message):
    new_game = dbController.create_game(message.from_user)
    # notify_admin_chat(bot, f"User @{message.from_user.username} created new game")
    print("--------------------------------")
    # print(new_game)
    print(new_game.players)
    print(len(new_game.players))
    print(new_game.creator)
    # print(new_game.creator.username)
    bot.reply_to(message, f"game created successfully, game id:{new_game.id}\ncreator: {new_game.creator}")
