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
