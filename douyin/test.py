import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("title")
top, left = 100, 100
img = pygame.image.load("hy.png")
img = pygame.transform.scale(img, (100, 100))

while True:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and left >= 5 and not(left == 305 and 100 <= top <= 350):
        left -= 5
    if keys[pygame.K_RIGHT] and left <= 395 and not(left == 200 and 100 <= top <= 350):
        left += 5
    if keys[pygame.K_UP] and top >= 5 and not(top == 350 and 200 <= left <= 305):
        top -= 5
    if keys[pygame.K_DOWN] and top <= 395 and not(top == 100 and 200 <= left <= 305):
        top += 5

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (300, 200, 5, 150))
    screen.blit(img, (left, top))
    pygame.display.update()
