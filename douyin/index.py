import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("title")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.circle(screen, (255, 255, 255), (150, 150), 50)
    pygame.draw.circle(screen, (255, 255, 255), (350, 150), 50, 35)

    pygame.draw.rect(screen, (255, 255, 255), (100, 250, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 250, 100, 100), 50, 15)

    pygame.display.update()
