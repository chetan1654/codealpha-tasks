import random

def choose_word():
    words = ["python", "developer", "hangman", "challenge", "programming", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
        else:
            print("Good guess!")
        
        if set(word).issubset(guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
