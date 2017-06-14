import curses
import level
import character


def print_screen(lvl, player, message):
    myscreen = curses.initscr()

    myscreen.border(0)
    for t in lvl.yield_level():
        myscreen.addch(*t)
    myscreen.addch(*player.print_character())
    myscreen.addstr(23, 1, message)
    myscreen.refresh()
    return myscreen.getch()


lvl = level.Level()
lvl.load_level("level1.txt")
player = character.Character()

key = print_screen(lvl, player, "")

while key != 27:
    key = print_screen(lvl, player, player.move(key, lvl))

curses.endwin()
print(player.health)
