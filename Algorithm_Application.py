# Name: Abby Villanueva
# Details: Culminaing project. The Algorithm application.  
# NOTE: To see the tests of this file, see file: test_Algorithm_Application

#IMPORTS
import sys

#CLASSES
class Algorithm():     #parent
    """
    Description:
    Describes algorithms.

    Attributes:
    self, dataset, recursive, list_type
    """
    def __init__(self, dataset = 'Size of Data', recursive = 'Coding Style', list_type = 'Type of Data'):
        # instance attributes
        self.dataset = dataset
        self.recursive = recursive
        self.list_type = list_type
    
    def __str__(self):  
        # prints a string of the instance
        return f'\nALGORITHMS\tAttributes:\n\t{self.dataset}\n\t{self.recursive}\n\t{self.list_type}\n'

class Quicksort(Algorithm):     #child  
    '''
    Description:
    Describes the Quick sort algorithm.

    Attributes:
    self, dataset, recursive, list_type
    '''
    def __init__(self, dataset = 'medium', recursive = 'yes', list_type = 'array'): 
        # instance attributes 
        self.dataset = dataset
        self.recursive = recursive
        self.list_type = list_type

    def __str__(self):  
        # prints a string of the instance
        return f'\nName: Quick sort\n\tSuited Dataset: {self.dataset}\n\tRecursion (?): {self.recursive}\n\tSuited List Type: {self.list_type}\n'

    #Methods 
    @staticmethod
    def quick_sort_helper(my_list, low, high):      #helps Quicksort  
        """
        sets up for the recursion! It nests the algorithm!
        The parameters make it accesible for the sublists-> remember partitioning
        (not all sublists have a starting index of 0!)

        NOTE: no returns, sorts the list itself!

        args:
            the list (list)
            low (num): rightmost index
            high (num): leftmost index
        returns:
            none
        """
        #tracks the index
        MOVING_LEFT = 0   #indentifies whcih direction you are moving in
        MOVING_RIGHT = 1

        if low < high:  #for each recursive call, it may be just a
                        #single value in a sublist! (base case)
            #copy of the values because left and right will change
            left = low
            right = high
            current_direction = MOVING_LEFT
            pivot = my_list[low]  #index of zero for now, later for sublists,
            #^^it will change to the first element of the sublistlist

            while (left < right): #stops the sort when right and left meet (pivot finds its permanent place)
                if (current_direction == MOVING_LEFT):
                    while ((my_list[right] >= pivot) and (left < right)):
                    # checks if right value is still greater than or equal to pivot and
                    # checks if they converge (triggers and end to move in the next direction)
                        right -= 1  #continues moving right / down
                    my_list[left] = my_list[right]
                    current_direction = MOVING_RIGHT

                if (current_direction == MOVING_RIGHT):
                    while ((my_list[left] <= pivot) and (left < right)):
                    # left has to be less than the pivot
                    # checks if they converge left -> right (triggers and end to move in the next direction)
                        left += 1 #continues moing left / up
                    my_list[right] = my_list[left]
                    current_direction = MOVING_LEFT

            my_list[left] = pivot   #does not matter, can be left or right
            Quicksort.quick_sort_helper(my_list, low, left - 1)
            Quicksort.quick_sort_helper(my_list, right + 1, high) #right and left are the same value!

    @staticmethod 
    def quick_sort(my_list):                        
            """
            Accomplishes the actual quick sort

            args:
                my_list (list): the list
            returns
                my_list (list): the list
            """
            Quicksort.quick_sort_helper(my_list, 0, len(my_list) - 1) #recursively calls,
            #input the unique values for the sublists because they will be different
            return my_list

class Insertion(Algorithm):     #child  
    '''
    Description:
    Describes the Insertion sort algorithm.

    Attributes:
    self, dataset, recursive, list_type
    '''
    def __init__(self, dataset = 'small', recursive = 'no', list_type = 'array'):
        # instance attributes 
        self.dataset = dataset
        self.recursive = recursive
        self.list_type = list_type

    def __str__(self):
        return f'\nName: Insertion sort\n\tSuited Dataset: {self.dataset}\n\tRecursion (?): {self.recursive}\n\tSuited List Type: {self.list_type}\n'

    #Methods 
    @staticmethod
    def insert_sort(my_list):   
        """
        Accomplishes the insertion sort algorithm

        args:
            my_list (list): the list being sorted
        returns:
            my_list (list): the list being sorted
        """
        #process
        for i in range(len(my_list) - 1):
            j = i + 1                   # j will go from 1 to max_index
                                        #^^j is the next item in the list
            item = my_list[j]           # temporary storage of item

            #Run through the list backwards until item is less than element
            while (j > 0) and (item < my_list[j-1]):
                # Shift larger items to the right by one
                my_list[j] = my_list[j-1]
                # Prepare to check the next item to the left
                j -= 1

            my_list[j] = item           # put sorted item in open location

        #output
        return my_list

