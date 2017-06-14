import tile


class Level:
    def __init__(self):
        self.map = []
        for x in range(0, 78):
            self.map.append([])
            for y in range(0, 22):
                self.map[x].append(tile.floor)
        self.map[10][3] = tile.lava
        self.map[10][4] = tile.heal
        self.map[10][10] = tile.wall
        self.map[9][9] = tile.button
        self.map[9][10] = tile.sign
        self.map[9][11] = tile.trap

    def yield_level(self):
        x_index, y_index = 0, 0
        for x in self.map:
            for y in x:
                yield y_index + 1, x_index + 1, y[0]
                y_index += 1
            y_index = 0
            x_index += 1

    def change(self, x, y, t):
        self.map[x][y] = t
        return "The walls shift"
