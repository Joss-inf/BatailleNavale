import render as r
import input as p


def LoadShip(player,game):
    txt = "write your coordinate ! format x1 y1 , x2, y2: 0a,0b with the maximum range of the current ship !\n input: "
    for boat in player.boats:
        num:int = boat.number
        for i in range(num):
            a:bool = True
            while a is True:
                r.render(player.pMapBase)
                print(player.name+" turn")
                print("ship: "+boat.name+"  length: "+str(boat.length))
                res = p.userInput(player,txt,game.ArenaLen,boat.length)
                a = placeBoat(res,player.pMapBase,boat.length)
                print(player.pMapAttack)

def placeBoat(res,Map,boatLen):
    x1 = res[0]
    y1 = res[1]
    x2 = res[2]
    y2 = res[3]
    if x1 == x2 and abs(y1-y2)+1 ==boatLen:
        """
        verticale
        """
        check1 = 0
        for j  in range(boatLen):
            if Map[j][x1] != "~":
                check1 += 1
        if check1 == 0:
            for i  in range(boatLen):
                Map[i][x1] = "O"
            return False
        else:
            print("collision")
            return True
    elif y1 == y2 and abs(x1-x2)+1 == boatLen:
        """
        horizontale
        """
        check2 = 0
        for j  in range(boatLen):
            if Map[y1][j] != "~":
                check2 += 1
        if check2 == 0:
            for i  in range(boatLen):
                Map[y1][i] = 'O'
            return False
        else:
            print("collision")
            return True
    else:
            print("coordonnées invalide ! colonne ou ligne")
            return True

def CheckCoordinate(x1,y1,x2,y2,tab):
    e = "~"
    """
    check si les coordoonées chevauche des items en ligne ou colonne  différent de e et renvoit true si oui
    """
    if x1 != x2:
        for y in range(min(y1, y2), max(y1, y2) ):
            if tab[x1][y] != e:
                return True
    else:
        for x in range(min(x1, x2), max(x1, x2) ):
            if tab[x][y1] != e:
                return True

    return False

