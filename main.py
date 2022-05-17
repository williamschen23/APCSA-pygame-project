import pygame

size = WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode(size)
pygame.display.set_caption("Tutorial")
FPS = 60
pygame.init()
clock = pygame.time.Clock()
image = pygame.image.load("paddle.png")
rect = image.get_rect()
rect2 = image.get_rect()
rect2.x = WIDTH - 100
print(rect, rect2)

def draw():
    WINDOW.blit(image, rect)
    WINDOW.blit(image, rect2)
    pygame.display.update()
    WINDOW.fill("white")


def main():
    run = True
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
                if event.key == pygame.K_w:
                    rect.y -= 10
                if event.key == pygame.K_s:
                    rect.y += 10
                if event.key == pygame.K_UP:
                    rect2.y -= 10
                if event.key == pygame.K_DOWN:
                    rect2.y += 10

        draw()
    pygame.quit()
    

if __name__ == "__main__":
    main()
