import MemoryGame
import GuessGame
import Currency_Roulette_Game
from Score import add_score, BAD_RETURN_CODE

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    game_choice = int(input("Please choose a game to play\n"
                            "1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                            "back\n "
                            "2.Guess Game - guess a number and see if you chose like the computer\n"
                            "3.Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                            "Enter your choice (1-3): "))
    while True:
        try:
            if game_choice in [1, 2, 3]:
                break
            else:
                print("Please choose a number between 1 to 3 for the game.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty_level in [1, 2, 3, 4, 5]:
                break
            else:
                print("Please choose a number between 1 to 5 for the difficulty level.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if game_choice == 1:
        result = MemoryGame.play_game(difficulty_level)
    elif game_choice == 2:
        result = GuessGame.play_game(difficulty_level)
    elif game_choice == 3:
        result = Currency_Roulette_Game.play_game(difficulty_level)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


    if result:
        try:
            add_score(difficulty_level)
        except Exception as e:
            print(f"Error updating score: {e}")
            return BAD_RETURN_CODE
    return result

