

import random_word
 
           
def ask_for_input():
    
    """
    Prompts user for letter and continue looping until letter is accepted (user input should be one alphabetical letter). 
    
    Code removes whitescapes and converts to lowercase and if else loop then checks it is a 1 alphabetical character. 
    
    Inputs:
    -
    
    Outputs:
    user_guess: letter guessed by user, used by check_guess(passed_user_guess)
    """
    
    guess_rejected = True
    
    while guess_rejected == True:
        
        print("\nPlease enter a single letter. For example: a. \nPlease do not include numbers or special characters.\n")
        user_guess = input("Please enter your chosen single letter: ").strip().casefold() 
        
        if (len(user_guess) == 1) and (user_guess.isalpha()):
            print(f'Good guess: {user_guess}\n')
            guess_rejected = False #answer is accepted
            check_guess(user_guess)
        elif (len(user_guess) != 1) or (user_guess.isalpha()==False):
            print(f'Invalid input: {user_guess}. Please, enter a single alphabetical character\n')   
            check_guess(user_guess)
        else: 
            print('Error in code')

#call check guess function 
    


def check_guess(user_guess):
    
    """
    Checks if letter user chooses is in randomly generated word and prints appropriate message to user. 
    
    Inputs:
    passed_user_guess: letter guessed by user, from ask_for_input() method
    
    Outputs:
    -
    """
    
    my_rw = random_word.RandomWords()
    my_random_word = my_rw.get_random_word()
   
   
    for letter in range(len(user_guess)):
        
        if user_guess[letter] in my_random_word:
            print(f'Good guess, "{user_guess}" is in the word {my_random_word}.\n')
        elif user_guess[letter] not in my_random_word:
            print(f'Sorry, "{user_guess}" is not in the word {my_random_word}. Try again.\n')
        else:
             print('Error in the code')





# #saves return statement from method into variable? 
# passed_user_guess = ask_for_input() 
# check_guess(passed_user_guess)
ask_for_input()
#call ask for input 
#put the check_guess in ask for input method 