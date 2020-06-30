def game_info_text(game):
    players_list = "".join(["<a href='tg://user?id={p.id}'>{p.fullname}</a>\n".format(p=p) for p in game.players])

    return ("<b>Your current game info:</b>\n"
            "Game id: <b>{game.id}</b>\n"
            "Game status: <b>{game.state}</b>\n"
            "\n"
            "<b>Players:\n</b>"
            "-----------------------\n"
            "{p_list}"
            "-----------------------\n").format(game=game, p_list=players_list)


def no_game_info_text():
    return "Your have no active games for a moment"


def game_main_message(game):
    players_list = "".join(["<a href='tg://user?id={p.id}'>{p.fullname}</a>\n".format(p=p) for p in game.players])

    return ("<b>Game info:</b>\n"
            "Game id: <b>{game.id}</b>\n"
            "Game status: <b>{game.state}</b>\n"
            "\n"
            "<b>Players:\n</b>"
            "-----------------------\n"
            "{p_list}"
            "-----------------------\n").format(game=game, p_list=players_list)


def accept_game(game_id):
    return "Do you want to accept game #" + str(game_id) + "?"


def game_accepted(game_id):
    return f"Game #{game_id} was accepted successfully!"


def notify_player_about_start_text(game, player_info, hitler_info):
    # todo finish this
    tasks = {
        "liberal": "Kill all nazi",
        "fascist": f"Kill all liberal swines and protect {hitler_info.fullname}",
        "hitler": "Rule the world"
    }

    return ("Game {g.id} was started.\n" +
            "Your membership is {p.curr_game_membership}\n" +
            ("You will be also acting as a <b>SECRET HITLER</b>" if player_info.curr_game_is_hitler else "") +
            "\nYOUR TASK FOR THE GAME:\n---------------\n").format(g=game, p=player_info)
