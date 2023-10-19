import random

word_list = ["Apple", "Pear", "Orange", "Watermelon", "Peach"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = []
        self.list_of_guesses = []
        self.word = random.choice(self.word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = ["_"] * len(self.word)
        print(self.word_guessed)

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.") 
            for char in range(0, len(self.word)):
                if guess == self.word[char]:
                    self.word_guessed[char] = guess
                    self.word_guessed = "".join(self.word_guessed)
                    print(self.word_guessed)
                    self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses += guess   


hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
    


          
