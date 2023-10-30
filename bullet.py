import pygame 
from enemy import Enemy
class Bullet:
    def __init__(self, screen, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.screen = screen
        self.hit_enemy = False

    def update(self):
        self.rect.y -= 10

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

    def check_collision_with_enemy(self, enemy):  
     if not self.hit_enemy:
        if self.rect.colliderect(enemy.rect):
            self.hit_enemy = True
