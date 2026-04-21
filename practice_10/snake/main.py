import pygame
import sys
import random

# -------------------- INIT --------------------
pygame.init()

# -------------------- WINDOW SETUP --------------------
width = 600
height = 600
cell = 20  # size of each snake block / food / wall

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# -------------------- FPS CONTROL --------------------
clock = pygame.time.Clock()

# -------------------- COLORS --------------------
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# -------------------- FONT --------------------
font = pygame.font.Font(None, 36)

# -------------------- SNAKE SETUP --------------------
snake = [(100, 100), (80, 100), (60, 100)]  # starting body
direction = (cell, 0)  # moving right initially

# -------------------- GAME VARIABLES --------------------
score = 0
level = 1
speed = 10
foods_eaten = 0

# -------------------- WALLS --------------------
walls = []

# -------------------- FOOD GENERATION --------------------
def generate_food():
    # keep generating until valid position found
    while True:
        x = random.randrange(0, width, cell)
        y = random.randrange(0, height, cell)

        # avoid spawning on snake or walls
        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

food = generate_food()

# -------------------- DRAW FUNCTIONS --------------------
def draw_snake():
    for seg in snake:
        pygame.draw.rect(screen, green, (*seg, cell, cell))

def draw_food():
    pygame.draw.rect(screen, red, (*food, cell, cell))

def draw_walls():
    for wall in walls:
        pygame.draw.rect(screen, blue, (*wall, cell, cell))

# -------------------- LEVEL SYSTEM --------------------
def upd_level():
    global level, speed, foods_eaten

    # every 3 foods -> level up
    if foods_eaten >= 3:
        level += 1
        speed += 1  # game gets faster
        foods_eaten = 0
        add_walls()

# -------------------- ADD WALLS --------------------
def add_walls():
    # add 5 random walls
    for _ in range(5):
        x = random.randrange(0, width, cell)
        y = random.randrange(0, height, cell)

        # avoid spawning on snake
        if (x, y) not in snake:
            walls.append((x, y))

# -------------------- GAME LOOP --------------------
running = True

while running:
    clock.tick(speed)  # control game speed

    # -------------------- EVENTS --------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------- INPUT (KEYBOARD) --------------------
    keys = pygame.key.get_pressed()

    # prevent instant reverse direction
    if keys[pygame.K_UP] and direction != (0, cell):
        direction = (0, -cell)
    if keys[pygame.K_DOWN] and direction != (0, -cell):
        direction = (0, cell)
    if keys[pygame.K_RIGHT] and direction != (-cell, 0):
        direction = (cell, 0)
    if keys[pygame.K_LEFT] and direction != (cell, 0):
        direction = (-cell, 0)

    # -------------------- MOVE SNAKE --------------------
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # -------------------- COLLISION CHECK --------------------
    if (
        head_x < 0 or head_x >= width or
        head_y < 0 or head_y >= height or
        new_head in snake or
        new_head in walls
    ):
        running = False  # game over

    # add new head to snake
    snake.insert(0, new_head)

    # -------------------- FOOD CHECK --------------------
    if new_head == food:
        score += 1
        foods_eaten += 1
        food = generate_food()
        upd_level()
    else:
        snake.pop()  # remove tail if no food eaten

    # -------------------- DRAW EVERYTHING --------------------
    screen.fill(black)

    draw_snake()
    draw_food()
    draw_walls()

    # -------------------- UI TEXT --------------------
    score_text = font.render(f"Score : {score}", True, white)
    level_text = font.render(f"Level {level}", True, white)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # -------------------- UPDATE SCREEN --------------------
    pygame.display.update()

# -------------------- EXIT --------------------
pygame.quit()
sys.exit()