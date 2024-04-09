import random

class life:
    def __init__(self, size, height):
        self.field = [[0] * size for i in range(height)]

    def initialize(self, life_fraction):
        for y in range (1, len(self.field) - 1):
            for x in range (1, len(self.field[0]) - 1):
                if random.randint(1, 100) <= life_fraction:
                    self.field[y][x] = 1
    def run_transition_rule(self):
        buffer_field = [[0] * len(self.field[0]) for i in range (len(self.field))]
        for y in range (1, len(self.field) - 1):
            for x in range (1, len(self.field[0]) - 1):
                living_neighbors = 0
                for dy in range (-1, 2):
                    for dx in range (-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if self.field [y + dy][x + dx] == 1:
                            living_neighbors += 1
                if living_neighbors < 2 or living_neighbors > 3:
                    buffer_field[y][x] = 0
                elif living_neighbors == 3:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]
        for y in range (1, len(self.field) - 1):
            for x in range (1, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]