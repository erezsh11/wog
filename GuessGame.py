import random


def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess the secret number (between 1 and {difficulty}): "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compare_results(secret_number, user_guess):
    if user_guess == secret_number:
        print("Congratulations! You guessed the secret number!")
        return True
    else:
        print(f"Sorry, the secret number was {secret_number}. Better luck next time!")
        return False

def play_game(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)

# Example usage:
def main():
    difficulty = 5  # Example difficulty level, you can set this based on your game design
    result = play_game(difficulty)
    print(f"Game over. You {'won' if result else 'lost'}!")

if __name__ == "__main__":
    main()