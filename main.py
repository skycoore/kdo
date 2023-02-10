import graphics
from graphics import console

console = console()
graphics.addEventListener(console.write, console.print)


console.gotoXY((6, 6))
console.write("Hello world")