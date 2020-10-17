import pygame
import Blocks
import Characters

pygame.init()

pygame.display.set_caption('Pyxel')

window_size = (600, 400)

screen = pygame.display.set_mode(window_size)
display = pygame.Surface((300,200))


clock = pygame.time.Clock()

hero = Characters.Hero(200, 200)

#improviso
block_list = [
    Blocks.Ground(80, (400 - 32)),
    Blocks.Ground(80, (400 - 48)),
    Blocks.Ground(144, (400 - 112)),
    Blocks.Ground(160, (400 - 112)),
    Blocks.Ground(176, (400 - 112))
]
for x in range(int(600/16)):
    block_list.append(Blocks.Ground((x * 16), (400 - 16)))

true_scroll = [0,0]
def scroll_view(player):
    true_scroll[0] += (player.player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player.player_rect.y-true_scroll[1]-80)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    return scroll

def renderDrawWindow(scroll):
    display.fill((107,222,255))
    for block in block_list:
        block.draw(display, scroll)
    hero.draw(display, scroll)
    screen.blit(pygame.transform.scale(display,window_size),(0,0))
    pygame.display.update()

#---------------------------

openedScreen = True

while openedScreen:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            openedScreen = False

    scroll = scroll_view(hero)

    keys = pygame.key.get_pressed()
    hero.movement(keys, block_list)
    
    renderDrawWindow(scroll)
    clock.tick(60)

pygame.quit()