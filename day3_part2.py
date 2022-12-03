result = 0
priority = {chr(x + 64): x + 26 for x in range(1, 27)} | {chr(x + 96): x for x in range(1, 27)}

with open('./data/input3.txt') as f:
    rucksack = f.readline().replace('\n', '')
    lines = 1
    rucksacks = [rucksack]
    while rucksack:
        while lines < 3:
            rucksack = f.readline().replace('\n', '')
            rucksacks.append(rucksack)
            lines += 1
        for item_type in rucksacks[0]:
            if item_type in rucksacks[1] and item_type in rucksacks[2]:
                if item_type in priority.keys():
                    result += priority[item_type]
                break
        rucksack = f.readline().replace('\n', '')
        rucksacks = [rucksack]
        lines = 1
print(f'Answer 2: {result}')
# Answer 2: 2760
