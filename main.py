import pygame
from math import floor, ceil
size = W, H = 900, 500
WINDOW = pygame.display.set_mode(size)
pygame.display.set_caption("Tutorial")
FPS = 60
pygame.init()
clock = pygame.time.Clock()
image = pygame.image.load("paddle.png").convert_alpha()
rect = image.get_rect()
rect2 = image.get_rect()
rect2.x = W - 100
rect.y = H/2 - rect.h/2
rect2.y = H/2 - rect2.h/2
print(rect, rect2)
print(rect.top, rect.bottom, rect.midtop, rect.midbottom, rect.midleft, rect.midright)
#TODO GRAPHICS


def draw():
    WINDOW.blit(image, rect)
    WINDOW.blit(image, rect2)
    pygame.display.update()
    WINDOW.fill("white")


def main():
    run = True
    speed = 0
    speed2 = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    WINDOW.fill("Green")
                if event.key == pygame.K_b:
                    WINDOW.fill("blue")
                if event.key == pygame.K_r:
                    WINDOW.fill("red")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_s]:
            speed = 0
        elif keys[pygame.K_w]:
            speed = 1
        elif keys[pygame.K_s]:
            speed = -1
        else:
            speed = 0
        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            speed2 = 0
        elif keys[pygame.K_UP]:
            speed2 = 1
        elif keys[pygame.K_DOWN]:
            speed2 = -1
        else:
            speed2 = 0

        rect.y += -speed * 5
        rect2.y += -speed2 * 5
        draw()
    pygame.quit()


if __name__ == "__main__":
    main()
