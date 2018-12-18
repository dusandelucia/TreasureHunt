from functional_approach.read_map import read

print('Treasure Hunt: Functional approach')
print('----------------------------------')


def get_first_clue(treasure_map, first_clue):
    row = first_clue // 10
    col = first_clue % 10

    value = treasure_map[row - 1][col - 1]

    return row, col, value


def step(treasure_map, clue):
    row = clue[2] // 10
    col = clue[2] % 10

    value = treasure_map[row - 1][col - 1]

    return row, col, value


def check_current(clue):
    if (clue[0] * 10 + clue[1]) == clue[2]:
        return True
    else:
        return False


first_clue = 11

treasure_map = read()

clue = get_first_clue(treasure_map, first_clue)

step_no = 1
timeout = 100

steps = []

while check_current(clue) is False and step_no <= timeout:
    steps.append(str(clue[0]) + " " + str(clue[1]))
    clue = step(treasure_map, clue)
    step_no += 1

if step_no <= timeout:
    for s in steps:
        print(s)
    print(str(clue[0]) + " " + str(clue[1]))
else:
    print("NO TREASURE")
