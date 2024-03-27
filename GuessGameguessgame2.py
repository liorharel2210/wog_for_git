import random

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
    user_guess_kids = input("Please enter a number between 0 and 10: ")

    if user_guess_kids.isdigit():
        user_selected_number_kids = int(user_guess_kids)

        if 0 <= user_selected_number_kids <= 10:
            return user_selected_number_kids
        else:
            print("Not supported. Please enter a number between 0 and 10.")
            return get_guess_from_user_kids()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_guess_from_user_kids()

def get_guess_from_user_easy():
    user_guess_easy = input("Please enter a number between 0 and 20: ")

    if user_guess_easy.isdigit():
        user_selected_number_easy = int(user_guess_easy)

        if 0 <= user_selected_number_easy <= 20:
            return user_selected_number_easy
        else:
            print("Not supported. Please enter a number between 0 and 20.")
            return get_guess_from_user_easy()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_guess_from_user_easy()

def get_guess_from_user_normal():
    user_guess_normal = input("Please enter a number between 0 and 30: ")

    if user_guess_normal.isdigit():
        user_selected_number_normal = int(user_guess_normal)

        if 0 <= user_selected_number_normal <= 30:
            return user_selected_number_normal
        else:
            print("Not supported. Please enter a number between 0 and 30.")
            return get_guess_from_user_normal()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_guess_from_user_normal()

def get_guess_from_user_hard():
    user_guess_hard = input("Please enter a number between 0 and 40: ")

    if user_guess_hard.isdigit():
        user_selected_number_hard = int(user_guess_hard)

        if 0 <= user_selected_number_hard <= 40:
            return user_selected_number_hard
        else:
            print("Not supported. Please enter a number between 0 and 40.")
            return get_guess_from_user_hard()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_guess_from_user_hard()

def get_guess_from_user_professional():
    user_guess_professional = input("Please enter a number between 0 and 50: ")

    if user_guess_professional.isdigit():
        user_selected_number_professional = int(user_guess_professional)

        if 0 <= user_selected_number_professional <= 50:
            return user_selected_number_professional
        else:
            print("Not supported. Please enter a number between 0 and 50.")
            return get_guess_from_user_professional()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_guess_from_user_professional()

def compare_results(compare_function):
    res_from_generate_number = compare_function()
    res_from_get_guess_from_user = get_guess_from_user_kids()

    if res_from_generate_number == res_from_get_guess_from_user:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results2(compare_function2):
    res_from_generate_number2 = compare_function2()
    res_from_get_guess_from_user2 = get_guess_from_user_easy()

    if res_from_generate_number2 == res_from_get_guess_from_user2:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results3(compare_function3):
    res_from_generate_number3 = compare_function3()
    res_from_get_guess_from_user3 = get_guess_from_user_normal()

    if res_from_generate_number3 == res_from_get_guess_from_user3:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results4(compare_function4):
    res_from_generate_number4 = compare_function4()
    res_from_get_guess_from_user4 = get_guess_from_user_hard()

    if res_from_generate_number4 == res_from_get_guess_from_user4:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results5(compare_function5):
    res_from_generate_number5 = compare_function5()
    res_from_get_guess_from_user5 = get_guess_from_user_professional()

    if res_from_generate_number5 == res_from_get_guess_from_user5:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")


def compare_results_kids():
    return generate_number_kids()

def compare_results_easy():
    return generate_number_easy()

def compare_results_normal():
    return generate_number_normal()

def compare_results_hard():
    return generate_number_hard()

def compare_results_professional():
    return generate_number_professional()

def play():
    compare_results(compare_results_kids)

def play2():
    compare_results2(compare_results_easy)

def play3():
    compare_results3(compare_results_normal)

def play4():
    compare_results4(compare_results_hard)

def play5():
    compare_results5(compare_results_professional)

if __name__ == "__main__":
    play()
    play2()
    play3()
    play4()
    play5()
