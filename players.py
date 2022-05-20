import random
class Players():
    pp_x = 0
    def __init__(self, pic_pl, name, player_id):
        self.pic_pl = pic_pl
        self.name = name
        self.player_id = player_id
        self.pp_x = 30
        self.pp_y = 50
        print("PLAY")

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