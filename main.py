import pygame
import Characters

pygame.init()

window_size = (600, 500)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pyxel')
clock = pygame.time.Clock()

hero = Characters.Hero(200, 200)

block_list = [
    pygame.Rect((80), (500 - 40), 20, 20),
    pygame.Rect((80), (500 - 60), 20, 20),
    pygame.Rect((140), (500 - 120), 20, 20),
    pygame.Rect((160), (500 - 120), 20, 20),
    pygame.Rect((180), (500 - 120), 20, 20)
]
for x in range(int(600/20)):
    block_list.append(pygame.Rect((x * 20), (500 - 20), 20, 20))

def renderDrawWindow():
    screen.fill((107,222,255))
    for block in block_list:
        pygame.draw.rect(screen, (0,0,255), block)
    hero.draw(screen)
    pygame.display.update()

openedScreen = True

while openedScreen:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            openedScreen = False

    keys = pygame.key.get_pressed()
    hero.movement(keys, block_list)
    
    renderDrawWindow()
    clock.tick(60)

pygame.quit()