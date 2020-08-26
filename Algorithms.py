

class Algorithms:
    def __init__(self):
        try:
            self.file = open('input.txt', "r")
        except:
            print("Can not read file \'" + 'input.txt' + "\'. Please check again!")
    def read_file(self):

        self.size = [int(x) for x in next(self.file).split()]
        self.raw_map = [[str(num) for num in line if num != '\n'] for line in self.file]
    def from_raw_to_info(self):
        pass


a = Algorithms()
b, c = a.read_file()
print(b, c)
