class Tile:
    blocked = True
    actorInTile = None
    token = ""
    #a tile of the map and its properties
    def __init__(self):
        self.blocked = False
        self.actorInTile = None
        self.token = "-"

    def __str__(self):
        return self.token

class TileLink(Tile):
    link = None

    def __init__(self):
        Tile.__init__(self)
        self.link = None

    def sendToLink(self):
        if(self.link.getActor() != None):
            return 0
        self.link.setActor(self.actorInTile)
        self.link.setBlocked(True)
        self.setActor(None)
        self.setBlocked(False)
