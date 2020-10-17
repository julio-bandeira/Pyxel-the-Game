import pygame

class Hero(object):
    def __init__(self, x, y):
        self.air_time = 0
        self.vertical_momentum = 0
        self.player_rect = pygame.Rect(x, y, 16, 32)
        self.color = pygame.Color(0,0,0,50)


    def movement(self, keys, tiles = []):
        def collision(rect, tiles):
            hit_list = []
            for tile in tiles:
                if rect.colliderect(tile.rect):
                    hit_list.append(tile.rect)
            
            return hit_list
        rect = self.player_rect.copy()
        move = [0,0]

        if keys[pygame.K_LEFT]:
            move[0] -= 2
        elif keys[pygame.K_RIGHT]:
            move[0] += 2
        if keys[pygame.K_UP]:
            if self.air_time < 6:
                self.vertical_momentum = -5
        move[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 3

        collision_types = {
            'top': False,
            'bottom': False,
            'left': False,
            'right': False
        }

        rect.x += move[0]
        hit_list = collision(rect, tiles)
        for tile in hit_list:
            if move[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif move[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True

        rect.y += move[1]
        hit_list = collision(rect, tiles)
        for tile in hit_list:
            if move[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            if move[1] < 0:
                self.vertical_momentum = 0
                rect.top = tile.bottom
                collision_types['top'] = True

        self.player_rect = rect.copy()

        if collision_types['bottom'] == True:
            self.air_time = 0
            self.vertical_momentum = 0
        else:
            self.air_time += 1
                

    def draw(self, display, scroll):
        rect_pos = pygame.Rect(
            (self.player_rect.x - scroll[0]),
            (self.player_rect.y - scroll[1]),
            self.player_rect.width,
            self.player_rect.height
        )
        pygame.draw.rect(display, self.color, rect_pos)
