import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("title")
top, left = 100, 100

while True:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and left >= 5:
        left -= 5
    if keys[pygame.K_RIGHT] and left <= 395:
        left += 5
    if keys[pygame.K_UP] and top >= 5:
        top -= 5
    if keys[pygame.K_DOWN] and top <= 395:
        top += 5

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (left, top, 100, 100))
    pygame.display.update()
