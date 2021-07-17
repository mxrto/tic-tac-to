#tic-tac-to
import random
import time

def print_scoreboard():
    print(f"{game_board[0]}  {game_board[1]}  {game_board[2]}\n{game_board[3]}  {game_board[4]}  {game_board[5]}\n{game_board[6]}  {game_board[7]}  {game_board[8]}")    

def check_win(board, i):
    if board[0] == i and board[1] == i and board[2] == i:
        return False

    elif board[3] == i and board[4] == i and board[5] == i:
        return False

    elif board[6] == i and board[7] == i and board[8] == i:
        return False

    elif board[0] == i and board[3] == i and board[6] == i:
        return False

    elif board[1] == i and board[4] == i and board[7] == i:
        return False

    elif board[2] == i and board[5] == i and board[8] == i:
        return False
    
    elif board[0] == i and board[4] == i and board[8] == i:
        return False

    elif board[2] == i and board[4] == i and board[6] == i:
        return False
    else:
        return True

def rand_com():
    return random.randint(0, 8)


game_board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

game_is_on = True
while game_is_on:
    user = int(input("Enter a location: "))
    com = rand_com()

    game_board[user] = "X"
    game_is_on = check_win(game_board, "X")
    print_scoreboard()

    print("\n")

    while game_board[com] != "_":
        com = rand_com()
    
    game_board[com] = "0"
    game_is_on = check_win(game_board, "0")
    print_scoreboard()




