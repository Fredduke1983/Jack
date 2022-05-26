import random
import sys
import pygame
from players import Players
from cards import Cards

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    pic = pygame.image.load("image/images.jpg")
    pic2 = pic3 = pic4 = pygame.image.load("image/trap.png")
    pic5 = pic6 = pic7= pic8 = pygame.image.load("image/empty.png")
    cubic1 = pygame.image.load("image/cubic_1.jpg")
    cubic2 = pygame.image.load("image/cubic_2.jpg")
    cubic3 = pygame.image.load("image/cubic_3.jpg")
    cubic4 = pygame.image.load("image/cubic_4.jpg")
    cubic5 = pygame.image.load("image/cubic_5.jpg")
    cubic6 = pygame.image.load("image/cubic_6.jpg")
    cubic = [cubic1,cubic2,cubic3,cubic4,cubic5,cubic6]


    pl1 = pygame.image.load("image/lovepik.png")
    player1 = Players(pl1, "Fred", 1)

    print("Player #",player1.id())
    print("Position Player X ->", player1.positionX())
    print("Position Player Y ->", player1.positionY())
    field = [pic, pic2, pic3, pic4, pic5, pic6, pic7, pic8]

    pos1 = 10
    click = 1
    random_cubic = 0

    FPS = 10
    mouse_click_count = 0
    clock = pygame.time.Clock()

    card = Cards(16)
    print(card.coordinate())
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
                    but_x, but_y = pygame.mouse.get_pos()

                    if but_x > 50 and but_x < 150 and but_y > 450 and but_y < 550:
                        random_cubic = random.randint(0, 5)
                        print(but_x, but_y, "   ", random_cubic+1)

                        # pos1 += (random_cubic+1)*100
                        if pl_x > 600:

                            pl_x, pl_y = player1.move(0, random_cubic+1)
                            print("plx2 = ", pl_x)
                            print("ply2 = ", pl_y)
                        else:

                            pl_x, pl_y = player1.move(random_cubic+1, 0)
                            print("plx1 = ", pl_x)
                            print("ply1 = ", pl_y)
                    click = 1

        if click == 1:
            click = 0
            col = 1
            for i in field:

                if col < 6:
                    screen.blit(i, (x, y))
                    pygame.draw.rect(screen, (50, 50, 250), (x, y, 100, 100), 2)
                    x += 100
                    col += 1
                else:
                    screen.blit(i, (x, y))
                    pygame.draw.rect(screen, (50, 50, 250), (x, y, 100, 100), 2)
                    y += 100

            screen.blit(cubic[random_cubic], (50, 450))
            if pl_x > 600:
                pl_x = pl_x - (random_cubic+1)*100
                for coun in range(0, (random_cubic+1)*100):
                    # print(coun)
                    pl_x += 2
                    if pl_x > 629:
                        print(' Player position X --',player1.positionX(), ' pl_x = ',pl_x)
                        pl_x, pl_y = player1.move(-1, int((player1.positionX()-pl_x)/100))
                        print(' Player position X --', player1.positionX(), ' pl_x = ', pl_x)
                        print(' pl_y ----', pl_y)
                        break
            print(' pl_y --', pl_y, ' pl_x = ', pl_x)
            screen.blit(pl1, (pl_x-60, pl_y))

            x = 50
            y = 50

        mouse_click_count = 0
        pygame.display.update()
run()