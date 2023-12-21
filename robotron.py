import pygame
import sys
from rooms import *

# Constants
ROWS, COLS = 9, 9
CELL_SIZE = 32
BOARD_SIZE = 9
HEIGHT = BOARD_SIZE * CELL_SIZE
WIDTH = BOARD_SIZE * CELL_SIZE
ROOM_NUMBER=0

# Initialize Pygame
pygame.init()
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

image_map = {
    0: wall_image,        # Wall index = 0
    1: robo_image,        # Robo index = 1
    2: door_image,        # Door index = 2
    3: space_image,       # Space index = 3
    4: dinamico_image,   # Dinamico index = 4
    5: dinexplo_image    # Dinexplo index = 5
}

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
                board[col][row] = 3
            elif i == "1":
                board[col][row] = 0
            elif i == "2":
                board[col][row] = 4

            row += 1
                
# Draw a grid
draw_board(room[0])

def draw_screenboard(board):
    door_positions = [(0, 4), (8, 4)]  # Define door positions

    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == 3:
                screen.blit(space_image, (col_index * CELL_SIZE, row_index * CELL_SIZE))
            elif cell == 0:
                screen.blit(wall_image, (col_index * CELL_SIZE, row_index * CELL_SIZE))
            elif cell == 4:
                screen.blit(dinamico_image, (col_index * CELL_SIZE, row_index * CELL_SIZE))
            elif cell == 9:
                screen.blit(dinexplo_image, (col_index * CELL_SIZE, row_index * CELL_SIZE))

    # Place door images on specific positions
    for door_pos in door_positions:
        screen.blit(door_image, (door_pos[0] * CELL_SIZE, door_pos[1] * CELL_SIZE))
        board[door_pos[1]][door_pos[0]] = 2  # Set board position as a door

def move_robot(dx, dy):
    new_x = robo_pos[0] + dx
    new_y = robo_pos[1] + dy
    global ROOM_NUMBER

    if 0 <= new_x < COLS and 0 <= new_y < ROWS and board[new_y][new_x] != 0:
        if board[new_y][new_x] == 4:
            last_position = find_last_position(new_x, new_y, dx, dy)
            if last_position and board[last_position[1]][last_position[0]] != 2:
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
        elif board[new_y][new_x] == 2 and board[robo_pos[1]][robo_pos[0]-1] !=2:
            ROOM_NUMBER+=1
            board[robo_pos[1]][robo_pos[0]] = 3
            robo_pos[0] = new_x - (8*dx)
            robo_pos[1] = new_y
            draw_board(room[ROOM_NUMBER])

def find_last_position(x, y, dx, dy):
    while 0 <= x < COLS and 0 <= y < ROWS:
        if board[y][x] == 3:
            return [x, y]
        elif board[y][x] == 4:
            x += dx
            y += dy
        elif board[y][x] == 2 or board[y][x] == 0:
            break
    return None

# Robo start position
robo_pos = [0, 4]

# Test
#wall_pos = [4,4]
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
                            
                            
            # Print grid to check if work
            for row in board:
                print(row)
            print("xxxxxxxxx")
      
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()

