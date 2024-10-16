import config as c
from parser import GetJsonParse

d = GetJsonParse()
"""
les data sont importé ici puis mis dans d pour une utilisation plus facile
"""
def setup():
    init()



def init():
    game = c.game_config(d["game"]["name"],d["game"]["rows"])
    """
    insertion des paramètres de jeu dans game
    """
    arena= [["~" for i in range(game.ArenaLen)] for j in range(game.ArenaLen)]
    """
    création de la grille de jeu
    """
    boats = Boat_Obj()

    player1 = c.player_config("player1",arena,arena,boats,initScore(boats))
    player2 = player1
    player2.name = "player2"
    """
    creation des joueurs
    """
def Boat_Obj():
    names:list = []
    lengths:list = []
    nums:list = []
    """
    init des list
    """

    for boat in d['boats']:
        names.append(boat["name"])
        lengths.append(int(boat["length"]))
        nums.append(int(boat["num"]))
        """
        itération des bateaux et ajout dans une list puis return en objets dans boat config
        """
    return c.boats_config(names,lengths,nums)

def initScore(b):
    score:int = 0
    for x, y in zip(b.length, b.number):
        score += x * y
#calcul du score pour determiner quand est ce que le joueur a perdu
setup()