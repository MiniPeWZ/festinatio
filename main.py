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

#place, time, player
def create_csv(highscores):
    columns=["place", "player", "time"]
    data = []
    place = 1
    for hs in highscores:
        print(pb)
        l=[hs["place"], hs["name"], hs["personal_best"]]
        data.append(l)
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(r'/Users/minipewz/Documents/YFF/bruh\\speedrunleaderboard.csv', index=False)
    print(df)


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
    highscores = []
    for run in leaderboard.runs:
        seconds = run["run"].times["primary_t"]
        time = datetime.timedelta(seconds=seconds)
        #place user, personal_bests, 0, 'place'
        highscore ={
                "place": 0,
                "name": run["run"].players[0].name,
                "personal_best": str(time)
        }

        highscores.append(highscore)

    create_csv(highscores)
