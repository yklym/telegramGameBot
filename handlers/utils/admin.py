from data.config import ADMIN_CHAT_ID


def notify_admin_chat(bot, text):
    bot.send_message(ADMIN_CHAT_ID, text)
