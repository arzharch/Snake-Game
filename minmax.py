import pygame
import sys
from pygame import display, time, draw, QUIT, init
from numpy import sqrt
from random import randint

init()

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Define the board size
board_width = 25
board_height = 25

# Initialize Pygame
pygame.init()

cols = 25
rows = 25

score = 0
width = 600
height = 600
wr = width / cols
hr = height / rows
direction = 1

screen = display.set_mode([width, height])
display.set_caption("snake_game")
clock = time.Clock()


class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.camefrom = []

    def show(self, color):
        draw.rect(screen, color, [self.x * hr - 2, self.y * wr - 2, hr - 4, wr - 4])

    def add_neighbors(self):
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.x < rows - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y < cols - 1:
            self.neighbors.append(grid[self.x][self.y + 1])


def check_collision():
    head_x, head_y = snake[-1].x, snake[-1].y

    # Check if the head has hit the boundary
    if head_x < 0 or head_x >= rows or head_y < 0 or head_y >= cols:
        return True

    for segment in snake[:-1]:
        if segment.x == head_x and segment.y == head_y:
            return True

    return False


def game_over(score):
    my_font = pygame.font.SysFont('times new roman', 40)
    game_over_surface = my_font.render(f'YOU DIED, SCORE: {score}', True, WHITE)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (height / 2, width / 2)
    screen.fill(BLACK)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()  # Update the display before quitting
    pygame.time.delay(30000)  # Delay for 30 seconds
    pygame.quit()
    quit()

def get_available_moves(board):
    available_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '-':
                available_moves.append((row, col))
    return available_moves

def getpath(food1, snake1):
    food1.camefrom = []
    for s in snake1:
        s.camefrom = []
    openset = [snake1[-1]]
    closedset = []
    dir_array1 = []

    while openset:  # Continue loop while openset is not empty
        current1 = min(openset, key=lambda x: x.f)
        openset = [openset[i] for i in range(len(openset)) if not openset[i] == current1]
        closedset.append(current1)
        for neighbor in current1.neighbors:
            if neighbor not in closedset and neighbor not in snake1:
                tempg = neighbor.g + 1
                if neighbor in openset:
                    if tempg < neighbor.g:
                        neighbor.g = tempg
                else:
                    neighbor.g = tempg
                    openset.append(neighbor)
                neighbor.h = sqrt((neighbor.x - food1.x) ** 2 + (neighbor.y - food1.y) ** 2)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.camefrom = current1
        if current1 == food1:
            break
        if not openset:  # Check if openset becomes empty
            score = len(snake) - 1
            print("Game Over! Your score is:", score)
            game_over(score)

    while current1.camefrom:
        if current1.x == current1.camefrom.x and current1.y < current1.camefrom.y:
            dir_array1.append(2)  # down
        elif current1.x == current1.camefrom.x and current1.y > current1.camefrom.y:
            dir_array1.append(0)  # up
        elif current1.x < current1.camefrom.x and current1.y == current1.camefrom.y:
            dir_array1.append(3)  # left
        elif current1.x > current1.camefrom.x and current1.y == current1.camefrom.y:
            dir_array1.append(1)  # right
        current1 = current1.camefrom

    for i in range(rows):
        for j in range(cols):
            grid[i][j].camefrom = []
            grid[i][j].f = 0
            grid[i][j].h = 0
            grid[i][j].g = 0
    return dir_array1


def minimax(board, depth, is_maximizing):
    # Minimax algorithm with alpha-beta pruning
    if depth == 0 or game_over(board):
        return evaluate_board(board)

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            new_board = make_move(board, move, 'X')
            score = minimax(new_board, depth - 1, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            new_board = make_move(board, move, 'O')
            score = minimax(new_board, depth - 1, True)
            best_score = min(score, best_score)
        return best_score


def evaluate_board(board):
    # Heuristic evaluation function
    # Currently just returning the length of the snake
    return len(board)


def make_move(board, move, player):
    # Make a move on the board for the given player
    new_board = [row[:] for row in board]
    new_board[move[0]][move[1]] = player
    return new_board


grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        grid[i][j].add_neighbors()

snake = [grid[round(rows / 2)][round(cols / 2)]]
food = grid[randint(0, rows - 1)][randint(0, cols - 1)]
current = snake[-1]
dir_array = getpath(food, snake)
food_array = [food]

while True:

    if check_collision():
        score = len(snake) - 1
        print("Game Over! Your score is:", score)
        pygame.time.delay(2000)  # 2000 milliseconds (2 seconds) delay
        pygame.quit()
        quit()

    clock.tick(105)
    screen.fill(BLACK)
    direction = dir_array.pop(-1)
    if direction == 0:  # down
        snake.append(grid[current.x][current.y + 1])
    elif direction == 1:  # right
        snake.append(grid[current.x + 1][current.y])
    elif direction == 2:  # up
        snake.append(grid[current.x][current.y - 1])
    elif direction == 3:  # left
        snake.append(grid[current.x - 1][current.y])
    current = snake[-1]

    if current.x == food.x and current.y == food.y:
        while 1:
            food = grid[randint(0, rows - 1)][randint(0, cols - 1)]
            if not (food in snake):
                break
        food_array.append(food)
        dir_array = getpath(food, snake)
    else:
        snake.pop(0)

    for spot in snake:
        spot.show(WHITE)

    food.show(GREEN)
    snake[-1].show(BLUE)
    display.flip()