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
    pl2 = pygame.image.load("image/lovepik2.png")
    pl3 = pygame.image.load("image/lovepik3.png")


    player1 = Players(pl1, "Fred", 1, 30, 50)
    player2 = Players(pl2, "Anna", 2, 35, 50)
    player3 = Players(pl3, "Mido", 3, 40, 50)
    fontik = pygame.font.SysFont('arial', 32)
    name_player1 = fontik.render(str(player1.getName()), True, (110, 110, 10))
    name_player2 = fontik.render(str(player2.getName()), True, (110, 110, 10))
    name_player3 = fontik.render(str(player3.getName()), True, (110, 110, 10))


    step = 1
    pl1_x, pl1_y = player1.getPositionXY()
    pl2_x, pl2_y = player2.getPositionXY()
    pl3_x, pl3_y = player3.getPositionXY()


    new_cards = []
    for n in range (18):
        card = Cards(n)
        new_cards.append(card)

    index_card_pl1 = index_card_pl2 = index_card_pl3 = 0
    mouse_click_count = 1
    random_cubic = 0

    FPS = 10
    clock = pygame.time.Clock()

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

                    mouse_click_count += 1
                    step += 1
                    random_cubic = random.randint(0, 5)

        if mouse_click_count == 1:
            mouse_click_count = 0

            for i in range(1, len(new_cards)):
                x, y = new_cards[i].coordinate()
                pic = new_cards[i].card()
                screen.blit(pic,(x, y))
                pygame.draw.rect(screen, (50, 200, 150), (x, y, 100, 100), 2)

            screen.blit(cubic[random_cubic], (50, 450))

            if step == 1:
                name_player = name_player1
                index_card_pl1 += random_cubic + 1
                new_x, new_y = new_cards[index_card_pl1].coordinate()
                pl1_x, pl1_y = player1.setPositionXY(new_x, new_y)

                print("index_card_pl1 : ", index_card_pl1, " pl_x, pl_y : ", pl1_x, pl1_y, "step = ", step)

            if step == 2:
                name_player = name_player2
                index_card_pl2 += random_cubic + 1
                new_x, new_y = new_cards[index_card_pl2].coordinate()
                pl2_x, pl2_y = player2.setPositionXY(new_x, new_y)

                print("index_card_pl2 : ", index_card_pl2, " pl_x, pl_y : ", pl2_x, pl2_y, "step = ", step)


            if step == 3:
                name_player = name_player3
                index_card_pl3 += random_cubic + 1
                new_x, new_y = new_cards[index_card_pl3].coordinate()
                pl3_x, pl3_y = player3.setPositionXY(new_x, new_y)

                print("index_card_pl3 : ", index_card_pl3, " pl_x, pl_y : ", pl3_x, pl3_y, "step = ", step)
            screen.blit(pl1, (pl1_x, pl1_y))
            screen.blit(pl2, (pl2_x + 5, pl2_y))
            screen.blit(pl3, (pl3_x + 10, pl3_y))

            screen.blit(name_player, (20, 10))

        if step == 3:
            step = 0
        mouse_click_count = 0
        pygame.display.update()
run()