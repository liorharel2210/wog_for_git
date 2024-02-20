import random

def gene_numb_kids():
    random_number_kids = random.randint(0, 20)
    selected_number_kids = random_number_kids
    return selected_number_kids

def gene_numb_easy():
    random_number_easy = random.randint(0, 40)
    selected_number_easy = random_number_easy
    return selected_number_easy

def gene_numb_normal():
    random_number_normal = random.randint(0, 60)
    selected_number_normal = random_number_normal
    return selected_number_normal

def gene_numb_hard():
    random_number_hard = random.randint(0, 80)
    selected_number_hard = random_number_hard
    return selected_number_hard

def gene_numb_professional():
    random_number_professional = random.randint(0, 100)
    selected_number_professional = random_number_professional
    return selected_number_professional

def money_interval_kids():
    uscurrency_kids = 3.73 * gene_numb_kids()
    uscurrency_kids_sum = uscurrency_kids
    return uscurrency_kids_sum

def money_interval_easy():
    uscurrency_easy = 3.73 * gene_numb_easy()
    uscurrency_easy_sum = uscurrency_easy
    return uscurrency_easy_sum

def money_interval_normal():
    uscurrency_normal = 3.73 * gene_numb_normal()
    uscurrency_normal_sum = uscurrency_normal
    return uscurrency_normal_sum

def money_interval_hard():
    uscurrency_hard = 3.73 * gene_numb_hard()
    uscurrency_hard_sum = uscurrency_hard
    return uscurrency_hard_sum

def money_interval_professional():
    uscurrency_professional = 3.73 * gene_numb_professional()
    uscurrency_professional_sum = uscurrency_professional
    return uscurrency_professional_sum

def get_gue_fro_user_kids():
    user_guess_kids = input("Please enter a number between 0 and 20: ")

    if user_guess_kids.isdigit():
        user_selected_number_kids = int(user_guess_kids)

        if 0 <= user_selected_number_kids <= 20:
            return user_selected_number_kids
        else:
            print("Not supported. Please enter a number between 0 and 20.")
            return get_gue_fro_user_kids()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_gue_fro_user_kids()

def get_gue_fro_user_easy():
    user_guess_easy = input("Please enter a number between 0 and 40: ")

    if user_guess_easy.isdigit():
        user_selected_number_easy = int(user_guess_easy)

        if 0 <= user_selected_number_easy <= 40:
            return user_selected_number_easy
        else:
            print("Not supported. Please enter a number between 0 and 40.")
            return get_gue_fro_user_easy()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_gue_fro_user_easy()

def get_gue_fro_user_normal():
    user_guess_normal = input("Please enter a number between 0 and 60: ")

    if user_guess_normal.isdigit():
        user_selected_number_normal = int(user_guess_normal)

        if 0 <= user_selected_number_normal <= 60:
            return user_selected_number_normal
        else:
            print("Not supported. Please enter a number between 0 and 60.")
            return get_gue_fro_user_normal()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_gue_fro_user_normal()

def get_gue_fro_user_hard():
    user_guess_hard = input("Please enter a number between 0 and 80: ")

    if user_guess_hard.isdigit():
        user_selected_number_hard = int(user_guess_hard)

        if 0 <= user_selected_number_hard <= 80:
            return user_selected_number_hard
        else:
            print("Not supported. Please enter a number between 0 and 80.")
            return get_gue_fro_user_hard()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_gue_fro_user_hard()

def get_gue_fro_user_professional():
    user_guess_professional = input("Please enter a number between 0 and 100: ")

    if user_guess_professional.isdigit():
        user_selected_number_professional = int(user_guess_professional)

        if 0 <= user_selected_number_professional <= 100:
            return user_selected_number_professional
        else:
            print("Not supported. Please enter a number between 0 and 100.")
            return get_gue_fro_user_professional()
    else:
        print("Not supported. Please enter a valid integer.")
        return get_gue_fro_user_professional()

def compare_results(compare_function):
    res_from_generate_number = compare_function()
    res_from_get_guess_from_user = get_gue_fro_user_kids()

    if res_from_generate_number == res_from_get_guess_from_user:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results2(compare_function2):
    res_from_generate_number2 = compare_function2()
    res_from_get_guess_from_user2 = get_gue_fro_user_easy()

    if res_from_generate_number2 == res_from_get_guess_from_user2:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results3(compare_function3):
    res_from_generate_number3 = compare_function3()
    res_from_get_guess_from_user3 = get_gue_fro_user_normal()

    if res_from_generate_number3 == res_from_get_guess_from_user3:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results4(compare_function4):
    res_from_generate_number4 = compare_function4()
    res_from_get_guess_from_user4 = get_gue_fro_user_hard()

    if res_from_generate_number4 == res_from_get_guess_from_user4:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_results5(compare_function5):
    res_from_generate_number5 = compare_function5()
    res_from_get_guess_from_user5 = get_gue_fro_user_professional()

    if res_from_generate_number5 == res_from_get_guess_from_user5:
        print("You guessed the number correctly, you win!")
    else:
        print("You guessed the number incorrectly, you lose!")

def compare_re_kids():
    return gene_numb_kids()

def compare_re_easy():
    return gene_numb_easy()

def compare_re_normal():
    return gene_numb_normal()

def compare_re_hard():
    return gene_numb_hard()

def compare_re_professional():
    return gene_numb_professional()

def play_cu():
    compare_results(compare_re_kids)

def play_cu2():
    compare_results2(compare_re_easy)

def play_cu3():
    compare_results3(compare_re_normal)

def play_cu4():
    compare_results4(compare_re_hard)

def play_cu5():
    compare_results5(compare_re_professional)

if __name__ == "__main__":
    play_cu()
    play_cu2()
    play_cu3()
    play_cu4()
    play_cu5()