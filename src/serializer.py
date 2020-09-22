from baseTypes.point import Point
from baseTypes.connection import Connection
from baseTypes.node import Node

class Serializer:
    def __init__(self):
        self.nodes = []
        self.connections = []
        self.readFile()

    def readFile(self):
        testFile = open("./testFile.nd", "r")
        testFile = testFile.read().splitlines()
        readNodes = True
        for line in testFile:
            if line == "":
                readNodes = False
                continue

            if readNodes == True:
                node = line.split()
                print(node)
                self.nodes.append(Node(Point(int(node[0]), int(node[1]))))

            if readNodes == False:
                node = line.split()
                print(node)
                self.connections.append(Connection(self.nodes[int(node[0])], self.nodes[int(node[1])]))
