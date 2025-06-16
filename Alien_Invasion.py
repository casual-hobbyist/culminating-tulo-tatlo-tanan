# Name: Abby Villanueva
# Details: Culminaing project. The Alien Invasion mini-game
# Game Tutorial link: http://tiny.cc/gzym001 (inspired from that one 1970s space invaders game)
# Countdown Tutorial link: https://stackoverflow.com/questions/72610393/how-do-i-make-a-python-turtle-program-wait-a-bit/72624152#72624152 

# IMPORTS
import random
import time
import turtle
from turtle import Screen, Turtle
from time import sleep

# INDEPENDENT CONSTANTS
FONT = ("Courier", 30, "bold")
CANNON_STEP = 20    #cannon movement
LASER_LENGTH = 20
LASER_SPEED = 10
LASER_SPEED = 10
ALIEN_SPAWN_INTERVAL = 1.5 
ALIEN_SPEED = 1

def game_play(): 
    """
    Holds all the data, functions and necessities that come with the game.

    args:
        none
    returns:
        none
    """
    # setting up screen and bg
    window = turtle.Screen()
    window.tracer(0)
    window.setup(0.5, 0.75)    #width, height
    window.bgcolor(0.2, 0.2, 0.2)
    window.title("The Alien Invasion!\t|\tMini-Game")

    # DEPENDENT CONSTANTS
    LEFT = -window.window_width() / 2
    RIGHT = window.window_width() / 2
    TOP = window.window_height() / 2
    BOTTOM = -window.window_height() / 2
    FLOOR_LEVEL = 0.9 * BOTTOM
    GUTTER = 0.025 * window.window_width()

    # Create laser cannon
    cannon = turtle.Turtle()
    cannon.penup()
    cannon.color(1, 1, 1)
    cannon.shape("square")
    cannon.setposition(0, FLOOR_LEVEL)

    # Create turtle for writing text
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.setposition(LEFT * 0.8, TOP * 0.8)
    text.color(1, 1, 1)

    # INITIATE LISTS
    lasers = []
    aliens = []

    # FUNCTIONS
    def draw_cannon():  
        """
        Laswer canon styling - change size and keep the shape on-screen.
        Facilitates the drawing of cannons

        args:
            none
        returns:
            none
        """
        #process
        cannon.clear()
        cannon.turtlesize(1, 4)  #body
        cannon.stamp()

        cannon.sety(FLOOR_LEVEL + 10)
        cannon.turtlesize(1, 1.5)  #peakhole
        cannon.stamp()

        cannon.sety(FLOOR_LEVEL + 20)
        cannon.turtlesize(0.8, 0.3)  #nozzle of cannon
        cannon.stamp()

        cannon.sety(FLOOR_LEVEL)    #sets position to bottom of screen

    def move_left():    
        """ 
        Moves the cannon left!

        args:
            none
        returns:
            none
        """
        new_x = cannon.xcor() - CANNON_STEP

        if new_x >= LEFT + GUTTER:  #checks for boundaries
            cannon.setx(new_x)
            draw_cannon()

    def move_right():   
        """ 
        Moves the cannon left!

        args:
            none
        returns:
            none
        """
        new_x = cannon.xcor() + CANNON_STEP
        if new_x <= RIGHT - GUTTER:
            cannon.setx(new_x)
            draw_cannon()

    def create_laser(): 
        """
        Facilitates the usage of the laser component of the game.
        
        args:
            none
        returns:
            none
        """
        laser = turtle.Turtle() #create instance

        laser.penup()
        laser.color(1, 0, 0)
        laser.hideturtle()

        laser.setposition(cannon.xcor(), cannon.ycor())
        laser.setheading(90)

        # Move laser to just above cannon tip
        laser.forward(20)
        
        # Prepare to draw the laser
        laser.pendown()
        laser.pensize(5)

        lasers.append(laser)    #add this instance to the list keeping track

    def move_laser(laser):  
        """
        Controls and manages the movement of the lasers. 

        args:
            laser (turtle): the turtle instance that is controlled
        returns:
            none
        """
        laser.clear()
        laser.forward(LASER_SPEED)  #set position based on the 'speed'

        # Draw the laser
        laser.forward(LASER_LENGTH)
        laser.forward(-LASER_LENGTH)

    def create_alien(): 
        """
        Makes the aliens that attack the player's homebase

        args:
            none
        returns:
            none
        """
        alien = turtle.Turtle() #create instance

        alien.penup()
        alien.turtlesize(2)   #make alien size

        # sets position to the top (y-axis)
        alien.setposition(
            random.randint(
                int(LEFT + GUTTER),
                int(RIGHT - GUTTER),
            ),
            TOP,
        )
        alien.shape("turtle")
        alien.setheading(-90)
        alien.color(random.random(), random.random(), random.random())  #sets position randomly (x-axis)

        aliens.append(alien)    #add this instance to the list keeping track

    def remove_sprite(sprite, sprite_list): 
        """
        Facilitates the removal of assets in the game.

        args:
            sprite (turtle): the instance being removed
            sprite_list (list): the list in which it is kept track in
        returns:
            none
        """
        # process
        sprite.clear()
        sprite.hideturtle()
        window.update()
        
        #remove from the list keeping track
        sprite_list.remove(sprite)
        turtle.turtles().remove(sprite) 

    # Keyboard-game connection
    window.onkeypress(move_left, "Left")
    window.onkeypress(move_right, "Right")
    window.onkeypress(create_laser, "space")
    window.onkeypress(turtle.bye, "q")  #press q to quit (other than x button)
    window.listen()

    # draw the cannons
    draw_cannon()

    # THE GAME LOOP
    #initiate variables        
    alien_timer = 0
    game_timer = time.time()
    score = 0
    game_running = True

    #main loop
    while game_running: 
        #Scoring and time-keeping
        time_elapsed = time.time() - game_timer
        text.clear()
        text.write(
        f"Time: {time_elapsed:5.1f}s\nScore: {score:5}",
        font=("Courier", 20, "bold"),
        )

        # Move all lasers
        for laser in lasers.copy():
            move_laser(laser)

            # Remove laser if it goes off screen
            if laser.ycor() > TOP:
                # clears it from the lasers list to keep game functioning
                remove_sprite(laser, lasers)
                break   #no need to keep checking so stop the loop

            # Check for collision with aliens
            for alien in aliens.copy():
                # checks if the lasere has hit the alien and removes the sprite if it has
                if laser.distance(alien) < 20:
                    remove_sprite(laser, lasers)
                    remove_sprite(alien, aliens)

                    score += 1
                    break

        # Spawn new aliens according to time!
        if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
            create_alien()
            alien_timer = time.time()

        # Move all aliens
        for alien in aliens:
            alien.forward(ALIEN_SPEED)

            # Check for game over
            if alien.ycor() < FLOOR_LEVEL:
                game_running = False
                break

        window.update() #keep up with player interactions

    # game over text
    splash_text = turtle.Turtle()
    splash_text.hideturtle()
    splash_text.color(1, 1, 1)
    splash_text.write("GAME OVER", font = FONT, align = "center")

    #keep window open
    turtle.done()

def countdown(pen, screen, seconds = 3): 
    """
    Facilitates the countdown of the game! 
    In addition to that, calls on the game_play() function.

    args:
        seconds (int): automatically set to 3, the seconds of countdown
    returns:
        none
    """
    #process
    pen.clear() #instance

    if seconds < 1:
        pen.write('Game Start!', align='center', font = FONT)
        sleep(1)
        pen.clear()
        turtle.ontimer(game_play, 1000)
    else:
        pen.write(seconds, align='center', font=FONT)
        screen.ontimer(lambda: countdown(pen, screen, seconds - 1), 1000)   # TW!!!: RECURSION

    #outta here
    turtle.done()
    
def main(): 
    """
    Contains all the needed components to run Alien Invasion.

    args:
        none
    returns:
        none
    """
    #create arg 1
    text = turtle.Turtle()
    text.hideturtle()
    text.color(1, 1, 1)

    #create arg 2
    background = turtle.Screen()
    background.tracer(0)
    background.setup(0.5, 0.75)    #width, height
    background.bgcolor(0.2, 0.2, 0.2)
    background.title("The Alien Invasion!\t|\tMini-Game")

    countdown(text, background, 3)

# #ICONIQUE if-statement
if __name__ == '__main__':  
    main()