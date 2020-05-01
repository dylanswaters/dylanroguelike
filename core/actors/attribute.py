class Attribute:
    name = ""
    baseScore = 0
    modifiedScore = 0
    minScore = 0
    maxScore = 0

    def __init__(self, name, min, max, score):
        self.name = name
        self.minScore = min #lowest value this attribute can have
        self.maxScore = max #highest value this attribute can have
        self.baseScore = score #the 'default' score, assuming no modifiers
        self.modifiedScore = self.baseScore #score including modifiers

    # ex:
    # name: strength
    # min: 1
    # max: 10
    # base: 5

    def __str__(self):
        return self.name + ": " + str(self.modifiedScore) + " [" + str(self.minScore) + "-" + str(self.maxScore) + "]"

    def getbaseScore(self):
        return self.baseScore

    def getModifiedScore(self):
        return self.modifiedScore

    def getMin(self):
        return self.minScore

    def getMax(self):
        return self.maxScore

    def getName(self):
        return self.name

    def setbaseScore(self, baseScore):
        if(baseScore < self.baseScore):
            self.baseScore = self.minScore
        elif(baseScore > self.baseScore):
            self.baseScore = self.maxScore
        else:
            self.baseScore = baseScore

    def setModifiedScore(self, modifiedScore):
        if(modifiedScore < self.modifiedScore):
            self.modifiedScore = self.minScore
        elif(modifiedScore > self.modifiedScore):
            self.modifiedScore = self.maxScore
        else:
            self.modifiedScore = modifiedScore

    def setMin(self,min):
        self.minScore = min
        if(self.baseScore < self.minScore):
            self.baseScore = self.minScore
        if(self.modifiedScore < self.minScore):
            self.modifiedScore = self.minScore

    def setMax(self,max):
        self.maxScore = max
        if(self.baseScore > self.maxScore):
            self.baseScore = self.maxScore
        if(self.modifiedScore > self.maxScore):
            self.modifiedScore = self.maxScore

    def setName(self,name):
        self.name = name

    def incrementBaseScore(self,value):
        self.baseScore += value
        self.modifiedScore += value
        if(self.baseScore > self.maxScore):
            self.baseScore = self.maxScore
        if(self.modifiedScore > self.maxScore):
            self.modifiedScore = self.maxScore

    def decrementBaseScore(self,value):
        self.baseScore -= value
        self.modifiedScore -= value
        if(self.baseScore < self.minScore):
            self.baseScore = self.minScore
        if(self.modifiedScore < self.minScore):
            self.modifiedScore = self.minScore

    def incrementModifiedScore(self,value):
        self.modifiedScore += value
        if(self.modifiedScore > self.maxScore):
            self.modifiedScore = self.maxScore

    def decrementModifiedScore(self,value):
        self.modifiedScore -= value
        if(self.modifiedScore < self.minScore):
            self.modifiedScore = self.minScore
