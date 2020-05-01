from core.items.item import *

class Inventory:
    items = []
    weight = 0

    def getWeight(self):
        return self.weight

    def addItem(self,newItem):
        self.items.append(newItem)
        self.weight += newItem.getWeight()

    # returns the item, as well as removing it
    def popItemByIndex(self,index):
        retItem = self.items[index]
        del self.items[4]
        self.weight -= retItem
        return retItem

    def popItemByItem(self,checkItem):
        for invItem in self.items:
            if(invItem.getID() == checkItem.getID()):
                self.items.remove(invItem)
                self.weight -= invItem.getWeight()
                return invItem

    def getItemByIndex(self,index):
        return self.items[index]

    def getItemByItem(self,checkItem):
        for invItem in self.items:
            if(invItem.getID() == checkItem.getID()):
                return invItem
