# Name: Abby Villanueva
# Details: Culminaing project. The main game

#IMPORT
from time import sleep
from Alien_Invasion import main as alien_main
from Algorithm_Application import main as algo_main

#FUNCTIONS
def int_check(highest = int, lowest = int): #NOTE: already tested for in test_Algorithm_Application 
    """
    Checks if an int input is valid.

    args:
        highest (int): inclusive, the highet value the user can input
        lowest (int): inclusive, the lowest value the user can input
    returns:
        user_choice (int): the number which the user chose
    """
    while True:
        try:
            user_choice = int(input('\nEnter your choice: '))

            if user_choice <= highest and user_choice >= lowest:
                break
        except:
            print('Invalid input. Try again.')
        
    #output
    return user_choice

def txt_use(file_name, n): #uses readlines 
    """
    Facilitates the usage of .txt files

    args:
        file_name (str): the name of the file being used
        n (int / ratio): the specific lines to be printed
    returns:
        mylist[n] (str): the line/s of specific code
    """
    # process
    infile = open(f'{file_name}', 'r', encoding = 'utf-8')

    # removes the '\n' from the ends of all the lines 
    with infile as f:
        mylist = f.read().splitlines() 

    infile.close()   #close the file!

    # output
    return mylist[n]

def main():        #the main game loop 
    """
    Allows the player to choose if what game they want to play. Allows user to read game instructions. 

    Args:
        none
    Returns:
        none
    """
    #initiate variables
    status = True

    # processs
    for i in range(3):      #prints intro 
        #change the indentation
        if i == 0:
            n = 30
        elif i == 2:
            n = 50
        else:
            n = 0

        print(' ' * n, txt_use('game_text.txt', i))

    #game loop
    while status:
        print('\n', txt_use('game_text.txt', 3))    #prints 'Mini-games'

        for j in range(4, 7):   #prints game choices    
            n = 10      #set indentation

            print(txt_use('game_text.txt', j), end = ' ' * n)

        game_choice = int_check(3, 1) #choose a game

        if game_choice == 1:    #alien invasion 
            # print text
            print('\n' + txt_use('game_text.txt', 11))
            for g in range(7, 9):
                print(txt_use('game_text.txt', g))

            sleep(1)    #delay!

            #the game!
            alien_main()

        if game_choice == 2:    #snake in the garden 
            # import it here
            from Snake_in_the_Garden import main as snake_main

            #initiate variables
            snake_status = True

            # print text
            print('\n' + txt_use('game_text.txt', 11))
            print(txt_use('game_text.txt', 9))

            #the game
            while snake_status:
                try:
                    snake_main()
                except:
                    snake_status = False
            
        if game_choice == 3:    #algorithm integration 
            # print text
            print('\n')
            for d in range(11, 9, -1):
                print(txt_use('game_text.txt', d))
            
            #the game!
            algo_main()

        print('\n') #add space
        for w in range(18, 20): #asks user if they want to continue 
            print(txt_use('game_text.txt', w))    
        
        cont_choice = int_check(3, 1)   #choose a game  
        if cont_choice == 2:            #ends the game loop 
            print('\n' + txt_use('game_text.txt', 20))
            status = False

#ICONIQUE if-statement
if __name__ == '__main__':
    main()