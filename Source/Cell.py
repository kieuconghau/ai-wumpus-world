from enum import Enum

class Object(Enum):
    GOLD   = 'G'
    PIT    = 'P'
    WUMPUS = 'W'
    BREEZE = 'B'
    STENCH = 'S'
    AGENT  = 'A'
    EMPTY  = '-'


class Cell:
    def __init__(self, pos, objects_str):
        self.pos = pos
        self.explored = False
        self.object_list = [False, False, False, False, False]  # [-G, -P, -W, -B, -S]
        self.init(objects_str)


    def init(self, objects_str):
        for obj in objects_str:
            if obj == Object.GOLD.value:
                self.object_list[0] = True
            elif obj == Object.PIT.value:
                self.object_list[1] = True
            elif obj == Object.WUMPUS.value:
                self.object_list[2] = True
            elif obj == Object.BREEZE.value:
                self.object_list[3] = True
            elif obj == Object.STENCH.value:
                self.object_list[4] = True
            elif obj == Object.AGENT.value:
                continue
            elif obj == Object.EMPTY.value:
                continue
            else:
                print('Error: Cell.init')
