import random

def hangman():
    # List of words with length greater than 6
    word_list = ["PYTHON", "DEVELOPER", "COMPUTER", "PROGRAMMING", "SOFTWARE", "ENGINEERING", "ALGORITHM"]
    
    # Randomly select a word from the list
    word = random.choice(word_list)
    word_length = len(word)
    
    # Initialize an empty list with underscores
    hidden_word = ["_"] * word_length
    
    # Number of allowed incorrect guesses
    max_incorrect_guesses = 6
    incorrect_guesses = 0
    
    # List to store guessed letters
    guessed_letters = []
    
   
    # Game loop
    while incorrect_guesses < max_incorrect_guesses and "_" in hidden_word:
        # Display current state of the word
        print("\nCurrent word: " + " ".join(hidden_word))
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        # Prompt the user to guess a letter
        guess = input("Guess a letter: ").upper()
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word:
            # Update the hidden word
            for i in range(word_length):
                if word[i] == guess:
                    hidden_word[i] = guess
            print("Good guess!")
        else:
            # Incorrect guess
            incorrect_guesses += 1
            print("Incorrect guess!")
        
    # Check if the player has won or lost
    if "_" not in hidden_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! You ran out of guesses.")
        print("The word was:", word)
        print(hangman_visual[incorrect_guesses])

# Start the game
hangman()
