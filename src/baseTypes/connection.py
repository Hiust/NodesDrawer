from .point import Point

class Connection:
    def __init__(self, startNode:Point, endNode:Point):
        self.startPoint = startNode.center_point
        self.endPoint = endNode.center_point
