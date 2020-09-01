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
