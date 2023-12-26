import pygame
import sys
from rooms import *
import time
# Constants
ROWS, COLS = 9, 9
CELL_SIZE = 32
BOARD_SIZE = 9
HEIGHT = BOARD_SIZE * CELL_SIZE
WIDTH = BOARD_SIZE * CELL_SIZE
ROOM_NUMBER = 0

# makes a menu


def roomcounter():
    global ROOM_NUMBER
    screen_room = pygame.display.set_mode((WIDTH, HEIGHT))
    screen_room.fill((255, 255, 255))
    font = pygame.font.Font(None, 40)
    text = font.render(f"ROOM {ROOM_NUMBER + 1}", True, (0, 0, 0))
    screen_room.blit(text, (85, 136))
    pygame.display.flip()


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
    screen_leftoff.blit(yes, (50, 175))
    screen_leftoff.blit(no, (200, 175))
    button_yes = pygame.Rect((50, 175), (30, 40))
    button_no = pygame.Rect((200, 175), (25, 40))
    # room num blit
    room_num = font.render(f"ROOM {data}", True, (0, 0, 0))
    screen_leftoff.blit(room_num, (85, 125))
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
                    ROOM_NUMBER = int(data)
                    a = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_no.collidepoint(event.pos):
                    ROOM_NUMBER = 0
                    a = False
    clock.tick(10)


def start_leftoff():
    file = open('storage.txt', 'r+')
    data = file.read()
    leftoff_screen(data)
    file.close()


def storage_update():
    global ROOM_NUMBER
    file = open('storage.txt', 'w')
    file.write(f'{ROOM_NUMBER}')
    file.close()


def menu():
    pygame.init()
    screen_menu = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu_Robotron")
    clock = pygame.time.Clock()
    play_button = pygame.image.load('play_button.png').convert_alpha()
    logo = pygame.image.load('logo2.png').convert_alpha()
    screen_menu.fill((255, 255, 255))
    screen_menu.blit(play_button, (119, 6 * CELL_SIZE))
    screen_menu.blit(logo, (16, 0))
    button = pygame.Rect((119, 6 * CELL_SIZE), (50, 50))
    font = pygame.font.Font(None, 25)
    text = font.render("press r to reset the room", True, (0, 0, 0))
    screen_menu.blit(text, (40, 140))
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

            # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button.collidepoint(event.pos):
                    a = False

    start_leftoff()
    clock.tick(10)


# menu
menu()
# inicialize mixer sound
pygame.mixer.init()

# create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robotron")
clock = pygame.time.Clock()

# LOAD IMAGES
wall_image = pygame.image.load('wall.bmp').convert_alpha()
robo_image = pygame.image.load('robo.bmp').convert_alpha()
door_image = pygame.image.load('door.bmp').convert_alpha()
space_image = pygame.image.load('space.bmp').convert_alpha()
dinamico_image = pygame.image.load('dinamico.bmp').convert_alpha()
dinexplo_image = pygame.image.load('dinexplo.bmp').convert_alpha()
explo_image = pygame.image.load('explo.bmp').convert_alpha()
game_over = pygame.image.load('game_over.png').convert_alpha()
restar_button = pygame.image.load('restart_button.png').convert_alpha()
boom1 = pygame.image.load('boom1.bmp').convert_alpha()
boom2 = pygame.image.load('boom2.bmp').convert_alpha()
boom3 = pygame.image.load('boom3.bmp').convert_alpha()
boom4 = pygame.image.load('boom4.bmp').convert_alpha()
boom5 = pygame.image.load('boom5.bmp').convert_alpha()
# load sounds
boom = pygame.mixer.Sound('boomsound.wav')
image_map = {
    0: wall_image,        # Wall index = 0
    1: robo_image,        # Robo index = 1
    2: door_image,        # Door index = 2
    3: space_image,       # Space index = 3
    4: dinamico_image,   # Dinamico index = 4
    5: dinexplo_image,    # Dinexplo index = 5
    6: explo_image         # Explo index = 6
}
# function for game over screen


