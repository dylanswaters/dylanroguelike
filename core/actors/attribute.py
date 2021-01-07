class Attribute:
    # name, currScore, minScore, maxScore
    stats = {}

    def __init__(self, dictToCopy):
        self.stats = dictToCopy
        self.stats["current"] = int(self.stats["min"])

    def getValue(self):
        return int(self.stats["current"])

    def setStat(self, newValue):
        if(newValue < int(self.stats["min"])):
            self.stats["current"] = int(self.stats["min"])
        if(newValue > int(self.stats["max"])):
            self.stats["current"] = int(self.stats["max"])
        else:
            self.stats["current"] = newValue

    def min(self):
        return int(self.stats["min"])

    def max(self):
        return int(self.stats["max"])

    def getName(self):
        return self.stats["name"]

    def __str__(self):
        return self.stats["name"] + ":" + str(self.stats["current"])
