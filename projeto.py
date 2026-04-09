import glfw
from OpenGL.GL import *

selecionado = 0
estado_clique = 0
p1x = 0
p1y = 0
p2x = 0
p2y = 0
p3x = 0
p3y = 0
tx = 0
ty = 0
rt = 0
##########
pp1x = 0
pp1y = 0
pp2x = 0
pp2y = 0
pp3x = 0
pp3y = 0
tx2 = 0.7
ty2 = 0
rt2 = 0

#################################################

def init():
    glClearColor(1, 1, 1, 1) # bg color
    global p1x, p1y, p2x, p2y, p3x, p3y, pp1x, pp1y, pp2x, pp2y, pp3x, pp3y
    p1x = -0.5
    p1y = -0.5
    p2x = 0.5
    p2y = -0.5
    p3x = 0.0
    p3y = 0.5
    #
    pp1x = -0.5
    pp1y = -0.5
    pp2x = 0.5
    pp2y = -0.5
    pp3x = 0.0
    pp3y = 0.5

#################################################

def render():
    global selecionado
    glClear(GL_COLOR_BUFFER_BIT) # limpa o buffer
    glLoadIdentity() # limpa a identidade

    # triangulo 1
    glPushMatrix()
    glColor3f(1, 0, 0) # cor do objeto
    glTranslatef(0 + tx, 0 + ty, 1)
    glRotatef(0 + rt, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2f(p1x, p1y) # vertice 1
    glVertex2f(p2x, p2y) # vertice 2
    glVertex2f(p3x, p3y) # vertice 3
    glEnd()
    # borda
    if selecionado == 1:
        glColor3f(0, 0, 0)
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        glVertex2f(p1x, p1y) # vertice 1
        glVertex2f(p2x, p2y) # vertice 2
        glVertex2f(p3x, p3y) # vertice 3
        glEnd()
        glPopMatrix()
    else:
        glPopMatrix()

    # triangulo 2
    glPushMatrix()
    glColor3f(0, 1, 0) # cor do objeto
    glTranslatef(0 + tx2, 0 + ty2, 1)
    glRotatef(0 + rt2, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2f(pp1x, pp1y) # vertice 1
    glVertex2f(pp2x, pp2y) # vertice 2
    glVertex2f(pp3x, pp3y) # vertice 3
    glEnd()
    # borda
    if selecionado == 2:
        glColor3f(0, 0, 0)
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        glVertex2f(pp1x, pp1y) # vertice 1
        glVertex2f(pp2x, pp2y) # vertice 2
        glVertex2f(pp3x, pp3y) # vertice 3
        glEnd()
        glPopMatrix()
    else:
        glPopMatrix()

#################################################

def teclado(window):
    global selecionado, tx, ty, rt, tx2, ty2, rt2
    if glfw.get_key(window, glfw.KEY_1) == glfw.PRESS:
        selecionado = 1
    ###################
    elif glfw.get_key(window, glfw.KEY_2) == glfw.PRESS:
        selecionado = 2
    ###################
    if selecionado == 1:
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
    #####################
    elif selecionado == 2:
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            ty2 += 0.001
        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            ty2 -= 0.001
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            tx2 -= 0.001
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            tx2 += 0.001
        if glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS:
            rt2 += 0.1
        if glfw.get_key(window, glfw.KEY_E) == glfw.PRESS:
            rt2 -= 0.1

#################################################

def mouse(window):
    global estado_clique
    if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
        if estado_clique == 0:
            estado_clique = 1
        elif estado_clique == 1:
            estado_clique = 0      
    if estado_clique == 1:
        teclado(window)

#################################################

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

#################################################

main()