def game_over_screen():
    global ROOM_NUMBER, robo_pos
    screen_gameover = pygame.display.set_mode((WIDTH, HEIGHT))
    screen_gameover.fill((255, 255, 255))
    screen_gameover.blit(game_over, (44, 0))
    screen_gameover.blit(restar_button, (119, 6 * CELL_SIZE))
    button = pygame.Rect((119, 6 * CELL_SIZE), (50, 50))
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

            # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button.collidepoint(event.pos):
                    ROOM_NUMBER = 0
                    draw_board(room[ROOM_NUMBER])
                    robo_pos = [0, 4]
                    a = False


# Create a 2D list representing the board
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
# Function to draw the board with walls


def draw_board(room):
    global board

    col = 1
    row = 1

    for i in room:
        if row == 8:
            col += 1
            row = 1

        if row != 8:
            if i == "0":
                board[col][row] = 3  # space
            elif i == "1":
                board[col][row] = 0  # wall
            elif i == "2":
                board[col][row] = 4  # dinamico
            elif i == "3":
                board[col][row] = 6  # explo
            elif i == "4":
                board[col][row] = 5  # dinexplo

            row += 1


# Draw a grid
draw_board(room[ROOM_NUMBER])


def draw_screenboard(board):
    door_positions = [(0, 4), (8, 4)]  # Define door positions

    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == 3:
                screen.blit(space_image, (col_index *
                            CELL_SIZE, row_index * CELL_SIZE))
            elif cell == 0:
                screen.blit(wall_image, (col_index *
                            CELL_SIZE, row_index * CELL_SIZE))
            elif cell == 4:
                screen.blit(dinamico_image, (col_index *
                            CELL_SIZE, row_index * CELL_SIZE))
            elif cell == 5:
                screen.blit(dinexplo_image, (col_index *
                            CELL_SIZE, row_index * CELL_SIZE))
            elif cell == 6:
                screen.blit(explo_image, (col_index *
                            CELL_SIZE, row_index * CELL_SIZE))

    # Place door images on specific positions
    for door_pos in door_positions:
        screen.blit(
            door_image, (door_pos[0] * CELL_SIZE, door_pos[1] * CELL_SIZE))
        board[door_pos[1]][door_pos[0]] = 2  # Set board position as a door


for row in board:
    print(row)


