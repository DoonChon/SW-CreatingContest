import pygame
import random

from pygame import mixer

pygame.init()

# 게임창 설정 
screen_width = 1200  # 가로 크기
screen_height = 900  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DoonChon HighSchool Game | Code Club") # 게임창의 이름 설정
icon = pygame.image.load('Icon.png')                               # 게임창의 아이콘 이미지 설정
pygame.display.set_icon(icon)

# 배경 설정
background = pygame.image.load("background.jpg")

# 배경 음악 
mixer.music.load("background.ogg") # 배경 음악 지정
mixer.music.play(-1)               # 음악 시간 ( -1 은 꺼질때 까지 켜짐 )

#플레이어 설정
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# 적캐릭터 설정
enemy = pygame.image.load("enemy.png")
enemyX = 200
enemyY = 100
randomNumber = 30
Speed = 10


# 점수 설정
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
ScoreX = 10
ScoreY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))


running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

    Rand1 = random.randrange(1,200)
    Rand2 = random.randrange(1,440)

    if enemyY > 640:
        enemyY = randomNumber
        enemyX = randomNumber2
        score += 1
        Speed += 2
    
    enemyY += Speed

    PlayerRect = playerImg.get_rect()
    PlayerRect.left = playerX
    PlayerRect.top = playerY
    
    enemyRect = enemy.get_rect()
    enemyRect.left = enemyX
    enemyRect.top = enemyY

    if characterRect.colliderect(enemyRect):
        game_over_text
        running = False

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    screen.blit(background, (0, 0))
    player(playerX, playerY)
    show_score(ScoreX, ScoreY)
    pygame.display.update()   # 위에 사항들을 디스플레이에 계속 업데이트
    
pygame.quit()