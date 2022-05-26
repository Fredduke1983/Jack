import pygame
import random

pic_castle = pygame.image.load("image/images.jpg")
pic_trap = pygame.image.load("image/trap.png")
pic_empty = pygame.image.load("image/empty.png")
pics = [pic_empty, pic_castle, pic_trap]
coord = {}


x0 = 100
y0 = 100
for i in range (1,10):
    coord[i] = [x0, y0]
    x0 += 100
for i in range (10,12):
    coord[i] = [x0, y0]
    y0 += 100
for i in range (12,22):
    coord[i] = [x0, y0]
    x0 -= 100
for i in range (22,24):
    coord[i] = [x0, y0]
    y0 += 100
for i in range (24,35):
    coord[i] = [x0, y0]
    x0 += 100

class Cards:

    def __init__(self, id):
        self.state = True
        self.pictures = pics[random.randint(0, 2)]
        self.id = id

    def coordinate(self):
        return coord[self.id]

    def stat(self):
        self.state = False

    def card(self):
        if self.state == True:
            print(self.state)
            return pics[0]
        else:
            print(self.state)
            return self.pictures





