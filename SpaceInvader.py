import pygame
from sys import exit
size = W, H = 700, 500
WINDOW = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
pygame.init()

surf_width = 35
op1 = pygame.image.load("assets/space_invaders/spaceship1.png")
op2 = pygame.image.load("assets/space_invaders/spaceship2.png")
op3 = pygame.image.load("assets/space_invaders/spaceship3.png")

op1 = pygame.transform.smoothscale(op1, (surf_width, surf_width))
op2 = pygame.transform.smoothscale(op2, (surf_width, surf_width))
op3 = pygame.transform.smoothscale(op3, (surf_width, surf_width))

background_surf = pygame.image.load('assets/space_invaders/background.png')
background_surf = pygame.transform.smoothscale(background_surf, size)
background_rect = background_surf.get_rect(center=(W/2, H/2))

spaceship_surf = pygame.image.load('assets/space_invaders/player_spaceship.png')
spaceship_surf = pygame.transform.smoothscale(spaceship_surf, (surf_width, surf_width))
spaceship_rect = spaceship_surf.get_rect(topleft=(W/2, H-spaceship_surf.get_height() - 20))

#TODO move the aliens + display score
class Alien:
    def __init__(self, points, x, y):
        if points == 40:
            self.image = op1
        elif points == 20:
            self.image = op2
        else:
            self.image = op3
        self.points = points
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # pygame.draw.rect(WINDOW, 'red', (self.rect.x, self.rect.y, surf_width, surf_width))
        WINDOW.blit(self.image, self.rect)

class Bullet:
    def __init__(self):
        self.image = pygame.image.load('assets/space_invaders/bullet.png')
        self.image = pygame.transform.smoothscale(self.image, (3, 15))
        self.rect = self.image.get_rect(midtop=spaceship_rect.midtop)

    def shoot(self):
        self.rect.y -= 5

    def update(self):
        self.shoot()

        WINDOW.blit(self.image, self.rect)

alien_list = []
bullet = None

def make_aliens():
    y = 20
    for i in range(1, 6):
        x = 20
        for j in range(8):
            if i == 1:
                alien_list.append(Alien(40, x, y))
            if i == 2 or i == 3:
                alien_list.append(Alien(20, x, y))
            if i == 4 or i == 5:
                alien_list.append(Alien(10, x, y))
            x += surf_width + 15
        y += surf_width + 15 # 52.5

def bullet_logic():
    global bullet
    if bullet:
        if bullet.rect.top <= 0:
            bullet = None
        else:
            for i, alien in enumerate(alien_list):
                if bullet.rect.colliderect(alien.rect):
                    alien_list.pop(i)
                    bullet = None
                    break




def draw():
    WINDOW.fill("black")
    if bullet:
        bullet.update()
    if alien_list:
        for alien in alien_list:
            alien.update()
    WINDOW.blit(spaceship_surf, spaceship_rect)

    pygame.display.flip()

make_aliens()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_rect.left > 0:
        spaceship_rect.x -= 3
    if keys[pygame.K_RIGHT] and spaceship_rect.right < W:
        spaceship_rect.x += 3
    if keys[pygame.K_SPACE] and not bullet:
        bullet = Bullet()

    bullet_logic()
    draw()

pygame.quit()
exit()
