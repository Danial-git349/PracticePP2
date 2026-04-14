import pygame
import sys
from clock import get_angles

pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Load image
def trim_image(image):
    rect = image.get_bounding_rect()
    cropped = image.subsurface(rect).copy()
    return cropped
sec_hand = pygame.image.load("practice_9/Mickeys_clock/images/left_hand.png").convert_alpha()
min_hand = pygame.image.load("practice_9/Mickeys_clock/images/right_hand.png").convert_alpha()

# OPTIONAL: fix rotation if needed
# hand_img = pygame.transform.rotate(hand_img, 90)

# Resize (optional)
sec_hand = pygame.transform.scale(sec_hand, (120, 120))
min_hand = pygame.transform.scale(min_hand, (120, 120))

center = (WIDTH // 2, HEIGHT // 2)

clock = pygame.time.Clock()

def draw_hand(image, angle, position):
    rotated = pygame.transform.rotate(image, -angle)
    rect = rotated.get_rect(center=position)
    screen.blit(rotated, rect)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 🧠 Get angles from clock.py
    sec_angle, min_angle = get_angles()

    # 🖐 Draw hands
    draw_hand(sec_hand, sec_angle, center)   # left hand = seconds
    draw_hand(min_hand, min_angle, center)   # right hand = minutes   

    pygame.display.flip()
    clock.tick(1)  # update every second

pygame.quit()
sys.exit()