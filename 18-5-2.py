import pygame, sys                                                        
from pygame.locals import *                                               
  
class MyBallClass(pygame.sprite.Sprite):                                  
    def __init__(self, image_file, speed, location):              
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)                        
        self.rect = self.image.get_rect()                                 
        self.rect.left, self.rect.top = location                          
        self.speed = speed
        
    def move(self):
        global points, score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            
        if self.rect.top <= 0 :                                           
            self.speed[1] = -self.speed[1]                                
            points = points + 1                                           
            score_text = font.render(str(points), 1, (0, 0, 0))
            
class MyPaddleClass(pygame.sprite.Sprite):                               
    def __init__(self, location):                                        
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([200, 20])                
        image_surface.fill([0,0,0])                                      
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()                           
        self.rect.left, self.rect.top = location
        
pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall1 = MyBallClass('wackyball.bmp', [10,5], [50, 50])
myBall2 = MyBallClass('wackyball.bmp', [-10,5], [590, 50])                  
ballGroup1 = pygame.sprite.Group(myBall1) 
ballGroup2 = pygame.sprite.Group(myBall2)                                 
paddle = MyPaddleClass([270, 400])
lives = 4
points = 0

font = pygame.font.Font(None, 50)
score_text = font.render(str(points), 1, (0,0,0))
textpos = [10,10]
done = False                                      

while 1:                                                                 
    clock.tick(30)                                                       
    screen.fill([255, 255, 255])                                         
    for event in pygame.event.get():                                     
        if event.type == QUIT:                                           
            sys.exit()                                                   
        elif event.type == pygame.MOUSEMOTION:                           
            paddle.rect.centerx = event.pos[0]
            
    if pygame.sprite.spritecollide(paddle, ballGroup1, False):
        if myBall1.rect.centerx > paddle.rect.right or myBall1.rect.centerx <paddle.rect.left:
            points = points + 2
            score_text = font.render(str(points), 1, (0, 0, 0))
        myBall1.speed[1] = -myBall1.speed[1]
    myBall1.move()                                                        
    
    if pygame.sprite.spritecollide(paddle, ballGroup2, False):
        if myBall2.rect.centerx > paddle.rect.right or myBall2.rect.centerx <paddle.rect.left:
            points = points + 2
            score_text = font.render(str(points), 1, (0, 0, 0))
        myBall2.speed[1] = -myBall2.speed[1]
    myBall2.move()     
    
    if not done:                                                          
        screen.blit(myBall1.image, myBall1.rect)
        screen.blit(myBall2.image, myBall2.rect)                                       
        screen.blit(paddle.image, paddle.rect)                            
        screen.blit(score_text, textpos)                                  
        for i in range (lives):                                           
            width = screen.get_width()                                    
            screen.blit(myBall1.image, [width - 40 * i, 20])               
        pygame.display.flip()               
    
    if myBall1.rect.top >= screen.get_rect().bottom or myBall2.rect.top >= screen.get_rect().bottom: 
        lives = lives - 1                                                 
        
        if lives == 0:                                                    
            final_text1 = "Game Over"                                     
            final_text2 = "Your final score is:  " + str(points)          
            ft1_font = pygame.font.Font(None, 70)                         
            ft1_surf = font.render(final_text1, 1, (0, 0, 0))             
            ft2_font = pygame.font.Font(None, 50)                         
            ft2_surf = font.render(final_text2, 1, (0, 0, 0))             
            screen.blit(ft1_surf, [screen.get_width()/2 - \
                        ft1_surf.get_width()/2, 100])
            screen.blit(ft2_surf, [screen.get_width()/2 - \
                        ft2_surf.get_width()/2, 200])
            pygame.display.flip()                                         
            done = True
        else:             
            pygame.time.delay(2000)                                       
            myBall1.rect.topleft = [50, 50] 
            myBall2.rect.topleft = [590,50] 
