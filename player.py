import pygame
from bullet import Bullet

class Player:
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.width = 20
        self.rect.height = 20
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT - 50
        self.bullets = []
        self.screen = screen
        self.shoot_cooldown = 500  # Cooldown de disparo en milisegundos (2 segundos)
        self.last_shot_time = 0

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= 5
        if direction == "right" and self.rect.right < 800:
            self.rect.x += 5

    def can_shoot(self):
        # Verificar si ha pasado suficiente tiempo desde el último disparo
        current_time = pygame.time.get_ticks()
        return current_time - self.last_shot_time >= self.shoot_cooldown

    def shoot(self):
        if self.can_shoot():
            bullet = Bullet(self.screen, self.rect.centerx, self.rect.top)
            self.bullets.append(bullet)
            self.last_shot_time = pygame.time.get_ticks()  # Registrar el tiempo del último disparo

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw()

    def collide_with(self, enemy):
        return self.rect.colliderect(enemy.rect)
