import render as r
def userInput(player,str1: str,L:int,boatL):
    """
    ici on gère certain inputs complexes 
    """
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


def SeconduserInput(player,str1: str,L:int):
    """
    ici on gere des inputs + simple
    """
    while True:
        res = input(str1)
        try:
            x1 = res[0].lower()
            y1 = res[1:]
            check = True
            # Validate x1 and x2 as single letters from the alphabet
            if not (x1.isalpha() and len(x1) == 1):
                print("x1  must be single letters from the alphabet.")
                check = False
            ch:list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

            if x1 in ch:
                x1 = ch.index(x1)
                """
                ajoute l'index de la lettre si elle existe
                """
            elif x1 not in ch:
                check = False
            x1 = int(x1)
            y1 = int(y1)-1
            if x1 < 0  or y1 < 0 or x1 > L or y1 > L  :
                check = False
                """
                check si l'input est correct
                """
            a:list = [x1,y1]
            if check is True :
                return a
            else:
                r.render(player.pMapBase)
                print("out of range !")
        except (ValueError, IndexError) as e:
            print(f"Invalid input: {e}")
            r.render(player.pMapBase)
            print("Must be a valid input!")