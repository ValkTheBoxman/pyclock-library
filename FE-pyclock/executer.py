import pygame
from pygame import event
from FEpyclock import pyclock

pygame.init()

screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("pyclock function executer")

print("eventOnTime() and eventOnDate() unavaiable at the moment.")
pyclock.vp(self=0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #if keystroke is pressed check whether its right or left   
        if event.type == pygame.KEYDOWN:
            #pyclock.function class
            if event.key == pygame.K_1:
                print("printTime() executed")
                pyclock.printTime()
            if event.key == pygame.K_2:
                print("showDigitalClock() executed")
                print("close the digital clock window in order to gain control of FE again")
                pyclock.showDigitalClock()
            if event.key == pygame.K_3:
                print("printTimezone() executed")
                pyclock.printTimezone()

            #pyclock.count.function class
            if event.key == pygame.K_4:
                print("count.countUp() executed, counting to 10")
                pyclock.count.countUp(10)
            if event.key == pygame.K_5:
                print("countDown1Num() executed counting down from num 10 and ending at 5")
                pyclock.count.countDown1Num(10,5)
            if event.key == pygame.K_6:
                print("countDown() executed starting from num 10")
                pyclock.count.countDown(10)    
               

            if event.key == pygame.K_ESCAPE:
                running = False


    pygame.display.update()