itemIDCounter = 0

class Item:
    name = ""
    itemType = ""
    id = 0
    weight = 0

    def __init__(self, name, itemType, weight):
        global itemIDCounter
        self.name = name
        self.itemType = itemType
        self.weight = weight
        self.id = itemIDCounter
        itemIDCounter += 1

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getItemType(self):
        return self.itemType

    def setItemType(self,newItemType):
        self.itemType = newItemType

    def getID(self):
        return

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight
