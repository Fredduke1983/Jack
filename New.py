import random
import sys
import pygame
from players import Players
from cards import Cards

def run():
    pygame.init()
    screen = pygame.display.set_mode((1300,720), pygame.RESIZABLE)

    cubic1 = pygame.image.load("image/cubic_1.jpg")
    cubic2 = pygame.image.load("image/cubic_2.jpg")
    cubic3 = pygame.image.load("image/cubic_3.jpg")
    cubic4 = pygame.image.load("image/cubic_4.jpg")
    cubic5 = pygame.image.load("image/cubic_5.jpg")
    cubic6 = pygame.image.load("image/cubic_6.jpg")
    exit = pygame.image.load("image/exit.png")
    cubic = [cubic1,cubic2,cubic3,cubic4,cubic5,cubic6]


    pl1 = pygame.image.load("image/lovepik.png")
    pl2 = pygame.image.load("image/lovepik2.png")
    pl3 = pygame.image.load("image/lovepik3.png")


    player1 = Players(pl1, "Fred", 1, 0, 100)
    player2 = Players(pl2, "Anna", 2, 5, 100)
    player3 = Players(pl3, "Mido", 3, 10, 100)
    step = 0
    start = True

    pl1_x, pl1_y = player1.getPositionXY()
    pl2_x, pl2_y = player2.getPositionXY()
    pl3_x, pl3_y = player3.getPositionXY()

    fontik = pygame.font.SysFont('arial', 15)
    name_player1 = fontik.render("Зараз ходить " + str(player1.getName()), True, (110, 110, 10))
    name_player2 = fontik.render("Зараз ходить " + str(player2.getName()), True, (110, 110, 10))
    name_player3 = fontik.render("Зараз ходить " + str(player3.getName()), True, (110, 110, 10))
    switch_cubic = fontik.render("Натисни на кубик для ходу ->", True, (110, 110, 8))
    name_player1_1 = fontik.render(str(player1.getName()), True, (110, 110, 7))
    name_player2_2 = fontik.render(str(player2.getName()), True, (110, 110, 7))
    name_player3_3 = fontik.render(str(player3.getName()), True, (110, 110, 7))

    new_cards = []
    for n in range (35):
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
                    click_button_x, click_button_y = pygame.mouse.get_pos()

                    if click_button_x > 1100 and click_button_x < 1200 and click_button_y > 20 and click_button_y < 100:
                        sys.exit()
                    if click_button_x > 850 and click_button_x < 900 and click_button_y > 20 and click_button_y < 70:
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

            screen.blit(cubic[random_cubic], (850, 20))
            screen.blit(switch_cubic, (680, 35))

            if start:
                screen.blit(name_player1, (50, 10))
                start = False

            if step == 1:
                index_card_pl1 += random_cubic + 1
                new_x, new_y = new_cards[index_card_pl1].coordinate()
                pl1_x, pl1_y = player1.setPositionXY(new_x, new_y)
                screen.blit(name_player2, (50, 10))

            if step == 2:
                index_card_pl2 += random_cubic + 1
                new_x, new_y = new_cards[index_card_pl2].coordinate()
                pl2_x, pl2_y = player2.setPositionXY(new_x, new_y)
                screen.blit(name_player3, (50, 10))

            if step == 3:
                index_card_pl3 += random_cubic + 1
                new_x, new_y = new_cards[index_card_pl3].coordinate()
                pl3_x, pl3_y = player3.setPositionXY(new_x, new_y)
                screen.blit(name_player1, (50, 10))

            screen.blit(exit, (1100, 20))
            screen.blit(name_player1_1, (pl1_x + 30, pl1_y - 17))
            screen.blit(name_player2_2, (pl2_x + 30, pl2_y - 30))
            screen.blit(name_player3_3, (pl3_x + 40, pl3_y - 41))
            screen.blit(pl1, (pl1_x, pl1_y))
            screen.blit(pl2, (pl2_x + 6, pl2_y))
            screen.blit(pl3, (pl3_x + 12, pl3_y))

        if step == 3:
            step = 0
        mouse_click_count = 0
        pygame.display.update()
run()