import pygame
from random import *

from pygame import mixer

pygame.init()

# 게임창 설정 
screen_width = 1200  # 가로 크기
screen_height = 672  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DoonChon HighSchool Game | Code Club") # 게임창의 이름 설정
icon = pygame.image.load('Icon.png')                               # 게임창의 아이콘 이미지 설정
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


# 배경 설정
background = pygame.image.load("background.jpg")

# 배경 음악 
mixer.music.load("background.ogg") # 배경 음악 지정
mixer.music.play(-1)               # 음악 시간 ( -1 은 꺼질때 까지 켜짐 )

#플레이어 설정
character = pygame.image.load('player.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]        # 캐릭터의 가로 크기
character_height = character_size[1]       # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height           # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
playerX_change = 0
character_speed = 10

# 적캐릭터 설정
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]                             # 적의 가로 크기
enemy_height = enemy_size[1]                            # 적의 세로 크기
enemy_x_pos = randrange(0 , screen_width - enemy_width) # 가로 위치 랜덤
enemy_y_pos = 0
enemy_speed = 10


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

# 이벤트 루프

running = True

while running:
    dt = clock.tick(30)
    score_value += 1
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:          # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:        # 캐릭터를 왼쪽으로
                playerX_change -= character_speed # 캐릭터 스피드 만큼 이동
            elif event.key == pygame.K_RIGHT:     # 캐릭터를 오른쪽으로
                playerX_change += character_speed
        
        if event.type == pygame.KEYUP:            # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += playerX_change
    enemy_y_pos += enemy_speed

    # 캐릭터 경계 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        game_over_text()
        running = False

    if enemy_y_pos > screen_height:
        enemy_x_pos = randrange(0 , screen_width-enemy_width) # 가로 위치 랜덤
        enemy_y_pos = 0

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    show_score(ScoreX,ScoreY)

    pygame.display.update()

pygame.quit()
