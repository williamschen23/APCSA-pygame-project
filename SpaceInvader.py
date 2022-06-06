import pygame
from sys import exit
size = W, H = 700, 500
WINDOW = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
pygame.init()

# game features
score = 0
level = 1

# controlling surfaces
surf_width = 35
surf_height = 30
gap = 15

# 3 different surfaces for aliens, all scaled
op1 = pygame.image.load("assets/space_invaders/spaceship1.png").convert_alpha()
op2 = pygame.image.load("assets/space_invaders/spaceship2.png").convert_alpha()
op3 = pygame.image.load("assets/space_invaders/spaceship3.png").convert_alpha()

op1 = pygame.transform.smoothscale(op1, (25, 25))
op2 = pygame.transform.smoothscale(op2, (surf_width, surf_height))
op3 = pygame.transform.smoothscale(op3, (surf_width, surf_height))

# background (calvin)
background_surf = pygame.image.load('assets/space_invaders/background.png').convert_alpha()
background_surf = pygame.transform.smoothscale(background_surf, size)
background_rect = background_surf.get_rect(center=(W/2, H/2))

# spaceship
spaceship_surf = pygame.image.load('assets/space_invaders/player_spaceship.png').convert_alpha()
spaceship_surf = pygame.transform.smoothscale(spaceship_surf, (surf_width, surf_height))
spaceship_rect = spaceship_surf.get_rect(topleft=(W/2, H-surf_height - 20))

# game controls
alien_speed = 20
game = True
run = True
ms = 500
alien_list = []
bullet = None

# font and text
font = pygame.font.Font('assets/pong/PixelType.ttf', 40)
game_score_surf = font.render(f"Score: {score}", False, 'white')
game_score_rect = game_score_surf.get_rect(topleft=(20, 20))
wave_score_surf = font.render(f"Wave: {level}", False, 'white')
wave_score_rect = wave_score_surf.get_rect(topleft=(20, 60))

# game timer
alien_move_timer = pygame.USEREVENT + 1
pygame.time.set_timer(alien_move_timer, 500)


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
        # pygame.draw.rect(WINDOW, 'red', (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
        WINDOW.blit(self.image, self.rect)


class Bullet:
    def __init__(self):
        self.image = pygame.image.load('assets/space_invaders/bullet.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (3, 15))
        self.rect = self.image.get_rect(midtop=spaceship_rect.midtop)

    def shoot(self):
        self.rect.y -= 5

    def update(self):
        self.shoot()
        WINDOW.blit(self.image, self.rect)


def make_aliens():
    y = level * 20
    for i in range(1, 6):
        x = 20
        for j in range(8):
            if i == 1:
                alien_list.append(Alien(40, x, y))
            if i == 2 or i == 3:
                alien_list.append(Alien(20, x, y))
            if i == 4 or i == 5:
                alien_list.append(Alien(10, x, y))
            x += surf_width + gap
        y += surf_height + gap


def bullet_logic():
    global bullet, score
    if bullet:
        bullet.update()
        if bullet.rect.top <= 0:
            bullet = None
        else:
            for i, alien in enumerate(alien_list):
                if bullet.rect.colliderect(alien.rect):
                    score += alien.points
                    alien_list.pop(i)
                    bullet = None
                    break


def would_collide():
    global game
    result = False
    for alien in alien_list:
        if alien.rect.right + alien_speed > W:
            result = True
        if alien.rect.left + alien_speed < 0:
            result = True
        if spaceship_rect.top - alien.rect.bottom <= 0:
            game = False
    if result:
        for alien in alien_list:
            alien.rect.y += 30
    return result


make_aliens()

while run:
    print(game)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == alien_move_timer and game:
            if would_collide():
                if ms > 150:
                    ms -= 50
                alien_speed *= -1
                pygame.time.set_timer(alien_move_timer, ms)
            else:
                for alien in alien_list:
                    alien.rect.x += alien_speed
    if game:
        if not alien_list:
            level += 1
            make_aliens()
            ms = 500
            pygame.time.set_timer(alien_move_timer, ms)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spaceship_rect.left > 0:
            spaceship_rect.x -= 3
        if keys[pygame.K_RIGHT] and spaceship_rect.right < W:
            spaceship_rect.x += 3
        if keys[pygame.K_SPACE] and not bullet:
            bullet = Bullet()

        WINDOW.blit(background_surf, background_rect)
        bullet_logic()
        if alien_list:
            for alien in alien_list:
                alien.update()
        WINDOW.blit(spaceship_surf, spaceship_rect)
        game_score = font.render(f"Score: {score}", False, (255, 255, 255))
        WINDOW.blit(game_score_surf, game_score_rect)
        WINDOW.blit(wave_score_surf, wave_score_rect)
        pygame.display.flip()
    else:
        WINDOW.fill('black')
        game_over = font.render("GAME OVER", False, 'white')
        WINDOW.blit(game_over, game_over.get_rect(center=(W/2, H/2-20)))
        WINDOW.blit(game_score_surf, game_score_surf.get_rect(center=(W/2, H/2+20)))
        pygame.display.flip()

pygame.quit()
exit()
