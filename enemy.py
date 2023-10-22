import pygame
import random

class Enemy:
    def __init__(self, screen):
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.width = 80 # Cambiar el ancho de la caja de colisión
        self.rect.height = 80 # Cambiar la altura de la caja de colisión
        self.rect.x = random.randint(0, 800 - self.rect.width)
        self.rect.y = random.randint(0, 300)
        self.bullets = []
        self.screen = screen

    def move(self):
        self.rect.y += 3
        if self.rect.top > 600:
            self.rect.x = random.randint(0, 800 - self.rect.width)
            self.rect.y = random.randint(-50, -10)

    

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw()

    def collide_with(self, player):
        return self.rect.colliderect(player.rect)

    def die(self):
        self.rect.x = random.randint(0, 800 - self.rect.width)
        self.rect.y = random.randint(-50, -10)



