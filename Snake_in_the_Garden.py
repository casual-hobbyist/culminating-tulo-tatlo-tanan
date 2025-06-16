# Name: Abby Villanueva
# Details: Culminaing project. The Alien Invasion mini-game
# Game Tutorial link: https://tinyurl.com/4zzv3y2t 

# IMPORTS
import pygame, sys, random
from pygame.math import Vector2
from Algorithm_Application import delete_last_line

#CLASSES
class MAIN:     
    """ 
    Description: 
    Contains all the logic for the code.

    Attributes:

    """
    def __init__(self): 
        # creates the usable instances we use throughout the game
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):   
        """
        User-game connection is here.

        args:
            self (instance): the instance
        returns:
            none
        """
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):    
        """
        Draws the elements.

        args:
            self (instance): the instance
        returns:
            none
        """
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):  
        """
        Checks if the snake has eaten the fruit

        args:
            self (instance): the instance
        returns:
            none
        """
        if self.fruit.pos == self.snake.body[0]:    #if the head of the snake is one the same block as the fruit
            # reposition the fruit to a random block
            self.fruit.randomise()

            # add another block to the snake (make the snake longer!)
            self.snake.add_block()

            #idiot-proofing - if the fruit randomises onthe snake's body
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomise    #re-randomise the fruit's position

    def check_fail(self):   
        """
        Adds the win / lose conditions of the game.

        args:
            self (instance): the snake
        returns:
            none
        """
        # check if snake is outside of screen
        #i made it <= to cell_num so that the player could still position the snake next to the wall
        if not 0 <= self.snake.body[0].x < CELL_NUM: #checks for left and right
            #if the head of the body is NOT between 0 and the number of cells, it is out of range (x-axis)
            self.game_over()
        if not 0 <= self.snake.body[0].y < CELL_NUM:   #checks for up and down
            self.game_over()

        # check if snake hits itself
        for block in self.snake.body[1:]:   #cycles through all of its area codes (except for the head)
            if block == self.snake.body[0]: #if the head coordinates are simialr to a body coordinate;
                self.game_over()              #game fail :(

    def game_over(self):    
        """
        The game over screen

        args:
            self (instance): the snake
        returns:
            none
        """
        self.snake.reset()

    def draw_grass(self):   
        """
        Draws grass.

        args:
            self (instance): the snake
        returns:
            none
        """
        #initiate variables
        grass_colour = (167, 209, 61)

        #process
        for row in range(CELL_NUM):
            if row % 2 == 0:
                for col in range(CELL_NUM): #horizontal acis
                    # cooridnates
                    x_axis = col * CELL_SIZE
                    y_axis = row * CELL_SIZE
                    
                    #colour it in
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(x_axis, y_axis, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_colour, grass_rect)
            else:
                for col in range(CELL_NUM): #horizontal acis
                    #coordinates
                    x_axis = col * CELL_SIZE
                    y_axis = row * CELL_SIZE

                    #colour it in
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(x_axis, y_axis, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_colour, grass_rect)

    def draw_score(self):   
        """
        Displays and draws score.

        args:
            self (instance): the snake
        returns:
            none
        """
        #initiate variables
        score_text = f'{len(self.snake.body) - 3}'
        score_surface = font.render(score_text, True, (57, 74, 12))
        score_x = int(CELL_SIZE * CELL_NUM - 60)
        score_y = int(CELL_SIZE * CELL_NUM - 40)

        #put rect in the bottom, center it there
        score_rect = score_surface.get_rect(center = (score_x, score_y))

        #put the apple icon to the left of the score_rect
        appleU_rect = appleUpdate.get_rect(midright = (score_rect.left, score_rect.centery))
        
        #create background - fit it to the values by the image/icon and score text
        bg_width = appleU_rect.width + score_rect.width + 6     #define the width
        bg_height = appleU_rect.height + 6                      #define the height
        bg_rect = pygame.Rect(appleU_rect.left, appleU_rect.top, bg_width, bg_height)

        #blits
        pygame.draw.rect(screen, (164, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(appleUpdate, appleU_rect)
        pygame.draw.rect(screen, (57, 74, 12), bg_rect, 2)

class SNAKE:    
    """
    Describes a snake. 

    Attributes:
    self
    """
    def __init__(self): 
        # instance attributes
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]    #starting position
        self.direction = Vector2(0, 0)
        self.new_block = False

        # LOAD -> SCALE Images
        #the heads
        self.initial_head_up = pygame.image.load('Image/head_up.png').convert_alpha()
        self.initial_head_down = pygame.image.load('Image/head_down.png').convert_alpha()
        self.initial_head_right = pygame.image.load('Image/head_right.png').convert_alpha()
        self.initial_head_left = pygame.image.load('Image/head_left.png').convert_alpha()

        #scale heads
        self.head_up = pygame.transform.scale(self.initial_head_up, (25, 30))
        self.head_down = pygame.transform.scale(self.initial_head_down, (25, 30))
        self.head_right = pygame.transform.scale(self.initial_head_right, (25, 20))
        self.head_left = pygame.transform.scale(self.initial_head_left, (25, 20))

        #the tails
        self.initial_tail_up = pygame.image.load('Image/tail_up.png').convert_alpha()
        self.initial_tail_down = pygame.image.load('Image/tail_down.png').convert_alpha()
        self.initial_tail_right = pygame.image.load('Image/tail_right.png').convert_alpha()
        self.initial_tail_left = pygame.image.load('Image/tail_left.png').convert_alpha()
        
        #scale tails
        self.tail_up = pygame.transform.scale(self.initial_tail_up, (25, 30))
        self.tail_down = pygame.transform.scale(self.initial_tail_down, (25, 30))
        self.tail_right = pygame.transform.scale(self.initial_tail_right, (25, 20))
        self.tail_left = pygame.transform.scale(self.initial_tail_left, (25, 20))

        #the body
        self.initial_body_vertical = pygame.image.load('Image/body_vertical.png').convert_alpha()
        self.initial_body_horizontal = pygame.image.load('Image/body_horizontal.png').convert_alpha()
        
        self.initial_body_tr = pygame.image.load('Image/body_tr.png').convert_alpha()
        self.initial_body_tl = pygame.image.load('Image/body_tl.png').convert_alpha()
        self.initial_body_br = pygame.image.load('Image/body_br.png').convert_alpha()
        self.initial_body_bl = pygame.image.load('Image/body_bl.png').convert_alpha()

        #scale body
        self.body_vertical = pygame.transform.scale(self.initial_body_vertical, (25, 30))
        self.body_horizontal = pygame.transform.scale(self.initial_body_horizontal, (25, 20))
        
        self.body_tr = pygame.transform.scale(self.initial_body_tr, (25, 20))
        self.body_tl = pygame.transform.scale(self.initial_body_tl, (25, 20))
        self.body_br = pygame.transform.scale(self.initial_body_br, (25, 20))
        self.body_bl = pygame.transform.scale(self.initial_body_bl, (25, 20))

    def draw_snake(self):   
        """ 
        Draws a snake using the graphics collected.

        Args:
            self
        Returns:
            none
        """
        #the logic of putting the correct images
        self.update_head_graphics()     #picks the best head
        self.update_tail_graphics()     #picks the best tail 

        for index, block in enumerate(self.body):   #enumerate = what object it is inside of list
            # need a rect for the positioning 
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

            # what direciton is the head/face heading 
            if index == 0:
                screen.blit(self.head, block_rect)    #put the face
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                # index is current element, finds what is next to it & the relation
                prev_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if prev_block.x == next_block.x:    #horizontal or vertical parts
                    screen.blit(self.body_vertical, block_rect)
                elif prev_block.y == next_block.y:  # left or right parts
                    screen.blit(self.body_horizontal, block_rect)

                # corner graphcs
                else:   #it is under else because of process of elimination
                    if (prev_block.x == -1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl, block_rect)   #top left

                    elif (prev_block.x == -1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, block_rect)   #bottom left

                    elif (prev_block.x == 1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, block_rect)   #top right

                    elif (prev_block.x == 1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, block_rect)   #bottom right

                    '''
                    explanation: 
                        - the () or () style is to check in the case where the cooridnates are flipped
                    Top left: x is moving right (-1), y is going up (-1)
                    Bottom Left: x is moving right (-1), y is going down (1)

                    Top right: x is moving left (1), y is moving up (-1)
                    Bottom right: x is moving left (1), y is going down (1)

                    the inverse (second '()' ) means the same thing
                    '''

    def update_head_graphics(self): 
        """ 
        Chooses the best head image out of the four.

        Args:
            self
        Returns:
            none
        """
        #body positon - head position =  the way they relate to each other (above, below, right, left)
        head_relation = self.body[1] - self.body[0] #points in one direction out of four

        #deducing the best head image
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self): 
        """ 
        Chooses the best head image out of the four.

        Args:
            self
        Returns:
            none
        """
        #2nd to last - last element =  the way they relate to each other (above, below, right, left)
        tail_relation = self.body[-2] - self.body[-1] #points in one direction out of four

        #deducing the best head image
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    def move_snake(self):   
        """
        Facilitates the movement of the snake. 
        The head is the general direction in which the whole snake moves.
        Everything is shifted to where the head goes, without the third vector2 value in self.body

        Args:
            self
        Returns:
            none
        """
        # adding a new block - activated by add_block()
        if self.new_block == True:
            body_copy = self.body[:]                            #do not change anything!
            body_copy.insert(0, body_copy[0] + self.direction)  #adds one more element to change direction. First elemnet + direction value
            self.body = body_copy[:]                            #moves the snake
            
            #reverts back to False to not extend the snake
            self.new_block = False
        else:
            # normal snake movement
            body_copy = self.body[:-1]                          #first two blocks of the snake
            body_copy.insert(0, body_copy[0] + self.direction)  #adds one more element to change direction. First elemnet + direction value
            self.body = body_copy[:]                            #moves the snake
       
    def add_block(self):    
        """
        Makes the snake longer using bool values.

        Args:
            self
        Returns:
            none
        """
        self.new_block = True

    def reset(self):        
        """
        resets the snake's position

        args:
            self (instance)
        returns:
            none
        """
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]    #starting position
        self.direction = Vector2(0, 0)

