from __future__ import print_function
import chess
from pprint import pprint

board = chess.Bitboard("k7/pp6/8/8/8/8/8/3R3K w - - 0 1")


for move in board.legal_moves:
    pprint(move)
    board.push(move)
    print(board.fen())
    board.pop()
