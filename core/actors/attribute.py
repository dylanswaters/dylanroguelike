class Attribute:
    # name, currScore, minScore, maxScore
    stats = {
        "name" # what the stat is called
        "min" # lowest possible val a stat can have
        "max" # highest possible val a stat can have
        "current" # current value for stat
        "softmax" # soft cap for current ex: max hp: 1000, current: 50, softmax: 100
    }

    def __init__(self, dictToCopy):
        self.stats = dictToCopy
        self.stats["current"] = int(self.stats["min"])
        self.stats["softmax"] = int(self.stats["current"])
        # print(self.stats)

    def getValue(self):
        return int(self.stats["current"])

    def setStat(self, newValue):
        if(newValue > int(self.stats["softmax"])):
            self.stats["current"] = int(self.stats["softmax"])
        elif(newValue < int(self.stats["min"])):
            self.stats["current"] = int(self.stats["min"])
        elif(newValue > int(self.stats["max"])):
            self.stats["current"] = int(self.stats["max"])
        else:
            self.stats["current"] = newValue

    def setsm(self, newValue):
        if(newValue < int(self.stats["softmax"])):
            self.stats["softmax"] = newValue
            self.stats["current"] = newValue
        elif(newValue > int(self.stats["softmax"])):
            diff = newValue - int(self.stats["softmax"])
            # print(diff)
            self.stats["softmax"] = newValue
            self.stats["current"] = self.stats["current"] + diff
        else:
            return

    def min(self):
        return int(self.stats["min"])

    def max(self):
        return int(self.stats["max"])

    def softmax(self):
        return int(self.stats["softmax"])

    def getName(self):
        return self.stats["name"]

    def __str__(self):
        return self.stats["name"] + ":" + str(self.stats["current"]) + "/" + str(self.stats["softmax"])
