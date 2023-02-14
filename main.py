import graphics
from graphics import console

def main():
    con = console()

    rectangle = graphics.rectangle([0, 0], [12, 6], "#")
    con.write([0, 0], rectangle)

    con.update()

if __name__ == "__main__":
    main()