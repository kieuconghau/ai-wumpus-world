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
    def __init__(self, pos, map_size, objects_str):
        self.pos = pos                                                  # (1, 1) (1, 2) ... (10, 10)
        self.index_pos = map_size * (self.pos[1] - 1) + self.pos[0]     # 1 2 3 ... 99 100
        self.map_size = map_size
        self.explored = False
        self.percept = [False, False, False, False, False]  # [-G, -P, -W, -B, -S]
        self.init(objects_str)


    def init(self, objects_str):
        for obj in objects_str:
            if obj == Object.GOLD.value:
                self.percept[0] = True
            elif obj == Object.PIT.value:
                self.percept[1] = True
            elif obj == Object.WUMPUS.value:
                self.percept[2] = True
            elif obj == Object.BREEZE.value:
                self.percept[3] = True
            elif obj == Object.STENCH.value:
                self.percept[4] = True
            elif obj == Object.AGENT.value:
                continue
            elif obj == Object.EMPTY.value:
                continue
            else:
                raise TypeError('Error: Cell.init')


    def exist_gold(self):
        return self.percept[0]

    def exist_pit(self):
        return self.percept[1]

    def exist_wumpus(self):
        return self.percept[2]

    def exist_breeze(self):
        return self.percept[3]

    def exist_stench(self):
        return self.percept[4]


    def get_clause(self):
        clause = []

        for i in range(1, len(self.percept)):
            literal = 1000 * i + self.index_pos         # P: 1, W: 2, B: 3, S: 4
            if not self.percept[i]:
                literal *= -1
            clause.append(literal)

        return clause
