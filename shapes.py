'''
Define shapes that have collision detection for each pairing of shape
'''

import math

class CollisionDetector:

    @staticmethod
    def collisionRectCircle(circle, rectangle):
        testX = circle.cx
        testY = circle.cy
        if (circle.cx < rectangle.rx):
            testX = rectangle.rx
        elif (circle.cx > rectangle.rx + rectangle.rw):
            testX = rectangle.rx + rectangle.rw

        if (circle.cy < rectangle.ry):
            testY = rectangle.ry
        elif (circle.cy > rectangle.ry + rectangle.rh):
            testY = rectangle.ry + rectangle.rh

        distX = circle.cx - testX
        distY = circle.cy - testY
        distR = math.sqrt(distX**2 + distY**2)
        collide = True if (distR < circle.r) else False

        return collide

    @staticmethod
    def collisionRectRect(rect1, rect2):
        pass

    @staticmethod
    def collisionCircleCircle(circle1, circle2):
        diffX = circle1.cx - circle2.cx
        diffY = circle1.cy - circle2.cy
        diffR = math.sqrt(diffX**2 + diffY**2)

        collide = True if (diffR < circle1.r + circle2.r) else False
        return collide

class Shape:
    pass

class Circle(Shape):
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r

class Rectangle(Shape):
    def __init__(self, rx, ry, rw, rh):
        self.rx = rx
        self.ry = ry
        self.rw = rw
        self.rh = rh

