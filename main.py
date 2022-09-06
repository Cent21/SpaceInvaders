#SPACEINVADERS

import math
import random

import pygame
from pygame import mixer


pygame.init()
clock = pygame.time.Clock()
menux = 0
menuy = 0
linex = 0

#the screen
screen = pygame.display.set_mode((900, 600), pygame.NOFRAME)


# imagess
background = pygame.image.load('background.png')
menubg = pygame.image.load('menubg.png')
menutitle = pygame.image.load('menutitle.png')
panel = pygame.image.load('panel.png')
gameover = pygame.image.load('gameoverscreen.png')
pausescreen = pygame.image.load('pausescreen.png')
earth = pygame.image.load('earth.png')



# sound
mixer.music.load("background.mp3")
mixer.music.play(-1)

# caption
pygame.display.set_caption("Space Invader")


# theplayer
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 830))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)


bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# score

score_value = 0
font = pygame.font.SysFont('Courier New.ttf', 30)

textX = 10
testY = 10



def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    paused = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] and close.collidepoint(pos):
                    pygame.quit()
                    quit()
            screen.blit(pausescreen, (0,0))

            pygame.display.update()

def game_over():
    global playerX,running,menu
    playerX = 1280
    screen.blit(gameover, (0, 0))
    screen.blit(panel, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:

                menu = True
                return
        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and close.collidepoint(pos):
                pygame.quit()
                quit()


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))





def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False




# Gameloop
menu = True
running = False

while menu:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    running =True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] and close.collidepoint(pos):
                    pygame.quit()
                    quit()
        pos = pygame.mouse.get_pos()
        earthrect = pygame.draw.rect(screen, (255, 255, 255), [130, 200, 200, 200])
        screen.blit(menubg, (menux, menuy))
        menux -= 1
        menuy -= 1
        if menux < -300: menux = 0
        if menuy < -300: menuy = 0
        close = pygame.draw.rect(screen, (255, 255, 255), [870, 3, 30, 30])
        screen.blit(menutitle,(150,150))
        pygame.draw.rect(screen, (255, 255, 255), [150, 400, linex, 5])
        linex +=5
        if linex > 610: linex = 610
        screen.blit(panel, (0, 0))

        #This if for the earth that becomes bigger when hovered po
        if earthrect.collidepoint(pygame.mouse.get_pos()):
            picture = pygame.transform.scale(earth, (200, 200))
            screen.blit(picture, (140, 200))


        clock.tick(60)
        pygame.display.update()

while running:

    screen.blit(background, (0, 0))
    close = pygame.draw.rect(screen, (255, 255, 255), [870, 3, 30, 30])
    screen.blit(panel, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current pos of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if (event.key == pygame.K_1):
                pause()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and close.collidepoint(pos):
                pygame.quit()
                quit()


    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 830:
        playerX = 830
    # enemy Movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000

            game_over()

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 830:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 830)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
