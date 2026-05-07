import glfw
from OpenGL.GL import *
import math
import os
import winsound 
import threading 
import random

selecionado = 0
enter_pressionado = False
erro_timer = 0
acerto_timer = 0
peca_com_erro = -1
jogo_concluido = False
pecas = []
pontos_fundo = []

for ponto in range(100):
    pontos_fundo.append({
        "x": random.uniform(-2, 2),
        "y": random.uniform(-2, 2),
        "vel": random.uniform(0.0001, 0.0005) 
    })

#### triangulos
# pequeno 1
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)],
    "tx": random.uniform(-1.5, 1.5), 
    "ty": random.uniform(-1.5, 1.5), 
    "rt": random.choice([0, 45, 90, 135, 180, 225, 270, 315]), 
    "scale": (1, 1, 1), 
    "cor": (1, 0, 0),
    "travada": False
    })
# pequeno 2
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx": random.uniform(-1.5, 1.5), 
    "ty": random.uniform(-1.5, 1.5), 
    "rt": random.choice([0, 45, 90, 135, 180, 225, 270, 315]), 
    "scale": (1, 1, 1), 
    "cor": (0, 1, 0),
    "travada": False
    }) 
# medio
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx": random.uniform(-1.5, 1.5), 
    "ty": random.uniform(-1.5, 1.5), 
    "rt": random.choice([0, 45, 90, 135, 180, 225, 270, 315]), 
    "scale": (math.sqrt(2), math.sqrt(2), 1), 
    "cor": (0, 0, 1),
    "travada": False
    }) 
# grande 1
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx": random.uniform(-1.5, 1.5), 
    "ty": random.uniform(-1.5, 1.5), 
    "rt": random.choice([0, 45, 90, 135, 180, 225, 270, 315]), 
    "scale": (2, 2, 1), 
    "cor": (1, 1, 0),
    "travada": False
    }) 
# grande 2
pecas.append({
    "triangulos": [(0, 0, 1, 0, 0, 1)], 
    "tx": random.uniform(-1.5, 1.5), 
    "ty": random.uniform(-1.5, 1.5), 
    "rt": random.choice([0, 45, 90, 135, 180, 225, 270, 315]), 
    "scale": (2, 2, 1), 
    "cor": (1, 0, 1),
    "travada": False
    }) 

#### quadrado
pecas.append({
    "triangulos": [
        (-0.5, -0.5, 0.5, -0.5, -0.5, 0.5),
        (0.5, -0.5, 0.5, 0.5, -0.5, 0.5)
    ],
    "tx": random.uniform(-1.5, 1.5), 
    "ty": random.uniform(-1.5, 1.5), 
    "rt": random.choice([0, 45, 90, 135, 180, 225, 270, 315]), 
    "scale": (1, 1, 1),
    "cor": (0, 1, 1),
    "travada": False
})

#### paralelograma 
pecas.append({
    "triangulos": [
        (0, 0,  1, 0,  0.5, 0.5),   
        (1, 0,  1.5, 0.5,  0.5, 0.5) 
    ],
    "tx": random.uniform(-1.5, 1.5), 
    "ty": random.uniform(-1.5, 1.5), 
    "rt": random.choice([0, 45, 90, 135, 180, 225, 270, 315]), 
    "scale": (math.sqrt(2), math.sqrt(2), 1),
    "cor": (1, 0.5, 0),
    "travada": False
})

#################################################

