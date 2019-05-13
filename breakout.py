# Import a library of functions called 'pygame'

import pygame, random

from math import pi


 

class Paddle:

    def __init__(self, screen_width, screen_height):

        #initialize a paddle at a given location.

        #also initialize internal variables self.screen_width and self.screen_height

        self.x = 450

        self.y = 580

        self.step = 2

        self.screen_width = screen_width

        self.width = 100

    def draw(self):

        #draws paddle at a given location
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width, 10])
       

   

    def move_left(self):

        #paddle should move left. update paddle x-position

        self.x -= self.step

        if self.x < 0:

            self.x = 0


    def move_right(self):

        #paddle should move right. update paddle x-position

        self.x += self.step

        if self.x > self.screen_width - self.width:

            self.x = self.screen_width - self.width

   

    def get_pos_x(self):

        #returns x position

        pass

        

    def get_pos_y(self):

        #returns y position

        pass

        

    def get_width(self):

        #returns paddle width

        pass

 

    def get_height(self):

        #returns paddle height

        pass

class SuperBrick:
    def __init__(self):
        self.x = 490
        self.y = 20
        self.width = 70
        self.health = 70
        self.height = 70

    def draw(self):
        pygame.draw.rect(screen, YELLOW, [self.x, self.y, self.width, self.height])
        pygame.draw.rect(screen, RED, [self.x, self.y + 80, self.health, 10])

    def check_hit_ball_vertical(self, ball):
        if ball.x > self.x and ball.x < self.x + 3 and ball.y > self.y and ball.y < self.y + self.height:
            return True

        if ball.x < self.x + self.width and ball.x > self.x + self.width - 3 and ball.y > self.y and ball.y < self.y + self.height:
            return True

          
        return False

    def check_hit_ball_horizontal(self, ball):
        if ball.y > self.y and ball.y < self.y + 3 and ball.x > self.x and ball.x < self.x + self.width:
            return True
        if ball.y > self.y + self.height and ball.y > self.y + self.height - 3 and ball.x > self.x and ball.x < self.x + self.width:
            return True
        return False
        

    def lose_life(self):
        self.health -= 34


class Brick:

    def __init__(self, x, y):

        #initializes a brick at a given location

        self.x = x

        self.y = y

        self.width = 100

        self.height = 50

       

        #Give it a Color

        self.colorPick = random.randint(0,1)

   

    def draw(self):

 

        #draws the brick at a given location
        if self.colorPick == 0:
            pygame.draw.rect(screen, GRAY, [self.x, self.y, self.width - 3, self.height])
            pygame.draw.rect(screen, BRICKISH, [self.x, self.y + (self.height/3), self.width - 3, self.height / 3])
        if self.colorPick == 1:
            pygame.draw.rect(screen, BRICKISH, [self.x, self.y, self.width - 3, self.height])
            pygame.draw.rect(screen, GRAY, [self.x, self.y + (self.height/3), self.width - 3, self.height / 3])
 

    def get_index(self):

        #returns block id

        pass

    def get_pos_x(self):

        #returns x position

        return self.x

        

    def get_pos_y(self):

        #returns y position

        return self.y

        

    def get_width(self):

        #returns brick width

        return self.width

 

    def get_height(self):

        #returns brick height

        return self.height

 

       

class Wall:

    def __init__(self):
        #initialize wall as a list of Bricks
        self.x = 0
        self.y = 150
        numcourter1 = 0
        self.id = 0
        self.bricks = []
        self.bricks_id = []
        end_WIDTH = SCREEN_WIDTH - 10
        Rows = 10 * 2
        for k in range (Rows):
            numcourter1 = numcourter1 + 1
            self.id = self.id + 1
            #make some Bricks
            self.brick = Brick(self.x, self.y)
            self.bricks.append(self.brick)
            self.bricks_id.append(self.id)
            self.bricks_id.append(self.brick)
           #make its not spawn on top of each other
            if self.x <= end_WIDTH:
               self.x = self.x + 103
            #make it make the next line
            if numcourter1 == 11:
                self.x = 51   
                self.y = self.y + 55
                numcourter1 = 0
                
    def draw(self):

        #draw wall

        for self.brick in self.bricks:

            self.brick.draw()

   

    def delete_brick(self, brick):

        #removes the brick from the wall

            self.bricks.remove(brick)

   

    def get_x(self, index):

        #returns the list of bricks that make up the wall
        self.index = index

        return self.index * 100

       

        

        

 

