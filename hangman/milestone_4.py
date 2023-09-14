

import random


class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        word_list = ['orange', 'california', 'biscuits', 'ivy', 'weather']
        word_to_be_guessed = random.choice(word_list).lower()
        
        letters_guessed_successfully = ['_' for element in len(range(word_to_be_guessed))]
        letters_guessed_unsuccessfully = list()
        all_letters_guessed = list()
        
        num_unique_letters_in_word = int()
        num_letters = int()
        num_lives = int()
        
        
        def check_guess(guess):
            #guess = guess.lowercase()
            
            if guess in word_to_be_guessed:
                print (f'Good guess! {guess} is in the word.')
                
                for letter in word_to_be_guessed:
                    if word_to_be_guessed[letter] == guess:
                        letters_guessed_successfully[letter] = guess
                    else:
                        num_lives =- 1
                        print(f'Sorry, {letter} is not in the word')
                        print(f'You have {num_lives} lives left.')
                num_letters =- 1     
    



        def ask_for_input():
            while True:
                guess = input('Please enter a letter: ').lowercase().strip()
                print(guess)

                if (len(guess) != 1) or (guess.isalpha()==False):
                    print(f'Invalid input: {guess}. Please, enter a single alphabetical character\n')   
                elif guess in all_letters_guessed: 
                    print('You already tried that letter!')
                elif (len(guess) != 1) and (guess.isalpha()==True) and (guess not in all_letters_guessed):
                    check_guess(guess)
                    all_letters_guessed.append(guess)
                else:
                    pass
        
        ask_for_input()
               
    