import os
import time

# file_path = "/Users/liorharel/pythonProject/Wog2/Scores.txt"
# SCORES_FILE_NAME = file_path
# BAD_RETURN_CODE = -1

file_path = "Scores.txt"
SCORES_FILE_NAME = os.path.join(os.path.dirname(__file__), file_path)
BAD_RETURN_CODE = -1


# def screen_cleaner():
#     os.system('clear' if os.name == 'posix' else 'cls')

def screen_cleaner():
    os.environ['TERM'] = 'xterm'
    time.sleep(2)
    os.system('clear' if os.name == 'posix' else 'cls')


