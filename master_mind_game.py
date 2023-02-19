# mastermind game
# 10 tries to guess the code
# colors are White (W), Yellow (Y), Red (R), Green (G), Orange (O) and Blue (B)
# Game tells you correct positions and incorrect positions
# tutorial from https://youtu.be/sP-gFDreaQ4

import random
def make_code(color_list):
    code = []
    for i in range(4):
        code.append(random.choice(color_list))
    # print(code)
    return code

def guess_code(): # error checking and converting to list
    while True:
        guess = input('Guess (space seperated): ').upper().split()
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            return guess

def check_code(guess, code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for i in code:
        color_counts[i] = color_counts.get(i,0) + 1
        # print(color_counts)
    
    for guess_item, code_item in zip(guess, code): # zip creates tuple pairs
        if guess_item == code_item:
            correct_pos += 1
            color_counts[guess_item] -= 1

    for guess_item, code_item in zip(guess, code):
        if guess_item in code and color_counts[guess_item] > 0:
            incorrect_pos += 1
            color_counts[guess_item] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind. You have {TRIES} tries to guess the code....")
    print("The valid colors are:", *COLORS)
    real_code = make_code(COLORS)
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, real_code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempt} tries!")
            break

        print(f"Correct positions: {correct_pos} | Incorrect positions {incorrect_pos}")
    else:
        print("You ran out of tries, the code was:", *real_code)


if __name__ == '__main__':
    TRIES = 10
    CODE_LENGTH = 4
    COLORS = ["W", "Y", "R", "G", "B", "O"]
    game()
