import random
class Players():

    def __init__(self, pic_pl, name, player_id, pp_x, pp_y):
        self.pic_pl = pic_pl
        self.name = name
        self.player_id = player_id
        self.pp_x = pp_x
        self.pp_y = pp_y
        print("Player -->", self.id())

    def positionXY(self, posX = 30, posY = 50):
        self.posX = posX
        self.posY = posY
        return (self.posX, self.posY)

    def positionX(self, posX = 30):
        self.posX = self.pp_x
        return self.posX

    def positionY(self, posY = 50):
        self.posY = self.pp_y
        return self.posY

    def id(self):
        return self.player_id

    def move(self, rand_x, rand_y):

        self.pp_x += rand_x * 100
        self.pp_y += rand_y * 100
        return self.pp_x, self.pp_y