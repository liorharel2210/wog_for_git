import random
#from app import start_play
###Please note the reson that i named my file in this why is
# that for some reason pycharm can't locate the file when there is space or special characters.
#im using mac m1 with sonoma 14 os
#import app
#app.start_play()
#def play():
def generate_number_kids():
    random_number_kids = random.randint(0, 10)
    selected_number_kids = random_number_kids
    return selected_number_kids


def generate_number_easy():
    random_number_easy = random.randint(0, 20)
    selected_number_easy = random_number_easy
    return selected_number_easy

def generate_number_normal():
    random_number_normal = random.randint(0, 30)
    selected_number_normal = random_number_normal
    return selected_number_normal

def generate_number_hard():
    random_number_hard = random.randint(0, 40)
    selected_number_hard = random_number_hard
    return selected_number_hard

def generate_number_professional():
    random_number_professional = random.randint(0, 50)
    selected_number_professional = random_number_professional
    return selected_number_professional

def get_guess_from_user_kids():
    user_guess_kids = int(input("Please enter a number between 0 and 10"))
    user_selected_number_kids = user_guess_kids
    return user_selected_number_kids

def get_guess_from_user_easy():
    user_guess_easy = int(input("Please enter a number between 0 and 20"))
    user_selected_number_easy = user_guess_easy
    return user_selected_number_easy

def get_guess_from_user_normal():
    user_guess_normal = int(input("Please enter a number between 0 and 30"))
    user_selected_number_normal = user_guess_normal
    return user_selected_number_normal

def get_guess_from_user_hard():
    user_guess_hard = int(input("Please enter a number between 0 and 40"))
    user_selected_number_hard = user_guess_hard
    return user_selected_number_hard

def get_guess_from_user_professional():
    user_guess_professional = int(input("Please enter a number between 0 and 50"))
    user_selected_number_professional = user_guess_professional
    return user_selected_number_professional

def compare_results():
    def compare_results_kids():
        res_from_generate_number_kids = generate_number_kids()
        res_from_get_guess_from_user_kids = get_guess_from_user_kids()
        if res_from_generate_number_kids == res_from_get_guess_from_user_kids:
            print("You guessed the number correctly, you win!")
        else:
            print("You guessed the number incorrectly, you lose!")
    def compare_results_easy():
        res_from_generate_number_easy = generate_number_easy()
        res_from_get_guess_from_user_easy = get_guess_from_user_easy()
        if res_from_generate_number_easy == res_from_get_guess_from_user_easy:
            print("You guessed the number correctly, you win!")
        else:
            print("You guessed the number incorrectly, you lose!")
    def compare_results_normal():
        res_from_generate_number_normal = generate_number_normal()
        res_from_get_guess_from_user_normal = get_guess_from_user_normal()
        if res_from_generate_number_normal == res_from_get_guess_from_user_normal:
            print("You guessed the number correctly, you win!")
        else:
            print("You guessed the number incorrectly, you lose!")
    def compare_results_hard():
        res_from_generate_number_hard = generate_number_hard()
        res_from_get_guess_from_user_hard = get_guess_from_user_hard()
        if res_from_generate_number_hard == res_from_get_guess_from_user_hard:
            print("You guessed the number correctly, you win!")
        else:
            print("You guessed the number incorrectly, you lose!")
    def compare_results_professional():
        res_from_generate_number_professional = generate_number_professional()
        res_from_get_guess_from_user_professional = get_guess_from_user_professional()
        if res_from_generate_number_professional == res_from_get_guess_from_user_professional:
            print("You guessed the number correctly, you win!")
        else:
            print("You guessed the number incorrectly, you lose!")

def play():
    generate_number_kids()
    get_guess_from_user_kids()
    compare_results(compare_results_kids)


#    compare_results()