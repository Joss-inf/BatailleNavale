import config as c
from parser import GetJsonParse

d = GetJsonParse()
"""
les data sont importé ici puis mis dans d pour une utilisation plus facile
"""
def init():
    game = c.game_config(d["game"]["name"],d["game"]["rows"])
    """
    insertion des paramètres de jeu dans game
    """
    arena = [["~" for i in range(game.ArenaLen)] for j in range(game.ArenaLen)]
    arena1 = [["~" for i in range(game.ArenaLen)] for j in range(game.ArenaLen)]
    """
    création de la grille de jeu
    """
    boats = Boat_ObjList()
    score:int = 0
    for boat in boats:
        score += boat.length*boat.number
    """
    calcul du score
    """
    player= c.player_config("player1",arena,arena1,boats,score)
    """
    creation du joueur
    """
    return game, player

def Boat_ObjList():
    boats = []
    for ship in d['boats']:
        boats.append(c.boats_config(str(ship["name"]),int(ship["length"]),int(ship["num"])))
        """
        itération des bateaux puis ajoue dans boat config
        """
    return boats
