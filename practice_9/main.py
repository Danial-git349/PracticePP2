import pygame
import sys
from practice_9.clock import get_angles

pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Load image
hand_img = pygame.image.load("images/Mickey_hand.png").convert_alpha()

# OPTIONAL: fix rotation if needed
# hand_img = pygame.transform.rotate(hand_img, 90)

# Resize (optional)
hand_img = pygame.transform.scale(hand_img, (200, 200))

center = (WIDTH // 2, HEIGHT // 2)

clock = pygame.time.Clock()

def draw_hand(image, angle, position):
    rotated = pygame.transform.rotate(image, -angle)
    rect = rotated.get_rect(center=position)
    screen.blit(rotated, rect)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 🧠 Get angles from clock.py
    sec_angle, min_angle = get_angles()

    # 🖐 Draw hands
    draw_hand(hand_img, sec_angle, center)   # seconds
    draw_hand(hand_img, min_angle, center)   # minutes

    pygame.display.flip()
    clock.tick(1)  # update every second

pygame.quit()
sys.exit()