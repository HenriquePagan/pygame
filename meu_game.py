import pygame
from random import randrange
import os

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)


pygame.init()

largura = 640
altura =  480
tamanho = 10
velocidade = 15

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snack")

font = pygame.font.SysFont(None, 28)

def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [largura/10, altura/2])


def cobra(cobraXY):
    for XY in cobraXY:
        pygame.draw.rect(fundo, verde, [XY[0], XY[1], tamanho,tamanho])

def maca(pos_x, pos_y):
    #pygame.image.load(os.path.join("corote_small.png"))
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y,tamanho,tamanho])    

def jogo():   
    fimdejogo = False    
    sair = True
    maca_x = randrange(0, largura-tamanho,10)#faz aparecer aleatoriamente
    maca_y = randrange(0, altura-tamanho,10) #faz aparecer aleatoriamente
    pos_x = randrange(0, largura-tamanho,10) #faz aparecer aleatoriamente
    pos_y = randrange(0, altura-tamanho,10) #faz aparecer aleatoriamente

    velocidade_x = 0
    velocidade_y = 0
    cobraXY = []
    cobraComp = 1

    while sair:
        while fimdejogo:
            fundo.fill(branco)
            texto("Fim de jogo, para continuar tecla C ou S para sair", vermelho)
            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False     
                
                if event.type == pygame.KEYDOWN:                
                    if event.key == pygame.K_c:
                        fimdejogo = False    
                        sair = True
                        maca_x = randrange(0, largura-tamanho,10)#faz aparecer aleatoriamente
                        maca_y = randrange(0, altura-tamanho,10) #faz aparecer aleatoriamente
                        pos_x = randrange(0, largura-tamanho,10) #faz aparecer aleatoriamente
                        pos_y = randrange(0, altura-tamanho,10) #faz aparecer aleatoriamente
                        velocidade_x = 0
                        velocidade_y = 0
                        cobraXY = []
                        cobraComp = 1

                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT and velocidade_x != tamanho: #ESQUERDA
                    velocidade_y = 0
                    velocidade_x =- tamanho

                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho: #DIREITA
                    velocidade_y = 0
                    velocidade_x =+ tamanho

                if event.key == pygame.K_UP and velocidade_y != tamanho: #CIMA
                    velocidade_x = 0
                    velocidade_y =- tamanho

                if event.key == pygame.K_DOWN and velocidade_y != -tamanho: #BAIXO
                    velocidade_x = 0
                    velocidade_y =+ tamanho            

        fundo.fill(preto)        
        pos_x += velocidade_x
        pos_y +=velocidade_y

        if pos_x + tamanho > largura:
            pos_x = 0
            
        if pos_x < 0:
            pos_x = largura-tamanho

        if pos_y + tamanho > altura:
            pos_y = 0
            
        if pos_y < 0:
            pos_y = altura-tamanho 
        
        
        cobraInicio = []
        cobraInicio.append(pos_x)
        cobraInicio.append(pos_y)

        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randrange(0, largura-tamanho, 10) #faz aparecer aleatoriamente
            maca_y = randrange(0, altura-tamanho, 10) #faz aparecer aleatoriamente
            cobraComp += 1

        cobraXY.append(cobraInicio)
        if len (cobraXY) > cobraComp:
            del cobraXY[0]
        
        if any (Bloco == cobraInicio for Bloco in cobraXY[:-1]):
            fimdejogo = True

        cobra(cobraXY)

        maca(maca_x, maca_y)
        relogio.tick(velocidade)

        # condicionais para fazer o player atravessar a parede e aparecer do outro lado           

        pygame.display.update()

jogo()

pygame.quit()
