#tic-tac-to
import random


def com_rand():
    com_choice = [random.randint(0, 2), random.randint(0, 2)]
    return com_choice


def user_input():
    user = input("Enter your row and line: ")
    user_choice = []

    for _ in user:
        user_choice.append(int(_))
    
    return user_choice

def check_win(i):
    game_over = False

    for row in rows:
        for item in row:
            print(item)
            print(i)
            if item != i:
                game_over = True
                
    
    return game_over
            




row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]

rows = [row1, row2, row3]

game_is_on = True

while game_is_on:


    com_choice = com_rand()
    user_choice = user_input()

    if "_" in rows[user_choice[0] - 1][user_choice[1] - 1]:
        rows[user_choice[0] - 1][user_choice[1] - 1] = "X"
        game_is_on = check_win(i="X")
        print(game_is_on)

    if "_" in rows[com_choice[0]][com_choice[1]]:
        rows[com_choice[0]][com_choice[1]] = "0"
        game_is_on = check_win(i="0")
        print(game_is_on)

    for row in rows:
        print(f"\n{row}")