#### posições de solução
solucao = [
    {"tx": 0.0, "ty": 0.0, "rt": 225.0},                         # pequeno 1
    {"tx": math.sqrt(2)/2, "ty": math.sqrt(2)/2, "rt": 315.0},   # pequeno 2
    {"tx": math.sqrt(2), "ty": -math.sqrt(2), "rt": 90.0},       # médio
    {"tx": 0.0, "ty": 0.0, "rt": 135.0},                         # grande 1
    {"tx": 0.0, "ty": 0.0, "rt": 45.0},                          # grande 2
    {"tx": math.sqrt(2)/2, "ty": 0.0, "rt": 45.0},               # quadrado
    {"tx": -math.sqrt(2), "ty": -math.sqrt(2), "rt": 0.0}        # paralelogramo
]

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

    # quando o jogador vence
    if jogo_concluido:
        # acelera os pontos e muda a cor para dourado
        glPointSize(random.randint(2, 6)) 
        glColor4f(1.0, 0.8, 0.0, 0.5)

    desenhar_background() # desenha os pontos em movimento do fundo
    desenhar_guia() # desenha o quadro no fundo
    
    peca_no_topo = None # variavel para guardar a peça selecionada

    # desenha apenas o que nao esta selecionado
    for i, p in enumerate(pecas):
        if selecionado == i + 1:
            peca_no_topo = (i, p) # guarda para desenhar depois
            continue # pula para a próxima peça
            
        desenha_cada_peca(i, p)

    # desenha a selecionada por cima de todas
    if peca_no_topo:
        desenha_cada_peca(peca_no_topo[0], peca_no_topo[1])

#################################################

def desenhar_background():
    glPointSize(3) # tamanho do ponto
    glColor4f(0.5, 0.5, 0.5, 0.3)
    
    glBegin(GL_POINTS)
    for p in pontos_fundo:
        glVertex2f(p["x"], p["y"])
        
        # movimenta o ponto para a direita
        p["x"] += p["vel"]
        
        # se sair da tela, volta para a esquerda
        if p["x"] > 2:
            p["x"] = -2
            p["y"] = random.uniform(-2, 2) # muda a altura para variar
    glEnd()

#################################################

def desenha_cada_peca(i, p):
    glPushMatrix()
    glTranslatef(p["tx"], p["ty"], 0)
    
    if jogo_concluido:
        # peças girando na comemoração
        glRotatef(glfw.get_time() * 150, 0, 0, 1)
    else:
        glRotatef(p["rt"], 0, 0, 1)
        
    glScalef(*p["scale"])

    # interior
    
    if erro_timer > 0 and peca_com_erro == i:
        glColor3f(1.0, 0.0, 0.0) # vermelho quando erro
    else:
        glColor3f(*p["cor"])     # cor original da peça
        
    for tri in p["triangulos"]:
        glBegin(GL_TRIANGLES)
        glVertex2f(tri[0], tri[1]); glVertex2f(tri[2], tri[3]); glVertex2f(tri[4], tri[5])
        glEnd()

    # contorno

    if p["travada"]:
        glColor3f(0, 0.8, 0) # contorno verde pra travadas
        glLineWidth(4)
    elif erro_timer > 0 and peca_com_erro == i:
        glColor3f(1, 0, 0)   # vermelho se errou, pelo tempo do timer
    # desenha contorno SE selecionado
    elif selecionado == i + 1:
        glColor3f(0, 0, 0) # contorno preto pra selecionada
        glLineWidth(4)
    else:
        glColor3f(0, 0, 0) # preto fino pras neutras
        glLineWidth(1)
    
    for tri in p["triangulos"]: # desenha contorno
        glBegin(GL_LINE_LOOP)
        glVertex2f(tri[0], tri[1])
        glVertex2f(tri[2], tri[3])
        glVertex2f(tri[4], tri[5])
        glEnd()

    glPopMatrix()

#################################################

def verifica_encaixe(indice):
    global acerto_timer, jogo_concluido
    peca = pecas[indice]
    alvo = solucao[indice]

    distancia = math.sqrt(((peca["tx"] - alvo["tx"])**2) + ((peca["ty"] - alvo["ty"])**2)) # pitagorar pra calcular distancia
    diferenca_rotacao = abs((peca["rt"] % 360) - (alvo["rt"] % 360)) # iguala 360, 720 e etc a 0. liberando a diferença real de rotaçao

    if distancia < 0.18 and (diferenca_rotacao < 10 or diferenca_rotacao > 350):
        peca["tx"], peca["ty"], peca["rt"] = alvo["tx"], alvo["ty"], alvo["rt"]
        peca["travada"] = True

        if all(p["travada"] for p in pecas):
            jogo_concluido = True
            tocar_som("vitoria")
            print("PARABÉNS! VOCÊ COMPLETOU O TANGRAM!")
            glClearColor(0.0, 0.0, 0.1, 1.0) # fundo azul escuro
        else:
            tocar_som("acerto")
            acerto_timer = 450
        return True
    return False

