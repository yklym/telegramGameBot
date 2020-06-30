from loader import bot
from ..utils.commands import update_rules_message

@bot.callback_query_handler(func=lambda call: "rules_page" in call.data)
def rules_pagination_callback(call):
    prev_page, direction,*_ = call.data.split('_')[::-1]
    chat_id = call.from_user.id
    message_id = call.message.message_id
    update_rules_message(int(prev_page),direction,bot,chat_id,message_id)
    