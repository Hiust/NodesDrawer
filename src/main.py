from pyglet.gl import *

from serializer import Serializer

class NodesDrawer(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        serializer = Serializer()
        self.nodes = serializer.nodes
        self.connections = serializer.connections

        glClearColor(0,0,0,0)
        self.on_draw()

        pyglet.app.run()

    def on_draw(self):
        for connection in self.connections:
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (connection.startPoint.x, connection.startPoint.y, connection.endPoint.x, connection.endPoint.y)))

        for node in self.nodes:
            for vert in node.verts:
                pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (vert.x, vert.y)))

if __name__ == "__main__":
    window = NodesDrawer(800,600, "NodesDrawer")
