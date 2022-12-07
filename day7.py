from collections import defaultdict

testing = False

data = []
with open('data/test7.txt' if testing else 'data/input7.txt') as f:
    line = f.readline().strip()
    while line:
        data.append(line.split())
        line = f.readline().strip()

sizes = defaultdict(int)
path = []
for words in data:
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] != 'ls' and words[0] != 'dir':
        size = int(words[0])
        for k in range(len(path) + 1):  # Add size of current directory to all parents!
            sizes['/'.join(path[:k])] += size

res = 0
for size in sizes.values():
    if size <= 100_000:
        res += size
print(f'Answer 1: {res}')

# Part 2
occupied_space = sizes['/']
candidate, cand_size = None, occupied_space
for directory, size in sizes.items():
    if 70000000 - occupied_space + size >= 30000000 and size <= cand_size:
        candidate, cand_size = directory, size

print(f'Answer 2: {cand_size}')
