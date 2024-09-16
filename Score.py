from Utils import SCORES_FILE_NAME,BAD_RETURN_CODE
POINTS_OF_WINNING = lambda difficulty:(difficulty * 3) + 5
import os

def add_score(difficulty):

        try:
            if os.path.exists(SCORES_FILE_NAME):
                if os.path.getsize(SCORES_FILE_NAME) > 0:
                    with open(SCORES_FILE_NAME, 'r') as file:
                        current_score = int(file.read().strip())
                        print(f"Current score read from '{SCORES_FILE_NAME}': {current_score}")
                else:
                    current_score = 0
                    print(f"The file '{SCORES_FILE_NAME}' is empty. Initializing score to 0.")
            else:
                current_score = 0
                print(f"File '{SCORES_FILE_NAME}' not found. Initializing score to 0.")
        except IOError as e:
            print(f"Error reading from file '{SCORES_FILE_NAME}': {e}")
            return BAD_RETURN_CODE

        try:
            points_to_add = POINTS_OF_WINNING(difficulty)  # Assuming POINTS_OF_WINNING is a defined function
            new_score = current_score + points_to_add
            with open(SCORES_FILE_NAME, 'w') as file:
                file.write(str(new_score))
                print(f"New score written to '{SCORES_FILE_NAME}': {new_score}")
            return new_score
        except Exception as e:
            print(f"Error writing to file '{SCORES_FILE_NAME}': {e}")
            return BAD_RETURN_CODE


