class Map(object):
    def __init__(self):
        print('Insert values (5 integeres per line separated by space):')
        self.map = []
        self.steps = []

        for i in range(5):
            line = input()
            line_list = []
            for num in line.split(' '):
                line_list.append(int(num))
            self.map.append(line_list)

    def find_treasure(self, first_clue):
        clue = (first_clue // 10,
                first_clue % 10,
                self.map[(first_clue // 10) - 1][(first_clue % 10) - 1])

        if self.step(clue, 100):
            for s in self.steps:
                print(s)
        else:
            print("NO TREASURE")

    def step(self, clue, timeout):
        self.steps.append(str(clue[0]) + " " + str(clue[1]))

        if timeout == 0:
            return False

        if (clue[0] * 10 + clue[1]) == clue[2]:
            return True
        else:
            row = clue[2] // 10
            col = clue[2] % 10

            value = self.map[row - 1][col - 1]

            return self.step((row, col, value), timeout - 1)
