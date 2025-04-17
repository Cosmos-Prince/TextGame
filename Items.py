class Item:
    def __init__(self, name:str, price:int, statName:str, statBonus:int, itemType:str):
        self.__itemName:str = name
        self.__price:int = price
        self.__statUpgraded:str = statName
        self.__bonus:int = statBonus
        self.__itemType:str = itemType
    # Constructor for every item, statUpgraded dictates which stat gets a bonus and itemType
    # dictates which inventory slot it will go in
    def getItemType(self):
        return self.__itemType 
    
    def getItemPrice(self):
        return self.__price
    # getter for price, used in shop price comparison/check to see if you have enough to buy

    def describeItem(self):
        return (f" {self.__itemName} | {self.__price} gold | +{self.__bonus} {self.__statUpgraded} | "
        f"{self.__itemType}")

    def __str__(self):
        return (f" {self.__itemName} | {self.__price} gold | +{self.__bonus} {self.__statUpgraded} |"
        f"{self.__itemType}")
    # When called with print(ItemName), will print the message above with all stats.
    # Will be used in shop "interface"

### creation of classes
# super parent class is item
# child class Armor which is parent to all armor classes (helmet, chest, pants, boots, arms)
# Weapon and misc are still childs of Item since they dont have the same stats changed as Armor
class Potion(Item):
    def __init__(self):
        super().__init__("Potion of healing", 10, "Health", None, "Potion")
    
potion:Potion = Potion()

class Armor(Item):
    def __init__(self, name:str, price:int, statBonus:int, itemType:str):
        super().__init__(name, price, "Defense", statBonus, itemType) 

