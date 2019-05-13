import pygame

from math import pi
import random

 
pygame.init()

grumpyMove = 2



WHITE = (255, 255, 255)

BLUE =  (  0,   0, 255)

BLACK = (  0,  0,  0)

RFILL = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

size = [600, 505]

screen = pygame.display.set_mode(size)

 
pygame.display.set_caption("Jamin's fish project")

 

done = False

clock = pygame.time.Clock()



class Fish():

    def __init__(self):

        self.stepx = random.randint(1, 5)

        self.stepy = random.randint(1, 5)

        self.x = random.randint(50, 550)

        self.y = random.randint(50, 455)

        self.gPos = 50

        self.two = 2

        self.activate = False
        
        self.fTime = 0

    def move(self):

        pygame.draw.circle(screen, RFILL, [self.x,self.y], 20, 10)
        pygame.draw.circle(screen, RFILL, [self.x - 16, self.y], 14)

        self.x = self.x + self.stepx

        self.y = self.y + self.stepy

        self.gPos += self.two
        if self.gPos >= 560:
            self.two = -self.two
        if self.gPos <= 40:
            self.two = -self.two


        if self.y >= 465 or self.y <= 40:

            self.stepy = -self.stepy

        if self.x >= 560 or self.x <= 40:

            self.stepx = -self.stepx

        if self.y > 230 and self.y < 270 and self.x > (self.gPos - 20) and self.x < (self.gPos + 20):
            self.stepx = 0
            self.stepy = 0
            self.x = 1000
            self.y = 1000
            self.activate = True
            
        if self.activate:
            self.fTime += 1
            if self.fTime < 50:
                pygame.draw.circle(screen, BLACK, [self.gPos, 320], 30, 5)
                pygame.draw.circle(screen, BLACK, [self.gPos - 8, 315], 5)
                pygame.draw.circle(screen, BLACK, [self.gPos + 8, 315], 5)
                pygame.draw.circle(screen, BLACK, [self.gPos, 330], 11, 5)


class grumpyFish():
    def __init__(self):

        self.stepx = grumpyMove

        self.x = 50

        self.y = 250

    def move(self):

        pygame.draw.circle(screen, BLACK, [self.x, self.y], 30, 10)

        self.x += self.stepx
        if self.x >= 560 or self.x <= 40:

            self.stepx = -self.stepx

        

oneFish = Fish()

gfish = grumpyFish()

fishes = []

for k in range(10):

    fish_variable = Fish()

    fishes.append(fish_variable)



while not done:

    clock.tick(100)
     

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 

            done=True 

 

     
    screen.fill(WHITE)

    gfish.move()
    for j in range(10):
        fishes[j].move()
    
   


    
    pygame.display.flip()

 

pygame.quit()


