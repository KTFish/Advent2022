def get_instructions(line):
    instructions = line.split()
    return int(instructions[1]), int(instructions[3]) - 1, int(instructions[5]) - 1


stacks = [
    ['N', 'S', 'D', 'C', 'V', 'Q', 'T'],
    ['M', 'F', 'V'],
    ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],
    ['D', 'Q', 'R', 'T', 'F'],
    ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'],
    ['C', 'F', 'G', 'N', 'P', 'W', 'Q'],
    ['W', 'F', 'R', 'L', 'T', 'C'],
    ['T', 'Z', 'N', 'S'],
    ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']
]

# PART 1
with open('data/input5.txt') as f:
    line = f.readline().strip()
    while line:
        num_of_crates, source, destination = get_instructions(line)
        for _ in range(num_of_crates):
            elem = stacks[source].pop()
            stacks[destination].append(elem)
        line = f.readline().strip()
    answer = ''
    for stack in stacks:
        answer += stack.pop()
print(f'Answer 1: {answer}')

# PART 2
stacks = [
    ['N', 'S', 'D', 'C', 'V', 'Q', 'T'],
    ['M', 'F', 'V'],
    ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],
    ['D', 'Q', 'R', 'T', 'F'],
    ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'],
    ['C', 'F', 'G', 'N', 'P', 'W', 'Q'],
    ['W', 'F', 'R', 'L', 'T', 'C'],
    ['T', 'Z', 'N', 'S'],
    ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']
]

with open('data/input5.txt') as f:
    # stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    # with open('data/test5.txt') as f:
    line = f.readline().strip()
    while line:
        num_of_crates, source, destination = get_instructions(line)
        if num_of_crates > 1:  # Move multiple
            # stacks[destination] += stacks[source][-num_of_crates]
            # print(num_of_crates)

            moved = stacks[source][-num_of_crates:]
            stacks[source] = stacks[source][:-num_of_crates]
            for elem in moved:
                stacks[destination].append(elem)
            # print(stacks)

        else:  # Move a single one
            elem = stacks[source].pop()
            stacks[destination].append(elem)

        line = f.readline().strip()
    answer = []
    for stack in stacks:
        answer.append(stack.pop())
    answer = ''.join(answer)
print(f'Answer 2: {answer}')
