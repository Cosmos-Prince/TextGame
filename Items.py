
class Item:
    def __init__(self, name:str, price:int, statName:str, statBonus:int, itemType:str):
        self.__itemName:str = name
        self.__price:int = price
        self.__statUpgraded:str = statName
        self.__bonus:int = statBonus
        self.__itemType:str = itemType
    # Constructor for every item, statUpgraded dictates which stat gets a bonus and itemType
    # dictates which inventory slot it will go in

    def __str__(self):
        return f"   {self.__itemName} | {self.__price} gold | +{self.__bonus} {self.__statUpgraded} | {self.__itemType}"
    # When called with print(ItemName), will print the message above with all stats.
    # Will be used in shop "interface"

### creation of classes
# super parent class is item
# child class Armor which is parent to all armor classes (helmet, chest, pants, boots, arms)
# Weapon and misc are still childs of Item since they dont have the same stats changed as Armor
class Armor(Item):
    def __init__(self, name:str, price:int, statBonus:int, itemType:str):
        super().__init__(name, price, "Defense", statBonus, itemType)

class Helmet(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Helmet")

class Chest(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Chestplate")

class Arms(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Bracers / Gloves")

class Pants(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Pants")

class Feet(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Shoes / Boots")
        
class Misc(Item):
    def __init__(self, name:str, price:int, statName:str, statBonus:int):
        super().__init__(name, price, statName, statBonus, "Miscellaneous")

class Weapon(Item):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, "Damage", statBonus, "Weapon")

# Creates all different kinds of child items to fit them into the inventory of the player

###############   Helmets    ###############    

Helmet1 = Helmet("Crane reluisant", 40, 4)
Helmet2 = Helmet("Yankee with no brim", 30, 3)
Helmet3 = Helmet("Fallen king's crown", 20, 2)
Helmet4 = Helmet("Perruque de Remilli", 10, 1)
Helmet5 = Helmet("Une tuque aek dla broche", 50, 5)

###############    Chestplates    ###############

Chest1 = Chest("Hoodie rouge a Emile", 50, 5)
Chest2 = Chest("Diamond chestplate", 40, 4)
Chest3 = Chest("Un beater blanc", 10, 1)
Chest4 = Chest("Power Armor", 30, 3)
Chest5 = Chest("Ugly Xmas Sweater", 20, 2)

###############    Arms    ###############

Arms1 = Arms("Ein ti braclet d'amitie", 10, 1)
Arms2 = Arms("Holy bracelet", 20, 2)
Arms3 = Arms("Shoulder Pad", 30, 3)
Arms4 = Arms("OJ's gloves", 50, 5)
Arms5 = Arms("Infinity Gauntlet", 40, 4)

###############    Pants    ###############

Pants1 = Pants("Les pants a Super Fancy Pants Adventure", 30, 3)
Pants2 = Pants("Joggings gris", 10, 1)
Pants3 = Pants("Chainmail pants", 40, 4)
Pants4 = Pants("Pyjamas", 20, 2)
Pants5 = Pants("Pantalons de neige", 50, 5)

###############    Feet    ###############

Feet1 = Feet("Gougounnes", 10, 1)
Feet2 = Feet("Timbs", 20, 2)
Feet3 = Feet("Bottes a cap d'acier", 30, 3)
Feet4 = Feet("Des crocs en mode sport", 40, 4)
Feet5 = Feet("Sonic's red shoes", 50, 5)

###############    Misc~    ###############

Misc1 = Misc("Skibidiamant", 20, "Damage", 2)
Misc2 = Misc("Pierres aux reins dans un p'tit pot d'pillules", 40, "Damage", 4)
Misc3 = Misc("Meni artefact famillial Tasse", 20, "Defense", 2)
Misc4 = Misc("Une garnotte", 10, "Damage", 1)
Misc5 = Misc("Une roche", 20, "Damage", 2)
Misc6 = Misc("Un pick de guit a Purok", 10, "Damage", 1)
Misc7 = Misc("Steve la roche", 20, "Damage", 2)
Misc8 = Misc("J'ai des lunettes tu peux pas mfesser", 20, "Defense", 2)
Misc9 = Misc("Une monster blanche", 30, "Damage", 3)
Misc10 = Misc("Un des kids a Le Sau ?", 30, "Damage", 3)
Misc11 = Misc("Ring of protection (Inscrit \"Juste pour le 21e doigt\" ?)", 20, "Defense", 2)
Misc12 = Misc("Jackstrap", 20, "Defense", 2)
Misc13 = Misc("The One Ring pogné au Walmart", 10, "Defense", 1)
Misc14 = Misc("Idole d'Astrarok", 30, "Defense", 3)
Misc15 = Misc("un set de dés", 20, "Defense", 2)

###############    Weapons    ###############

Weapon1 = Weapon("Epee des cramptes", 60, 6)
Weapon2 = Weapon("Quoicoupelle", 70, 7)
Weapon3 = Weapon("Le boulet a Boulet", 50, 5)
Weapon4 = Weapon("Objet phallique mauve en sillicone", 10, 1)
Weapon5 = Weapon("Cool stick you found", 20, 2)
Weapon6 = Weapon("Crowbar", 30, 3)
Weapon7 = Weapon("La guit a Purok", 40, 4)


# list containing all items
weaponList:list = [Weapon1, Weapon2, Weapon3, Weapon4, Weapon5, Weapon6, Weapon7]
miscList:list = [Misc1, Misc2, Misc3, Misc4, Misc5, Misc6, Misc7, Misc8, Misc9, Misc10, Misc11, Misc12, Misc13, Misc14, Misc15]
feetList:list = [Feet1, Feet2, Feet3, Feet4, Feet5]
pantsList:list = [Pants1, Pants2, Pants3, Pants4, Pants5]
chestList:list = [Chest1, Chest2, Chest3, Chest4, Chest5]
helmetList:list = [Helmet1, Helmet2, Helmet3, Helmet4, Helmet5]
# sublists for better readability & maybe future updates

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
# creates a list containing every item in all the other sub lists
# itemList = [stuffList] would create a list of lists, i dont want that