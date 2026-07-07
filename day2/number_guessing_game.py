import random

def play_game():
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)
    
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    attempts = 0
    
    #repeat until the user guesses correctly
    while True:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check if guess is within bounds
            if guess < lower_bound or guess > upper_bound:
                print(f"Please keep your guess between {lower_bound} and {upper_bound}.")
                continue
          
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
                
        except ValueError:
            #if user types letters or symbols instead of a number
            print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    play_game()
