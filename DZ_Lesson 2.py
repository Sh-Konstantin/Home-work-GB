class Road:
    def __init__(self, length, width):
        self:_length = length
        self._width = width

        def get_full_profit(self):
            return f"{self._length} m * {self._width} m * 25 * 5 = {(self._length * self._width * 25 * 5) / 1000}"

road_to_hell = Road (500, 50)
print(road_to_hell.get_full_profit())