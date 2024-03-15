import pygame
import random
from apple import Apple

GRAVITY = 0.1




# pygame setup
pygame.init()
screen = pygame.display.set_mode((1250, 700))

background = pygame.image.load("assets/bg_horizontal.jpeg")
background = pygame.transform.scale(background, (1250, 700))
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
running = True
dt = 0
apple_list = []

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40
apple = Apple(screen)
apple_generation_timer = 0



def check_collision(apple, player_pos, player_radius):
    distance = ((apple.x - player_pos.x) ** 2 +  (apple.y - player_pos.y) ** 2) ** 0.5

    if distance <= apple.radius + player_radius:
        return True
    return False

while running:
    if apple_generation_timer > 100:
        # apple = Apple(screen)
        apple_list.append(Apple(screen))
        apple_generation_timer = 0
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))


    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, player_radius)
    # apple.draw()

    for one_apple in apple_list:
        one_apple.draw()
        one_apple.fall()
        if check_collision(one_apple, player_pos, player_radius):
            apple_list.remove(one_apple)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame used for framerate-independent physics
    dt = clock.tick(60) / 1000
    apple_generation_timer += 1

pygame.quit()