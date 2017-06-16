# TODO:

import curses
import level
import character


def print_screen(lvl, player, message):
    myscreen.border(0)
    for t in lvl.yield_level():
        myscreen.addch(*t)
    myscreen.addch(*player.print_character())
    myscreen.addstr(23, 1, message)
    myscreen.refresh()
    return myscreen.getch()


try:
    myscreen = curses.initscr()
    curses.start_color()
    if curses.can_change_color():
        curses.init_color(10, 1000, 0, 0)
        curses.init_color(11, 700, 700, 700)
        curses.init_pair(1, 10, curses.COLOR_BLACK)
        curses.init_pair(2, 11, curses.COLOR_BLACK)
    else:
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    lvl = level.Level()
    lvl.load_level("level1.txt")
    player = character.Character()

    key = print_screen(lvl, player, "")

    while key != 27 and player.health > 0:
        key = print_screen(lvl, player, player.move(key, lvl))
finally:
    curses.endwin()
    print(player.health)
