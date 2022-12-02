# A/X for Rock +1 point
# B/Y for Paper +2 points
# C/Z for Scissors +3 points

def play(your_move, opponents_move):
    """
    Simulates playing one round with the given rules and returns your score.
    """
    if your_move == 'X':
        if opponents_move == 'A':
            return 4
        elif opponents_move == 'B':
            return 1
        else:
            return 7
    elif your_move == 'Y':
        if opponents_move == 'A':
            return 8
        elif opponents_move == 'B':
            return 5
        else:
            return 2
    elif your_move == 'Z':
        if opponents_move == 'A':
            return 3
        elif opponents_move == 'B':
            return 9
        else:
            return 6


total = 0
with open('data/input2.txt') as f:
    line = f.readline()
    while line:
        opponents_move, your_move = line.split()
        total += play(your_move, opponents_move)
        line = f.readline()
print(f'Answer 1: {total}')
