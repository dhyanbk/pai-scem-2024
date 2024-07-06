import random

def hangman():
    words = ["python", "hangman", "challenge", "programming"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    
    while attempts > 0 and "_" in guessed:
        print("Word:", " ".join(guessed))
        guess = input("Guess a letter: ").lower()
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Incorrect! Attempts remaining: {attempts}")
        
    if "_" not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

hangman()