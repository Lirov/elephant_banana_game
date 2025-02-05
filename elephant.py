import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elephant Banana Catcher")

# Colors
WHITE = (255, 255, 255)

# Load images
bg = pygame.image.load("forest.jpg")  # Add a jungle background image
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

elephant_right_img = pygame.image.load("elephant_right.png")  # Load the right-facing elephant image
elephant_right_img = pygame.transform.scale(elephant_right_img, (120, 120))

elephant_left_img = pygame.image.load("elephant_left.png")  # Load the left-facing elephant image
elephant_left_img = pygame.transform.scale(elephant_left_img, (120, 120))

elephant_img = elephant_right_img  # Default elephant image

banana_img = pygame.image.load("banana.png")  # Load the banana image
banana_img = pygame.transform.scale(banana_img, (40, 40))

# Elephant properties
elephant_x = 100
elephant_y = HEIGHT - 120
elephant_speed = 6
elephant_jump = False
elephant_jump_speed = 10
jump_height = 100
jump_counter = jump_height

# Banana properties
banana_x = random.randint(200, WIDTH - 50)
banana_y = -50
banana_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.blit(bg, (0, 0))
    screen.blit(elephant_img, (elephant_x, elephant_y))
    screen.blit(banana_img, (banana_x, banana_y))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and elephant_x > 0:
        elephant_x -= elephant_speed
        elephant_img = elephant_left_img
    if keys[pygame.K_RIGHT] and elephant_x < WIDTH - 80:
        elephant_x += elephant_speed
        elephant_img = elephant_right_img
    if keys[pygame.K_SPACE] and not elephant_jump:
        elephant_jump = True
    
    # Jump logic
    if elephant_jump:
        if jump_counter >= -jump_height:
            elephant_y -= (jump_counter * abs(jump_counter)) * 0.02
            jump_counter -= 1
        else:
            jump_counter = jump_height
            elephant_jump = False
    
    # Banana movement
    banana_y += banana_speed
    if banana_y > HEIGHT:
        banana_y = -50
        banana_x = random.randint(200, WIDTH - 50)
    
    # Collision detection
    elephant_rect = pygame.Rect(elephant_x, elephant_y, 80, 80)
    banana_rect = pygame.Rect(banana_x, banana_y, 40, 40)
    if elephant_rect.colliderect(banana_rect):
        score += 1
        banana_y = -50
        banana_x = random.randint(200, WIDTH - 50)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
