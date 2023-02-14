from numpy import full, array

def rectangle(start, end, character):
    return array(full((end[1] - start[1] + 1, end[0] - start[0] + 1), ord(character)))

def line(start, end, character):
    matrix = array(full())