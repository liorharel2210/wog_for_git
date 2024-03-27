import GuessGameguessgame2
from GuessGameguessgame2 import play, play2, play3, play4, play5
import CurrencyRouletteGamecurrencyroulettegame
from CurrencyRouletteGamecurrencyroulettegame import play_cu, play_cu2, play_cu3, play_cu4, play_cu5
import MemoryGame_memory_game
from MemoryGame_memory_game import me_memo, generate_sequence_kids, get_list_from_user_kids, generate_sequence_easy, get_list_from_user_easy, generate_sequence_normal, get_list_from_user_normal, generate_sequence_hard, get_list_from_user_hard, generate_sequence_professional, get_list_from_user_professional
from Score_utils_file_score import add_score
import Utils_file_utils

def welcome():
    uname = str(input("Please enter your name: "))
    return uname

username = welcome()

print(f'Hi {username} and welcome to the world of games: The Epic Journey ')

def start_play():
    select = input("Please choose a game to play:\n 1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n 2.Guess Game - guess a number and see if you chose like the computer.\n 3.Currency Roulette - try and guess the value of a random amount USD in ILS.\n Your selection is: ")

    game_menu = ['Memory Game', 'Guess Game', 'Currency Roulette']

    if not select.isdigit() or int(select) < 1 or int(select) > len(game_menu):
        print('Not supported, Please choose again ')
        return start_play()

    game_level = input("Please select difficulty level:\n 1.Kids\n 2.Easy\n 3.Normal\n 4.Hard\n 5.Professional\n Your selection is: ")
    game_level_diff = ['Kids', 'Easy', 'Normal', 'Hard', 'Professional']

    if not game_level.isdigit() or int(game_level) < 1 or int(game_level) > len(game_level_diff):
        print('Not supported, Return to the main menu and choose again ')
        return start_play()

    user_won = True

    if user_won:
        game_name, difficulty_level = game_menu[int(select) - 1], game_level_diff[int(game_level) - 1]
        add_score(difficulty_level)  # Call add_score when the user wins

    return game_menu[int(select) - 1], game_level_diff[int(game_level) - 1]

def guess_game2(game, level):
    #game, level = start_play()
    if game == 'Guess Game' and level == 'Kids':
        GuessGameguessgame2.play()

def guess_game3(game, level):
    #game3, level3 = start_play()
    if game == 'Guess Game' and level == 'Easy':
        GuessGameguessgame2.play2()

def guess_game4(game, level):
    #game3, level3 = start_play()
    if game == 'Guess Game' and level == 'Normal':
        GuessGameguessgame2.play3()

def guess_game5(game, level):
    #game3, level3 = start_play()
    if game == 'Guess Game' and level == 'Hard':
        GuessGameguessgame2.play4()

def guess_game6(game, level):
    #game3, level3 = start_play()
    if game == 'Guess Game' and level == 'Professional':
        GuessGameguessgame2.play5()


def currency_game2(gamecur, levelcur):
    #game3, level3 = start_play()
    if gamecur == 'Currency Roulette' and levelcur == 'Kids':
        CurrencyRouletteGamecurrencyroulettegame.play_cu()

def currency_game3(gamecur, levelcur):
    #game3, level3 = start_play()
    if gamecur == 'Currency Roulette' and levelcur == 'Easy':
        CurrencyRouletteGamecurrencyroulettegame.play_cu2()

def currency_game4(gamecur, levelcur):
    #game3, level3 = start_play()
    if gamecur == 'Currency Roulette' and levelcur == 'Normal':
        CurrencyRouletteGamecurrencyroulettegame.play_cu3()

def currency_game5(gamecur, levelcur):
    #game3, level3 = start_play()
    if gamecur == 'Currency Roulette' and levelcur == 'Hard':
        CurrencyRouletteGamecurrencyroulettegame.play_cu4()

def currency_game6(gamecur, levelcur):
    #game3, level3 = start_play()
    if gamecur == 'Currency Roulette' and levelcur == 'Professional':
        CurrencyRouletteGamecurrencyroulettegame.play_cu5()

def memo_game_kids():
    MemoryGame_memory_game.me_memo(generate_sequence_kids, get_list_from_user_kids)

def memo_game_easy():
    MemoryGame_memory_game.me_memo(generate_sequence_easy, get_list_from_user_easy)

def memo_game_normal():
    MemoryGame_memory_game.me_memo(generate_sequence_normal, get_list_from_user_normal)

def memo_game_hard():
    MemoryGame_memory_game.me_memo(generate_sequence_hard, get_list_from_user_hard)

def memo_game_professional():
    MemoryGame_memory_game.me_memo(generate_sequence_professional, get_list_from_user_professional)


if __name__ == "__main__":
    game_choice, level_choice = start_play()

    if game_choice == 'Guess Game':
        if level_choice == 'Kids':
            guess_game2(game_choice, level_choice)
        elif level_choice == 'Easy':
            guess_game3(game_choice, level_choice)
        elif level_choice == 'Normal':
            guess_game4(game_choice, level_choice)
        elif level_choice == 'Hard':
            guess_game5(game_choice, level_choice)
        elif level_choice == 'Professional':
            guess_game6(game_choice, level_choice)


    elif game_choice == 'Currency Roulette':
        if level_choice == 'Kids':
            currency_game2(game_choice, level_choice)
        elif level_choice == 'Easy':
            currency_game3(game_choice, level_choice)
        elif level_choice == 'Normal':
            currency_game4(game_choice, level_choice)
        elif level_choice == 'Hard':
            currency_game5(game_choice, level_choice)
        elif level_choice == 'Professional':
            currency_game6(game_choice, level_choice)

    elif game_choice == 'Memory Game':
        if level_choice == 'Kids':
            memo_game_kids()
        elif level_choice == 'Easy':
            memo_game_easy()
        elif level_choice == 'Normal':
            memo_game_normal()
        elif level_choice == 'Hard':
            memo_game_hard()
        elif level_choice == 'Professional':
            memo_game_professional()
