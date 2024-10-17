import copy, init, loading as l, game as g

def menu():
    while True:
        txt = "new party : 0, continue :1, record : 2, leaderboard : 3 input: "
        a = userInput(txt)
        if a == 0:
            game,player= init.init()
            player1 = copy.deepcopy(player)
            player2 = copy.deepcopy(player)
            """
            deep copy  pour creer un nouvel objet unique avec sa propre adresse sinon c'est la meme adresse
            """
            player1.name = "player1"
            player2.name = "player2"
            """
                chargement de la config des bateaux
            """
    
            l.LoadShip(player1,game)
            l.LoadShip(player2,game)
          
            """
            lancement du jeu
            """
            print("GAME GAME GAME")
            g.game(player1,player2,game)

            if a == 1:
                 #LoadLastGame()
                i = 1
            if a == 2:
                 #LoadRecord()
                i = 1
            if a == 3:
                i = 1
                #LoadLeaderBoard()


def userInput(str1: str):
    """
    validation de  l input entre 0 et 3
    si pas un int error print
    """
    n:int = -1
    while n < 0  or n > 3:
        try:
            res = int(input(str1))
            return res
        except ValueError:
            print('Must be a valid input')
