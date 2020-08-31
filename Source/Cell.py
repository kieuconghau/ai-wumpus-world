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
    def __init__(self, matrix_pos, map_size, objects_str):
        self.matrix_pos = matrix_pos                                            # (0, 0) (0, 1) ... (9, 9)   (TL -> BR)
        self.map_pos = matrix_pos[1] + 1, map_size - matrix_pos[0]              # (1, 1) (1, 2) ... (10, 10) (BL -> TR)
        self.index_pos = map_size * (self.map_pos[1] - 1) + self.map_pos[0]     # 1 2 3 ... 99 100           (BL -> TR)
        self.map_size = map_size

        self.explored = False
        self.percept = [False, False, False, False, False]  # [-G, -P, -W, -B, -S]
        self.init(objects_str)

        self.parent = None
        self.child_list = []


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

    def is_OK(self):
        return not self.exist_breeze() and not self.exist_stench()


    def update_parent(self, parent_cell):
        self.parent = parent_cell


    def grab_gold(self):
        self.percept[0] = False


    def kill_wumpus(self, cell_matrix, kb):
        # Delete Wumpus.
        self.percept[2] = False

        # Delete Stench of adjacent cells.
        adj_cell_list_of_wumpus_cell = self.get_adj_cell_list(cell_matrix)
        for stench_cell in adj_cell_list_of_wumpus_cell:
            del_stench_flag = True
            adj_cell_list_of_stench_cell = stench_cell.get_adj_cell_list(cell_matrix)
            for adj_cell in adj_cell_list_of_stench_cell:
                if adj_cell.exist_wumpus():
                    del_stench_flag = False
                    break
            if del_stench_flag:
                stench_cell.percept[4] = False
                literal = self.get_literal(Object.STENCH, '+')
                kb.del_clause([literal])
                literal = self.get_literal(Object.STENCH, '-')
                kb.add_clause([literal])

                adj_cell_list = stench_cell.get_adj_cell_list(cell_matrix)
                # S => Wa v Wb v Wc v Wd
                clause = [stench_cell.get_literal(Object.STENCH, '-')]
                for adj_cell in adj_cell_list:
                    clause.append(adj_cell.get_literal(Object.WUMPUS, '+'))
                kb.del_clause(clause)

                # Wa v Wb v Wc v Wd => S
                for adj_cell in adj_cell_list:
                    clause = [stench_cell.get_literal(Object.STENCH, '+'),
                              adj_cell.get_literal(Object.WUMPUS, '-')]
                    kb.del_clause(clause)




    def get_adj_cell_list(self, cell_matrix):
        adj_cell_list = []
        adj_cell_matrix_pos_list = [(self.matrix_pos[0], self.matrix_pos[1] + 1),   # Right
                                    (self.matrix_pos[0], self.matrix_pos[1] - 1),   # Left
                                    (self.matrix_pos[0] - 1, self.matrix_pos[1]),   # Up
                                    (self.matrix_pos[0] + 1, self.matrix_pos[1])]   # Down

        for ajd_cell_matrix_pos in adj_cell_matrix_pos_list:
            if 0 <= ajd_cell_matrix_pos[0] < self.map_size and 0 <= ajd_cell_matrix_pos[1] < self.map_size:
                adj_cell_list.append(cell_matrix[ajd_cell_matrix_pos[0]][ajd_cell_matrix_pos[1]])

        return adj_cell_list


    def is_explored(self):
        return self.explored

    def explore(self):
        self.explored = True


    def update_child_list(self, valid_adj_cell_list):
        for adj_cell in valid_adj_cell_list:
            if adj_cell.parent is None:
                self.child_list.append(adj_cell)
                adj_cell.update_parent(self)


    def get_literal(self, obj: Object, sign='+'):    # sign='-': not operator
        if obj == Object.PIT:
            i = 1
        elif obj == Object.WUMPUS:
            i = 2
        elif obj == obj.BREEZE:
            i = 3
        elif obj == obj.STENCH:
            i = 4
        else:
            raise TypeError('Error: ' + self.get_literal.__name__)

        factor = 10 ** len(str(self.map_size * self.map_size))
        literal = i * factor + self.index_pos
        if sign == '-':
            literal *= -1

        return literal
