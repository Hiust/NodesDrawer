from pyglet.gl import *

from serializer import Serializer

class NodesDrawer(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pyglet.gl.glLineWidth(4)

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
            verts = []
            for vert in node.verts:
                verts.append(vert)
                if len(verts) == 2:
                    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v2i', (verts[0].x, verts[0].y, verts[1].x, verts[1].y, node.center_point.x, node.center_point.y)))
                    verts[:] = verts[1:]

if __name__ == "__main__":
    config = pyglet.gl.Config(sample_buffers=1, samples=4)
    window = NodesDrawer(800,600, "NodesDrawer", config=config)
