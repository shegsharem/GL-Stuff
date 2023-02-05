import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
cubeColors = ((1,0,0),(0,1,0),(0,0,1),(0,1,0),(1,1,1),(0,1,1),(1,0,0),(0,1,0),(0,0,1),(1,0,0),(1,1,1),(0,1,1))

class Cube:
    def __init__(self, edges, vertices, quads, colors=None):
        self.vertices = vertices # location (x,y,z) of each vertex
        self.edges = edges # e.g. (vertex 0, vertex 1) connects two vertices within the list of tuples
        self.quads = quads # group of vertices to create a surface - usually 4 vertices
        self.colors = colors

    def draw(self):
        # Draw surfaces
        glBegin(GL_QUADS)
        for quad in self.quads:
            x=1
            for vertex in quad:
                x+=1

                if self.colors != None:
                    glColor3fv(self.colors[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()

        # Draw Wireframe
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

def getScreenData():
        pygame.init()
        screendata = pygame.display.Info()
        windowSize = (screendata.current_w, screendata.current_h)
        print(windowSize)
        return windowSize

def initGL(screenResolution):
    gluPerspective(45, (screenResolution[0]/screenResolution[1]), 0.1, 50.0)
    # Black background
    glClearColor (0.0, 0.0, 0.0, 0.5);
    # Depth buffer setup
    #glClearDepth (1.0);
    ## Type of depth test
    #glDepthFunc(GL_LEQUAL)
    ## Smooth shading
    #glShadeModel(GL_SMOOTH)
#
    #glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT0)
    #glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    #glEnable( GL_POLYGON_SMOOTH )
#
    #glEnable(GL_COLOR_MATERIAL);        
    #glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.7, 0.7, 0.7, 0])
    #glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.8, 0.8, 0.7, 0])
    #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.8, 0.8, 0.8, 0])
    #glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 30)
    #glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE); 
#
    #glLightModeli( GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR );
    #glLightfv(GL_LIGHT0, GL_POSITION, [0.85, 0.8, 0.75, 0])
    #glLightfv(GL_LIGHT0, GL_AMBIENT, [0.8, 0.8, 0.7, 0])
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 0])
    #glLightfv(GL_LIGHT0, GL_SPECULAR, [0.8, 0.8, 0.8, 0])
#
#

def main():
    pygame.init()
    resolution = getScreenData()
    pygame.display.set_mode(resolution, DOUBLEBUF|OPENGL)

    initGL(resolution)

    cube = Cube(cubeEdges, cubeVertices, cubeQuads, cubeColors)

    # Transformation matrix, ExT where T is the transformation and E is the original location
    # (x,y,z)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                # IF KEY IS PRESSED DOWN
                if event.key == pygame.key.key_code(K_ESCAPE):
                    pygame.quit()
                    quit()
                
        
        # Center of rotation vertex (angle of rotation,x,y,z)
        glRotatef(0.1, -1, -1, -1)
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #solidCube()
        cube.draw()
        pygame.display.flip()
        pygame.time.wait(1)

if __name__ == "__main__":
    main()