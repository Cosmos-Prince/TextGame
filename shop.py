import random
from player import *
from Items import *
from functions import askInput

numberItems:int = random.randint(5, 9)
# creates an int that will show a random ammount of items available in the shop

startChoices:list = ["Enter the shop and see the shopkeeper's finest wares", "Leave and continue your journey"]
askInput(startChoices)

shopList:list = []
# initiates a shopList list that will contain the "#id" of all items coded in the game
# ex: shopList = [1, 3, 9, 7, 2] will show item # 1-3-9-7-2
for i in range(0, numberItems+1):
    check:int = random.randint(1, NOMBRES-DITEMS-TOTAUX-FAUT-CHANGER-CA-LA-LA)
    # stores the id of the item
    if check in shopList:
        numberItems +=1
    # checks if the check value has already been slected, if so, tries again
    else:
        shopList += check
    # else, simply adds the check value into the list

def comparator(player, )
