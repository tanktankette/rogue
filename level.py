import tile
from curses import color_pair


class Level:
    def __init__(self):
        self.map = []
        for x in range(0, 78):
            self.map.append([])
            for y in range(0, 22):
                self.map[x].append(tile.floor)

    def __str__(self):
        r = ""
        temp = ""
        for y in range(0, 22):
            for x in range(0, 78):
                temp += chr(self.map[x][y][0])
            r += temp + "\n"
            temp = ""
        return r

    def yield_level(self):
        """Yield the level one tile at a time for curses"""
        x_index, y_index = 0, 0
        for x in self.map:
            for y in x:
                color = 2
                if chr(y[0]) == "~":
                    color = 1
                yield y_index + 1, x_index + 1, y[0], color_pair(color)
                y_index += 1
            y_index = 0
            x_index += 1

    def change(self, coord: list, t=tile.floor):
        """Change a tile (or tiles) of the map"""
        x = 0
        while x < len(coord):
            if self.map[coord[x]][coord[x+1]] is not tile.lava:
                self.map[coord[x]][coord[x+1]] = t
            x += 2
        return "The walls shift"

    def load_level(self, filename):
        """Load level from file"""
        x_index, y_index = 0, 0
        with open(filename, "r") as opened_file:
            for line in opened_file:
                if line[0] != "!":  # Base level map: floors, walls, and lava
                    for c in line[:-1]:
                        self.map[x_index][y_index] = tile.get_tile(c)
                        x_index += 1
                    x_index = 0
                    y_index += 1
                else:  # Button or sign
                    params = line[1:-1].split(", ")
                    for x in [0, 1, 3, 4]:
                        params[x] = int(params[x])
                    if len(params[5]) > 1:
                        self.map[params[0]][params[1]] = \
                            tile.create_sign(params[5])
                    else:
                        t = tile.get_tile(params[5])
                        coord = [params[3], params[4]]
                        if len(params) > 6:
                            for x in params[6:]:
                                x = int(x)
                                coord.append(x)
                        self.map[params[0]][params[1]] = tile.create_button(
                            params[2], coord, t)
