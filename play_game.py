import pygame
import sys
from pygame import display, time, draw, QUIT, init
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

    def show(self, color):
        draw.rect(screen, color, [self.x * hr - 2, self.y * wr - 2, hr - 4, wr - 4])


def move_snake(snake_segments, direction):
    head = snake_segments[-1]
    if direction == 0:  # up
        new_head = Spot(head.x, head.y - 1)
    elif direction == 1:  # down
        new_head = Spot(head.x, head.y + 1)
    elif direction == 2:  # left
        new_head = Spot(head.x - 1, head.y)
    elif direction == 3:  # right
        new_head = Spot(head.x + 1, head.y)
    snake_segments.append(new_head)


def check_collision(snake_segments):
    head = snake_segments[-1]
    # Check if the head has hit the boundary
    if head.x < 0 or head.x >= rows or head.y < 0 or head.y >= cols:
        return True
    # Check if the head has hit its own body
    for segment in snake_segments[:-1]:
        if segment.x == head.x and segment.y == head.y:
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
    pygame.time.delay(3000)  # Delay for 3 seconds
    pygame.quit()
    quit()


def generate_food(snake_segments):
    # Generate food at a random location not occupied by the snake
    while True:
        food = Spot(randint(0, rows - 1), randint(0, cols - 1))
        if food not in snake_segments:
            return food


snake_segments = [Spot(12, 12)]  # Initial position of the snake
food = generate_food(snake_segments)

direction = 1  # Initialize the direction

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Check for key presses to change the direction of the snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 0
    elif keys[pygame.K_DOWN]:
        direction = 1
    elif keys[pygame.K_LEFT]:
        direction = 2
    elif keys[pygame.K_RIGHT]:
        direction = 3

    move_snake(snake_segments, direction)

    if check_collision(snake_segments):
        score = len(snake_segments) - 1
        print("Game Over! Your score is:", score)
        game_over(score)

    # Check if the snake has eaten the food
    if snake_segments[-1].x == food.x and snake_segments[-1].y == food.y:
        food = generate_food(snake_segments)
        score += 1  # Increase the score
    else:
        snake_segments.pop(0)  # Remove the tail segment

    screen.fill(BLACK)
    for segment in snake_segments[:-1]:
        segment.show(WHITE)  # Draw the snake body
    snake_segments[-1].show(BLUE)  # Draw the snake head in blue
    food.show(GREEN)  # Draw the food
    display.flip()
    clock.tick(10)  # Adjust the speed of the snake
