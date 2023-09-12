import random

def create_fruit_list():
    my_fruit_list = ['Apple', 'Banana', 'Melon', 'Mango', 'Kiwi']
    word_from_fruit_list = random.choices(my_fruit_list)


def receive_user_letter():
    """
    Prompt user for letter and continue looping until letter is accepted (user input should be one alphabetical letter). 
    
    Non-numerical, length of 1 and no special characters dependent on user input.
    Code removes whitespaces and makes input lowercase to reduce errors in if else loop. 

    No return, just print statements to user. 
    """
    guess_accepted = False
    
    while guess_accepted == False:
        print("\nPlease enter a single letter. For example: a. \nPlease do not include numbers or special characters.\n")
        
        user_guess = input("Please enter your chosen single letter: ").strip().casefold() 
        
        if (len(user_guess) == 1) and (user_guess.isalpha()):
            print(f'Good guess: {user_guess}')
            guess_accepted = True
        elif (len(user_guess) != 1) or (user_guess.isalpha()==False):
            print(f'Bad guess: {user_guess}')
        #else statement hopefully won't ever run but might make easier to catch errors...
        else:
            print('Error')

receive_user_letter()
