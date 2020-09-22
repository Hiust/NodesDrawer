import math
from .point import Point

class Node:
    def __init__(self, center_point:Point):
        self.center_point = center_point
        self.verts = self.generate_verts(24, 20)

    def generate_verts(self, max_verts, radius):
        verts = []
        angle = 360/max_verts
        for i in range(max_verts):
            angleInRadians = (angle*i)*(math.pi/180)
            cosT = math.cos(angleInRadians)
            sinT = math.sin(angleInRadians)
            x = cosT*radius - sinT*radius+self.center_point.x
            y = sinT*radius + cosT*radius+self.center_point.y
            verts.append(Point(int(x), int(y)))
        verts.append(Point(verts[0].x, verts[0].y))
        return verts
