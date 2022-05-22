import random
import sys
import pygame
from players import Players
from cards import Cards

def run():
    pygame.init()
    screen = pygame.display.set_mode((900,600))

    cubic1 = pygame.image.load("image/cubic_1.jpg")
    cubic2 = pygame.image.load("image/cubic_2.jpg")
    cubic3 = pygame.image.load("image/cubic_3.jpg")
    cubic4 = pygame.image.load("image/cubic_4.jpg")
    cubic5 = pygame.image.load("image/cubic_5.jpg")
    cubic6 = pygame.image.load("image/cubic_6.jpg")
    cubic = [cubic1,cubic2,cubic3,cubic4,cubic5,cubic6]


    pl1 = pygame.image.load("image/lovepik.png")


    player1 = Players(pl1, "Fred", 1, 30, 50)
    player2 = Players(pl1, "Anna", 2, 35, 50)
    player3 = Players(pl1, "Mido", 3, 40, 50)


    new_cards = []
    for n in range (18):
        card = Cards(n)
        new_cards.append(card)

    index_card = 0
    pos1 = 10
    click = 1
    mouse_click_count = 0
    random_cubic = 0

    FPS = 10

    clock = pygame.time.Clock()
    x, y = 50, 50
    pl_x, pl_y = 30, 50
    start = True
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mouse_click_count == 0:
                    screen.fill((0, 0, 0))
                    isPlayer1 = True
                    mouse_click_count += 1
                    random_cubic = random.randint(0, 5)
                    click = 1

        if click == 1:
            click = 0
            col = 1

            for i in range(1, len(new_cards)):
                x, y = new_cards[i].coordinate()
                pic = new_cards[i].card()
                screen.blit(pic,(x, y))
                pygame.draw.rect(screen, (50, 200, 150), (x, y, 100, 100), 2)

            screen.blit(cubic[random_cubic], (50, 450))

            index_card += random_cubic + 1
            new_x, new_y = new_cards[index_card].coordinate()
            pl_x, pl_y = player1.positionXY(new_x, new_y)
            screen.blit(pl1, (pl_x, pl_y))

            x = 50
            y = 50

        mouse_click_count = 0
        pygame.display.update()
run()