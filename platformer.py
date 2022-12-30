import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((640, 480))

# Load assets
player_image = pygame.image.load("player.png")
platform_image = pygame.image.load("platform.png")

# Set up game objects
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = pygame.math.Vector2(0, 0)
        
    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = platform_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player(320, 240)
platforms = pygame.sprite.Group()
platforms.add(Platform(0, 400))
platforms.add(Platform(200, 350))
platforms.add(Platform(400, 300))

# Create the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.velocity.x = -5
            if event.key == pygame.K_RIGHT:
                player.velocity.x = 5
            if event.key == pygame.K_UP:
                player.velocity.y = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.velocity.x = 0
            if event.key == pygame.K_UP:
                player.velocity.y = 0
    
    # Update game state
    player.update()
    
    # Check for collisions
    collisions = pygame.sprite.spritecollide(player, platforms, False)
    if collisions:
        player.velocity.y = 0
    
    # Render game objects
    screen.fill((0, 0, 0))
    platforms.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.update()

# Quit Pygame
pygame.quit()
