import pygame
import sys

size = W, H = 900, 600
WINDOW = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
FPS = 60

opponents = [[] for _ in range(5)]

op1 = pygame.image.load("assets/space_invaders/spaceship1.png")
op2 = pygame.image.load("assets/space_invaders/spaceship2.png")
op3 = pygame.image.load("assets/space_invaders/spaceship3.png")

op1 = pygame.transform.smoothscale(op1, (50, 50))
op2 = pygame.transform.smoothscale(op2, (50, 50))
op3 = pygame.transform.smoothscale(op3, (50, 50))


class Alien(pygame.sprite.Sprite):
    def __init__(self, pts, x_val, y_val):
        super().__init__()
        if pts == 10:
            self.image = op1
        elif pts == 20:
            self.image = op2
        else:
            self.image = op3
        self.rect = self.image.get_rect(topleft=(x_val, y_val))
        self.points = pts



opponents = pygame.sprite.Group()


def make_aliens():
    y = 20
    for i in range(1, 6):
        x = 20
        for j in range(8):
            if i == 1:
                opponents.add(Alien(10, x, y))
            if i == 2 or i == 3:
                opponents.add(Alien(20, x, y))
            if i == 4 or i == 5:
                opponents.add(Alien(40, x, y))
            x += 55
        y += 55




def draw():
    WINDOW.fill("white")
    opponents.draw(WINDOW)
    #for image in range(len(opponents)):
        #for part in range(len(opponents[image])):
            #pass
    pygame.display.flip()

make_aliens()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #for sets in opponents:
        #for person in sets:
            #person.x += 1
    # opponents.draw(WINDOW)
    draw()

pygame.quit()
sys.exit()
