import config as config
import init as init


def gameLoop():
    i = init.init()
    game, player = i
    step:int = 0
    print("Welcome in the game "+game.name+" !")
    if step == 0:
        txt = "new party : 0, continue :1, record : 2, leaderboard : 3 input: "
        userInput(txt)

def userInput(type: str, str1: str):
    while True:
        try:
            res = int(input(str1))
            return res
        except ValueError:
            print('Must be a valid input')
gameLoop()
