while True:
    guess = input("Guess a letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please enter a single alphabetical character")

