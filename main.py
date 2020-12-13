import pygame
import math
import random

# initilizer
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))
# icon and name
pygame.display.set_caption("space shuttle")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')
playerImg = pygame.image.load('ship.png')
playerX = 370
playerY = 480
playerScore = 0

enemyImg = []
enemyX = []
enemyY = []
enemyScoreY = []
enemyScoreX = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyScoreX.append(4)
    enemyScoreY.append(40)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletScoreX = 0
bulletScoreY = 10
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX= 10
textY= 10
game_over =  pygame.font.Font('freesansbold.ttf',100)



def show_score(x,y):
    score = font.render("Score "+ str(score_value) ,True ,(255,255,255))
    screen.blit(score, (x, y))

def game():
    game_text = font.render("GAME OVER " , True, (255, 255, 255))
    screen.blit(game_text,(250,300))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))
    if distance <= 27:
        return True
    else:
        return False


running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerScore -= 5

            if event.key == pygame.K_RIGHT:
                playerScore += 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerScore = 0

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    for i in range(num_of_enemy):
        if enemyY[i]>440:
            for j in range(num_of_enemy):
                enemyY[j]=1000
                game()
                break
        enemyX[i] += enemyScoreX[i]
        if enemyX[i] <= 0:
            enemyScoreX[i] = 4
            enemyY[i] += enemyScoreY[i]
        if enemyX[i] >= 736:
            enemyScoreX[i] = -4
            enemyY[i] += enemyScoreY[i]

        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)


    playerX += playerScore

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletScoreY

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
