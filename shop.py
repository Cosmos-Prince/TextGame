import random
from player import *
from Items import *
from functions import askInput


def numberItems():
    return random.randint(5, 9)
    # creates an int that will show a random ammount of items available in the shop    

def getCurrentShopList(numberOfItems:int):
    shopList:list = []
    # initiates a shopList list that will contain certain items out of 
    # all the items coded in the game. Chosen between 5-9 items and given 
    # at random out of all the getItemList() function which contains all items.
    for i in range(0, numberOfItems+1):
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

    print("Do you wish to purchase this item?")
    match askInput(["Yes", "No"]):
        case 1:
            buy(getItemID(itemToCompare), player)
            if buy(getItemID(itemToCompare), player) == False:
                return False
            else:
                return

        case 2:
            return False
    
def buy(itemNumber:int, player:Player):
    itemID:Item = itemListID(itemNumber)
    if player.getGold() < itemID.getItemPrice():
        print("You can't buy that! You're broke af!")
        return False
    else:
        player.changeGold(itemID.getItemPrice(), False)
        player.setItems(itemID)


def undo(purchaseHistory:list):
    if len(purchaseHistory) == 0:
        print("You can't undo something you haven't done yet!")
        return
        # checks if the purchase history is empty 
    else:
        purchaseHistory.pop()
        return
        # pop simply removes the last entry of a list, removing the last purchase in the shop

def shopEntrance(player:Player):
    purchaseHistory:list = []
    # creates/empties a purchase history list to enable stack logic for undo function
    while True:
    # Loop to keep you in the shop logic, breaks at a couple of points to 
    # let you exit and return to fighting whenever broke
        numberOfItemsInstance:int = numberItems()
        # creates a variable that stores the ammount of items for this instance of the shop
        currentShopList:list = getCurrentShopList(numberOfItemsInstance)
        startChoices:list = ["See the shopkeeper's finest wares", 
                         "Leave and continue your journey"]
        input = askInput(startChoices)
        match input:
            case 1:
                print("Hello and welcome to my shop humble adventurer!"
                "Please take a look at my wares!\n")
                shopMenu(player, numberOfItemsInstance, currentShopList, purchaseHistory)
            case 2:
                print("You leave the shop and continue your journey.")
                break

            
def shopMenu(player:Player, numberOfItems:int, itemInShopList:list, pruchaseHistory:list):
    print("\n Please choose an item you wish to purchase.")
    choice:int = askInput(itemInShopList.append("Leave the shop."))
    if choice == len(itemInShopList):
        print("Thank you come again!")
        return
    
    else:
        if comparator(player, itemInShopList[choice]) == False:
            shopMenu(player, numberOfItems, itemInShopList)
        else:
            pruchaseHistory.append(itemInShopList[choice])
