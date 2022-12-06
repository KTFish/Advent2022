# Advent of Code 2022 - Day 6

def is_marker(letters):
    return len(letters) == len(set(letters)) == 4


def is_message(letters):
    return len(letters) == len(set(letters)) == 14


# PART 1
with open('data/input6.txt') as f:
    signal = f.readline().strip()
    while signal:
        l, r = 0, 4
        probe = signal[l:r]
        while not is_marker(probe):
            l, r = l + 1, r + 1
            probe = signal[l:r]
        signal = f.readline().strip()
print(f'Answer 1: {r}')

# PART 2
with open('data/input6.txt') as f:
    signal = f.readline().strip()
    while signal:
        l, r = 0, 14
        probe = signal[l:r]
        while not is_message(probe):
            l, r = l + 1, r + 1
            probe = signal[l:r]
        signal = f.readline().strip()
print(f'Answer 2: {r}')
