import pygame
import numpy as np
import time


def game_life():
    """ Juego de la vida
    Reglas:
    1. Una celula muerta con 3 vecinas revive
    2. Una celula viva con mas de 3 vecinos o menos de 2 muere
    """
    # Variables de entorno
    WIDTH, HEIGHT = 600, 600
    ceilsX, ceilsY = 30, 30
    xSize = 600/ceilsX
    ySize = 580/ceilsY

    pygame.init()  # Inicializar el juego

    screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Establecer tamaño del juego.


    BG_COLOR = (0, 43, 54)  # Definir color de fondo
    LIVE_COLOR = (181, 137, 0) # Definir color de celulas vivas
    DEAD_COLOR = (147, 161, 161) # Definir color de celular muertas
    GAME_FONT = pygame.freetype.Font("NewYork.otf", 16) # Tipografia para el score


    # Celdas vivas = 1  | Celdas muertas = 0
    status = np.zeros((ceilsX, ceilsY))  # Inicializar estado de las celdas


    pauseRun = False  # Pausar la ejecuciòn
    running = True  # Mostrar siempre la pantalla en ejecuciòn
    loop = 0 # Contador de ciclos



    while running:
        cont_cell = 0 # Contador de celulas vivas
        newStatus = np.copy(status)  # Copia del estado

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                pauseRun = not pauseRun
        
            mouseClick = pygame.mouse.get_pressed()
            if sum(mouseClick) > 0:
                posX, posY = pygame.mouse.get_pos()
                x, y = int(np.floor(posX/xSize)), int(np.floor(posY/ySize))
                newStatus[x, y] = not mouseClick[2]
                

        screen.fill(BG_COLOR)  # Limpiar fondo
        for x in range(0, ceilsX):
            for y in range(0, ceilsY):
                
                if not pauseRun:
                    

                    # Numero de vecinos
                    nNeigh = status[(x-1) % ceilsX, (y-1) % ceilsY] + status[(x) % ceilsX, (y-1) % ceilsY] + \
                        status[(x+1) % ceilsX, (y-1) % ceilsY] + status[(x-1) % ceilsX, (y) % ceilsY] + \
                        status[(x+1) % ceilsX, (y) % ceilsY] + status[(x-1) % ceilsX, (y+1) % ceilsY] + \
                        status[(x) % ceilsX, (y+1) % ceilsY] + \
                        status[(x+1) % ceilsX, (y+1) % ceilsY]

                    # Rule 1: Una celula muerta con 3 vecinas revive
                    if status[x, y] == 0 and nNeigh == 3:
                        newStatus[x, y] = 1

                    # Rule 2: Una celula viva con mas de 3 vecinos o menos de 2 muere
                    elif status[x, y] == 1 and (nNeigh < 2 or nNeigh > 3):
                        newStatus[x, y] = 0

                poly = [(x*xSize, y*ySize),
                        ((x+1)*xSize, y*ySize),
                        ((x+1)*xSize, (y+1)*ySize),
                        (x*xSize, (y+1)*ySize)]

                if newStatus[x, y] == 1:
                    pygame.draw.polygon(screen, LIVE_COLOR, poly, 0)
                    cont_cell +=1
                    

                else:
                    pygame.draw.polygon(screen, DEAD_COLOR, poly, 1)
        loop += 1           
        status = np.copy(newStatus)
        GAME_FONT.render_to(screen, (10, 585), f"Celulas Vivas: {cont_cell} \t\tCiclos: {loop}", (245, 196, 13))
        time.sleep(0.5)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    help(game_life)
    game_life() # Empezar juego