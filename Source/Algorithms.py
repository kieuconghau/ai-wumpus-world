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
    PERCEIVE_BREEZE = 7
    PERCEIVE_STENCH = 8
    SHOOT_AN_ARROW = 9
    KILL_WUMPUS = 10
    BE_EATEN_BY_WUMPUS = 11
    FALL_INTO_PIT = 12
    KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD = 13
    CLIMB_OUT_OF_THE_CAVE = 14


class Algorithms:
    def __init__(self, map_filename):
        self.map_size = None
        self.cell_matrix = None
        self.agent_cell = None
        self.read_map(map_filename)
        self.action_list = []
        self.KB = []


    def convert_to_standard_pos(self, pos):
        return pos[0] + 1, self.map_size - pos[1]


    def read_map(self, map_filename):
        file = open(map_filename, 'r')

        self.map_size = int(file.readline())
        raw_map = [line.split('.') for line in file.read().splitlines()]

        self.cell_matrix = [[None for _ in range(self.map_size)] for _ in range(self.map_size)]
        for ir in range(self.map_size):
            for ic in range(self.map_size):
                self.cell_matrix[ir][ic] = Cell.Cell(self.convert_to_standard_pos((ic, ir)), self.map_size, raw_map[ir][ic])
                if Cell.Object.AGENT.value in raw_map[ir][ic]:
                    self.agent_cell = self.cell_matrix[ir][ic]

        file.close()


    def pl_resolution(self, alpha):
        pass


    def solve_cave(self):
        while True:
            if self.agent_cell.exist_pit():
                self.action_list.append(Action.FALL_INTO_PIT)
                break

            if self.agent_cell.exist_wumpus():
                self.action_list.append(Action.BE_EATEN_BY_WUMPUS)
                break

            if self.agent_cell.exist_gold():
                self.action_list.append(Action.PICK_UP_GOLD)

            if self.agent_cell.exist_breeze():
                self.action_list.append(Action.PERCEIVE_BREEZE)

            if self.agent_cell.exist_stench():
                self.action_list.append(Action.PERCEIVE_STENCH)

        return self.action_list


a = Algorithms(MAP_LIST[0])
