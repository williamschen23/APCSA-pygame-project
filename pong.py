import pygame
from random import choice
from math import floor

# setup
size = W, H = 900, 500
WINDOW = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption("Pong")

# misc
FPS = 60
run = True
clock = pygame.time.Clock()

# background
back_surf = pygame.image.load("assets/pong/background.png")
back_rect = back_surf.get_rect(center=(W/2, H/2))

# paddles and score
surf_height = 100
player1_score = 0
player2_score = 0
player_surf = pygame.image.load("assets/pong/paddle.png").convert_alpha()
player_surf_scale = pygame.transform.smoothscale(player_surf, (5, surf_height))
player1_rect = player_surf_scale.get_rect(midleft=(10, H/2))
player2_rect = player_surf_scale.get_rect(midright=(W-10, H/2))

# display score
font = pygame.font.Font('assets/pong/PixelType.ttf', 100)
game_score = font.render(f"{player1_score}   {player2_score}", False, (255, 255, 255))
game_score_rect = game_score.get_rect(center=(W/2, 50))
game_active = True

# ball
speed = 5
ball_surf = pygame.image.load("assets/pong/ball.png").convert_alpha()
ball_rect = ball_surf.get_rect(center=(W/2, H/2))
ball_x_speed = choice([-7, 7])
ball_y_speed = choice([-7, 7])

# an event triggers every 5 minute
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 5000)


# drawing surfaces
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


while run:
    # controlling the frames
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == timer and game_active:
            # at a certain time interval the paddles gets smaller
            if surf_height > 50:
                surf_height -= 5
                player_surf_scale = pygame.transform.smoothscale(player_surf, (5, surf_height))
                player1_rect = player_surf_scale.get_rect(center=player1_rect.center)
                player2_rect = player_surf_scale.get_rect(center=player2_rect.center)
                speed += .2
                speed = floor(speed * 10) / 10
                print(speed)

        # reactivate the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True

    # if the game is active check keyboard inputs
    if game_active:
        keys = pygame.key.get_pressed()
        # paddle movements
        if keys[pygame.K_w] and player1_rect.top > 0:
            player1_rect.y -= speed
        if keys[pygame.K_s] and player1_rect.bottom < H:
            player1_rect.y += speed
        if keys[pygame.K_UP] and player2_rect.top > 0:
            player2_rect.y -= speed
        if keys[pygame.K_DOWN] and player2_rect.bottom < H:
            player2_rect.y += speed

        # ball movements
        ball_rect.x += ball_x_speed
        ball_rect.y += ball_y_speed

        # checks if the ball hit the wall or go past the paddle
        if ball_rect.bottom >= H or ball_rect.top <= 0:
            ball_y_speed = -ball_y_speed

        if ball_rect.colliderect(player2_rect) and ball_x_speed > 0:
            if abs(ball_rect.right - player2_rect.left) < 10:
                ball_x_speed *= -1
            elif abs(ball_rect.bottom - player2_rect.top) < 10 and ball_y_speed > 0:
                ball_y_speed *= -1
            elif abs(ball_rect.top - player2_rect.bottom) < 10 and ball_y_speed < 0:
                ball_y_speed *= -1

        if ball_rect.colliderect(player1_rect) and ball_x_speed < 0:
            if abs(ball_rect.left - player1_rect.right) < 10:
                ball_x_speed *= -1
            elif abs(ball_rect.bottom - player1_rect.top) < 10 and ball_y_speed > 0:
                ball_y_speed *= -1
            elif abs(ball_rect.top - player1_rect.bottom) < 10 and ball_y_speed < 0:
                ball_y_speed *= -1

        if ball_rect.left <= -30:
            player2_score += 1
            game_active = False

        if ball_rect.right >= W + 30:
            player1_score += 1
            game_active = False

    # reset the game while waiting for input
    else:
        # game score
        game_score = font.render(f"{player1_score}   {player2_score}", False, (255, 255, 255))
        game_score_rect = game_score.get_rect(center=(W/2, 50))
        WINDOW.blit(game_score, game_score_rect)

        # reset the paddle to original length and the speed of paddle
        surf_height = 100
        speed = 5
        player_surf_scale = pygame.transform.smoothscale(player_surf, (5, surf_height))
        player1_rect = player_surf_scale.get_rect(midleft=(10, H/2))
        player2_rect = player_surf_scale.get_rect(midright=(W - 10, H/2))

        # resets the ball
        ball_rect.center = (W/2, H/2)
        ball_x_speed = choice([-7, 7])
        ball_y_speed = choice([-7, 7])

    # draws the elements
    draw()

pygame.quit()
