result = 0
priority = {chr(x + 64): x + 26 for x in range(1, 27)} | {chr(x + 96): x for x in range(1, 27)}
get_compartments = lambda backpack: (backpack[:len(backpack) // 2], backpack[len(backpack) // 2:])


with open('./data/input3.txt') as f:
    rucksack = f.readline()
    while rucksack:
        compartment_a, compartment_b = get_compartments(rucksack)
        for item_type in compartment_a:
            if item_type in compartment_b:
                if item_type in priority.keys():
                    result += priority[item_type]
                break
        rucksack = f.readline()
print(f'Answer 1: {result}')
# Answer 1: 7878
