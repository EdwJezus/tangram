import glfw
from OpenGL.GL import *

selecionado = 0
estado_clique = 0
triangulos = []
cores = [
    (1, 0, 0), 
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
]

for i in range(3): #define quantidade de triangulos
    pos_y = -0.8 + i * 0.5
    cor = cores[i % len(cores)] #gera ciclos de cores no indice 

    #p1x, p1y, p2x, p2y, p3x, p3y, tx, ty, rt
    triangulos.append((-0.5, -0.5, 0.5, -0.5, 0, 0.5, pos_y, 0, 0, cor))


#################################################

def init():
    glClearColor(1, 1, 1, 1) # bg color

#################################################

def cria_triangulo(p1x, p1y, p2x, p2y, p3x, p3y, tx, ty, rt, color, obj):
    glPushMatrix()
    glColor3f(*color) # cor do objeto
    glTranslatef(0 + tx, 0 + ty, 1)
    glRotatef(0 + rt, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2f(p1x, p1y) # vertice 1
    glVertex2f(p2x, p2y) # vertice 2
    glVertex2f(p3x, p3y) # vertice 3
    glEnd()
    # borda
    if selecionado == obj:
        glColor3f(0, 0, 0)
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        glVertex2f(p1x, p1y) # vertice 1
        glVertex2f(p2x, p2y) # vertice 2
        glVertex2f(p3x, p3y) # vertice 3
        glEnd()
    glPopMatrix()

#################################################

def render():
    global selecionado, triangulos
    glClear(GL_COLOR_BUFFER_BIT) # limpa o buffer
    glLoadIdentity() # limpa a identidade

    for t in range(len(triangulos)): #for para criar triangulos
        cria_triangulo(
                triangulos[t][0], #p1x
                triangulos[t][1], #p1y
                triangulos[t][2], #p2x
                triangulos[t][3], #p2y
                triangulos[t][4], #p3x
                triangulos[t][5], #p3y
                triangulos[t][6], #tx
                triangulos[t][7], #ty
                triangulos[t][8], #rt
                triangulos[t][9], #color
                t + 1, )

#################################################

def movimento(window, indice):
    triangulo = list(triangulos[indice]) #transforma tupla em lista
    if selecionado == indice + 1:
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            triangulo[7] += 0.001
        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            triangulo[7] -= 0.001
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            triangulo[6] -= 0.001
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            triangulo[6] += 0.001
        if glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS:
            triangulo[8] += 0.1
        if glfw.get_key(window, glfw.KEY_E) == glfw.PRESS:
            triangulo[8] -= 0.1  
    triangulos[indice] = tuple(triangulo) #transforma lista em tupla de volta

#################################################

def teclado(window):
    global triangulos, selecionado

    for t in range(len(triangulos)): #for que percorre todos triangulos
        movimento(window, t) #aplica movimento pra cada triangulo criado
        if glfw.get_key(window, glfw.KEY_1 + t) == glfw.PRESS: #faz if de seletor para cada triangulo
            selecionado = t+1

#################################################

'''
def mouse(window):
    global estado_clique
    if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
        if estado_clique == 0:
            estado_clique = 1
        elif estado_clique == 1:
            estado_clique = 0      
    if estado_clique == 1:
        teclado(window)
'''

#################################################

def main():
    glfw.init()
    window = glfw.create_window(500, 500, 'Projeto', None, None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        glfw.poll_events()
        #mouse(window)
        teclado(window)
        render()
        glfw.swap_buffers(window) # troca frames
    glfw.terminate() # finaliza api

#################################################

main()