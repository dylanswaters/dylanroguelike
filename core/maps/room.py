class Room:
    xMin = 0
    xMax = 0
    yMin = 0
    yMax = 0
    size = 1.0
    prevXMax = 0
    prevYMax = 0

    def __init__(self, xMin, xMax, yMin, yMax, size):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.size = size
        self.prevXMax = xMax
        self.prevYMax = yMax

    def __str__(self):
        return "x:"+str(self.xMin)+"-"+str(self.xMax)+" y:"+str(self.yMin)+"-"+str(self.yMax)+" size:"+str(self.size)

    def getXMin(self):
        return self.xMin

    def setXMin(self, xMin):
        self.xMin = xMin

    def getXMax(self):
        return self.xMax

    def setXMax(self, xMax):
        self.xMax = xMax

    def getYMin(self):
        return self.yMin

    def setYMin(self, yMin):
        self.yMin = yMin

    def getYMax(self):
        return self.yMax

    def setYMax(self, yMax):
        self.yMax = yMax

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getPrevXMax(self):
        return self.prevXMax

    def setPrevXMax(self, prevXMax):
        self.prevXMax = prevXMax

    def getPrevYMax(self):
        return self.prevYMax

    def setPrevYMax(self, prevYMax):
        self.prevYMax = prevYMax

    def getCenterX(self):
        return self.xMin + int((self.xMax - self.xMin)/2)

    def getCenterY(self):
        return self.yMin + int((self.yMax - self.yMin)/2)
