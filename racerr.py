import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()
FPS = pygame.time.Clock()

is_playing, lose = True, False

# Цвета
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

game_over1 = font.render("Game Over", True, BLACK)

# Размеры экрана
dw = 400
dh = 600
SPEED = 5
SCORE = 0
coin_score = 0

# Фон
screen = pygame.display.set_mode((dw, dh))
pygame.display.set_caption("Racer")
game_over = pygame.image.load("C:/images/gameover.jpg")
game_over = pygame.transform.scale(game_over, (dw, dh))
backg = pygame.image.load("C:/images/AnimatedStreet.png")

pygame.mixer.music.load("C:/images/background.wav")  # Укажи путь к своему файлу
pygame.mixer.music.set_volume(0.3)  # Громкость (0.0 - 1.0)
pygame.mixer.music.play(-1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < dw and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, dw - 40), 0)

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > dh:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, dw - 40), 0)
        if SCORE >= 20:
            self.rect.move_ip(0, SPEED * 0.5)  # Ускорение машин

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/images/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.value = random.randint(1, 10)  # Случайный вес монеты
        self.spawn()

    def spawn(self):
        while True:
            self.rect.center = (random.randint(30, dw - 30), random.randint(30, dh - 130))
            if not pygame.sprite.spritecollideany(self, enemies):
                break

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > dh:
            self.spawn()

# Создание объектов
P1 = Player()
E1 = Enemy()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

coins = pygame.sprite.Group()
C = Coin()
coins.add(C)

# Таймер для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while is_playing:
    FPS.tick(60)
    
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(backg, (dw, dh)), (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    for coin in coins:
        coin.move()
        screen.blit(coin.image, coin.rect)
        if pygame.sprite.collide_rect(P1, coin):
            coin_score += coin.value  # Учитываем вес монеты
            coin.kill()
            new_coin = Coin()
            coins.add(new_coin)
    
    if pygame.sprite.spritecollideany(P1, enemies):
        lose = True
    
    if lose:
        pygame.mixer.Sound("C:/images/crash.wav").play()
    
    while lose:
        FPS.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        time.sleep(2)
        screen.fill(RED)
        screen.blit(game_over1, (30, 250))
        pygame.display.flip()
    
    final_score_text = font_small.render(f"Coins: {coin_score}", True, BLACK)
    screen.blit(final_score_text, (300, 10))
    pygame.display.flip()

pygame.quit()
