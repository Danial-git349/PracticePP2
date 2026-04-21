import pygame
import sys 

# -------------------- INIT PYGAME --------------------
pygame.init()

# -------------------- WINDOW SETUP --------------------
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

# -------------------- FPS CLOCK --------------------
clock = pygame.time.Clock()

# -------------------- COLORS (RGB) --------------------
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = [black, red, green, blue]

# -------------------- STATE VARIABLES --------------------
current_color = black      # active drawing color
tool = "brush"             # current tool (brush, rect, circle, eraser)

drawing = False            # is mouse being held down?
start_pos = (0, 0)         # where shape starts

# -------------------- INITIAL SCREEN FILL --------------------
screen.fill(white)

# -------------------- DRAW UI FUNCTION --------------------
def draw_ui():
    # Draw color palette
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i * 40, 10, 30, 30))

    # Draw tool buttons (outline rectangles)
    pygame.draw.rect(screen, black, (10, 60, 80, 30), 2)
    pygame.draw.rect(screen, black, (100, 60, 80, 30), 2)
    pygame.draw.rect(screen, black, (190, 60, 80, 30), 2)
    pygame.draw.rect(screen, black, (280, 60, 80, 30), 2)

    # Draw tool labels
    font = pygame.font.Font(None, 24)
    screen.blit(font.render("Brush", True, black), (15, 65))
    screen.blit(font.render("Rect", True, black), (110, 65))
    screen.blit(font.render("Circle", True, black), (200, 65))
    screen.blit(font.render("Eraser", True, black), (285, 65))

# -------------------- DRAWING SURFACE (CANVAS) --------------------
canvas = pygame.Surface((width, height))
canvas.fill(white)

# -------------------- MAIN LOOP --------------------
running = True

while running:
    clock.tick(60)  # limit FPS to 60

    # -------------------- EVENT HANDLING --------------------
    for event in pygame.event.get():

        # Quit window
        if event.type == pygame.QUIT:
            running = False

        # -------------------- MOUSE DOWN --------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Check color selection
            for i, color in enumerate(colors):
                if pygame.Rect(10 + i * 40, 10, 30, 30).collidepoint(x, y):
                    current_color = color

            # Check tool selection
            if pygame.Rect(10, 60, 80, 30).collidepoint(x, y):
                tool = "brush"
            if pygame.Rect(100, 60, 80, 30).collidepoint(x, y):
                tool = "rect"
            if pygame.Rect(190, 60, 80, 30).collidepoint(x, y):
                tool = "circle"
            if pygame.Rect(280, 60, 80, 30).collidepoint(x, y):
                tool = "eraser"

            # Start drawing action
            drawing = True
            start_pos = event.pos

        # -------------------- MOUSE UP --------------------
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # Draw rectangle on canvas
            if tool == "rect":
                rect = pygame.Rect(
                    start_pos,
                    (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                )
                pygame.draw.rect(canvas, current_color, rect, 2)

            # Draw circle on canvas
            if tool == "circle":
                radius = int(
                    ((end_pos[0] - start_pos[0])**2 +
                     (end_pos[1] - start_pos[1])**2) ** 0.5
                )
                pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

        # -------------------- MOUSE MOVE (DRAWING) --------------------
        if event.type == pygame.MOUSEMOTION and drawing:

            # Brush tool
            if tool == "brush":
                pygame.draw.circle(canvas, current_color, event.pos, 5)

            # Eraser tool (draws white circles)
            if tool == "eraser":
                pygame.draw.circle(canvas, white, event.pos, 10)

    # -------------------- RENDERING --------------------

    # Clear screen
    screen.fill(white)

    # Draw saved canvas
    screen.blit(canvas, (0, 0))

    # Draw UI on top
    draw_ui()

    # Update display
    pygame.display.update()

# -------------------- CLEAN EXIT --------------------
pygame.quit()
sys.exit()