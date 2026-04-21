import pygame
import random
import sys

# -------------------- INIT --------------------
pygame.init()

# -------------------- SCREEN SETTINGS --------------------
WIDTH = 600
HEIGHT = 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

clock = pygame.time.Clock()

# -------------------- COLORS --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
READ = (255, 0, 0)  # (typo: probably meant RED)

# -------------------- PLAYER SETTINGS --------------------
player_width = 50
player_height = 80

player_x = WIDTH // 2
player_y = HEIGHT - 120
player_speed = 10

# -------------------- COIN SETTINGS --------------------
coins = []  # list of coin rectangles
coin_size = 20
coin_spawn_delay = 30  # frames between spawns
spawn_timer = 0

# -------------------- SCORE --------------------
score = 0

# -------------------- FONT --------------------
font = pygame.font.Font(None, 36)

# -------------------- COIN SPAWN FUNCTION --------------------
def spawn_coin():
    # random x position, starts above screen
    x = random.randint(0, WIDTH - coin_size)
    y = -coin_size

    # store coin as a rectangle
    coins.append(pygame.Rect(x, y, coin_size, coin_size))

# -------------------- GAME LOOP --------------------
running = True

while running:
    clock.tick(FPS)  # control speed

    # -------------------- EVENT HANDLING --------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------- PLAYER MOVEMENT --------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # keep player inside screen bounds
    player_x = max(0, min(WIDTH - player_width, player_x))

    # -------------------- PLAYER COLLISION BOX --------------------
    # defines where collisions are detected
    player_rect = pygame.Rect(player_x + 60, player_y,
                              player_width, player_height)

    # -------------------- LOAD CAR IMAGE --------------------
    # (NOTE: this should ideally be loaded once outside loop)
    car_img = pygame.image.load("practice_10/racer/image/carr.png")
    car_img = pygame.transform.scale(car_img, (player_width + 40, player_height))

    # -------------------- COIN SPAWNING --------------------
    spawn_timer += 1
    if spawn_timer >= coin_spawn_delay:
        spawn_coin()
        spawn_timer = 0

    # -------------------- MOVE COINS + COLLISIONS --------------------
    for coin in coins[:]:  # copy list to safely remove items

        # move coin downward
        coin.y += 14

        # collision with player
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1

        # remove coin if it goes off screen
        elif coin.y > HEIGHT:
            coins.remove(coin)

    # -------------------- DRAW EVERYTHING --------------------
    screen.fill(BLACK)

    # draw player car
    screen.blit(car_img, (player_x, player_y))

    # draw coins
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin.center, coin_size // 2)

    # -------------------- SCORE DISPLAY --------------------
    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 10))

    # -------------------- UPDATE SCREEN --------------------
    pygame.display.update()

# -------------------- EXIT --------------------
pygame.quit()
sys.exit()