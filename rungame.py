import sys, pygame
from pygame.locals import *
import gameengine

size = (500, 500)
FPS = 166

pygame.init()
clock = pygame.time.Clock()

BACKGROUND = (0,0,0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Asteroid Blaster")

rocket_img = pygame.image.load("rocket.png").convert_alpha(screen)
laser_img =  pygame.image.load("laserbeam.png").convert_alpha(screen)
asteroid_img = pygame.image.load("asteroid.png").convert_alpha(screen)

font = pygame.font.SysFont(None, 24)

game = gameengine.GameEngine()
game.start()

while True:
    clock.tick(FPS)

    action_list = [False] * 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pressed = pygame.key.get_pressed()

    if (pressed[K_LEFT] or pressed[K_a]):
        action_list[0] = True

    if (pressed[K_RIGHT] or pressed[K_d]):
        action_list[1] = True

    if (pressed[K_UP] or pressed[K_w]):
        action_list[2] = True

    if (pressed[K_DOWN] or pressed[K_s]):
        action_list[3] = True

    if (pressed[K_SPACE]):
        action_list[4] = True

    action = tuple(action_list)

    game.simulateTimeStep(action)

    screen.fill(BACKGROUND)

    # Iterate over all objects and draw them
    for projectile in game.projectiles:
        #projectile_rect = pygame.Rect(projectile.x, projectile.y, projectile.width, projectile.height)
        #pygame.draw.rect(screen, (255, 0, 0), projectile_rect)
        screen.blit(laser_img, (projectile.x, projectile.y))
        pass
    for asteroid in game.asteroids:
        #pygame.draw.circle(screen, (255, 255, 255), (asteroid.x, asteroid.y), asteroid.r)
        asteroid_trans = pygame.transform.scale(asteroid_img, (2 * asteroid.r, 2 * asteroid.r))
        screen.blit(asteroid_trans, (asteroid.x - asteroid.r, asteroid.y - asteroid.r))

        pass

    fitness_text = font.render(f"Fitness: {game.fitness}", True, (255, 255, 255))
    screen.blit(fitness_text, (10, 10))
    #rocket_rect = pygame.Rect(game.rocket.x, game.rocket.y, game.rocket.width, game.rocket.height)
    #pygame.draw.rect(screen, (0,255, 255), rocket_rect)
    screen.blit(rocket_img, (game.rocket.x, game.rocket.y))

    pygame.display.flip()