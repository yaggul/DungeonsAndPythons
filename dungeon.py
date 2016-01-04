from copy import deepcopy
from random import choice


class Dungeon:

    def __init__(self, map_level_file):
            self.level = map_level_file
            self.x_coord = 0
            self.y_coord = 0
            self.map_string = ''
            self.map_matrix = []
            self.map_walkable = ['E', 'T', '+', 'G']
            self.previous_location = []
            self.next_location = []
            self.map_entrance = []
            self.treasure_items = ['health_potion', 'mana_potion', 'weapon', 'spell']

    def gen_map_matrix(self):
        b = []
        with open(self.level, 'r') as map2filein:
            for i in map2filein.readlines():
                for j in i[:-1]:
                    b.append(j)
                self.map_matrix.append(b)
                b = []

    def gen_map_string(self):
        self.map_string = '\n'.join([''.join(x) for x in self.map_matrix])

    def __str__(self):
        return '{}'.format(self.map_string)

    def __repr__(self):
        return '{}'.format(self.map_string)

    def print_map(self, map=''):
        return self

    def move_hero(self, direction):
        if direction == 'up':
            if self.go_up():
                self.clear_trace(*self.previous_location)
                self.move()
                self.previous_location = deepcopy(self.next_location)
                return True
            else:
                return False
        elif direction == 'down':
            if self.go_down():
                self.clear_trace(*self.previous_location)
                self.move()
                self.previous_location = deepcopy(self.next_location)
                return True
            else:
                return False
        elif direction == 'left':
            if self.go_left():
                self.clear_trace(*self.previous_location)
                self.move()
                self.previous_location = deepcopy(self.next_location)
                return True
            else:
                return False
        elif direction == 'right':
            if self.go_right():
                self.clear_trace(*self.previous_location)
                self.move()
                self.previous_location = deepcopy(self.next_location)
                return True
            else:
                return False

    def move(self):
        self.map_matrix[self.y_coord][self.x_coord] = 'H'
        self.gen_map_string()

    def is_walkable(self, x, y):
        if self.map_matrix[y][x] in self.map_walkable:
            return True
        else:
            return False

    def go_up(self):
        if self.y_coord - 1 >= 0:
            if self.is_walkable(self.x_coord, self.y_coord - 1):
                self.y_coord -= 1
                self.save_next_location()
                # self.save_last_location()
                return True
            else:
                return False
        else:
            return False

    def go_down(self):
        if self.y_coord + 1 <= len(self.map_matrix) - 1:
            if self.is_walkable(self.x_coord, self.y_coord + 1):
                self.y_coord += 1
                self.save_next_location()
                # self.save_last_location()
                return True
            else:
                return False
        else:
            return False

    def go_left(self):
        if self.x_coord - 1 >= 0:
            if self.is_walkable(self.x_coord - 1, self.y_coord):
                self.x_coord -= 1
                self.save_next_location()
                # self.save_last_location()
                return True
            else:
                return False
        else:
            return False

    def go_right(self):
        if self.x_coord + 1 <= len(self.map_matrix[0]):
            if self.is_walkable(self.x_coord + 1, self.y_coord):
                self.x_coord += 1
                self.save_next_location()
                # self.save_last_location()
                return True
            else:
                return False
        else:
            return False

    def save_last_location(self):
        self.previous_location = [self.y_coord, self.x_coord, self.map_matrix[self.y_coord][self.x_coord]]

    def save_next_location(self):
        self.next_location = [self.y_coord, self.x_coord, self.map_matrix[self.y_coord][self.x_coord]]

    def spawn(self, coords):
        self.y_coord, self.x_coord = coords[:]
        self.save_last_location()
        self.move()
        return True

    def clear_trace(self, *args):
        self.map_matrix[args[0]][args[1]] = args[2]

    def find_map_start(self):
        for i in self.map_matrix:
            for j in i:
                if j == 'S':
                    self.map_entrance = [self.map_matrix.index(i), i.index(j)]
                    return True
                else:
                    pass
        return False

    def pick_item(self, *args):
        return choice(self.treasure_items)
