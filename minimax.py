import math
from numpy import Infinity


def minimax(board, is_maximizing, player_that_should_win, player_that_should_lose):
    player_should_win_result = check_for_win(player_that_should_win, board)
    player_should_lose_result = check_for_win(player_that_should_lose, board)

    if (
        player_should_win_result == player_that_should_win or
        player_should_lose_result == player_that_should_lose or 
        player_should_win_result == 1
    ):
        if (player_should_win_result == player_that_should_win):
            score = 1
        elif (player_should_lose_result == player_that_should_lose):
            score = -1
        elif (player_should_win_result == 1):
            score = 0
        return score

    if is_maximizing:
        best_score = -Infinity
        for position in available_positions(board):
            board[position] = player_that_should_win
            score = minimax(board, False, player_that_should_win, player_that_should_lose)
            board[position] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = Infinity
        for position in available_positions(board):
            board[position] = player_that_should_lose
            score = minimax(board, True, player_that_should_win, player_that_should_lose)
            board[position] = ' '
            best_score = min(score, best_score)
        return best_score


def print_board(board):
    print()
    print(f" {board[1]} | {board[2]} | {board[3]}   1 2 3\n")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]}   4 5 6\n")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]}   7 8 9\n")
    print()

def available_positions(board):
    available = []
    for i in range(1, len(board)):
        if board[i] == ' ':
            available.append(i)
    return available

def input_is_valid(position, board):
    valid_inputs = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    if len(position) == 1:
        if position in valid_inputs:
            if int(position) in available_positions(board):
                return 1
            else:
                return -1
        else:
            return 0
    else:
        return 0

def check_for_win(identifier, board):
    if (
        board[1] == identifier and board[2] == identifier and board[3] == identifier or \
        board[4] == identifier and board[5] == identifier and board[6] == identifier or \
        board[7] == identifier and board[8] == identifier and board[9] == identifier or \
        board[1] == identifier and board[4] == identifier and board[7] == identifier or \
        board[2] == identifier and board[5] == identifier and board[8] == identifier or \
        board[3] == identifier and board[6] == identifier and board[9] == identifier or \
        board[1] == identifier and board[5] == identifier and board[9] == identifier or \
        board[3] == identifier and board[5] == identifier and board[7] == identifier
    ):
        return identifier
    elif len(available_positions(board)) == 0:
        return 1
    else:
        return 0

def main():
    board = [ ' ' for _ in range(10) ]

    while True:
        # Player 1 Turn
        print_board(board)
        position = input("What is X's move? (1-9)\n> ")
        while True:
            if input_is_valid(position, board) == 1:
                break
            elif input_is_valid(position, board) == -1:
                print("That position is not free.")
            else:
                print("Invalid input.")
            position = input("What is X's move? (1-9)\n> ")
        board[int(position)] = 'X'

        result = check_for_win('X', board)
        if result == 'X':
            print_board(board)
            print("X wins!")
            print("Thanks for playing!")
            break
        elif result == 1:
            print_board(board)
            print("The game is a tie!")
            print("Thanks for playing!")
            break

        # Computer Turn
        print_board(board)

        best_score = -math.inf
        best_move = None
        for position in available_positions(board):
            board[position] = 'O'
            score = minimax(board, False, 'O', 'X')
            board[position] = ' '
            if score > best_score:
                best_score = score
                best_move = position

        board[best_move] = 'O'

        result = check_for_win('O', board)
        if result == 'O':
            print_board(board)
            print("O wins!")
            print("Thanks for playing!")
            break
        elif result == 1:
            print_board(board)
            print("The game is a tie!")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

