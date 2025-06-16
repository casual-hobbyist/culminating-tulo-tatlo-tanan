# Name: Abby Villanueva
# Details: Culminaing project. Testing the file: Algorithm_Application.  

# IMPORTS
import unittest
from unittest import mock

#classes
from Algorithm_Application import Algorithm
from Algorithm_Application import Quicksort
from Algorithm_Application import Insertion
from Algorithm_Application import Merge

#functions
from Algorithm_Application import int_check
from Algorithm_Application import str_check
from Algorithm_Application import txt_use           #do i need to test this?
from Algorithm_Application import delete_last_line  #do i need to test this?
from Algorithm_Application import multiple_inputs

#INITIATE CONTSTANT (lists)
TEST_LIST1 = [5, 6, 23, 1, -4, 9078, 24, 83, 0, -32]
TEST_LIST2 = [8, 2, 123, 234, 75, 45, 54, 23, 56, 89, 60, 2, 5, 37, 102]

#UNIT TESTING - CLASSES
class testAlgorithm(unittest.TestCase):               
    # dunder method: __str__
    def test1_A_StrStructure(self):                   
        #set-up instances
        a = Algorithm()

        #set-up checks for correct_result
        text = f'\nALGORITHMS\tAttributes:\n\t{a.dataset}\n\t{a.recursive}\n\t{a.list_type}\n'

        #set up the test
        result_reg = str(a)   
        correct_result = text 

        #output        
        print(f'\t\tTESTING FOR Algorithm()')  
        print('-' * 50)
        print(f'Test Case (Dunder): __str__     Args: a (Algorithm instance)')
        print(f'The program outputs:\t', result_reg)
        print(f'Expected outputs:\t', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')

class testQuicksort(unittest.TestCase):               
    # dunder method: __str__
    def test1_QS_StrStructure(self):                   
        #set-up instances
        q = Quicksort()

        #set-up checks for correct_result
        text = f'\nName: Quick sort\n\tSuited Dataset: {q.dataset}\n\t'
        text2 = f'Recursion (?): {q.recursive}\n\tSuited List Type: {q.list_type}\n'

        #set up the test
        result_reg = str(q)   
        correct_result = text + text2

        #output        
        print(f'\t\tTESTING FOR Quicksort')  
        print('-' * 50)
        print(f'Test Case (Dunder): __str__     Args: q (Quicksort instance)')
        print(f'The program outputs:\t', result_reg)
        print(f'Expected outputs:\t', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')

    #methods
    #with 10-element list  
    def test2_QS_10(self):       
        result_reg = Quicksort.quick_sort(TEST_LIST1)
        correct_result = ([-32, -4, 0, 1, 5, 6, 23, 24, 83, 9078])
        print('-' * 50)
        print(f'Test Case: 2 | Args: TEST_LIST1')
        print(f'The program outputs: ', result_reg)
        print(f'Expected outputs:    ', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')
        print('-' * 50)

    #with 15-element list
    def test3_QS_15(self):     
        result_reg = Quicksort.quick_sort([8, 2, 123, 234, 75, 45, 54, 23, 56, 89, 60, 2, 5, 37, 102])
        correct_result = ([2, 2, 5, 8, 23, 37, 45, 54, 56, 60, 75, 89, 102, 123, 234])
        print('-' * 50)
        print(f'\nTest Case: 3 | Args: TEST_LIST2')
        print(f'The program outputs: ', result_reg)
        print(f'Expected outputs:    ', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')
        print('-' * 50)

class testInsertionsort(unittest.TestCase):               
    # dunder method: __str__
    def test1_QS_StrStructure(self):                   
        #set-up instances
        i = Insertion()

        #set-up checks for correct_result
        text = f'\nName: Insertion sort\n\tSuited Dataset: {i.dataset}\n\t'
        text2 = f'Recursion (?): {i.recursive}\n\tSuited List Type: {i.list_type}\n'

        #set up the test
        result_reg = str(i)   
        correct_result = text + text2

        #output        
        print(f'\t\tTESTING FOR Inertion Sort')  
        print('-' * 50)
        print(f'Test Case (Dunder): __str__     Args: i (Insertion instance)')
        print(f'The program outputs:\t', result_reg)
        print(f'Expected outputs:\t', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')

    #methods
    #with 10-element list  
    def test2_QS_10(self):       
        result_reg = Insertion.insert_sort(TEST_LIST1)
        correct_result = ([-32, -4, 0, 1, 5, 6, 23, 24, 83, 9078])
        print('-' * 50)
        print(f'Test Case: 2 | Args: TEST_LIST1')
        print(f'The program outputs: ', result_reg)
        print(f'Expected outputs:    ', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')
        print('-' * 50)

    #with 15-element list
    def test3_QS_15(self):     
        result_reg = Insertion.insert_sort([8, 2, 123, 234, 75, 45, 54, 23, 56, 89, 60, 2, 5, 37, 102])
        correct_result = ([2, 2, 5, 8, 23, 37, 45, 54, 56, 60, 75, 89, 102, 123, 234])
        print('-' * 50)
        print(f'\nTest Case: 3 | Args: TEST_LIST2')
        print(f'The program outputs: ', result_reg)
        print(f'Expected outputs:    ', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')
        print('-' * 50)

class testMergeSortAndHelper(unittest.TestCase): 
    # dunder method: __str__
    def test1_MSaH_StrStructure(self):                   
        #set-up instances
        m = Merge()

        #set-up checks for correct_result
        text = f'\nName: Merge sort\n\tSuited Dataset: {m.dataset}\n\t'
        text2 = f'Recursion (?): {m.recursive}\n\tSuited List Type: {m.list_type}\n'

        #set up the test
        result_reg = str(m)   
        correct_result = text + text2

        #output        
        print(f'\t\tTESTING FOR Merge Sort')  
        print('-' * 50)
        print(f'Test Case (Dunder): __str__     Args: m (Merge instance)')
        print(f'The program outputs:\t', result_reg)
        print(f'Expected outputs:\t', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')

    #methods  
    #with 10-element list  
    def test2_MSaH_10(self):       
        result_reg = Merge.merge_helper(TEST_LIST1)
        correct_result = ([-32, -4, 0, 1, 5, 6, 23, 24, 83, 9078])
        print('-' * 50)
        print(f'Test Case: 2 | Args: TEST_LIST1')
        print(f'The program outputs: ', result_reg)
        print(f'Expected outputs:    ', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')
        print('-' * 50)

    #with 15-element list
    def test3_MSaH_15(self):     
        result_reg = Merge.merge_helper([8, 2, 123, 234, 75, 45, 54, 23, 56, 89, 60, 2, 5, 37, 102])
        correct_result = ([2, 2, 5, 8, 23, 37, 45, 54, 56, 60, 75, 89, 102, 123, 234])
        print('-' * 50)
        print(f'\nTest Case: 3 | Args: TEST_LIST2')
        print(f'The program outputs: ', result_reg)
        print(f'Expected outputs:    ', correct_result)
        try:
            self.assertEqual(result_reg, correct_result, 'The outputs are wrong')
            print('Test Passed')
        except:
            print('Test Failed')
        print('-' * 50)

#UNIT TESTING - FUNCTIONS
class testInt_Check(unittest.TestCase):            
    @mock.patch('builtins.input', create = True)
    def test1_IC_zero(self, mock_input):     
        mock_input.side_effect = [0, 4]
        input_return = int_check(5, 1)
        correct_return = 4
        print(f'\t\tTESTING FOR int_check()')  
        print('-' * 50)
        print('Test Case 1: Inputs: 0, 4')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test2_IC_OnePossibleAnswer(self, mock_input):     
        mock_input.side_effect = [0, 2, 1]
        input_return = int_check(1, 1)
        correct_return = 1
        print('-' * 50)
        print('Test Case 2: Inputs: 0, 2, 1')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test3_IC_LeftInclusive(self, mock_input):     
        mock_input.side_effect = [0, -1, 5, 2]
        input_return = int_check(2, 1)
        correct_return = 2
        print('-' * 50)
        print('Test Case 3: Inputs: 0, -1, 5, 2')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test4_IC_RightInclusive(self, mock_input):     
        mock_input.side_effect = [0, 10, 3]
        input_return = int_check(8, 3)
        correct_return = 3
        print('-' * 50)
        print('Test Case 4: Inputs: 0, 10, 3')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

class testStr_Check(unittest.TestCase):
    @mock.patch('builtins.input', create = True)
    def test1_SC_LowerCase(self, mock_input):     
        mock_input.side_effect = ['atom', 'Yes']
        input_return = str_check('yes')
        correct_return = 'Yes'
        print(f'\t\tTESTING FOR str_check()')  
        print('-' * 50)
        print('Test Case 1: Inputs: "atom", "Yes"')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test2_SC_UpperCaseInput(self, mock_input):     
        mock_input.side_effect = ["fake", "Falsehood"]
        input_return = str_check('falsehood')
        correct_return = 'Falsehood'
        print('-' * 50)
        print('Test Case 2: Inputs: "fake", "Falsehood"')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test3_SC_DifferentWords(self, mock_input):     
        mock_input.side_effect = ["cat", "dog", "crocodile"]
        input_return = str_check("armadillo", "zebra", "crocodile")
        correct_return = "crocodile"
        print('-' * 50)
        print('Test Case 3: Inputs: "cat", "dog", "crocodile"')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test4_SC_StringNumbers(self, mock_input):     
        mock_input.side_effect = ["sparkle", "10"]
        input_return = str_check('9', '10')
        correct_return = '10'
        print('-' * 50)
        print('Test Case 4: Inputs: "sparkle", "10"')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

class testMultiple_Inputs(unittest.TestCase):   
    @mock.patch('builtins.input', create = True)
    def test1_MI_NegativeNumbers(self, mock_input):     
        mock_input.side_effect = [-2, -9, -10, -1]
        input_return = multiple_inputs()
        correct_return = [-2, -9, -10]
        print(f'\t\tTESTING FOR multiple_numbers()')  
        print('-' * 50)
        print('Test Case 1: Negative Numbers    Inputs: [-2, -9, -10]')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test2_MI_OneElement(self, mock_input):     
        mock_input.side_effect = [2, -1]
        input_return = multiple_inputs()
        correct_return = [2]
        print('-' * 50)
        print('Test Case 2: One Element List    Inputs: [2, -1]')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test3_MI_Zeros(self, mock_input):     
        mock_input.side_effect = [0, 0, -1]
        input_return = multiple_inputs()
        correct_return = [0, 0] 
        print('-' * 50)
        print('Test Case 3: Zeros    Inputs: [0, 0, -1]')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

    @mock.patch('builtins.input', create = True)
    def test3_MI_NoContents(self, mock_input):     
        mock_input.side_effect = [-1, 0]
        input_return = multiple_inputs()
        correct_return = [] 
        print('-' * 50)
        print('Test Case 3: No Contents    Inputs: [-1, 0]')
        print('Your program outputs: ', input_return)
        print('Expected outputs:     ', correct_return)
        try:
            self.assertEqual(input_return, correct_return)
            print('Test Passed')
        except:
            print('Test Failed') 
        print('-' * 50 + '\n')

#iconique if-statement
if __name__ == '__main__':
    unittest.main()