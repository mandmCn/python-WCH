import pygame, sys
pygame.init()

screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("wackyball.bmp")
x = 50
y = 50
speedx = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    pygame.time.delay(10)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x = x + speedx
    if x > 410 or x < 0:
        speedx = -speedx
    screen.blit(my_ball,[x,y])
    pygame.display.flip()