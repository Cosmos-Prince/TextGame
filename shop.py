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
            return
        case 2:
            return False
    
def buy(itemNumber:int, player:Player, history:list):
    itemID:Item = itemListID(itemNumber)
    if player.getGold() < itemID.getItemPrice():
        print("You can't buy that! You're broke af!")
        return False
    else:
        player.changeGold(itemID.getItemPrice(), False)
        history.append(BuyOperation(player, itemID))
        return history
    # handles the logic of buying items, checks if the player has 
    # enough gold to buy desired item and stores info into list of purchase history

class BuyOperation():
    def __init__(self, player:Player, item:Item):
        self.__player:Player = player
        self.__price:int = item.getItemPrice()
        self.__oldItem:Item = player.setItems(item)
    
    def undo(self):
        self.__player.changeGold(self.__price, True)
        self.__player.setItems(self.__oldItem)
# class to store single transactions in the shop
# used in undo logic

def undoPurchase(purchaseHistory:list):
    if len(purchaseHistory) == 0:
        print("You can't undo something you haven't done yet!")
        return
        # checks if the purchase history is empty 
    else:
        purchaseHistory.pop().undo()
        return
        # pop simply removes the last entry of a list, removing the last purchase in the shop
        # gives it to BuyOperation's function to undo the effects of the purchase 
        # (gold change + item change)

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

            
def shopMenu(player:Player, numberOfItems:int, itemInShopList:list, purchaseHistory:list):
    print("\n Please choose an item you wish to purchase.")
    choice:int = askInput(itemInShopList.append("Undo my last purchase", "Sell my items", "Leave the shop."))
    if choice == len(itemInShopList):
        print("Thank you come again!")
        return
    elif choice == len(itemInShopList) - 1:
        print("You want to sell me your old smelly and broken gear? "
        "HA! On me l'avais pas fait celle la depuis longtemps!")
        shopMenu(player, numberOfItems, itemInShopList, purchaseHistory)

    elif choice == len(itemInShopList) - 2:
        undoPurchase(purchaseHistory)
    else:
        wishToBuy:bool = comparator(player, itemInShopList[choice])
        if wishToBuy == False:
            shopMenu(player, numberOfItems, itemInShopList, purchaseHistory)
        else:
            newPurchaseHistory:list = buy(itemInShopList[choice], player, purchaseHistory)        
            shopMenu(player, numberOfItems, itemInShopList, newPurchaseHistory)

            
