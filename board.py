import chess
import numpy as np
# from numpy.random import default_rng
# rng = default_rng()


def play_chess(color): # randomly playing against itself
    board = chess.Board()

    if color == "white": # human color
        ai_turn = False
    else:
        ai_turn = True

    step = 0
    is_stop = False
    while True:
        if board.is_game_over():
            break 
        
        if board.turn == ai_turn:
            move = np.random.choice(list(board.legal_moves))
            board.push(move)
        else:
            while True:
                move = input("Enter your move: \n")
                if move == "break":
                    is_stop = True
                    break
                try:
                    board.push_san(move)
                    break
                except ValueError:
                    print("Not a valid move, try another move.")
        if is_stop:
            break
        print(board)
        print()
        step += 1
        
    print(board)
    print(step)

