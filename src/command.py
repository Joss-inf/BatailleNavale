import init
import loading as l
import copy

def command():
        gameLoaded = False
        gameLoading = False
        while True:
            if gameLoaded is False and gameLoading is False:
                txt = "new party : 0, continue :1, record : 2, leaderboard : 3 input: "
                a = userInput(txt)
                if a == 0:
                    game,player= init.init()
                    player1 = copy.deepcopy(player)
                    player2 = copy.deepcopy(player)
                    player1.name = "player1"
                    player2.name = "player2"
                    l.LoadShip(player1,game)
                    l.LoadShip(player2,game)
                    
                if a == 1:
                     #LoadLastGame()
                     i = 1
                if a == 2:
                     #LoadRecord()
                     i = 1
                if a == 3:
                     i = 1
                     #LoadLeaderBoard()
            if gameLoaded is True and gameLoading is True:
                 userInput(txt)


def userInput(str1: str):
    while True:
        try:
            res = int(input(str1))
            return res
        except ValueError:
            print('Must be a valid input')
