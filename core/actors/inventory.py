from core.items.item import *

class Inventory:
    items = []
    weight = 0

    def __init__(self):
        self.items = []
        self.weight = 0

    def getWeight(self):
        return self.weight

    def addItem(self,newItem):
        self.items.append(newItem)
        self.weight += newItem.getStat("weight")

    # returns the item, as well as removing it
    def popItemByIndex(self,index):
        retItem = self.items[index]
        del self.items[index]
        self.weight -= retItem.getStat("weight")
        return retItem

    def popItemByItem(self,checkItem):
        for invItem in self.items:
            if(invItem == checkItem):
                self.items.remove(invItem)
                self.weight -= invItem.getStat("weight")
                return invItem

    def popItemByID(self,id):
        for invItem in self.items:
            if(invItem.getStat("ID") == id):
                self.items.remove(invItem)
                self.weight -= invItem.getStat("weight")
                return invItem

    # returns and removes the first item with a matching name
    def popItemByName(self,name):
        for invItem in self.items:
            if(invItem.getStat("name") == name):
                self.items.remove(invItem)
                self.weight -= invItem.getStat("weight")
                return invItem

    def getItemByIndex(self,index):
        return self.items[index]

    def getItemByItem(self,checkItem):
        for invItem in self.items:
            if(invItem == checkItem):
                return invItem

    def getItemByID(self,id):
        for invItem in self.items:
            if(invItem.getStat("ID") == id):
                return invItem

    def getCountOfItem(self, itemName):
        count = 0
        for item in self.items:
            if(item.getStat("name") == itemName):
                count += 1
        return count

    def getCountOfItems(self):
        countDict = {}
        for item in self.items:
            if(item.getStat("name") in countDict):
                countDict[item.getStat("name")] = countDict[item.getStat("name")] + 1
            else:
                countDict[item.getStat("name")] = 1
        return countDict
