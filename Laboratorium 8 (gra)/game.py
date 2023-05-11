import random

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.start = None
        self.end = None
        self.obstacles = set()
        self.generate_board()

    def generate_board(self):
        for i in range(self.width):
            for j in range(self.height):
                if i == 0 or i == self.width - 1 or j == 0 or j == self.height - 1:
                    self.obstacles.add((i, j))  # add border as obstacles
        self.start = self.generate_random_position()
        self.end = self.generate_random_position()
        while self.end == self.start:
            self.end = self.generate_random_position()
        for i in range(self.width):
            for j in range(self.height):
                if (i, j) not in self.obstacles and (i, j) != self.start and (i, j) != self.end:
                    if random.random() < 0.2:  # probability of obstacle occurrence
                        self.obstacles.add((i, j))

    def generate_random_position(self):
        x = random.randint(1, self.width - 2)
        y = random.randint(1, self.height - 2)
        return (x, y)

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacles

    def is_border(self, x, y):
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def is_valid_position(self, x, y):
        return not self.is_obstacle(x, y) and not self.is_border(x, y)

    def display(self):
        for i in range(self.width):
            for j in range(self.height):
                if (i, j) == self.start:
                    print('A', end=' ')
                elif (i, j) == self.end:
                    print('B', end=' ')
                elif (i, j) in self.obstacles:
                    print('X', end=' ')
                else:
                    print('.', end=' ')
            print()

board = Board(10, 10)
board.display()