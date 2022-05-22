import pygame

coord = {}

x0 = 50
y0 = 50
for i in range (1,8):
    coord[i] = [x0, y0]
    x0 += 100
for i in range (8,12):
    coord[i] = [x0, y0]
    y0 += 100
for i in range (12,20):
    coord[i] = [x0, y0]
    x0 -= 100

class Cards:
    trap = pygame.image.load("image/trap.png")
    pic = pygame.image.load("image/images.jpg")
    ce = pygame.image.load("image/empty.png")
    def __init__(self, id):
        self.id = id
    def coordinate(self):
        return coord[self.id]




