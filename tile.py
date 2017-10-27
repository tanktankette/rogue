# (character, passable, player/map interaction, clear after activated)

floor = (ord("."), True, None, False)
wall = (ord("#"), False, None, False)
finish = (ord("W"), True, lambda c, m: c.finish(), False)
lava = (ord("~"), True, lambda c, m: c.damage(10, "burned by lava"), False)
heal = (ord("*"), True, lambda c, m: c.heal(10, "holy light heals you"), True)


def create_button(ch, coords, t):
    return (ord(ch), True, lambda c, m: m.change(coords, t), True)


def create_sign(text):
    return (ord("^"), True, lambda c, m: text, False)


def get_tile(c):
    if c == "#" or c == "x":
        return wall
    if c == " " or c == ".":
        return floor
    if c == "~":
        return lava
    if c == "*":
        return heal
    if c == "W":
        return finish
    return floor