class Merge(Algorithm):         #child  
    '''
    Description:
    Describes the Insertion sort algorithm.

    Attributes:
    self, dataset, recursive, list_type
    '''
    def __init__(self, dataset = 'large', recursive = 'yes', list_type = 'linked'):
        # instance attributes 
        self.dataset = dataset
        self.recursive = recursive
        self.list_type = list_type

    def __str__(self):
        return f'\nName: Merge sort\n\tSuited Dataset: {self.dataset}\n\tRecursion (?): {self.recursive}\n\tSuited List Type: {self.list_type}\n'

    #Methods 
    @staticmethod
    def merge_helper(a_list):                       #the helper (with the return)   
        """
        Aids the execution of merge_sort

        args:
            a_list (list): the list being sorted
        returns:
            the_list (list): the list that was changed
        """   
        #Initiate Variables
        the_list = a_list[:]    #make a copy
        comparisons = []        #the list containing the total comparisons

        #Process
        Merge.merge_sort(the_list, comparisons)    #use the merge sort algoritm on the copied list

        #Output
        return the_list   #add all the numbers in the list to get the total comaprisons

    @staticmethod 
    def merge_sort(my_list, counter):               #merge sort algorithm    
        """ 
        Merge sort uses the idea of splitting an unsorted list into smaller arrays until there is only one in a group.
        The process continues until all the elements are merged and sorted.

        args:
            my_list (list): the list being sorted
            counter (list): contains the number of comparisons being made
        returns:
            none
        """ 
        #Initiate variables
        comparison_no = 0

        #Process
        comparison_no += 1     #keep track of comparisons
        if len(my_list) > 1:
            mid = len(my_list) // 2
            left_half = my_list[:mid]
            right_half = my_list[mid:]

            #Recursion
            Merge.merge_sort(left_half, counter)
            Merge.merge_sort(right_half, counter)

            #some Process
            left_half_index = 0
            right_half_index = 0
            full_list_index = 0

            comparison_no += 1     #keep track of comparisons
            while left_half_index < len(left_half) and right_half_index < len(right_half):
                comparison_no += 1     #keep track of comparisons

                comparison_no += 1     #keep track of comparisons
                if left_half[left_half_index] < right_half[right_half_index]:
                    my_list[full_list_index] = left_half[left_half_index]
                    left_half_index += 1
                else:
                    my_list[full_list_index] = right_half[right_half_index]
                    right_half_index += 1
                full_list_index += 1

            comparison_no += 1     #keep track of comparisons
            while left_half_index < len(left_half):
                comparison_no += 1     #keep track of comparisons

                my_list[full_list_index] = left_half[left_half_index]
                left_half_index += 1
                full_list_index += 1

            comparison_no += 1     #keep track of comparisons
            while right_half_index < len(right_half):
                comparison_no += 1     #keep track of comparisons (inside the list!)

                my_list[full_list_index] = right_half[right_half_index]
                right_half_index += 1
                full_list_index += 1
        
        #add all the tallied comparisons to the list
        counter.append(comparison_no)

#FUNCTIONS
def int_check(highest = int, lowest = int):     #checks int input 
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

def str_check(*correct):                        #checks str inputs  
    '''
    Checks the string inputted.

    arg:
        correct (str, *args): the valid strings.
    returns:
        string (str): the string inputted by user.
    '''
    while True:
        try:
            word = input('')
            if word.lower() in correct:
                return word
        except:
            print('Invalid input. Check Spelling.')

def txt_use(file_name, n):                      #uses readlines 
    """
    Facilitates the usage of .txt files using readlines and the list it creates.

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

def delete_last_line():                         
    """ 
    Deletes lines from the terminal.

    args:
        none
    returns:
        none
    """
    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def multiple_inputs():            
    """
    Stores multiple inputs as ints into a list.

    args:
        none
    returns:
        storage (list): the list in which all the inputs will be
    """
    # initiate list
    storage = []

    #process
    while True:
        try:
            item = int(input('Enter your inputs (Enter "-1" to stop): '))

            if item == -1:
                break
            else:
                storage.append(item)
                delete_last_line()      # deletes the line allowing the screen to save space
                                        # stackoverflow: https://tinyurl.run/BQiZRT
        except:
            print('You did something wrong, buddy.')
    
    #output
    return storage

def main():                                     
    """ 
    Describes the actual game.

    args:
        none
    returns:
        none
    """
    #initiate variables
    game_play = True

    #process
    print('\n' + txt_use('game_text.txt', 14))

    while game_play:   
        #Introduction
        for a in range(15, 16):
            print(txt_use('game_text.txt', a))
        
        user_choice = int_check(3, 1)

        if user_choice == 1:    
            print(' ')
            for b in range(16, 18):
                print(txt_use('game_text.txt', b))

            algo_choice = int_check(3, 1)

            if algo_choice == 1:
                #gets the list from the user
                new_list = multiple_inputs()
                print(f'\nYour list:\t{new_list}')

                #sorts the list and returns it
                Quicksort.quick_sort(new_list)
                print(f'Sorted list:\t{new_list}\n')

            elif algo_choice == 2:
                #gets the list from the user
                new_list = multiple_inputs()
                print(f'\nYour list:\t{new_list}')

                #sorts the list and returns it
                Insertion.insert_sort(new_list)
                print(f'Sorted list:\t{new_list}\n')
            
            elif algo_choice == 3:
                #gets the list from the user
                new_list = multiple_inputs()
                print(f'\nYour list:\t{new_list}')

                #sorts the list and returns it
                print(f'Sorted list:\t{Merge.merge_helper(new_list)}\n')

        if user_choice == 2:    
            print(' ')
            for c in range(16, 18):
                print(txt_use('game_text.txt', c))

            description_choice = int_check(3, 1)

            if description_choice == 1:
                q_instance = Quicksort()
                print(q_instance)
            elif description_choice == 2:
                i_instance = Insertion()
                print(i_instance)
            else:
                m_instance = Merge()
                print(m_instance)

        if user_choice == 3:    
            game_play = False

    #output / goodbye
    print('\n' + txt_use('game_text.txt', 12))
        
#ICONIQUE if-statement
if __name__ == '__main__':
    main()