class FRUIT:    
    """
    Description:
    Describes a fruit.

    Attributes:
    self    
    """
    def __init__ (self):
        self.randomise()

    def draw_fruit(self):
        """
        Creates then draws a rectangle.

        args:
            self
        returns
            none
        """
        #initiate variables
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)

        #process
        fruit_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        screen.blit(appleUpdate, fruit_rect)

    def randomise(self):
        """
        Generates random numbers
        
        Args:
            self: the instance
        returns:
            none
        """
        #creates random positon
        self.x = random.randint(0, CELL_NUM -1) 
        self.y = random.randint(0, CELL_NUM - 1)

        # puts the element on the random position
        self.pos = pygame.math.Vector2(self.x, self.y)

#BEGIN PYGAME  
pygame.init         #begins pygame
pygame.font.init()  #initialise font

#deletes the uncecessary lines after game has closed
delete_last_line()
delete_last_line()

#INITIATE VARIABLES
CELL_SIZE = 25  #each block is y units big
CELL_NUM = 20   #there will be x blocks wide

#display the screen and set the game's time
screen = pygame.display.set_mode((CELL_NUM * CELL_SIZE, CELL_NUM * CELL_SIZE))
clock =  pygame.time.Clock()
font = pygame.font.Font('fonts/Gogh-ExtraBoldItalic.ttf', 15) #font, fontsize
    #font link: https://www.dafont.com/type-forward-foundry.d10031 

