import pygame
import sys

# Constants
ROWS, COLS = 9, 9
cell_size = 32
board_size = 9
height = board_size * cell_size
width = board_size * cell_size

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Robotron")
clock = pygame.time.Clock()


# load pictures
wall_image = pygame.image.load('wall.bmp').convert_alpha()
robo_image = pygame.image.load('robo.bmp').convert_alpha()
door_image = pygame.image.load('door.bmp').convert_alpha()
space_image = pygame.image.load('space.bmp').convert_alpha()
dinamico_image = pygame.image.load('dinamico.bmp').convert_alpha()
dinexplo_image = pygame.image.load('dinexplo.bmp').convert_alpha()

pics = ["wall_image", "robo_image", "door_image",
        "space_image", "dinamico_image", "dinexplo_image"]
# wall index = 0
# robo index = 1
# door index = 2
# space index = 3
# dinamico index = 4
wall_id = pics.index('wall_image')
door_id = pics.index('door_image')
robo_id = pics.index('robo_image')
space_id = pics.index('space_image')
dinamico_id = pics.index('dinamico_image')
dinexplo_id = pics.index('dinexplo_image')


# Create a 2D list representing the board
board = [[0 for _ in range(board_size)] for _ in range(board_size)]
# Function to draw the board with walls


def draw_board():
    global board, room1
    col = 1
    row = 1
    for i in room1:
        if row != 8:
            if i == "0":
                board[col][row] = 3
                row += 1
            elif i == "1":
                board[col][row] = 0
                row += 1
            elif i == "2":
                board[col][row] = 4
                row += 1
        else:
            col += 1
            row = 1
            if row != 8:
                if i == "0":
                    board[col][row] = 3
                    row += 1
                elif i == "1":
                    board[col][row] = 0
                    row += 1
                elif i == "2":
                    board[col][row] = 4
                    row += 1


# Rooms
room1 = "0000102002220022201200202200220002202201212202000"

draw_board()


def draw_screenboard(board):
    col = 0
    row = 0
    for i in board:
        for j in i:
            if j == 3:
                screen.blit(space_image, (row*cell_size, col*cell_size))
            elif j == 0:
                screen.blit(wall_image, (row*cell_size, col*cell_size))
            elif j == 4:
                screen.blit(dinamico_image, (row*cell_size, col*cell_size))
            elif j == 9:
                screen.blit(dinexplo_image, (row*cell_size, col*cell_size))
            row += 1
        row = 0
        col += 1

    # Place door images on specific positions
    screen.blit(door_image, (0 * cell_size, 4 * cell_size))
    board[4][0] = 2  # Set board position as a door
    screen.blit(door_image, (8 * cell_size, 4 * cell_size))
    board[4][8] = 2  # Set board position as a door


# Position robo
robo_pos = [1, 4]

