# Insert bot commands here
commands_list = [
    {"command": "start", "description": "press start"},
    {"command": "chat_info", "description": "get chat and your ids"},
    {"command": "cat", "description": "meow "},
    {"command": "create_game", "description": "Use it in chat to create a game"},
]

commands_str_list = ["/" + elem["command"] for elem in commands_list]
# help, settings, start game, contacts
