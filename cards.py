import pygame
import random

pic1 = pygame.image.load("image/images.jpg")
pic2 = pygame.image.load("image/trap.png")
pic3 = pygame.image.load("image/empty.png")
pics = [pic1, pic2, pic3]
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
        self.pictures = pics[random.randint(0, 2)]
        self.id = id
    def coordinate(self):
        return coord[self.id]
    def card(self):
        return self.pictures