class Ball:

    def __init__(self, x, y, screen_width, screen_height):

        #initialize a ball at a given location

        #make sure that the ball is initialized at the same y-position as the paddle

        #and that the initial movement of the ball is toward the wall.

        #also initialize internal variables self.screen_width and self.screen_height

        # 300 435

        self.Startx = x

        self.Starty = y

        self.x = self.Startx

        self.y = 575.0

        self.width = 5

        self.screen_width = screen_width

        self.step = 1

        self.stepy = -1.0

        self.stepx = -1

        self.accel = -0.01



    def draw(self, x):

        #draws the ball at a given location
        self.x = x
        pygame.draw.circle(screen, BLUE, [self.x, int(self.y)], 10)

        self.y = self.y + self.stepy

        self.x = self.x - self.stepx   

 

    def change_horizontal_direction(self):

        #changes horizontal direction of Ball movement to an opposite

        self.stepx = -self.stepx

   

    def change_vertical_direction(self):

        #changes vertical direction of Ball movement to an opposite

        self.stepy = -self.stepy

 

    def _check_hit_brick(self, brick):

        #checks if the ball hit the brick 

        #if yes, returns True, otherwise returns False.

        #this function should be used only inside check_hit_wall(...) and nowhere else

        if brick.x < self.x and self.x < brick.x + brick.width and brick.y < self.y and self.y < brick.y + brick.height:

           #self.HitBrick = wall.brick

          

           return True

        return False

        

    def check_hit_wall(self, wall):

        #checks if the ball hit the wall.

        #if yes, returns the brick that was hit, otherwise returns None

        #if ball._check_hit_brick(wall.brick) == True:

        #    return

        for b in wall.bricks:

            if self._check_hit_brick(b) == True:

 

                return b

        return None

 

    def check_hit_paddle(self, paddle):

        #returns True of the ball hit the paddle, otherwise returns False

       
       if paddle.x < self.x and self.x < paddle.x + paddle.width and paddle.y < self.y and self.y < paddle.y + paddle.width:

           return True

       return False

 

   

    def check_hit_screen_side(self):

        #returns True of the ball hit the left or the right side of the screen, otherwise returns False

        if self.x <= 2 or self.x >= size [0]:

            return True

        return False       

 

    def check_hit_screen_top(self):

        #returns True of the ball hit the top of the screen, otherwise returns False

        if self.y <= 2:

            return True

        return False  

 

    def check_hit_screen_bottom(self):

        #returns True of the ball hit the bottom of the screen, otherwise returns False

        if self.y > size [1]:

            return True

        return False

    def respawn(self):
        self.x = paddle.x + 50
        self.y = paddle.y - 10
        self.stepx = 0
        self.stepy = 0

    def move_right(self):
        self.stepx = -1
    def move_left(self):
        self.stepx = 1


    def accel_up(self):
        self.stepy += self.accel

    def accel_down(self):
        self.stepy -= self.accel





























 
class stars:
    
    def __init__(self):
        self.x = random.randint(20, 980)
        self.y = random.randint(20, 580)


    def draw(self):
        pygame.draw.rect(screen, WHITE, [self.x, self.y, 3, 3])

star = stars()

manyStars = []

# Initialize the game engine

pygame.init()


# Define the colors we will use in RGB format
color_v = 255
col_state = True

BLACK = (  0,   0,   0)

WHITE = (255, 255, 255)

BLUE =  (  0,   0, 255)

GREEN = (  0, 255,   0)

GREENV = (0, color_v, 0)

RED =   (255,   0,   0)

REDV = (color_v, 0, 0)

YELLOW = (255, 255, 0)

YELLOWV = (color_v, color_v, 0)

GRAY = (150, 150, 150)

BRICKISH = (150, 70, 0)

DEEPSPACE = (20, 10, 35)

for i in range (100):
    star = stars()
    manyStars.append(star)


# Set the height and width of the screen

SCREEN_WIDTH = 1025

SCREEN_HEIGHT = 600

size = [SCREEN_WIDTH, SCREEN_HEIGHT]

screen = pygame.display.set_mode(size)


pygame.display.set_caption("Breakout")


#Loop until the user clicks the close button.
respawn = True
lives = 3
done = False
l_timer = 0
destroyed = False

clock = pygame.time.Clock()

#CREATE Wall, Ball AND Paddle HERE

wall = Wall()

sb = SuperBrick()

ball = Ball(450.0, 640.0, SCREEN_WIDTH, SCREEN_HEIGHT)

paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT)

 

ball_lives = 0

 

