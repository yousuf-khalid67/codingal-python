import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Game Screen")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Font for text
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 32)

# Game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white background
    screen.fill(WHITE)
    
    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (150, 150, 300, 200))
    pygame.draw.rect(screen, RED, (150, 150, 300, 200), 3)  # Border
    
    # Render text
    title_text = font.render("Welcome to Pygame!", True, BLACK)
    info_text = small_font.render("Press QUIT to exit", True, BLACK)
    
    # Display text on screen
    screen.blit(title_text, (200, 250))
    screen.blit(info_text, (250, 350))
    
    # Update display
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()