import sys
import pygame

from Button import Button

pygame.init()
screen = pygame.display.set_mode((800, 600),flags=pygame.DOUBLEBUF)
pygame.display.set_caption("DungeonRush")
clock = pygame.time.Clock()

def start_game():
    print("Игра началась!")

def open_settings():
    print("Открываем настройки...")

def exit_game():
    pygame.quit()
    sys.exit()

buttons = [
    Button("Start", 300, 150, 200, 60, (50, 150, 50), (70, 200, 70), start_game),
    Button("Settings", 300, 250, 200, 60, (50, 50, 150), (70, 70, 200), open_settings),
    Button("Exit", 300, 350, 200, 60, (150, 50, 50), (200, 70, 70), exit_game)
]

running = True
while running:
    screen.fill((30, 30, 30))

    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        for btn in buttons:
            btn.handle_event(event)