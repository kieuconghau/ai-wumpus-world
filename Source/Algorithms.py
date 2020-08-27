from enum import Enum
import Cell

from Specification import *

class Action(Enum):
    TURN_LEFT = 1
    TURN_RIGHT = 2
    TURN_UP = 3
    TURN_DOWN = 4
    MOVE_FORWARD = 5
    PICK_UP_GOLD = 6
    SHOOT_AN_ARROW = 7
    KILL_WUMPUS = 8
    BE_EATEN_BY_WUMPUS = 9
    FALL_INTO_PIT = 10
    KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD = 11
    CLIMB_OUT_OF_THE_CAVE = 12


class Algorithms:
    def __init__(self, map_filename):
        self.size = None
        self.cell_matrix = None
        self.agent_cell = None
        self.read_map(map_filename)


    def convert_to_standard_pos(self, pos):
        return pos[0] + 1, self.size - pos[1]


    def read_map(self, map_filename):
        file = open(map_filename, 'r')

        self.size = int(file.readline())
        raw_map = [line.split('.') for line in file.read().splitlines()]

        self.cell_matrix = [[None for _ in range(self.size)] for _ in range(self.size)]
        for ir in range(self.size):
            for ic in range(self.size):
                self.cell_matrix[ir][ic] = Cell.Cell(self.convert_to_standard_pos((ic, ir)), raw_map[ir][ic])
                if Cell.Object.AGENT.value in raw_map[ir][ic]:
                    self.agent_cell = self.cell_matrix[ir][ic]

        file.close()


    def solve_cave(self):

        pass


a = Algorithms(MAP_LIST[0])
print(a.size)
print(a.agent_cell.pos)
print(a.cell_matrix[0][0].object_list)
