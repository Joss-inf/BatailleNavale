class game_config:
    def __init__(self,name:str,ArenaLen:int):
        self.name = name
        self.ArenaLen =  ArenaLen
"""
objet config du jeu pour les paramètres de base
"""
class boats_config:
    def __init__(self, name:list,caseLen:list,number:list):
        self.name = name
        self.length= caseLen
        self.number=  number
"""
objet boats pour les bateaux
"""
class player_config:
    def __init__(self, name:str,PmapAttack:list,PmapBase:list,boats:list,score:int):
        self.name = name
        self.pMapAttack = PmapAttack
        self.pMapBase =  PmapBase
        self.boats = boats
        self.score = score

"""
objet player avec ses parametres
"""