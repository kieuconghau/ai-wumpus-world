
class Algorithms:
    def __init__(self, map_filename):
        self.file = open(map_filename, 'r')
        self.size = [int(x) for x in next(self.file).split()][0]
        self.raw_map = [[str(num) for num in line if num != '\n'] for line in self.file]
        self.file.close()

