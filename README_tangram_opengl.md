# 🎮 Tangram OpenGL (Python + GLFW)

Este projeto implementa um jogo clássico de Tangram utilizando Python, OpenGL e GLFW. O objetivo é encaixar todas as peças no modelo correto, utilizando controles de teclado para mover e rotacionar as formas até completar a figura.

---

## 📁 Estrutura do Projeto

.
├── projeto.py
├── sounds/
│   ├── error.wav
│   ├── correct_place.wav
│   ├── level_finished.wav
│   └── soundtrack.wav
├── manual_tangram.jpg
├── modelo_tangram.jpg
└── README.md

---

## 🎯 Objetivo do Jogo

O jogador deve mover e rotacionar as peças até completar o modelo.

Quando concluir:
- Vitória é ativada
- Som de vitória toca
- Animação especial no jogo

---

## 🎮 Controles

- 1 a 7 → Selecionar peça
- Setas → Mover peça
- Q / E → Rotacionar
- Enter → Confirmar encaixe

---

## 🚀 Como Executar

### Instalar dependências
pip install glfw PyOpenGL

### Rodar o jogo
python projeto.py

---

## 🧠 Como Funciona

- Peças desenhadas com OpenGL (GL_TRIANGLES)
- Cada peça tem posição, rotação, escala e cor
- Encaixe baseado em distância + rotação

---

## 📌 Feedback

✔ Acerto → trava peça + som  
❌ Erro → vermelho temporário + som  
🏁 Vitória → animação + música

---

## 🌌 Extras

- Fundo animado
- Música ambiente em loop
- Animação de vitória

---

## 🧪 Tecnologias

- Python
- OpenGL
- GLFW
- Winsound

---

## 📜 Licença

MIT License © Eduardo Jesus