while not done:


    # This limits the while loop to a max of 10 times per second.

    # Leave this out and we will use all CPU we can.

    clock.tick(300)

   

    screen.fill(DEEPSPACE)

    for j in range (100):
        manyStars[j].draw()

    GREENV = (0, color_v, 0)
    REDV = (color_v, 0, 0)
    YELLOWV = (color_v, color_v, 0)

    keys = pygame.key.get_pressed()  #checking pressed keys

    if keys[pygame.K_LEFT]:

        paddle.move_left()

    if keys[pygame.K_RIGHT]:

        paddle.move_right()

    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close

            done=True # Flag that we are done so we exit this loop

 


    #GAME LOGIC SHOULD GO HERE

    if sb.check_hit_ball_vertical(ball) == True:
       sb.lose_life()
       ball.change_horizontal_direction()

    if sb.check_hit_ball_horizontal(ball) == True:
        sb.lose_life()
        ball.change_vertical_direction()
    
    if sb.health < 0:
        destroyed = True
        sb.x = 2000


    

    if ball.check_hit_screen_top() == True:

        ball.change_vertical_direction()

    if ball.check_hit_screen_side() == True:

        ball.change_horizontal_direction()

    if ball.check_hit_paddle(paddle) == True:

        ball.change_vertical_direction()

    b = ball.check_hit_wall(wall)
    
    if not b is None:

        wall.delete_brick(b)
        if ball.y > 151 and ball.y < 199 or ball.y > 206 and ball.y < 254:
            ball.change_horizontal_direction()
        else:
            ball.change_vertical_direction()

    if ball.check_hit_screen_bottom() == True:
        lives -= 1
        respawn = True
        
    if respawn == True:
        
        
        ball.respawn()
        if keys[pygame.K_SPACE]:
            ball.draw(paddle.x + 50)
            respawn = False
            ball.stepy = -1
            if paddle.x < 450:
                ball.stepx = -1
            if paddle.x >= 450:
                ball.stepx = 1
        if keys[pygame.K_LEFT]:
            ball.move_left()
        if keys[pygame.K_RIGHT]:
            ball.move_right()
        

    if keys[pygame.K_UP] and respawn == False and ball.x > paddle.x and ball.x < paddle.x + paddle.width:
        ball.accel_up()
    if keys[pygame.K_DOWN] and respawn == False and ball.x > paddle.x and ball.x < paddle.x + paddle.width:
        ball.accel_down()

    if wall.bricks == [] and destroyed == True:
        done = True
        print 'You WIN'

 
    if lives == 3:
        pygame.draw.rect(screen, REDV, [0, 0, 50, 15])
        pygame.draw.rect(screen, YELLOWV, [50, 0, 50, 15])
        pygame.draw.rect(screen, GREENV, [100, 0, 50, 15])
        pygame.draw.rect(screen, REDV, [975, 0, 50, 15])
        pygame.draw.rect(screen, YELLOWV, [925, 0, 50, 15])
        pygame.draw.rect(screen, GREENV, [875, 0, 50, 15])
       
    if lives == 2:
        pygame.draw.rect(screen, REDV, [0, 0, 50, 15])
        pygame.draw.rect(screen, YELLOWV, [50, 0, 50, 15])
        pygame.draw.rect(screen, REDV, [975, 0, 50, 15])
        pygame.draw.rect(screen, YELLOWV, [925, 0, 50, 15])
    
    if lives == 1:
        pygame.draw.rect(screen, REDV, [0, 0, 50, 15])
        pygame.draw.rect(screen, REDV, [975, 0, 50, 15])

    
 

   
    if respawn == True:
        if col_state == True:
            color_v -= 2
        if color_v < 2:
            color_v = 255
    else:
        color_v = 255
    
    #DRAW GAME ELEMENTS

    wall.draw()

    ball.draw(ball.x)

    paddle.draw()

    sb.draw()

 

  

    #if    

 

    # Draw a rectangle

   # pygame.draw.rect(screen, BLACK, [75, 150, 30, 10])

    # Draw a circle

   # pygame.draw.circle(screen, BLUE, [200, 250], 4)

       
    if lives == 0:
        l_timer += 2
        pygame.draw.rect(screen, REDV, [0, 0, l_timer + 50, l_timer + 15])
        pygame.draw.rect(screen, REDV, [975 + (-(l_timer)), 0, 50 + l_timer, 15 + l_timer])
        if l_timer > 650:
            screen.fill(BLACK)
            
        if l_timer > 1000:
            done = True
            print 'WASTED'

    # Go ahead and update the screen with what we've drawn.

    # This MUST happen after all the other drawing commands.

    pygame.display.flip()

 

# Be IDLE friendly

pygame.quit()