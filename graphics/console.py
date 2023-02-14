from numpy import array, full
from os import get_terminal_size
from inspect import currentframe

class console:
    def __init__(self):
        self.size = get_terminal_size()
        self.matrix = array(full((self.size.lines, self.size.columns), 32))

    def write(self, position, message):
        if message is str:
            message = message.split("\n")

        for line in range(len(message)):
            for column in range(len(message[line])):
                try: message[line][column] = ord(message[line][column])
                except TypeError: pass

                if message[line][column] != 32:
                    self.matrix[position[1] + line][position[0] + column] = message[line][column]

    def update(self):
        self.size = get_terminal_size()
        self.matrix.resize((self.size.lines, self.size.columns))

        for line in self.matrix:
            for column in range(len(line)):
                print(chr(line[column]), end="")