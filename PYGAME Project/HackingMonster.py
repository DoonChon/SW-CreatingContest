import pygame

from pygame import mixer
pygame.init()

# 게임창 설정 
screen_width = 1200  # 가로 크기
screen_height = 900 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DoonChon HighSchool Game | Code Club") # 게임창의 이름 설정
icon = pygame.image.load('Icon.png') # 게임창의 아이콘 이미지 설정
pygame.display.set_icon(icon)

# 배경 설정
background = pygame.image.load("background.jpg")

# 배경 음악 
mixer.music.load("background.ogg") # 배경 음악 지정
mixer.music.play(-1) # 음악 시간 ( -1 은 꺼질때 까지 켜짐 )

#플레이어 설정
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    
    screen.blit(background, (0, 0))
    pygame.display.update()


pygame.quit()

    
