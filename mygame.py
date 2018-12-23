import pygame
import time
from pygame.locals import *
import pygame,sys


###define colors
white=(255,255,255)
lightblue= (204,249,245)
green=(181,230,28)
red=(126,10,16)
black=(0,0,0)
lightblue2=(0,223,255)

###make screen
pygame.init()
screen = pygame.display.set_mode((900,580))
pygame.display.set_caption("********welcom********")

#set start window

screen.fill(lightblue2)
pygame.mixer.music.load('music.mp3')
first=pygame.image.load('first.png')
definegameway=pygame.image.load('definegameway.png')
pygame.mixer.music.play()
screen.blit(first, (195, 120))
pygame.display.flip()


##load image

main = pygame.image.load('main.jpg')
guide= pygame.image.load('guide.png')
guidechart=pygame.image.load('guidechart.png')
exit= pygame.image.load('exit.png')
win= pygame.image.load('won.jpg')


######main loop of game
firstloop=True
while firstloop:
  for evento in pygame.event.get():


    #checking the events
    if evento.type == QUIT:
        pygame.quit()
        sys.exit()
        firstloop= False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        (x, y) = pygame.mouse.get_pos()


        if   275<x<595 and 240<y<295:####how to play

            screen.blit(definegameway, (220, 300))
            pygame.display.flip()
            break
        if 275<x<595 and 173<y<221: ###starting main page of game
            firstloop = False
            #set pictures and screen

            screen.fill(white)
            screen.blit(guidechart, (690, 0))
            screen.blit(guide, (620, 81))
            screen.blit(exit, (150, 380))
            screen.blit(main, (0, 40))

            pygame.display.flip()


            click1 = 0
            click2 = 0
            click3 = 0
            click4 = 0
            click5 = 0
            score = 0



            gameloop = True
            while gameloop:
                for evento in pygame.event.get():

                    pygame.display.set_caption("str(score)")

                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        print(x)
                        print(y)


                        if 365 < x < 410 and 335< y < 365 and click1 == 0:  #1

                            score = score + 1
                            click1 = 1
                            pygame.draw.line(screen,green,(x-7,y-8),(x,y),3)
                            pygame.draw.line(screen, green, (x , y), (x + 7, y - 25),5)
                            pygame.draw.line(screen, red, (820, 295), (829, 301), 3)
                            pygame.draw.line(screen, red, (829,301), (840, 280), 5)
                            pygame.display.flip()

                        if  399< x < 411 and 130 < y < 140 and click2 == 0:  #2

                            score = score + 1
                            click2 = 1
                            pygame.draw.line(screen, green, (x -5, y - 5), (x, y), 3)
                            pygame.draw.line(screen, green, (x, y), (x + 5, y - 15), 5)
                            pygame.draw.line(screen, red, (683, 125), (688, 136), 3)
                            pygame.draw.line(screen, red, (688, 136), (700, 115), 5)
                            pygame.display.flip()
                        if 549 < x < 618 and 260 < y <290 and click3== 0:  #3

                            score = score + 1
                            click3 =1
                            pygame.draw.line(screen, green, (x - 7, y - 8), (x, y), 3)
                            pygame.draw.line(screen, green, (x, y), (x + 7, y - 25), 5)
                            pygame.draw.line(screen, red, (670, 225), (680, 232), 3)
                            pygame.draw.line(screen, red, (680, 232), (690, 210), 5)
                            pygame.display.flip()

                        if 534 < x < 554 and 308< y < 360 and click4 == 0:  #4

                            score = score + 1
                            click4= 1
                            pygame.draw.line(screen, green, (x - 7, y - 8), (x, y), 3)
                            pygame.draw.line(screen, green, (x, y), (x + 7, y - 25), 5)
                            pygame.draw.line(screen,red, (820,160 ), (827, 168), 3)
                            pygame.draw.line(screen, red, (827, 168), (840, 140), 5)

                            pygame.display.flip()
                        if 475< x < 517 and 51 < y < 99 and click5 == 0:  #5

                            score = score + 1
                            click5 =1
                            pygame.draw.line(screen, green, (x - 7, y - 8), (x, y), 3)
                            pygame.draw.line(screen, green, (x, y), (x + 7, y - 25), 5)
                            pygame.draw.line(screen, red, (690, 325), (697, 337), 3)
                            pygame.draw.line(screen, red, (697, 337), (707, 310), 5)
                            pygame.display.flip()


                        if 150<x<735 and 370<y<560:###exit button
                             pygame.quit()
                             gameloop= False

                        if score==5:

                            time.sleep(1)
                            screen.fill(lightblue)
                            screen.blit(win,(350,180))
                            pygame.mixer.music.load('winer.mp3')
                            pygame.mixer.music.play()
                            pygame.display.flip()


                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        gameloop = False










