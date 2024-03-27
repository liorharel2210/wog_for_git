import os
from Utils_file_utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def calculate_points(difficulty):
    return int(difficulty * 3) + 5


def add_score(difficulty):
    try:
        current_score = read_score_from_file()
        new_score = current_score + calculate_points(difficulty)
        write_score_to_file(new_score)
    except FileNotFoundError:
        create_new_score_file(difficulty)
    except ValueError:
        print()


def read_score_from_file():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            content = file.read().strip()
            return int(content) if content.isdigit() else 0
    except FileNotFoundError:
        return 0


def write_score_to_file(score):
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(score))


def create_new_score_file(difficulty):
    new_score = calculate_points(difficulty)
    write_score_to_file(new_score)
