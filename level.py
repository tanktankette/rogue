import tile


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
        x_index, y_index = 0, 0
        for x in self.map:
            for y in x:
                yield y_index + 1, x_index + 1, y[0]
                y_index += 1
            y_index = 0
            x_index += 1

    def change(self, x, y, t=tile.floor):
        self.map[x][y] = t
        return "The walls shift"

    def load_level(self, filename):
        x_index, y_index = 0, 0
        with open(filename, "r") as opened_file:
            for line in opened_file:
                if line[0] != "!":
                    for c in line:
                        if c == "#":
                            self.map[x_index][y_index] = tile.wall
                        if c == " " or c == ".":
                            self.map[x_index][y_index] = tile.floor
                        if c == "~":
                            self.map[x_index][y_index] = tile.lava
                        if c == "\n":
                            pass
                        x_index += 1
                else:
                    params = line[1:-1].split(", ")
                    for x in [0, 1, 3, 4]:
                        params[x] = int(params[x])
                    t = ""
                    if params[5] == ".":
                        t = tile.floor
                    elif params[5] == "~":
                        t = tile.lava
                    elif len(params[5]) > 1:
                        self.map[params[0]][params[1]] = tile.create_sign(params[5])
                        continue
                    self.map[params[0]][params[1]] = \
                        tile.create_button(params[2], params[3], params[4], t)
                x_index = 0
                y_index += 1
