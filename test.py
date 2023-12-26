import pygame
import sys
ROOM_NUMBER = 0
CELL_SIZE = 32
BOARD_SIZE = 9
HEIGHT = BOARD_SIZE * CELL_SIZE
WIDTH = BOARD_SIZE * CELL_SIZE


def leftoff_screen(data):
    global ROOM_NUMBER
    pygame.init()
    screen_leftoff = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("left_off")
    clock = pygame.time.Clock()
    screen_leftoff.fill((255, 255, 255))
    font = pygame.font.Font(None, 30)
    text = font.render(
        f"Do you wish to start where", True, (0, 0, 0))
    text2 = font.render(
        f"you have left off?", True, (0, 0, 0))
    screen_leftoff.blit(text, (17, 50))
    screen_leftoff.blit(text2, (50, 75))
    # yes and no button
    yes = font.render(f"yes", True, (0, 0, 0))
    no = font.render(f"no", True, (0, 0, 0))
    screen_leftoff.blit(yes, (60, 150))
    screen_leftoff.blit(no, (180, 150))
    button_yes = pygame.Rect((60, 150), (30, 40))
    button_no = pygame.Rect((180, 150), (25, 40))
    pygame.display.flip()
    a = True
    while a == True:
        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_yes.collidepoint(event.pos):
                    ROOM_NUMBER = data
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_no.collidepoint(event.pos):
                    ROOM_NUMBER = 0
    clock.tick(10)


def start_leftoff():
    file = open('storage.txt', 'r+')
    data = file.read()
    leftoff_screen(data)
    file.close()


leftoff_screen()
