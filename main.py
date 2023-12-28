import random

#class definition
class Hangman:
    """
    The class is used to represent an instance of a game of Hangman. 
    
    It receives a letter from user input, checks it is a single alphabetical letter and checks if it present in the Hangman word chosen.
    It starts with a default number of lives and a word chosen randomly from the word_list variable.
    
    Parameters:
    ----------
        word_list (list): 
            A list of words that the Hangman word used in the game is randomly selected from. 
        num_lives (int): 
            The number of lives the user has left. Default is 5. 
    
    Arguments:
    ----------
        word_to_guess(str): 
            The word that is used in the Hangman game that the user must guess. 
        word_guessed_user_visible(list): 
            A list of underscores that represent letters in the word. Underscores are replaced when the letter is guessed. 
        num_unique_correct_letters_unguessed(int): 
            The number of unique letters in the word_to_guess. 
        all_guessed_letters(list): 
            The letters guessed by the user, correct and incorrect. 
        
    Methods:
    ---------
        check_letters(self, letter): 
            Confirms whether the letter from the ask_letter method is in the word_to_guess being guessed. 
        ask_letter(self): 
            Accepts letter user enters only if the input is a singular alphabetical character. 
    """
    

    def __init__(self, word_list, num_lives=5):
        """Initalise variables of the class and prints start message to user. 

        Args:
            word_list (list): hard coded list of words that the word_to_guess used in the game is randomly selected from. 
            num_lives (int): number of lives user has left. Default is 5. 
        """
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word_to_guess = random.choice(word_list).lower()
        self.word_guessed_user_visible = ['_' for element in range(len(self.word_to_guess))]
        self.num_unique_correct_letters_unguessed = int(len(set(self.word_to_guess))) 
        self.all_guessed_letters = list()

        print(f'\nThe mystery word has {self.num_unique_correct_letters_unguessed} character(s) unguessed.')
        print(f'\t{self.word_guessed_user_visible}')
    
    
   
    def __check_letter(self, letter):
        """Confirms whether the letter passed from the ask_letter method is in the word_to_guess variable. 
        
        If the letter is in the word_to_guess it prints a confirmation message to the user and reduces the number of unique letters in the num_unique_correct_letters_unguessed variable. It then 
        tells the user how many letters are left to guess in the word_guessed_user_visible and replaces every underscore that represents the presence of the letter. After, it prints a confirmation
        message and prints the word_guessed_user_visible to reflect the correct guess. 
        
        If the letter is not in the word_to_guess, it prints a commiseration message to user, reduces the number of lives by 1 and prints the incorrect letter and updated number of lives to user. 

        Args:
            letter (str): user input of letter to search word_to_guess for, passed from ask_letter method. 
        """
        
        if letter in self.word_to_guess:
            print (f'\nGood guess! "{letter}" is in the word.')
            self.num_unique_correct_letters_unguessed -= 1
            print(f'The mystery word has {self.num_unique_correct_letters_unguessed} character(s) unguessed.')

            for index in range(len(self.word_guessed_user_visible)):
                
                if self.word_to_guess[index] == letter:
                    self.word_guessed_user_visible[index] = letter
                    
            print(f'\t{self.word_guessed_user_visible}')  
      
        else:
            self.num_lives = self.num_lives - 1
            print(f'\nSorry, "{letter}" is not in the word. You have {self.num_lives} live(s) left.')       



    def ask_letter(self):
        """Accepts a letter that the user enters only if the input is a singular alphabetical character. 
        
        It formats the input so that all characters are lowercase and removes whitespace. 
        
        If the user input is 1 character, is alphabetical and has not been guessed before, it adds the guess to the all_guessed_letters list of guessed letters and calls
        the check_letter method. 
        
        If the user input does not meet the above conditions, it prints a message restating what the user needs to do and asks the user to input another character until 
        it gets one that meets the conditons.  
        """
        
        letter = input('\nPlease enter a letter: ').casefold().strip()

        if (len(letter)!= 1) or (letter.isalpha()==False):
            print(f'Invalid input: "{letter}". Please, enter a single alphabetical character\n')     

        elif letter in self.all_guessed_letters: 
            print(f'You already tried "{letter}"!')   

        else:
            self.all_guessed_letters.append(letter)
            self.__check_letter(letter)
    
    
     
def play_game(word_list):
    """Creates an object of the class Hangman, checks if the game has finished and prints the appropriate message to the user. 
    
    While there is still an unguessed letter in the word_to_guess_user_visible, it checks if the user has a life left or not. If the user doesn't have a life left, it prints a commiseration message and ends the game. 
    If the user does have a life left, it calls the ask_letter method which in turn calls the check_letter method. 
    
    If all the letters in the word_to_guess_user_visible have been guessed, it prints a congratulations message to the user and ends the game. 

    Args:
        word_list (list): list of words that the Hangman word_to_guess is chosen from. 

    Returns:
        0 : ends the game when the user has no lives left. 
    """
    game = Hangman (word_list, num_lives=5)
    
    while '_' in game.word_guessed_user_visible:

        if game.num_lives > 0:
            game.ask_letter()

        elif game.num_lives == 0:
            print(f'\nYou lost, you have {game.num_lives} live(s) left. The word was "{game.word_to_guess}".')
            return 0
        #shouldn't run   
        else:
            print('Error.')
        
    print(f'\nCongratulations, "{game.word_to_guess}" was the right answer! You won!')
            


# check if main program or not   
if __name__ == '__main__':
    word_list = ['orange', 'california', 'biscuits', 'ivy', 'weather'] 
    play_game(word_list)
