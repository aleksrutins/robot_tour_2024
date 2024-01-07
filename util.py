class Vec2:
    x = 0
    y = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod                      
    def diff(a, b):
        return Vec2(a.x - b.x, a.y - b.y)