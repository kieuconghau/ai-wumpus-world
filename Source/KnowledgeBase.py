from pysat.solvers import Glucose3
import copy

class KnowledgeBase:
    def __init__(self):
        self.KB = []


    @staticmethod
    def standardize_clause(clause):
        return sorted(list(set(clause)))


    def add_clause(self, clause):
        clause = self.standardize_clause(clause)
        if clause not in self.KB:
            self.KB.append(clause)

    def del_clause(self, clause):
        clause = self.standardize_clause(clause)
        if clause in self.KB:
            self.KB.remove(clause)

    @staticmethod
    def is_opposite(literal_1, literal_2):
        return literal_1 == -literal_2


    def resolve(self, clause_1, clause_2):
        temp_1 = []
        temp_2 = []
        for literal_1 in clause_1:
            for literal_2 in clause_2:
                if self.is_opposite(literal_1, literal_2):
                    temp_1.append(literal_1)
                    temp_2.append(literal_2)

        temp_clause_1 = clause_1.copy()
        temp_clause_2 = clause_2.copy()
        for literal in temp_1:
            temp_clause_1.remove(literal)
        for literal in temp_2:
            temp_clause_2.remove(literal)

        return self.standardize_clause(temp_clause_1 + temp_clause_2)


    def pl_resolution(self, not_alpha):
        # clause_list = KB ^ not alpha
        clause_list = copy.deepcopy(self.KB)
        negative_alpha = not_alpha

        for clause in negative_alpha:
            clause = self.standardize_clause(clause)
            if clause not in clause_list:
                clause_list.append(clause)

        pre_pre_clause_list_len = 0
        while True:
            pre_clause_list_len = len(clause_list)
            for i in range(pre_clause_list_len):
                for j in range(pre_pre_clause_list_len + i, pre_clause_list_len):
                    resolvents = self.resolve(clause_list[i], clause_list[j])
                    if len(resolvents) == 0:
                        return True
                    if resolvents not in clause_list:
                        clause_list.append(resolvents)
            if len(clause_list) == pre_clause_list_len:
                return False
            pre_pre_clause_list_len = pre_clause_list_len


    def infer(self, not_alpha):
        g = Glucose3()
        clause_list = copy.deepcopy(self.KB)
        negative_alpha = not_alpha
        for it in clause_list:
            g.add_clause(it)
        for it in negative_alpha:
            g.add_clause(it)
        sol = g.solve()
        if sol:
            return False
        return True
