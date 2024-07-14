from Utils import SCORES_FILE_NAME,BAD_RETURN_CODE
POINTS_OF_WINNING = lambda difficulty:(difficulty * 3) + 5

def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME,'r') as file:
            current_score = int(file.read().strip())
    except FileNotFoundError:
        current_score=0
    except ValueError:
        print("Error:Unable to get a grade from file")
        return BAD_RETURN_CODE

    points_to_add=POINTS_OF_WINNING(difficulty)
    new_score=current_score+points_to_add
    try:
        with open(SCORES_FILE_NAME,'w') as file:
             file.write(str(new_score))
    except Exception as e:
        print("fError: {e}")
        return BAD_RETURN_CODE

    return new_score

