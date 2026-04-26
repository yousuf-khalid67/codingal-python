import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Screen")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background
    screen.fill(WHITE)
    
    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (100, 100, 200, 150))
    
    # Draw another rectangle
    pygame.draw.rect(screen, RED, (500, 150, 150, 120))
    
    # Render text
    text_surface = font.render("Welcome to Game Screen", True, BLACK)
    screen.blit(text_surface, (250, 50))
    
    # Render more text
    text_surface2 = font.render("Score: 100", True, RED)
    screen.blit(text_surface2, (300, 350))
    
    # Update display
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()