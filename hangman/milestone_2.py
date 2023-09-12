import random

def create_list():
    my_list = ['Apple', 'Banana', 'Melon', 'Mango', 'Kiwi']
    word = random.choices(my_list)
    
    print(my_list, word)


def receive_user_letter():
    #finish loop only when have a valid guess
    guessed = False
    
    while guessed == False:
        #make it obvious to user what expected
        print("\nPlease enter a single letter. For example: a. \nPlease do not include numbers or special characters.\n")
        #strip white space and casefold to help if loop
        guess = input("Please enter your chosen single letter: ").strip().casefold() 
        
        if (len(guess) == 1) and (guess.isalpha()):
            print(f'Good guess: {guess}')
            guessed = True
        elif (len(guess) != 1) or (guess.isalpha()==False):
            print(f'Bad guess: {guess}')
        #else statement hopefully won't ever run but might make easier to catch errors...
        else:
            print('Error')

receive_user_letter()