import random
from player import *
from Items import *
from functions import askInput

def numberItems():
    return random.randint(5, 9)
    # creates an int that will show a random ammount of items available in the shop

startChoices:list = ["Enter the shop and see the shopkeeper's finest wares", 
                     "Leave and continue your journey"]
askInput(startChoices)

def getCurrentShopList():
    shopList:list = []
    # initiates a shopList list that will contain certain items out of 
    # all the items coded in the game. Chosen between 5-9 items and given 
    # at random out of all the getItemList() function which contains all items.
    for i in range(0, numberItems()+1):
        check:int = random.randint(1, len(getItemList()))
        # stores the id of the item
        if itemListID(check) in shopList:
            numberItems +=1
        # checks if the check value item has already been slected, if so, tries again
        else:
            shopList.append(itemListID(check))
        # else, simply adds the check value item into the list
    return shopList

def comparator(player:Player, itemToCompare:Item):
    inventoryList:list = ["Helmet", "Chestplate", "Bracers / Gloves",
                           "Pants", "Shoes / Boots", "Miscellaneous","Weapon"]
    # creates a list of all different type of items in the game
    type:str = itemToCompare.getItemType()
    for i in range(0, len(inventoryList) - 1):
        if type == inventoryList[i]:
            return i
        # compares the list inventoryList to the item type that is chosen by the player
        # used to verify which inventory slot to compare the chosen item to 
    if i == 5:
        print(f"You currently have :\n{player.getInventory()[5]}"
              f"\n{player.getInventory()[6]}"
              f"\n{player.getInventory()[7]}"
              f"\n{player.getInventory()[8]}")
        # misc items have 4 slots so need to show all 4
    elif i == 6:
        print(f"You currently have :\n{player.getInventory()[9]}")
        # special case for weapons since if i == 6 need to print list index #9
    else: 
        print(f"You currently have :\n{player.getInventory()[i]}")
        # every other case is simple enough
    
        
def shopChoicesPrinter():
    print("\n Please choose an item you wish to purchase.")
    choice:int = askInput(getCurrentShopList())
    

