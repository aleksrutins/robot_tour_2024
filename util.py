from __future__ import annotations

class Vec2:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod                      
    def diff(a: Vec2, b: Vec2) -> Vec2:
        return Vec2(a.x - b.x, a.y - b.y)