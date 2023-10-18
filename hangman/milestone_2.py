import random

word_list = ["Apple", "Pear", "Orange", "Watermelon", "Peach"]
print(word_list)

# print random word from list
word = random.choice(word_list)
print(word)

# input a single letter as a guess and check it's valid
guess = input("Enter single letter: ")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!") 
    
else:
    print("Oops! That is not a valid input.")