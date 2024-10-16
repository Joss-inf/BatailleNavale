import config as config
import init as init


def gameLoop():
    init.init()

    step:int = 0
    if step == 0:
        
        userInput()
        step+=1
    if step == 1:step+=1

    if step == 2:print("goulougoulou")

gameLoop()

def userInput(type:str,str1:str):
    while True:
        try:
            res =''
            if(type == "float"):
                res = float(input(str1))
            if(type == "str"):.
                res = str(input(str1))
            if(type == "int"):
                res = int(input(str1))
            return res
        except ValueError:
            print('Must be a valid input ')