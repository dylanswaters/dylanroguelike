class Tile:
    blocked = True
    actorInTile = None
    token = ""
    #a tile of the map and its properties
    def __init__(self):
        self.blocked = False
        self.actorInTile = None
        self.token = "-"

    def getActor(self):
        return self.actorInTile

    def setActor(self,newActor):
        self.actorInTile = newActor

    def getBlocked(self):
        return self.blocked

    def setBlocked(self,blocked):
        self.blocked = blocked

    def setToken(self,newToken):
        self.token = newToken

    def getToken(self):
        return self.token

    def __str__(self):
        return self.token
