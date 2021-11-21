import pygame

def run():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('hot hockey')
    bg_color = (0, 0, 0)

    x=50
    y=240
    y1=240
    width=10
    height=60
    speed=10
    x1 = 550-width


    k=True

    while k:
        pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                k=False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and y<600-height:
            y+=speed
        if keys[pygame.K_UP] and y>0:
            y-=speed
        if keys[pygame.K_s] and y1<600-height:
            y1+=speed
        if keys[pygame.K_w] and y1>0:
            y1-=speed
        screen.fill(bg_color)
        pygame.display.flip()
        pygame.draw.rect(screen,(255,255,255),(x,y,width,height))
        pygame.draw.rect(screen, (255, 255, 255), (x1,y1, width, height))
        pygame.display.update()

run()
