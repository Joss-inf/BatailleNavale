
import render as r


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
                res = userInput(player,txt,game.ArenaLen,boat.length)
                a = placeBoat(res,player.pMapBase,boat.length)


def userInput(player,str1: str,L:int,boatL):
    while True:
        res = input(str1)
        try:
            a, b = res.split(",")
            x1 = a[0].lower()
            y1 = a[1:]
            x2 = b[0].lower()
            y2 = b[1:]
            check = True
            # Validate x1 and x2 as single letters from the alphabet
            if not (x1.isalpha() and len(x1) == 1 and x2.isalpha() and len(x2) == 1):
                print("x1 and x2 must be single letters from the alphabet.")
                check = False
            ch:list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

            if x1 in ch:
                x1 = ch.index(x1)
            elif x1 not in ch:
                check = False
            if x2 in ch:
                x2 = ch.index(x2)
            elif x2 not in ch:
                check = False
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)-1
            y2 = int(y2)-1

            if x1 < 0 or x2 < 0 or y1 < 0 or x2 < 0 or x1 > L or x2 > L or y1 > L or x2 > L or x1 == x2 and abs(y1-y2) != boatL-1  or y1 == y2 and abs(x1-x2) != boatL-1  :
                check = False
                """
                check si l'input est correct
                """
            a:list = [x1,y1,x2,y2]
            if check is True :
                return a
            else:
                r.render(player.pMapBase)
                print("out of range !")
        except (ValueError, IndexError) as e:
            print(f"Invalid input: {e}")
            r.render(player.pMapBase)
            print("Must be a valid input!")

def placeBoat(res,Map,boatLen):
    x1 = res[0]
    y1 = res[1]
    x2 = res[2]
    y2 = res[3]
    print(x1,x2,y1,y2)
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
                Map[i][x1] = 'O'
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

