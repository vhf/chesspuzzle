from __future__ import print_function
import chess
from pprint import pprint
from collections import defaultdict

import subprocess, time


def tree():
    return defaultdict(tree)

puzzle_1 = "k7/pp6/8/8/8/8/8/3R3K w - - 0 1"


def generate_move_tree(fen, depth=0):
    board = chess.Bitboard(fen)

    move_tree = tree()
    move_tree[fen]

    if depth < 1:
        for move in board.legal_moves:
            board.push(move)
            move_tree[fen][generate_move_tree(board.fen(), depth+1)]
            board.pop()

generate_move_tree(puzzle_1)



engine = subprocess.Popen(
    '/usr/games/stockfish',
    universal_newlines=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

def put(command):
    print('\nyou:\n\t'+command)
    engine.stdin.write(command+'\n')

def get():
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
    engine.stdin.write('isready\n')
    print('\nengine:')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'readyok':
            break
        if text != '':
            if 'bestmove' in text:
                print('\t'+text)

get()
put('position fen k7/pp6/8/8/8/8/8/3R3K w - - 0 80')
get()
put('go movetime 500')
get()
put('setoption name Hash value 1024')
get()
put('quit')
