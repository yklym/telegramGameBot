from data.text.rules import rules
from data.keyboards.commands import rules_pagination

def get_page(prev_page, direction):
    max_page = len(rules)
    if direction == "left":
        page_number = max_page if prev_page - 1 <= 0 else prev_page - 1
    else:
        page_number = 1 if prev_page + 1 > max_page else prev_page + 1

    left = max_page if page_number - 1 <= 0 else page_number -1
    right = 1 if page_number >= max_page else page_number + 1
    return {
        "text": rules[page_number - 1],
        "page_number": page_number,
        "left_button": left,
        "right_button": right,
    }

def update_rules_message(page,direction,bot,chat_id,message_id):
    page_data = get_page(page,direction)
    bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=page_data['text'],
                          reply_markup=rules_pagination(page_data,message_id),parse_mode="HTML")