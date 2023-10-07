
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


    

# Loop principal do jogo

# Desenha o fundo na tela
while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        tela.blit(plano_fundo, (0, 0))
        tela.blit(plano_fundo_jogo, (200,10))
        
        tela.blit(candys_superficies[0], (265,15))
        tela.blit(candys_superficies[1], (265,82))
        tela.blit(candys_superficies[3], (198,82))
        tela.blit(candys_superficies[4], (327,82))
        tela.blit(candys_superficies[4], (327,149))
        tela.blit(candys_superficies[2], (265,149))
        tela.blit(candys_superficies[10], (388,149))
        tela.blit(candys_superficies[11], (452,149))
        tela.blit(candys_superficies[15], (510,149))
        tela.blit(candys_superficies[19], (570,149))
        tela.blit(candys_superficies[19], (632,149))

        tela.blit(candys_superficies[12], (570,87))
        tela.blit(candys_superficies[17], (632,18))
        tela.blit(candys_superficies[0], (694,87))

        tela.blit(candys_superficies[2], (327,211))
        tela.blit(candys_superficies[1], (388,211))
        tela.blit(candys_superficies[16], (452,211))
        tela.blit(candys_superficies[20], (510,211))
        tela.blit(candys_superficies[20], (572,211))


        tela.blit(candys_superficies[3], (327,273))
        tela.blit(candys_superficies[4], (388,273))
        tela.blit(candys_superficies[18], (452,273))
        tela.blit(candys_superficies[0], (510,273))
        tela.blit(candys_superficies[19], (572,273))


        tela.blit(candys_superficies[0], (327,335))
        tela.blit(candys_superficies[13], (388,335))
        tela.blit(candys_superficies[11], (452,335))
        tela.blit(candys_superficies[10], (510,335))
        tela.blit(candys_superficies[8], (572,335))


        tela.blit(candys_superficies[2], (327,397))
        tela.blit(candys_superficies[1], (388,397))
        tela.blit(candys_superficies[16], (452,397))
        tela.blit(candys_superficies[10], (510,397))
        tela.blit(candys_superficies[3], (572,397))

        # Cria um relógio para controlar os FPS
        relogio = pygame.time.Clock()

        pygame.display.update()

    # Define a quantidade de frames por segundo
        relogio.tick(60)

    

    candys_aleatorios()