class Helmet(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Helmet")

    def __str__():
        Item.__str__()    

class Chest(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Chestplate")

    def __str__():
        Item.__str__()    

class Arms(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Bracers / Gloves")

    def __str__():
        Item.__str__()    

class Pants(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Pants")

    def __str__():
        Item.__str__()    

class Feet(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Shoes / Boots")

    def __str__():
        Item.__str__()    
        
class Misc(Item):
    def __init__(self, name:str, price:int, statName:str, statBonus:int):
        super().__init__(name, price, statName, statBonus, "Miscellaneous")

    def __str__():
        Item.__str__()    

class Weapon(Item):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, "Damage", statBonus, "Weapon")

    def __str__():
        Item.__str__()    

# Creates all different kinds of child items to fit them into the inventory of the player

###############   Helmets    ###############    

baseHelmet:Helmet = Helmet("Tes vieux cheveux laites", 0, 0)
Helmet1:Helmet = Helmet("Crane reluisant", 40, 4)
Helmet2:Helmet = Helmet("Yankee with no brim", 30, 3)
Helmet3:Helmet = Helmet("Fallen king's crown", 20, 2)
Helmet4:Helmet = Helmet("Perruque de Remilli", 10, 1)
Helmet5:Helmet = Helmet("Une tuque aek dla broche", 50, 5)

###############    Chestplates    ###############

baseChest:Chest = Chest("Ton poil de chest", 0, 0)
Chest1:Chest = Chest("Hoodie rouge a Emile", 50, 5)
Chest2:Chest = Chest("Diamond chestplate", 40, 4)
Chest3:Chest = Chest("Un beater blanc", 10, 1)
Chest4:Chest = Chest("Power Armor", 30, 3)
Chest5:Chest = Chest("Ugly Xmas Sweater", 20, 2)

###############    Arms    ###############

baseArms:Arms = Arms("absolument rien", 0, 0)
Arms1:Arms = Arms("Ein ti braclet d'amitie", 10, 1)
Arms2:Arms = Arms("Holy bracelet", 20, 2)
Arms3:Arms = Arms("Shoulder Pad", 30, 3)
Arms4:Arms = Arms("OJ's gloves", 50, 5)
Arms5:Arms = Arms("Infinity Gauntlet", 40, 4)

###############    Pants    ###############

basePants:Pants = Pants("Pantalons en lambeaux", 0, 0)
Pants1:Pants = Pants("Les pants a Super Fancy Pants Adventure", 30, 3)
Pants2:Pants = Pants("Joggings gris", 10, 1)
Pants3:Pants = Pants("Chainmail pants", 40, 4)
Pants4:Pants = Pants("Pyjamas", 20, 2)
Pants5:Pants = Pants("Pantalons de neige", 50, 5)

###############    Feet    ###############

baseFeet:Feet = Feet("T'es nu pieds", 0, 0)
Feet1:Feet = Feet("Gougounnes", 10, 1)
Feet2:Feet = Feet("Timbs", 20, 2)
Feet3:Feet = Feet("Bottes a cap d'acier", 30, 3)
Feet4:Feet = Feet("Des crocs en mode sport", 40, 4)
Feet5:Feet = Feet("Sonic's red shoes", 50, 5)

###############    Misc~    ###############

baseMisc:Misc = Misc("Absolument rien", 0, "nothing", 0)
Misc1:Misc = Misc("Skibidiamant", 20, "Damage", 2)
Misc2:Misc = Misc("Pierres aux reins dans un p'tit pot d'pillules", 40, "Damage", 4)
Misc3:Misc = Misc("Meni artefact famillial Tasse", 20, "Defense", 2)
Misc4:Misc = Misc("Une garnotte", 10, "Damage", 1)
Misc5:Misc = Misc("Une roche", 20, "Damage", 2)
Misc6:Misc = Misc("Un pick de guit a Purok", 10, "Damage", 1)
Misc7:Misc = Misc("Steve la roche", 20, "Damage", 2)
Misc8:Misc = Misc("J'ai des lunettes tu peux pas mfesser", 20, "Defense", 2)
Misc9:Misc = Misc("Une monster blanche", 30, "Damage", 3)
Misc10:Misc = Misc("Un des kids a Le Sau ?", 30, "Damage", 3)
Misc11:Misc = Misc("Ring of protection (Inscrit \"Juste pour le 21e doigt\" ?)", 20, "Defense", 2)
Misc12:Misc = Misc("Jackstrap", 20, "Defense", 2)
Misc13:Misc = Misc("The One Ring pogné au Walmart", 10, "Defense", 1)
Misc14:Misc = Misc("Idole d'Astrarok", 30, "Defense", 3)
Misc15:Misc = Misc("un set de dés", 20, "Defense", 2)

###############    Weapons    ###############

baseWeapon:Weapon = Weapon("Epee en bois", 0, 0)
Weapon1:Weapon = Weapon("Epee des cramptes", 60, 6)
Weapon2:Weapon = Weapon("Quoicoupelle", 70, 7)
Weapon3:Weapon = Weapon("Le boulet a Boulet", 50, 5)
Weapon4:Weapon = Weapon("Objet phallique mauve en sillicone", 10, 1)
Weapon5:Weapon = Weapon("Cool stick you found", 20, 2)
Weapon6:Weapon = Weapon("Crowbar", 30, 3)
Weapon7:Weapon = Weapon("La guit a Purok", 40, 4)


# list containing all items
weaponList:list = [Weapon1, Weapon2, Weapon3, Weapon4, Weapon5, Weapon6, Weapon7]
miscList:list = [Misc1, Misc2, Misc3, Misc4, Misc5, Misc6, Misc7, Misc8, Misc9, Misc10, Misc11, Misc12, Misc13, Misc14, Misc15]
feetList:list = [Feet1, Feet2, Feet3, Feet4, Feet5]
pantsList:list = [Pants1, Pants2, Pants3, Pants4, Pants5]
chestList:list = [Chest1, Chest2, Chest3, Chest4, Chest5]
helmetList:list = [Helmet1, Helmet2, Helmet3, Helmet4, Helmet5]
# sublists for better readability & maybe future updates
def getItemList():
    itemList:list = []
    for w in weaponList:
        itemList.append(w)
    for m in miscList:
        itemList.append(m)
    for f in feetList:
        itemList.append(f)
    for p in pantsList:
        itemList.append(f)
    for c in chestList:
        itemList.append(f)
    for h in helmetList:
        itemList.append(f)
    return itemList
    # creates a list containing every item in all the other sub lists
    # itemList = [stuffList] would create a list of lists, i dont want that

def itemListID(position:int):
    tempList:list = getItemList()
    item:Item = tempList[position]
    return item
    # function to return the item at position x in the item list

def getItemID(item:Item):
    itemList:list = getItemList()
    for i in range(0, len(itemList)):
        if item == itemList[i]:
            return i
# returns a number associated with which item in the entire list this is, inverse of itemListID