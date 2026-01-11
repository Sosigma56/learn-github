import random

def number_guessing_game():
    """A simple number guessing game"""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print(f"Too low! Try again. ({max_attempts - attempts} attempts left)\n")
            elif guess > secret_number:
                print(f"Too high! Try again. ({max_attempts - attempts} attempts left)\n")
            else:
                print(f"\n🎉 You got it! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempt(s)!")
                return
        except ValueError:
            print("Please enter a valid number.\n")
    
    print(f"\n❌ Game Over! The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()