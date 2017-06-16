# (character, passable, player/map interaction, clear after activated)

floor = (ord("."), True, None, False)
wall = (ord("#"), False, None, False)
lava = (ord("~"), True, lambda c, m: c.damage(10, "burned by lava"), False)
heal = (ord("*"), True, lambda c, m: c.heal(10, "magically healed"), True)


def create_button(ch, coords, t):
    return (ord(ch), True, lambda c, m: m.change(coords, t), True)


def create_sign(text):
    return (ord("^"), True, lambda c, m: text, False)


def get_tile(c):
    if c == "#":
        return wall
    if c == " " or c == ".":
        return floor
    if c == "~":
        return lava
    if c == "*":
        return heal
    return floor
