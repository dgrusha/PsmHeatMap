class Point:
    x = 1
    y = 0
    value = 0

    def __init__(self, x1, y1, w, h, value):
        self.value = value
        self.x = x1
        self.y = y1
        x = x1
        y = y1
        if x == w + 1:
            self.value = 50
        elif y == h + 1:
            self.value = 200
        elif x == 0:
            self.value = 100
        elif y == 0:
            self.value = 150
