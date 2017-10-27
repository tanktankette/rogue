class Character:
    def __init__(self):
        self.pos_x, self.pos_y = 0, 0
        self.health = 100
        self.win = False

    def print_character(self):
        """Return coordinates and character for curses"""
        return self.pos_y + 1, self.pos_x + 1, ord("@")

    def damage(self, amount, description):
        """Damage the character and return a message"""
        self.health -= amount
        return f"You were {description} for {amount} damage"

    def heal(self, amount, description):
        """Heal the character and return a message"""
        self.health += amount
        return f"A {description} for {amount} damage"

    def finish(self):
        """VICTORY!!!"""
        self.win = True
        return "YAY!   -Press any button to quit"

    def parse_move(self, key):
        """Parse out a key press into the resulting new position"""
        temp_x = self.pos_x
        temp_y = self.pos_y

        if key == 49 or key == 52 or key == 55:
            temp_x -= 1
        if key == 57 or key == 54 or key == 51:
            temp_x += 1
        if key == 49 or key == 50 or key == 51:
            temp_y += 1
        if key == 55 or key == 56 or key == 57:
            temp_y -= 1

        return temp_x, temp_y

    def move(self, key, lvl):
        """Move the character and activate the tile at new position"""
        temp_x, temp_y = self.parse_move(key)

        if 0 > temp_x or temp_x > 77 or 0 > temp_y or temp_y > 21:
            return "That's the edge of the map"

        if lvl.map[temp_x][temp_y][1]:
            self.pos_x = temp_x
            self.pos_y = temp_y
            if lvl.map[self.pos_x][self.pos_y][2]:
                ret = lvl.map[self.pos_x][self.pos_y][2](self, lvl)
                if lvl.map[self.pos_x][self.pos_y][3]:
                    lvl.change([self.pos_x, self.pos_y])
                return ret
            return ""
        else:
            return "That's a wall!"
