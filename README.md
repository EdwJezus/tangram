# 🎮 Tangram OpenGL (Python + GLFW)

Este projeto implementa um jogo clássico de **Tangram** utilizando **Python, OpenGL e GLFW**. O objetivo é encaixar todas as peças no modelo correto, utilizando controles de teclado para mover e rotacionar as formas até completar a figura.

---

## 📁 Estrutura do Projeto

.
├── projeto.py              # Código principal do jogo (OpenGL + GLFW)
├── sounds/                 # Sons do jogo (acerto, erro, vitória e música de fundo)
│   ├── error.wav
│   ├── correct_place.wav
│   ├── level_finished.wav
│   └── soundtrack.wav
├── manual_tangram.jpg      # Manual com teclas e instruções do jogo
├── modelo_tangram.jpg      # Referência visual do encaixe final das peças
└── README.md               # Este documento

---

## 🎯 Objetivo do Jogo

O jogador deve mover e rotacionar as peças do tangram até que todas se encaixem corretamente na posição final mostrada no `modelo_tangram.jpg`.

Quando todas as peças estão corretas:
- O jogo é concluído automaticamente
- Um som de vitória é reproduzido
- O fundo muda e há uma animação comemorativa

---

## 🎮 Controles

| Tecla | Ação |
|------|------|
| `1` a `7` | Selecionar peça |
| `Setas` | Mover peça selecionada |
| `Q` | Rotacionar anti-horário |
| `E` | Rotacionar horário |
| `Enter` | Confirmar encaixe da peça |

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/tangram-opengl.git
cd tangram-opengl
