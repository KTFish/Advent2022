# A for Rock +1 point
# B for Paper +2 points
# C for Scissors +3 points

# X for Loose
# Y for end in a Draw
# Z for Win

def play(your_move, opponents_move):
    if your_move == 'X':  # Need to loose
        if opponents_move == 'A':
            return 3
        elif opponents_move == 'B':
            return 1
        else:
            return 2
    elif your_move == 'Y':
        if opponents_move == 'A':
            return 4
        elif opponents_move == 'B':
            return 5
        else:
            return 6
    elif your_move == 'Z':
        if opponents_move == 'A':
            return 8
        elif opponents_move == 'B':
            return 9
        else:
            return 7


total = 0
with open('data/input2.txt') as f:
    line = f.readline()
    while line:
        opponents_move, your_move = line.split()
        total += play(your_move, opponents_move)
        line = f.readline()
print(f'Answer 2: {total}')
