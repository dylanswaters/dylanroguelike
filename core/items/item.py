import csv
itemIDCounter = 0

# returns list of items
def createItemsFromCSV(csvFile, itemType):
    itemList = []
    itemDicts = csv.DictReader(open(csvFile))

    for item in itemDicts:
        item["itemType"] = itemType
        itemList.append(Item(item))

    return itemList


class Item:
    stats = {}

    def __init__(self, dictToCopy):
        global itemIDCounter
        # we want to make a copy of the dict
        self.stats = dict(dictToCopy)
        self.stats["ID"] = itemIDCounter
        itemIDCounter += 1
        if("itemType" not in self.stats):
            self.stats["itemType"] = "Misc Item"
        if("weight" not in self.stats):
            self.stats["weight"] = 0

    def getStat(self, name):
        return self.stats[name]

    def setStat(self, name, newValue):
        self.stats[name] = newValue
