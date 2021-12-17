import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption('hot hockey(не очень хот)') #название
bg_color = (0, 0, 0) #фон она
x=50  #начальные координаты первой ракетки#
y=240 #начальные координаты первой ракетки
y1=240 #начальные координаты второй ракетки
width=10 #ширина платформы
height=80 #длина платформы
speed=4 #скорость платформ
h=0 #дополнительный индикатор
k=0 #подсчет количества касаний платформами
x1 = 550-width #начальные координаты второй ракетки
ballx=300 #начальные координаты мяча
bally=270 #начальные координаты мяча
speedball=10 #скорость мяча
key=0  #индикатор кто бьет
gol1='0' #счет первого игрока
gol2='0' #счет второго игрока
otskok=[-1,-2,1,2] #список возможных ударов
r=10 #радиус мяча
pobed1=pygame.image.load('pictures/p1.jpg') #экран победы для 1 игрока
pobed2 = pygame.image.load('pictures/p2.jpg') #экран победы для 2 игрока
vrezanie=0   #индикатор врезания в границы верх и низ
a = random.randint(0, 1) #индикатор отвечающий за начало(в какую сторону полетит мяч)

def raketki():
    '''Функция движения платформ'''
    global y
    global y1
    global speed
    global height
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and y < 600 - height:
        y += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y1 < 600 - height:
        y1 += speed
    if keys[pygame.K_w] and y1 > 0:
        y1 -= speed
    c=[y,y1]
    return c

def ball():
    '''Функция движения мяча'''
    global height
    global speed
    global h
    global x1
    global ballx
    global bally
    global speedball
    global key
    global gol1
    global gol2
    global otskok
    global r
    global z
    global k

    if bally <= 0 + r:
        key = 3

    if bally >= 600 - r:
        key = 4

    if key == 0:

        if a == 1:
            ballx -= speedball
        if a == 0:
            ballx += speedball
    if ballx == x + width + r and y - height // 2 + r * 3 <= bally <= y + height + r:
        key = 1
        h = 1
        k+=1
    if ballx == x1 - r and y1 - height // 2 + r * 3 <= bally <= y1 + height + r:
        key = 2
        h = 2
        k+=1
    if (ballx == x + width + r and y - height // 2 + r * 3 <= bally <= y + height + r) or (
            ballx == x1 - r and y1 - height // 2 + r * 3 <= bally <= y1 + height + r):
        z = random.choice(otskok)
    if key == 1:
        ballx += speedball
        bally -= z

    if key == 2:
        ballx -= speedball
        bally -= z

    if key == 3:
        bally += abs(z)
        if h == 1:
            ballx += speedball
        if h == 2:
            ballx -= speedball
    if key == 4:
        bally -= abs(z)
        if h == 1:
            ballx += speedball
        if h == 2:
            ballx -= speedball
    return k


def goal():
    '''Функция, отвечающая за забитие гола'''
    global height
    global speed
    global h
    global x1
    global ballx
    global bally
    global speedball
    global key
    global gol1
    global gol2
    global otskok
    global r
    if ballx <= 0:
        gol2 = str(int(gol2) + 1)
        ballx = 300
        bally = 270
    if ballx >= 600:
        gol1 = str(int(gol1) + 1)
        ballx = 300
        bally = 270
    d=[gol1,gol2]
    return d
def pobed():
    '''Функция, показывающая, кто победил'''
    global height
    global speed
    global h
    global x1
    global ballx
    global bally
    global speedball
    global key
    global gol1
    global gol2
    global otskok
    global r
    if int(gol1) == 10:
        key = 5
        screen.blit(pobed1, (0, 0))
        return 'Player1 win'
    if int(gol2) == 10:
        key = 5
        screen.blit(pobed2, (0, 0))
        return 'Player2 win'

def zapusk():
    '''Функция инициализации платформ, мяча, экрана'''
    screen.fill(bg_color)
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.draw.rect(screen, (255, 255, 255), (x1, y1, width, height))
    pygame.draw.rect(screen, (255, 255, 255), (0, 600, 600, 1))
    pygame.draw.circle(screen, (255, 255, 255), (ballx, bally), r)  # мячик и что с ним связано

def run():
    '''Функция-цикл, отвечающая за работу игры и выход из нее'''
    k=True

    while k:

        pygame.time.delay(28)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                k=False
                return 'Game closed'
        raketki()
        zapusk()
        ball()

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface1 = myfont.render('Player 1', False, (255, 255, 255))
        textsurface2 = myfont.render('Player 2', False, (255, 255, 255))
        score1 = myfont.render(str(gol1), False, (255, 255, 255))
        score2 = myfont.render(str(gol2), False, (255, 255, 255))
        screen.blit(textsurface1, (0, 610))
        screen.blit(textsurface2, (460, 610))
        screen.blit(score1, (50, 650))
        screen.blit(score2, (510, 650))

        goal()

        pobed()
        pygame.display.update()

run()