# the main instance used throughout the event loop
main_game = MAIN()

# user-machine relationship
screen_UPDATE = pygame.USEREVENT
pygame.time.set_timer(screen_UPDATE, 125)   #EVENT IS TRIGGERED EVERY 150 MILISECONDS

#creates the apple element of the game
apple = pygame.image.load('Image/apple.webp').convert_alpha() #folder/image name
appleUpdate = pygame.transform.scale(apple, (30, 20))
#link: https://www.codespeedy.com/scale-image-to-fit-screen-in-pygame-python/ 

#FUNCTIONs
def main(): 
    # event loop
    game_status = True
    while game_status: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = False
                pygame.quit()
                sys.exit()

            if event.type == screen_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:        #moves up
                    if main_game.snake.direction.y != 1:        #prevents reversing directions
                        main_game.snake.direction = Vector2(0, -1)   

                if event.key == pygame.K_DOWN:      #moves down
                    if main_game.snake.direction.y != -1:        #prevents reversing directions
                        main_game.snake.direction = Vector2(0, 1)    
                
                if event.key == pygame.K_RIGHT:     #moves right
                    if main_game.snake.direction.x != -1:        #prevents reversing directions
                        main_game.snake.direction = Vector2(1, 0)
                
                if event.key == pygame.K_LEFT:      #moves left
                    if main_game.snake.direction.x != 1:        #prevents reversing directions
                        main_game.snake.direction = Vector2(-1, 0)    

        screen.fill((175, 215, 70))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)

#ICONIQUE if-statement
if __name__ == '__main__':
    main()