# Insert bot commands here
commands_list = [
    {"command": "start", "description": "press start"},
    {"command": "chat_info", "description": "get chat and your ids"},
    {"command": "cat", "description": "meow "},
    {"command": "game_create", "description": "Use it in chat to create a game"},
    {"command": "game_info", "description": "Get game info"},
    {"command": "game_start", "description": "Start created game"},
    {"command": "rules", "description": "An interactive game rules"}

]

commands_str_list = ["/" + elem["command"] for elem in commands_list]
# help, settings, start game, contacts
