import graphics

def main():
    scr = graphics.screen()
    
    scr.gotoxy(5, 5)
    scr.print("Hello world!")

    scr.display()

if __name__ == "__main__":
    main()