import glfw
from OpenGL.GL import *

p1x = 0
p1y = 0
p2x = 0
p2y = 0
p3x = 0
p3y = 0
tx = 0
ty = 0
rt = 0
mouse_antes = glfw.RELEASE
modo_mouse = False

def init():
    glClearColor(1, 1, 1, 1) # bg color
    global p1x, p1y, p2x, p2y, p3x, p3y
    p1x = -0.5
    p1y = -0.5
    p2x = 0.5
    p2y = -0.5
    p3x = 0.0
    p3y = 0.5
    
def render():
    glClear(GL_COLOR_BUFFER_BIT) # limpa o buffer
    glLoadIdentity() # limpa a identidade

    glPushMatrix()
    glColor3f(1, 0, 0) # cor do objeto
    
    glTranslatef(0 + tx, 0 + ty, 1)
    glRotatef(0 + rt, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2f(p1x, p1y) # vertice 1
    glVertex2f(p2x, p2y) # vertice 2
    glVertex2f(p3x, p3y) # vertice 3
    glEnd()
    glPopMatrix()


def teclado(window):
    global tx, ty, rt
    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        ty += 0.001
    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        ty -= 0.001
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        tx -= 0.001
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        tx += 0.001
    if glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS:
        rt += 0.1
    if glfw.get_key(window, glfw.KEY_E) == glfw.PRESS:
        rt -= 0.1

def mouse(window):
    global mouse_antes, modo_mouse
    estado = glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) 
    if estado == glfw.PRESS and mouse_antes == glfw.RELEASE:
        modo_mouse = not modo_mouse
    mouse_antes = estado
    if modo_mouse:
        teclado(window)

def main():
    glfw.init()
    window = glfw.create_window(500, 500, 'Projeto', None, None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        glfw.poll_events()
        mouse(window)
        render()
        glfw.swap_buffers(window) # troca frames
    glfw.terminate() # finaliza api

if __name__ == '__main__':
    main()