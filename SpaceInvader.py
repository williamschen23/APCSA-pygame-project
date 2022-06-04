import pygame
import sys

size = W, H = 900, 600
WINDOW = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
FPS = 30
level = 1
# opponents = [[] for _ in range(5)]

op1 = pygame.image.load("assets/space_invaders/spaceship1.png")
op2 = pygame.image.load("assets/space_invaders/spaceship2.png")
op3 = pygame.image.load("assets/space_invaders/spaceship3.png")

op1 = pygame.transform.smoothscale(op1, (50, 50))
op2 = pygame.transform.smoothscale(op2, (50, 50))
op3 = pygame.transform.smoothscale(op3, (50, 50))

player_score = 0

#TODO movement for the Alient group

class Alien(pygame.sprite.Sprite):
    speed = 10
    def __init__(self, pts, x_val, y_val):
        super().__init__()
        self.points = pts
        if pts == 40:
            self.image = op1
        elif pts == 20:
            self.image = op2
        else:
            self.image = op3
        self.rect = self.image.get_rect(topleft=(x_val, y_val))

    def movement(self):
        self.rect.x += Alien.speed
        if self.rect.left <= 0 or self.rect.right >= W:
            Alien.speed *= -1

            self.rect.x += Alien.speed

    def update(self):
        self.movement()


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        print(player_score)
        super().__init__()
        self.image = pygame.image.load("assets/space_invaders/bullet.png")
        self.image = pygame.transform.smoothscale(self.image, (3, 15))
        self.rect = self.image.get_rect(midtop=spaceship_rect.midtop)

    def shoot(self):
        self.rect.y -= 10

    def collision(self):
        global player_score
        if sprite := pygame.sprite.spritecollideany(self, opponents):
            player_score += sprite.points
            sprite.kill()
            self.kill()

    def update(self):
        self.shoot()
        self.collision()


spaceship_surf = pygame.image.load("assets/space_invaders/player_spaceship.png").convert_alpha()
spaceship_surf = pygame.transform.smoothscale(spaceship_surf, (50, 50))
spaceship_rect = spaceship_surf.get_rect(topleft=(W/2, H-spaceship_surf.get_height() - 20))


bullet = pygame.sprite.GroupSingle()
opponents = pygame.sprite.Group()


def make_aliens():
    y = 20
    for i in range(1, 6):
        x = 20
        for j in range(8):
            if i == 1:
                opponents.add(Alien(40, x, y))
            if i == 2 or i == 3:
                opponents.add(Alien(20, x, y))
            if i == 4 or i == 5:
                opponents.add(Alien(10, x, y))
            x += 70
        y += 52.5 # 52.5




def draw():
    WINDOW.fill("black")
    WINDOW.blit(spaceship_surf, spaceship_rect)
    if bullet.sprite and bullet.sprite.alive():
        bullet.draw(WINDOW)
        bullet.update()

    opponents.draw(WINDOW)
    opponents.update()
    pygame.display.flip()

make_aliens()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        spaceship_rect.x += 5
    if keys[pygame.K_SPACE] and not bullet.sprite:
        bullet.add(Bullet())


    #for sets in opponents:
        #for person in sets:
            #person.x += 1
    # opponents.draw(WINDOW)
    draw()

pygame.quit()
sys.exit()
