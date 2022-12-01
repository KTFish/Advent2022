def part_one() -> None:
    max_calories = 0
    with open('./data/input1.txt') as file:
        line = file.readline()
        curr = 0
        while line:
            line = file.readline()
            if line == '\n':
                max_calories = max(curr, max_calories)
                curr = 0
            elif line.strip().isnumeric():
                curr += int(line)

    print(f'Answer 1: {max_calories}')


def part_two() -> None:
    best_elves = [0, 0, 0]
    with open('./data/input1.txt') as file:
        line = file.readline()
        curr = 0
        while line:
            line = file.readline()
            if line == '\n':
                if best_elves[0] < curr:
                    best_elves[0], best_elves[1], best_elves[2] = curr, best_elves[0], best_elves[1]
                elif best_elves[1] < curr:
                    best_elves[1], best_elves[2] = curr, best_elves[1]
                elif best_elves[2] < curr:
                    best_elves[2] = curr
                curr = 0
                print(best_elves)
            elif line.strip().isnumeric():
                curr += int(line)
    print(f'Answer 2: {sum(best_elves)}')


part_one()
part_two()
