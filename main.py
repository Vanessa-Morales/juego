import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet 
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
GAME_OVER_FONT = pygame.font.Font(None, 36)
game_over = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("combate")

background = pygame.image.load("background.png")

player = Player(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

enemies = []  

death_sound = pygame.mixer.Sound("muerte.mp3")
death_sound.set_volume(1.0)
explosion_sound=pygame.mixer.Sound("explosion.mp3")
disparo_sound=pygame.mixer.Sound("laser_sound.mp3")
disparo_sound.set_volume(0.2)
explosion_sound.set_volume(0.2)
score=0
pygame.mixer.music.load("fondo.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)  

running = True
clock = pygame.time.Clock()

new_enemy_timer = 0
enemy_spawn_interval = 3000 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")
        if keys[pygame.K_e]:
            player.shoot()
            disparo_sound.play()


        for enemy in enemies:
            enemy.move()

        player.update()

        for enemy in enemies:
            enemy.update()
            if player.collide_with(enemy):
                game_over = True
                death_sound.play()

        for bullet in player.bullets:
            bullet.update()
            bullet.draw()

            for enemy in enemies:
                bullet.check_collision_with_enemy(enemy)  
                if bullet.hit_enemy:
                    enemy.die()
                    score+=1
                    explosion_sound.play()
            player.bullets = [bullet for bullet in player.bullets if not bullet.hit_enemy]

        new_enemy_timer += clock.get_time()
        if new_enemy_timer >= enemy_spawn_interval:
            new_enemy = Enemy(screen)
            enemies.append(new_enemy)
            new_enemy_timer = 0

        screen.blit(background, (0, 0))
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))


        player.draw()

        for enemy in enemies:
            enemy.draw()

        pygame.display.flip()

        clock.tick(60)
    else:
        game_over_text = GAME_OVER_FONT.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))

        restart_text = GAME_OVER_FONT.render("Press SPACE to restart", True, WHITE)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 20))

        quit_text = GAME_OVER_FONT.render("Press Q to quit", True, WHITE)
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_over = False
                    player = Player(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
                    enemies = [] 
                if event.key == pygame.K_q:
                    running = False  

pygame.quit()
