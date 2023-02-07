import os

class screen:
    def __init__(self):
        self.gotoxy(0, 0)

    def gotoxy(self, x, y):
        try: 
            value = self.matrix[y][x]
            self.x, self.y = x, y
            return
        except AttributeError:
            self.matrix = []
            self.width = self.height = 0
        except IndexError:
            missing_lines = y - len(self.matrix) + 1
            for line in range(missing_lines):
                self.matrix += [[32]]
                self.height += 1

            missing_columns = x - len(self.matrix[y]) + 1
            for column in range(missing_columns):
                self.matrix[y] += [32]
                if len(self.matrix[y]) >= self.width:
                    self.width += 1

        return self.gotoxy(x, y)

    def print(self, message):
        x = self.x
        for character in range(len(message)):
            self.gotoxy(x + character, self.y)
            self.matrix[self.y][self.x] = ord(message[character])
        self.gotoxy(x, self.y)

    def display(self):
        window_width, window_height = os.get_terminal_size()
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                print(chr(self.matrix[y][x]), end="")

                if x + 1 == len(self.matrix[y]):
                    print(" "*(window_width - len(self.matrix[y])), end="")

            if y + 1 == self.height:
                print(" "*window_width*(window_height - self.height), end="")