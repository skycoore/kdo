import numpy as np

from .event import fire

class console:
    def __init__(self):
        self.matrix = np.array([[32]])
        self.width = self.height = 0

        return fire()

    def gotoXY(self, coordinates: list):
        self.x, self.y = coordinates

        try:
            self.matrix[self.y][self.x]
        except IndexError:
            for line in range(self.y - len(self.matrix) + 1):
                np.append(self.matrix, [32])
            self.height = self.y
            print(self.matrix)
            
            for column in range(self.x - len(self.matrix[self.y]) - 1):
                self.matrix[self.y] += [32]
            if self.width <= self.x:
                self.width = self.x

        return fire()

    def write(self, text: str):
        for letter in range(len(text)):
            try:
                self.matrix[self.y][self.x + letter] = ord(text[letter])
            except IndexError:
                self.matrix[self.y] += [ord(text[letter])]
        
        return fire()

    def print(self):
        for y in self.matrix:
            for x in range(len(y)):
                print(chr(y[x]), end="")

                if x == len(y) - 1:
                    print("")

        return fire()