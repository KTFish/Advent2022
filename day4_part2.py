from day4 import clean_line


def check_any_overlaps(line):
    a_low, a_high, b_low, b_high = clean_line(line)
    if b_low <= a_low <= b_high:
        return 1
    elif a_low <= b_low <= a_high:
        return 1
    elif b_low <= a_high <= b_high:
        return 1
    elif a_low <= b_high <= a_high:
        return 1
    return 0


overlaps = 0
with open('data/input4.txt') as f:
    line = f.readline().strip()
    while line:
        overlaps += check_any_overlaps(line)
        line = f.readline().strip()
print(f'Answer 2: {overlaps}')
