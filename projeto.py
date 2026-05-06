import glfw
from OpenGL.GL import *
import math

selecionado = 0
estado_clique = 0
pecas = []

#### triangulos
# pequeno 1
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)],
    "tx": -0.7, 
    "ty": 0, 
    "rt": 0, 
    "scale": (1, 1, 1), 
    "cor": (1, 0, 0)
    })
# pequeno 2
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx":-0.5, 
    "ty": 0, 
    "rt": 0, 
    "scale": (1, 1, 1), 
    "cor": (0, 1, 0)
    }) 
# medio
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx": -0.3,
    "ty": 0, 
    "rt": 0, 
    "scale": (math.sqrt(2), math.sqrt(2), 1), 
    "cor": (0, 0, 1)
    }) 
# grande 1
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx": -0.1, 
    "ty": 0, 
    "rt": 0, 
    "scale": (2, 2, 1), 
    "cor": (1, 1, 0)
    }) 
# grande 2
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx": 0.1, 
    "ty": 0, 
    "rt": 0, 
    "scale": (2, 2, 1), 
    "cor": (1, 0, 1)
    }) 

#### quadrado
pecas.append({
    "triangulos": [
        (-0.5, -0.5, 0.5, -0.5, -0.5, 0.5),
        (0.5, -0.5, 0.5, 0.5, -0.5, 0.5)
    ],
    "tx": -0.7,
    "ty": 0,
    "rt": 0,
    "scale": (1, 1, 1),
    "cor": (0, 1, 1)
})

#### paralelograma 
pecas.append({
    "triangulos": [
        (0, 0,  1, 0,  0.5, 0.5),   
        (1, 0,  1.5, 0.5,  0.5, 0.5) 
    ],
    "tx": 0.3,
    "ty": 0,
    "rt": 0,
    "scale": (math.sqrt(2), math.sqrt(2), 1),
    "cor": (1, 0.5, 0)
})

#################################################

def init():
    glClearColor(1, 1, 1, 1) # bg color
    
    glMatrixMode(GL_PROJECTION) # muda pra projection
    glLoadIdentity() 
    glMatrixMode(GL_MODELVIEW)  # volta pro modelview

#################################################

def resize(window, width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -1, 1)

    glMatrixMode(GL_MODELVIEW)

#################################################

def render():
    global selecionado
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    for i, p in enumerate(pecas):
        glPushMatrix()

        glTranslatef(p["tx"], p["ty"], 0)
        glRotatef(p["rt"], 0, 0, 1)
        glScalef(*p["scale"])
        
        # desenha preenchimento
        glColor3f(*p["cor"])
        for tri in p["triangulos"]:
            glBegin(GL_TRIANGLES)
            glVertex2f(tri[0], tri[1])
            glVertex2f(tri[2], tri[3])
            glVertex2f(tri[4], tri[5])
            glEnd()

        # desenha contorno SE selecionado
        if selecionado == i + 1:
            glColor3f(0, 0, 0)
            glLineWidth(3)

            for tri in p["triangulos"]:
                glBegin(GL_LINE_LOOP)
                glVertex2f(tri[0], tri[1])
                glVertex2f(tri[2], tri[3])
                glVertex2f(tri[4], tri[5])
                glEnd()

        glPopMatrix()

#################################################

def movimento(window, indice):
    peca = pecas[indice]

    if selecionado == indice + 1:
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            peca["ty"] += 0.001
        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            peca["ty"] -= 0.001
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            peca["tx"] -= 0.001
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            peca["tx"] += 0.001
        if glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS:
            peca["rt"] += 0.1
        if glfw.get_key(window, glfw.KEY_E) == glfw.PRESS:
            peca["rt"] -= 0.1

    # limitar area de movimento
    limite = 2

    peca["tx"] = max(-limite, min(limite, peca["tx"]))
    peca["ty"] = max(-limite, min(limite, peca["ty"]))

#################################################

def teclado(window):
    global selecionado

    for i in range(len(pecas)):  #for que percorre todas peças
        movimento(window, i)     #aplica movimento pra cada peça criada

        if glfw.get_key(window, glfw.KEY_1 + i) == glfw.PRESS: #faz if de seletor para cada peça
            selecionado = i + 1

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
    window = glfw.create_window(500, 500, 'Projeto Tangram', None, None)
    glfw.set_window_aspect_ratio(window, 1, 1) # mantem janela em formato quadrado
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, resize)
    init()
    width, height = glfw.get_framebuffer_size(window)
    resize(window, width, height)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        #mouse(window)
        teclado(window)
        render()
        glfw.swap_buffers(window) # troca frames
    glfw.terminate() # finaliza api

#################################################

main()