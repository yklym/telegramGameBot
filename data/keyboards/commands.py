from telebot import types
from data.text.rules import rules

def rules_pagination(page_data,message_id):
    max_page = len(rules)
    rules_kb = types.InlineKeyboardMarkup()
    left = types.InlineKeyboardButton(str(page_data["left_button"]),callback_data="rules_page_left_"+str(page_data["page_number"]))
    right = types.InlineKeyboardButton(str(page_data["right_button"]),callback_data="rules_page_right_"+str(page_data["page_number"]))
    current_page = types.InlineKeyboardButton(str(page_data["page_number"]) + ' / ' + str(max_page), callback_data='_')
    rules_kb.add(left, current_page, right)
    return rules_kb