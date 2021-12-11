import srcomapi, srcomapi.datatypes as dt
import pandas as pd
import datetime

api = srcomapi.SpeedrunCom()
api.debug = 1
name = "Celeste"


def find_game(name):
    games = api.search(srcomapi.datatypes.Game, {"name": name})
    for game in games:
        # print(game.name)
        if game.name == "Celeste":
            return game
    return None


def find_category(game, name):
    for category in game.categories:
        if category.name == name:
            return category
    return None


def find_user(username):
    return dt.User(api, data=api.get("users/{}".format(username)))


def get_personal_best(user, category):
    for pb in user.personal_bests:
        run = pb["run"]
        if run.category == category.id:
            return run


def create_csv(pb_list):
    df = pd.DataFrame({user: pb_list})
    df.to_csv(r'/Users/minipewz/Documents/YFF/webscraping\\speedrunleaderboard.csv', index=False)


def bruh():
    data_frame = pd.read_json(leaderboard.content, orient='index').append(pd.leaderboard)
    ape = data_frame.to_csv(r'/Users/minipewz/Documents/YFF/webscraping\\speedrunleaderboard.csv', index=False)

    print(ape)


if __name__ == "__main__":
    game = find_game("Celeste")
    category = find_category(game, "Any%")
    user = find_user("MiniPeWZ")
    pb = get_personal_best(user, category)
    time = "primary_t"
    seconds = pb.times["primary_t"]

    leaderboard = dt.Leaderboard(api, data=api.get("leaderboards/{}/category/{}?top=10".format(game.id, category.id)))
    pb_list = []
    for run in leaderboard.runs:
        seconds = run["run"].times["primary_t"]
        # timedelta fucker pga har ikke vanlige datetime-greier. finne noe annet eller caste på en eller annen måte????
        time = datetime.timedelta(seconds=seconds)  # .strftime("%H:%M:%S")
        print(time)
        # TODO: slette days og timer??
        pb_list.append(time)

    create_csv(pb_list)
