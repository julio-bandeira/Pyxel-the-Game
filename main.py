import pygame
import Characters

pygame.init()

pygame.display.set_caption('Pyxel')

window_size = (600, 400)

screen = pygame.display.set_mode(window_size)
display = pygame.Surface((300,200))

true_scroll = [0,0]

clock = pygame.time.Clock()

hero = Characters.Hero(200, 200)

#improviso
block_list = [
    pygame.Rect((80), (400 - 40), 20, 20),
    pygame.Rect((80), (400 - 60), 20, 20),
    pygame.Rect((140), (400 - 120), 20, 20),
    pygame.Rect((160), (400 - 120), 20, 20),
    pygame.Rect((180), (400 - 120), 20, 20)
]
for x in range(int(600/20)):
    block_list.append(pygame.Rect((x * 20), (400 - 20), 20, 20))

def renderDrawWindow(scroll):
    display.fill((107,222,255))
    for block in block_list:
        pygame.draw.rect(display, (0,0,255), (
                (block.x - scroll[0]),
                (block.y - scroll[1]),
                block.width,
                block.height
            )
        )
    hero.draw(display, scroll)
    screen.blit(pygame.transform.scale(display,window_size),(0,0))
    pygame.display.update()

#---------------------------

openedScreen = True

while openedScreen:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            openedScreen = False

    true_scroll[0] += (hero.player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (hero.player_rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    keys = pygame.key.get_pressed()
    hero.movement(keys, block_list)
    
    renderDrawWindow(scroll)
    clock.tick(60)

pygame.quit()