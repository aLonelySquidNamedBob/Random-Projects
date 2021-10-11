from OpenGL.GL import *
from OpenGL.GLUT import *

w, h = 500, 500


def Square(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()


def Trianlge():
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(100, 200)
    glVertex2f(100, 100)
    glEnd()


def Iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def ShowScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    Iterate()
    glColor3f(1.0, 0.0, 3.0)
    Square(100, 100, 100, 100)
    glColor3f(0.0, 3.0, 0.0)
    Trianlge()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(700, 100)
    wind = glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(ShowScreen)
    glutIdleFunc(ShowScreen)
    glutMainLoop()


if __name__ == '__main__':
    main()
