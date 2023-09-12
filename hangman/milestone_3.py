

import random_word
 
           
def ask_for_input():
    
    """
    Prompts user for letter and continue looping until letter is accepted (user input should be one alphabetical letter), 
    calling check_guess method when condition is true. 
    
    
    Inputs:
    -
    
    Outputs:
    user_guess: letter guessed by user, used by check_guess(user_guess)
    """
    
    guess_rejected = True
    
    while guess_rejected == True:
        
        print("\nPlease enter a single letter. For example: a. \nPlease do not include numbers or special characters.\n")
        user_guess = input("Please enter your chosen single letter: ").strip().casefold() 
        
        if (len(user_guess) == 1) and (user_guess.isalpha()):
            guess_rejected = False #answer is accepted
            check_guess(user_guess)
        elif (len(user_guess) != 1) or (user_guess.isalpha()==False):
            print(f'Invalid input: {user_guess}. Please, enter a single alphabetical character\n')   
        else: 
            print('Error in code')



def check_guess(user_guess):
    
    """
    Checks if letter user chooses is in randomly generated word and prints appropriate message to user. 
    
    Inputs:
    user_guess: letter guessed by user, from ask_for_input() method
    
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




ask_for_input()
