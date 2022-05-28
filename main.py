import pygame
from random import choice
import math
size = W, H = 900, 500
WINDOW = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
FPS = 60
player1_score = 0
player2_score = 0
pygame.init()
clock = pygame.time.Clock()
surf_height = 100
player_surf = pygame.image.load("assets/paddle.png").convert_alpha()
player_surf_scale = pygame.transform.smoothscale(player_surf, (5, surf_height))
player1_rect = player_surf_scale.get_rect(midleft=(10, H/2))
player2_rect = player_surf_scale.get_rect(midright=(W-10, H/2))
font = pygame.font.Font('assets/PixelType.ttf', 100)
game_score = font.render(f"{player1_score}   {player2_score}", False, (255, 255, 255))
game_score_rect = game_score.get_rect(center=(W/2, 50))
game_active = True

ball_surf = pygame.image.load("assets/ball.png").convert_alpha()
ball_rect = ball_surf.get_rect(center=(W/2, H/2))
ball_x_speed = choice([-7, 7])
ball_y_speed = choice([-7, 7])

back_surf = pygame.image.load("assets/background.png")
back_rect = back_surf.get_rect(center=(W/2, H/2))
print(player1_rect.w, player2_rect.h)
print(player1_rect, player2_rect)

current_time = int(pygame.time.get_ticks()/1000)
# print(rect.top, rect.bottom, rect.midtop, rect.midbottom, rect.midleft, rect.midright)
#TODO ORGANIZE
speed = 5

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 5000)


def draw():
    WINDOW.blit(back_surf, back_rect)
    WINDOW.blit(game_score, game_score_rect)
    WINDOW.blit(player_surf_scale, player1_rect)
    WINDOW.blit(player_surf_scale, player2_rect)
    WINDOW.blit(ball_surf, ball_rect)
    if not game_active:
        game_screen = font.render("Press Space to Continue", False, (255, 255, 255))
        game_screen_rect = game_screen.get_rect(center=(W/2, H/2))
        WINDOW.blit(game_screen, game_screen_rect)
    pygame.display.update()


run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == timer and game_active:
            if surf_height > 50:
                surf_height -= 5
                player_surf_scale = pygame.transform.smoothscale(player_surf, (5, surf_height))
                player1_rect = player_surf_scale.get_rect(center=player1_rect.center)
                player2_rect = player_surf_scale.get_rect(center=player2_rect.center)
                speed += .2
                speed = math.floor(speed * 10) / 10
                print(speed)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True
        """
            if event.key == pygame.K_g:
                WINDOW.fill("Green")
            if event.key == pygame.K_b:
                WINDOW.fill("black")
            if event.key == pygame.K_r:
                WINDOW.fill("red")
        """
    if game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_rect.top > 0:
            player1_rect.y -= speed
        if keys[pygame.K_s] and player1_rect.bottom < H:
            player1_rect.y += speed
        if keys[pygame.K_UP] and player2_rect.top > 0:
            player2_rect.y -= speed
        if keys[pygame.K_DOWN] and player2_rect.bottom < H:
            player2_rect.y += speed

        ball_rect.x += ball_x_speed
        ball_rect.y += ball_y_speed

        if ball_rect.bottom >= H or ball_rect.top <= 0:
            ball_y_speed = -ball_y_speed
        if ball_rect.colliderect(player1_rect):
            ball_x_speed = -ball_x_speed
        if ball_rect.colliderect(player2_rect):
            ball_x_speed = -ball_x_speed
        if ball_rect.left <= -30:
            player2_score += 1
            game_active = False
        if ball_rect.right >= W + 30:
            player1_score += 1
            game_active = False
    else:
        # reset the game while waiting for input
        game_score = font.render(f"{player1_score}   {player2_score}", False, (255, 255, 255))
        game_score_rect = game_score.get_rect(center=(W/2, 50))
        WINDOW.blit(game_score, game_score_rect)
        surf_height = 100
        ball_rect.center = (W/2, H/2)
        player_surf_scale = pygame.transform.smoothscale(player_surf, (5, surf_height))
        player1_rect = player_surf_scale.get_rect(midleft=(10, H/2))
        player2_rect = player_surf_scale.get_rect(midright=(W - 10, H/2))
        speed = 5

    draw()
print(pygame.font.get_fonts())
pygame.quit()



