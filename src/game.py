import render as r
import input as p

def game(p1,p2,game):
    """
    la fonction permet de determiner qui attaque , si le joueur a touché  , a l'eau ou gagné
    """
    turn:int = 0
    while True:
        if turn == 0:
            """
            turn 0 = p1
            """
            while True:
                print("Attack")
                r.render(p1.pMapAttack)
                print("Base")
                r.render(p1.pMapBase)
                print(p1.name+" turn")
                txt:str = "what coordinate do you want to attack ? example: b1 input :"
                res = p.SeconduserInput(p1,txt,game.ArenaLen)
                x:int = res[0]
                y:int = res[1]
                """
                on verifie si  la case est pas deja overwrite
                """
                if p1.pMapAttack[y][x] != "x"and p1.pMapAttack[y][x] != "X" :
                    break
                else:
                    print("coordinate already used")
            if p2.pMapBase[y][x] != "~":
                """
                on modifie chaque tableau pour montrer que on a touché
                """
                p2.score -= 1
                p2.pMapBase[y][x] ="X"
                p1.pMapAttack[y][x] = "X"
                print("player 2 touched !")
                if(p2.score == 0):
                    return print("PLAYER 2 HAVE NO MORE SHIP, PLAYER 1 WIN")
            else:
                p2.pMapBase[y][x] ="x"
                p1.pMapAttack[y][x] = "x"
                print("player 1 in the water")
            turn +=1
        elif turn == 1:
            """
            turn 1 = p2
            """
            while True:
                print("Attack")
                r.render(p2.pMapAttack)
                print("Base")
                r.render(p2.pMapBase)
                print(p2.name+" turn")
                txt:str = "what coordinate do you want to attack ? example: b1 input :"
                res = p.SeconduserInput(p2,txt,game.ArenaLen)
                x:int = res[0]
                y:int = res[1]
                if p2.pMapAttack[y][x] != "x"and p2.pMapAttack[y][x] != "X" :
                    break
                else:
                    print("coordinate already used")
            if p1.pMapBase[y][x] != "~":
                p1.score -= 1
                p1.pMapBase[y][x] ="X"
                p2.pMapAttack[y][x] = "X"
                print("player 2 touched !")
                if(p1.score == 0):
                    return print("PLAYER 1 HAVE NO MORE SHIP, PLAYER 1 WIN")
            elif p1.pMapBase[y][x] == "~":
                p1.pMapBase[y][x] ="x"
                p2.pMapAttack[y][x] ="x"
                print("player 2 in the water")
            turn -=1

            """
            O(n²)+O(n²)+render
            """