#################################################

def desenhar_guia():
    # desenha o quadro
    tamanho = math.sqrt(2)
    glColor3f(0.7, 0.7, 0.7) # cinza
    glLineWidth(2)
    
    glBegin(GL_LINE_LOOP)
    glVertex2f(-math.sqrt(2), -math.sqrt(2))
    glVertex2f(math.sqrt(2), -math.sqrt(2))
    glVertex2f(math.sqrt(2), math.sqrt(2))
    glVertex2f(-math.sqrt(2), math.sqrt(2))
    glEnd()

#################################################

def tocar_som(causa):
    global erro_timer, acerto_timer
    som_desejado = None 

    if causa == "erro":
        som_desejado = os.path.join("sounds", "error.wav")
    elif causa == "acerto":
        som_desejado = os.path.join("sounds", "correct_place.wav")
    elif causa == "vitoria":
        som_desejado = os.path.join("sounds", "level_finished.wav")

    if causa == "vitoria":
        winsound.PlaySound(None, winsound.SND_PURGE)
    
    winsound.PlaySound(som_desejado, winsound.SND_FILENAME | winsound.SND_ASYNC)

#################################################

def iniciar_musica():
    caminho_musica = os.path.join("sounds", "soundtrack.wav")
    if os.path.exists(caminho_musica):
        winsound.PlaySound(caminho_musica, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

#################################################

def checar_vitoria():
    global jogo_concluido
    # verifica se TODAS as peças estão travadas
    todas_travadas = all(p["travada"] for p in pecas)
    
    if todas_travadas and not jogo_concluido:
        jogo_concluido = True
        #tocar_som("fase_concluida")
        #print("PARABÉNS! VOCÊ COMPLETOU O TANGRAM!")

#################################################

def movimento(window, indice):
    peca = pecas[indice]
    if peca["travada"]: return

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
    global selecionado, enter_pressionado, erro_timer, acerto_timer, peca_com_erro

    # diminui o timer do erro a cada frame
    if erro_timer > 0:
        erro_timer -= 1
        if erro_timer == 1:
            iniciar_musica()

    if acerto_timer > 0:
        acerto_timer -= 1
        if acerto_timer == 1: 
            iniciar_musica()

    for i in range(len(pecas)):  # for que percorre todas peças
        movimento(window, i)     # aplica movimento pra cada peça criada
        if glfw.get_key(window, glfw.KEY_1 + i) == glfw.PRESS: # faz if de seletor para cada peça
            selecionado = i + 1
    
    estado_enter = glfw.get_key(window, glfw.KEY_ENTER)
    
    if estado_enter == glfw.PRESS and not enter_pressionado:
        enter_pressionado = True # bloqueia novas execuções até soltar
        if selecionado > 0:
            idx = selecionado - 1
            if not pecas[idx]["travada"]:
                if not verifica_encaixe(idx):
                    print("Lugar errado!")
                    peca_com_erro = idx # marca qual peça ficou vermelha
                    erro_timer = 450
                    tocar_som("erro")
    
    elif estado_enter == glfw.RELEASE:
        enter_pressionado = False # libera

#################################################

def main():
    glfw.init()
    window = glfw.create_window(500, 500, 'Projeto Tangram', None, None)
    glfw.set_window_aspect_ratio(window, 1, 1) # mantem janela em formato quadrado
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, resize)
    init()
    iniciar_musica()
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