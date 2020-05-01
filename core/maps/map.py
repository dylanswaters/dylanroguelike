class Map:
    maxHeight = 0
    maxWidth = 0

    def __init__(self, l, h, nr):
        self.maxWidth = l
        self.maxHeight = h

    def getHeight(self):
        return self.maxHeight

    def getWidth(self):
        return self.maxWidth