def move_robot(dx, dy):
    new_x = robo_pos[0] + dx
    new_y = robo_pos[1] + dy
    global ROOM_NUMBER, boom1, boom2, boom3, boom4, boom5

    if 0 <= new_x < COLS and 0 <= new_y < ROWS and board[new_y][new_x] != 0:
        if board[new_y][new_x] == 4:
            last_position = find_last_position(new_x, new_y, dx, dy)
            if last_position and board[last_position[1]][last_position[0]] != 2:
                if board[last_position[1]][last_position[0]] == 6 or board[last_position[1]][last_position[0]] == 5:
                    screen.blit(
                        space_image, (new_x*CELL_SIZE, new_y*CELL_SIZE))
                    screen.blit(
                        boom1, (last_position[0]*CELL_SIZE, last_position[1]*CELL_SIZE))
                    pygame.display.flip()
                    pygame.mixer.Sound.play(boom)
                    time.sleep(0.02)
                    screen.blit(
                        boom2, (last_position[0]*CELL_SIZE, last_position[1]*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        boom3, (last_position[0]*CELL_SIZE, last_position[1]*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        boom4, (last_position[0]*CELL_SIZE, last_position[1]*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        boom5, (last_position[0]*CELL_SIZE, last_position[1]*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        space_image, (last_position[0]*CELL_SIZE, last_position[1]*CELL_SIZE))
                    pygame.display.flip()
                    board[new_y+(dy)][new_x+(dx)] = 3
                else:
                    board[last_position[1]][last_position[0]] = 4
                board[robo_pos[1]][robo_pos[0]] = 3
                robo_pos[0] = new_x
                robo_pos[1] = new_y
                board[robo_pos[1]][robo_pos[0]] = 1
        elif board[new_y][new_x] == 3:
            board[new_y][new_x] = 1
            board[robo_pos[1]][robo_pos[0]] = 3
            robo_pos[0] = new_x
            robo_pos[1] = new_y
        elif board[new_y][new_x] == 2 and board[robo_pos[1]][robo_pos[0]-1] != 2:
            ROOM_NUMBER += 1
            board[robo_pos[1]][robo_pos[0]] = 3
            robo_pos[0] = new_x - (8*dx)
            robo_pos[1] = new_y
            roomcounter()
            storage_update()
            time.sleep(1)
            draw_board(room[ROOM_NUMBER])

        elif board[new_y][new_x] == 5:
            if board[new_y+(dy)][new_x+(dx)] != 2 and board[new_y+(dy)][new_x+(dx)] != 0:
                if board[new_y+(dy)][new_x+(dx)] == 4 or board[new_y+(dy)][new_x+(dx)] == 5 or board[new_y+(dy)][new_x+(dx)] == 6:
                    screen.blit(
                        space_image, (new_x*CELL_SIZE, new_y*CELL_SIZE))
                    screen.blit(
                        boom1, ((new_x+(dx))*CELL_SIZE, (new_y+(dy))*CELL_SIZE))
                    pygame.display.flip()
                    pygame.mixer.Sound.play(boom)
                    time.sleep(0.02)
                    screen.blit(
                        boom2, ((new_x+(dx))*CELL_SIZE, (new_y+(dy))*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        boom3, ((new_x+(dx))*CELL_SIZE, (new_y+(dy))*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        boom4, ((new_x+(dx))*CELL_SIZE, (new_y+(dy))*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        boom5, ((new_x+(dx))*CELL_SIZE, (new_y+(dy))*CELL_SIZE))
                    pygame.display.flip()
                    time.sleep(0.02)
                    screen.blit(
                        space_image, ((new_x+(dx))*CELL_SIZE, (new_y+(dy))*CELL_SIZE))
                    pygame.display.flip()
                    board[new_y+(dy)][new_x+(dx)] = 3
                else:
                    board[new_y+(dy)][new_x+(dx)] = 5
                board[robo_pos[1]][robo_pos[0]] = 3
                robo_pos[0] = new_x
                robo_pos[1] = new_y
                board[robo_pos[1]][robo_pos[0]] = 1
        elif board[new_y][new_x] == 6:
            game_over_screen()


def find_last_position(x, y, dx, dy):
    while 0 <= x < COLS and 0 <= y < ROWS:
        if board[y][x] == 3:
            return [x, y]
        elif board[y][x] == 4:
            x += dx
            y += dy
        elif board[y][x] == 5 or board[y][x] == 6:
            return [x, y]
        elif board[y][x] == 2 or board[y][x] == 0:
            break
    return None


# Robo start position
robo_pos = [0, 4]

# Test
# wall_pos = [4,4]
running = True
while running:
    # Fill the screen with white
    screen.fill((255, 255, 255))
    # Draw board
    draw_screenboard(board)

    # Place the robot at its current position
    screen.blit(robo_image, (robo_pos[0]*CELL_SIZE, robo_pos[1]*CELL_SIZE))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_robot(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_robot(1, 0)
            elif event.key == pygame.K_UP:
                move_robot(0, -1)
            elif event.key == pygame.K_DOWN:
                move_robot(0, 1)
            elif event.key == pygame.K_r:
                draw_board(room[ROOM_NUMBER])
                robo_pos = [0, 4]
            # Print grid to check if work
            for row in board:
                print(row)
            print("xxxxxxxxx")

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
