
import pygame
from sys import exit
from random import randint, choice

# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 640)
tela = pygame.display.set_mode(tamanho)

# Define o Titulo da Janela
pygame.display.set_caption("Candy Supreme")

##
## Importa os arquivos necessários
##

def candys_aleatorios():
    posicao = (randint(10, 950), randint(-100, 0))
    posicao = candys_superficies[0].get_rect(center=posicao)
    

def gera_nova_caixa():
    tipo_caixa = randint(1, 20)
    caixa = candys_superficies[tipo_caixa]

    pos_x, pos_y = (198, 82)

    retangulo = caixa.get_rect(center=(pos_x, pos_y))

    lista_caixas.append({
        'superficie': caixa,
        'objeto': retangulo
    })

def gravidade():
    for caixa in lista_caixas:
        caixa['objeto'].y += valor_gravidade
        tela.blit(caixa['superficie'], caixa['objeto'])

# Carrega o plano de fundo
plano_fundo = pygame.image.load('PNG/Fundo1.png').convert_alpha()
plano_fundo_jogo = pygame.image.load('PNG/Fundo3.png').convert_alpha()

# Transforma o tamanho da imagem de fundo

Fundo_jogo = []
lista_candys = []
plano_index = 0
plano_fundo = pygame.transform.scale(plano_fundo, (tamanho))
plano_fundo_jogo = pygame.transform.scale(plano_fundo_jogo, (560,600))

# Carrega os candys
candys_superficies = []
candys_index = 0
for imagem in range(1, 22):
    img = pygame.image.load(f'PNG/ico/{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (62, 62))
    candys_superficies.append(img)


# Cria um relógio para controlar os FPS
relogio = pygame.time.Clock()

nova_caixa_timer = pygame.USEREVENT + 1
pygame.time.set_timer(nova_caixa_timer, 300)

lista_caixas = []
valor_gravidade = 5

# Desenha o fundo na tela
while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if evento.type == nova_caixa_timer:
            gera_nova_caixa()

    tela.blit(plano_fundo, (0, 0))
    tela.blit(plano_fundo_jogo, (200,10))

    candys_aleatorios()
    gravidade()

    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)