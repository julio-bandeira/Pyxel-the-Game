import pygame

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Pyxel')
clock = pygame.time.Clock()

def renderDrawWindow():
    screen.fill((107,222,255))
    pygame.display.update()

openedScreen = True

while openedScreen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            openedScreen = False
    
    renderDrawWindow()
    clock.tick(60)

pygame.quit()