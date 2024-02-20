import random
import time
from Utils_file_utils import screen_cleaner


def generate_sequence_kids():
    numbers = [random.randint(0, 20) for _ in range(3)]
    return numbers

def generate_sequence_easy():
    numbers = [random.randint(0, 40) for _ in range(3)]
    return numbers

def generate_sequence_normal():
    numbers = [random.randint(0, 60) for _ in range(3)]
    return numbers

def generate_sequence_hard():
    numbers = [random.randint(0, 80) for _ in range(3)]
    return numbers

def generate_sequence_professional():
    numbers = [random.randint(0, 100) for _ in range(3)]
    return numbers

def get_list_from_user_kids():
    numbers = []
    for _ in range(3):
        while True:
            try:
                user_input = int(input("Please enter three matching numbers between 0 and 20: "))
                if 0 <= user_input <= 20:
                    numbers.append(user_input)
                    break
                else:
                    print("Please enter a number between 0 and 20.")
            except ValueError:
                print("Please enter a valid integer.")
    return numbers

def get_list_from_user_easy():
    numbers = []
    for _ in range(3):
        while True:
            try:
                user_input = int(input("Please enter three matching numbers between 0 and 40: "))
                if 0 <= user_input <= 40:
                    numbers.append(user_input)
                    break
                else:
                    print("Please enter a number between 0 and 40.")
            except ValueError:
                print("Please enter a valid integer.")
    return numbers

def get_list_from_user_normal():
    numbers = []
    for _ in range(3):
        while True:
            try:
                user_input = int(input("Please enter three matching numbers between 0 and 60: "))
                if 0 <= user_input <= 60:
                    numbers.append(user_input)
                    break
                else:
                    print("Please enter a number between 0 and 60.")
            except ValueError:
                print("Please enter a valid integer.")
    return numbers

def get_list_from_user_hard():
    numbers = []
    for _ in range(3):
        while True:
            try:
                user_input = int(input("Please enter three matching numbers between 0 and 80: "))
                if 0 <= user_input <= 80:
                    numbers.append(user_input)
                    break
                else:
                    print("Please enter a number between 0 and 80.")
            except ValueError:
                print("Please enter a valid integer.")
    return numbers

def get_list_from_user_professional():
    numbers = []
    for _ in range(3):
        while True:
            try:
                user_input = int(input("Please enter three matching numbers between 0 and 100: "))
                if 0 <= user_input <= 100:
                    numbers.append(user_input)
                    break
                else:
                    print("Please enter a number between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer.")
    return numbers

def is_list_equal(user_numbers, generated_sequence):
    return user_numbers == generated_sequence

#if __name__ == "__main__":
def me_memo(generate_func, get_list_func):
    generated_sequence = generate_func()
    print(f"Generated numbers: {generated_sequence}")
    # time.sleep(1)
    print("Time's up! Numbers will disappear now.")
    screen_cleaner()

    user_numbers = get_list_func()
    print(f"You entered: {user_numbers}")

    if is_list_equal(user_numbers, generated_sequence):
        print("You guessed the number correctly, you win!")
        return True
    else:
        print("You guessed the number incorrectly, you lose!")
        return False


if __name__ == "__main__":

    me_memo(generate_sequence_kids, get_list_from_user_kids)
    me_memo(generate_sequence_easy, get_list_from_user_easy)
    me_memo(generate_sequence_normal, get_list_from_user_normal)
    me_memo(generate_sequence_hard, get_list_from_user_hard)
    me_memo(generate_sequence_professional, get_list_from_user_professional)

