from __future__ import print_function
import chess
from pprint import pprint
from collections import defaultdict

def tree():
    return defaultdict(tree)

puzzle_1 = "k7/pp6/8/8/8/8/8/3R3K w - - 0 1"


def generate_move_tree(fen, depth=0):
    board = chess.Bitboard(fen)

    move_tree = tree()
    move_tree[fen]

    if depth < 4:
        for move in board.legal_moves:
            board.push(move)
            move_tree[fen][generate_move_tree(board.fen(), depth+1)]
            board.pop()

generate_move_tree(puzzle_1)
