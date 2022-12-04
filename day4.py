overlaps = 0


def clean_line(line):
    a_low, a_high = line.split(',')[0].split('-')
    b_low, b_high = line.split(',')[1].split('-')
    return int(a_low), int(a_high), int(b_low), int(b_high)


def check_overlaps(line):
    a_low, a_high, b_low, b_high = clean_line(line)
    print(a_low, a_high, b_low, b_high)
    if b_low >= a_low and b_high <= a_high:
        return 1
    elif a_low >= b_low and a_high <= b_high:
        return 1
    else:
        return 0


with open('data/input4.txt') as f:
    line = f.readline().strip()
    while line:
        overlaps += check_overlaps(line)
        line = f.readline().strip()
print(f'Answer 1: {overlaps}')
