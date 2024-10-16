def command():
        gameLoaded = False
        gameLoading = False
        while True:
            if gameLoaded is False and gameLoading is False:
                txt = "new party : 0, continue :1, record : 2, leaderboard : 3 input: "
                a = userInput(txt)
                if a == 0:
                    LoadGame()
                if a == 1:
                     LoadLastGame()
                if a == 2:
                     LoadRecord()
                if a == 3:
                     LoadLeaderBoard()
            if gameLoaded is False and gameLoading is True:
                txt = "rotate the boat : clockwise: e , anti clockwise: r \n placing the boat :  up: z, down: s , left: q, right:d"
                a = userInput(txt)
            if gameLoaded is True and gameLoading is True:
                 userInput(txt)


def userInput(str1: str):
    while True:
        try:
            res = int(input(str1))
            return res
        except ValueError:
            print('Must be a valid input')
