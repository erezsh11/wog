import requests
import random

api_url = (" https://v6.exchangerate-api.com/v6/e1fbb9f18daa341e45b71b0d/latest/USD")

def get_money_interval(difficulty,total_value):
    differnce = 5 - difficulty
    lower_bound = total_value - differnce
    upper_bound = total_value + differnce
    return (lower_bound, upper_bound)

def get_exchange_rate(api_url):
    try:
        response = requests.get(api_url)
        conversion_rates = response.json()
        rate = conversion_rates['conversion_rates']['ILS']

    except ValueError as e:
        print(f"Error fetching exchange rate : {e}")
       # return None
    return rate


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Enter your guess for the exchange rate (USD to ILS):"))

        except ValueError:
            print("Invalid input ,please enter a valid number .")
        return guess

def play_game(difficulty):

    generated_number = random.randint(1, 100)
    print(f"The generated number is: {generated_number}")
    exchange_rate = get_exchange_rate(api_url)
    if exchange_rate is None:
        return False

    lower_bound, upper_bound = get_money_interval(difficulty, exchange_rate)
    print(f"Guess the exchange rate for USD to ILS between {lower_bound:.4f} and {upper_bound:.4f}")

    guess = get_guess_from_user()
    if lower_bound <= guess <= upper_bound:
        print("Congratulations! Your guess is correct.")
    else:
        print(f"Sorry, your guess {guess:.4f} was not within the correct range.")
        print(f"The correct exchange rate is {exchange_rate:.4f}")