# Test
wall_pos = [4, 4]
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white
    draw_screenboard(board)

    # Place the robot at its current position
    screen.blit(robo_image, (robo_pos[0]*cell_size, robo_pos[1]*cell_size))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Ensure it doesn't go out of bounds
                if robo_pos[0] > 1 and board[robo_pos[1]][robo_pos[0] - 1] != 0:
                    wall = 0
                    if board[robo_pos[1]][robo_pos[0]-1] == 4:
                        last_position = []
                        index = robo_pos[0]-1

                        while index >= 0:
                            print(index)
                            if board[robo_pos[1]][index] == 3:
                                last_position.append(robo_pos[1])
                                last_position.append(index)
                                print(last_position)
                                break
                            elif board[robo_pos[1]][index] == 4:
                                index -= 1
                            elif board[robo_pos[1]][index] == 2:
                                wall = 1
                                print(wall)
                                break
                            elif board[robo_pos[1]][index] == 0:
                                wall = 1
                                print(wall)
                                break

                        if wall != 1:
                            board[last_position[0]][last_position[1]] = 4
                            board[robo_pos[1]][robo_pos[0]] = 3
                            robo_pos[0] -= 1
                            board[robo_pos[1]][robo_pos[0]] = 1
                        last_position = []
                    elif board[robo_pos[1]][robo_pos[0]-1] == 3:
                        board[robo_pos[1]][robo_pos[0]-1] = 1
                        board[robo_pos[1]][robo_pos[0]] = 3
                        robo_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                if robo_pos[0] < COLS - 2 and board[robo_pos[1]][robo_pos[0] + 1] != 0:
                    wall = 0
                    if board[robo_pos[1]][robo_pos[0]+1] == 4:
                        last_position = []
                        index = robo_pos[0]+1

                        while index < 10:
                            print(index)
                            if board[robo_pos[1]][index] == 3:
                                last_position.append(robo_pos[1])
                                last_position.append(index)
                                print(last_position)
                                break
                            elif board[robo_pos[1]][index] == 4:
                                index += 1
                            elif board[robo_pos[1]][index] == 2:
                                wall = 1
                                print(wall)
                                break
                            elif board[robo_pos[1]][index] == 0:
                                wall = 1
                                print(wall)
                                break
                        if wall != 1:
                            board[last_position[0]][last_position[1]] = 4
                            board[robo_pos[1]][robo_pos[0]] = 3
                            robo_pos[0] += 1
                            board[robo_pos[1]][robo_pos[0]] = 1
                        last_position = []

                    elif board[robo_pos[1]][robo_pos[0]+1] == 3:
                        board[robo_pos[1]][robo_pos[0]+1] = 1
                        board[robo_pos[1]][robo_pos[0]] = 3
                        robo_pos[0] += 1
            elif event.key == pygame.K_UP:
                if robo_pos[1] > 1 and board[robo_pos[1] - 1][robo_pos[0]] != 0:
                    wall = 0
                    if board[robo_pos[1]-1][robo_pos[0]] == 4:
                        last_position = []
                        index = robo_pos[1]-1

                        while index >= 0:
                            print(index)
                            print(board[index][robo_pos[0]])
                            if board[index][robo_pos[0]] == 3:
                                last_position.append(robo_pos[0])
                                last_position.append(index)
                                print(last_position)
                                break
                            elif board[index][robo_pos[0]] == 4:
                                index -= 1
                            elif board[index][robo_pos[0]] == 2:
                                wall = 1
                                print(wall)
                                break
                            elif board[index][robo_pos[0]] == 0:
                                wall = 1
                                print(wall)
                                break
                        if wall != 1:
                            print(last_position)
                            board[last_position[1]][last_position[0]] = 4
                            board[robo_pos[1]][robo_pos[0]] = 3
                            robo_pos[1] -= 1
                            board[robo_pos[1]][robo_pos[0]] = 1
                        last_position = []
                    elif board[robo_pos[1]-1][robo_pos[0]] == 3:
                        board[robo_pos[1]-1][robo_pos[0]] = 1
                        board[robo_pos[1]][robo_pos[0]] = 3
                        robo_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                if robo_pos[1] < ROWS - 2 and board[robo_pos[1] + 1][robo_pos[0]] != 0:
                    wall = 0
                    if board[robo_pos[1]+1][robo_pos[0]] == 4:
                        last_position = []
                        index = robo_pos[1]+1

                        while index < 10:
                            print(index)
                            print(board[index][robo_pos[0]])
                            if board[index][robo_pos[0]] == 3:
                                last_position.append(robo_pos[0])
                                last_position.append(index)
                                print(last_position)
                                break
                            elif board[index][robo_pos[0]] == 4:
                                index += 1
                            elif board[index][robo_pos[0]] == 2:
                                wall = 1
                                print(wall)
                                break
                            elif board[index][robo_pos[0]] == 0:
                                wall = 1
                                print(wall)
                                break
                        if wall != 1:
                            print(last_position)
                            board[last_position[1]][last_position[0]] = 4
                            board[robo_pos[1]][robo_pos[0]] = 3
                            robo_pos[1] += 1
                            board[robo_pos[1]][robo_pos[0]] = 1
                        last_position = []
                    elif board[robo_pos[1]+1][robo_pos[0]] == 3:
                        board[robo_pos[1]+1][robo_pos[0]] = 1
                        board[robo_pos[1]][robo_pos[0]] = 3
                        robo_pos[1] += 1

            # Update the grid
            for row in board:
                print(row)
            print("xxxxxxxxx")

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
