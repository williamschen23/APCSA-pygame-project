import pygame
size = W, H = 900, 500
WINDOW = pygame.display.set_mode(size)
pygame.display.set_caption("Tutorial")
FPS = 60
pygame.init()
clock = pygame.time.Clock()
surf_height = 50
player_surf = pygame.image.load("assets/paddle.png").convert_alpha()
player_surf_scale = pygame.transform.smoothscale(player_surf, (5, 100))
player1_rect = player_surf_scale.get_rect(midleft=(10, H/2))
player2_rect = player_surf_scale.get_rect(midright=(W-10, H/2))

ball_surf = pygame.image.load("assets/ball.png").convert_alpha()
ball_rect = ball_surf.get_rect(center=(W/2, H/2))
ball_x_speed = 7
ball_y_speed = 7

back_surf = pygame.image.load("assets/background.png")
back_rect = back_surf.get_rect(center=(W/2, H/2))
print(player1_rect.w, player2_rect.h)
print(player1_rect, player2_rect)

current_time = int(pygame.time.get_ticks()/1000)
# print(rect.top, rect.bottom, rect.midtop, rect.midbottom, rect.midleft, rect.midright)
#TODO ADD SCORE AND ORGANIZE
MOVE = 5

def draw():
    WINDOW.blit(back_surf, back_rect)
    WINDOW.blit(player_surf_scale, player1_rect)
    WINDOW.blit(player_surf_scale, player2_rect)
    WINDOW.blit(ball_surf, ball_rect)
    pygame.draw.rect(WINDOW, "black", player1_rect, 1)
    pygame.display.update()


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
                WINDOW.fill("black")
            if event.key == pygame.K_r:
                WINDOW.fill("red")
    #print(current_time)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_rect.top > 0:
        player1_rect.y -= MOVE
    if keys[pygame.K_s] and player1_rect.bottom < H:
        player1_rect.y += MOVE
    if keys[pygame.K_UP] and player2_rect.top > 0:
        player2_rect.y -= MOVE
    if keys[pygame.K_DOWN] and player2_rect.bottom < H:
        player2_rect.y += MOVE

    ball_rect.x += ball_x_speed
    ball_rect.y += ball_y_speed

    #if ball_rect.left <= 0 or ball_rect.right >= W:
        #ball_x_speed = -ball_x_speed
    if ball_rect.bottom >= H or ball_rect.top <= 0:
        ball_y_speed = -ball_y_speed
    if ball_rect.colliderect(player1_rect):
        ball_x_speed = -ball_x_speed
    if ball_rect.colliderect(player2_rect):
        ball_x_speed = -ball_x_speed

    # print(player1_rect.bottom)

    draw()
print(pygame.font.get_fonts())
pygame.quit()



