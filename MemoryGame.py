import random
import time
def generate_sequence(difficulty):
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    return sequence

def get_list_from_user(difficulty):
    time.sleep(0.7)  # Display numbers for 0.7 seconds
    user_input = []
    for i in range(difficulty):
        num = int(input(f"Enter number {i + 1}: "))
        user_input.append(num)
    return user_input
def is_list_equal(list1, list2):
    return list1 == list2

def play_game(difficulty):
    sequence = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_list):
        print("Congratulations ! ,You won")
        return True
    else:
        print("Sorry,you lost")
        return False



