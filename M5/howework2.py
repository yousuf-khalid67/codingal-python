import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Set up clock for frame rate
clock = pygame.time.Clock()
FPS = 60

# Game loop
running = True
while running:
    clock.tick(FPS)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white background
    screen.fill(WHITE)
    
    # Draw a simple rectangle
    pygame.draw.rect(screen, BLUE, (100, 100, 200, 150))
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()