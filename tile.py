# (character, passable, player/map interaction, clear after activated)

floor = (ord("."), True, None, False)
wall = (ord("#"), False, None, False)
lava = (ord("~"), True, lambda c, m: c.damage(10, "burned by lava"), False)
sign = (ord("^"), True, lambda c, m: "To the south is a trap", False)
heal = (ord("*"), True, lambda c, m: c.heal(10, "magically healed"), True)


def create_button(c, x, y, t):
    return (ord(c), True, lambda c, m: m.change(x, y, t), True)


def create_sign(text):
    return (ord("^"), True, lambda c, m: text, False)
