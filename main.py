import sys

import pygame
from pygame import Rect
from pygame.color import THECOLORS

pygame.init()

# Settings
screen_size = (800, 600)
font = "couriernew"
font_size = 40

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("My Awesome Game")

r = Rect(300, 400, 200, 50)
pygame.draw.rect(screen, (255, 0, 0), r)

sys_font = pygame.font.SysFont(font, font_size)
text = sys_font.render(str('Start'), True, THECOLORS['green'])
screen.blit(text, (340, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if r.collidepoint(event.pos):
                print("Start button clicked!")
    pygame.display.flip()
