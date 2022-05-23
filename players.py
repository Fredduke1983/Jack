import random
class Players():

    def __init__(self, pic_pl, name, player_id, posX, posY):
        self.pic_pl = pic_pl
        self.name = name
        self.player_id = player_id
        self.posX = posX
        self.posY = posY
        print("Player -->", self.id())

    def getPositionXY(self):
        return (self.posX, self.posY)

    def setPositionXY(self, posX, posY ):
        self.posX = posX
        self.posY = posY
        return (self.posX, self.posY)

    def id(self):
        return self.player_id
