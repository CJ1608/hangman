

import random

#class definition
class Hangman:
    """
    The class is used to represent an instance of game of Hangman. 
    
    Hangman game that receives letter guess from user and checks if it present in the word chosen.
    Start with default number of lives that can be changed in the code and a word chosen randomly from a hard-coded list.
    
    Parameters:
    ----------
        word_list (list): 
            hard coded list of words that the word used in the game is randomly selected from. 
        num_lives (int): 
            number of lives user has left. Default is 5. 
    
    Arguments:
    ----------
        word(str): 
            word that is used in the hangman game that the user must guess. 
        word_guessed(list): 
            list of underscores that represent letters in the word. Underscores replaced when letter is guessed. 
        num_letters(int): 
            the number of unique letters in the word. 
        lists_letters(list): 
            the letters guessed by the user, correct and incorrect. 
        
    Methods:
    ---------
        check_letters(self, letter): 
            Confirms whether the letter from from the ask_letter method is in the word being guessed. 
        ask_letter(self): 
            Accepts letter user enters only if the input is a singular alphabetical character. 
    """
    

    def __init__(self, word_list, num_lives=5):
        """Initalise variables of the class and prints start message to user. 

        Args:
            word_list (list): hard coded list of words that the word used in the game is randomly selected from. 
            num_lives (int): number of lives user has left. Default is 5. 
        """
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for element in range(len(self.word))]
        self.num_letters = int(len(set(self.word))) 
        self.lists_letters = list()

        print(f'\nThe mystery word has {self.num_letters} characters unguessed.')
        print(f'\t{self.word_guessed}')
    
    
   
    def __check_letter(self, letter):
        """Confirms whether the letter passed from the ask_letter method is in the Hangman word being guessed. 
        
        If the letter is in the word it prints a confirmation message to the user and reduces the number of unique letters in the Hangman word that have not been guessed yet. It then 
        tells the user how many letters are left to guess in the Hangman word and replaces every underscore that represents the presence of the letter. After, it prints a confirmation
        message and prints the updated word guessed to reflect the correct guess. 
        
        If the letter is not in the word, it prints a commiseration message to user, reduces the number of lives by 1 and prints the incorrect letter and updated number of lives to user. 

        Args:
            letter (str): user input of letter to search word for, passed from ask_letter method. 
        """
        
        if letter in self.word:
            print (f'\nGood guess! "{letter}" is in the word.')
            self.num_letters -= 1
            print(f'You have {self.num_letters} characters unguessed.')

            for index in range(len(self.word_guessed)):
                
                if self.word[index] == letter:
                    self.word_guessed[index] = letter
                    
            print(f'\t{self.word_guessed}')  
      
        else:
            self.num_lives = self.num_lives - 1
            print(f'\nSorry, "{letter}" is not in the word. You have {self.num_lives} lives left.')       



    def ask_letter(self):
        """Accepts a letter that the user enters only if the input is a singular alphabetical character. 
        
        It formats the input so that all characters are lowercase and removes whitespace. 
        
        If the user input is 1 character, is alphabetical and has not been guessed before, it adds the guess to the lists_letters list of guessed letters and calls
        the check_letter method. 
        
        If the user input does not meet the above conditions, it prints a message restating what the user needs to do and asks the user to input another character until 
        it gets one that meets the conditons.  
        """
        
        letter = input('\nPlease enter a letter: ').casefold().strip()

        if (len(letter)!= 1) or (letter.isalpha()==False):
            print(f'Invalid input: "{letter}". Please, enter a single alphabetical character\n')     

        elif letter in self.lists_letters: 
            print(f'You already tried "{letter}"!')   

        else:
            self.lists_letters.append(letter)
            self.__check_letter(letter)
    
    
     
