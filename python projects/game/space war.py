import pygame
from time import sleep
import random
from tkinter import messagebox
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((500,400))

health = 20

ship = pygame.image.load('spaceship.png')
background = pygame.image.load('background.jpg')

pos_x = 230
pos_y = 350
x_change = 0

boss = pygame.image.load('ufo.png')
boss_x = 200
boss_y = 50
boss_speed = 1

enemy = []
ene_x = []
ene_y = []
x_ene = []
y_ene = []

no_ene = 10
bull_c = 6
for i in range(no_ene):
    enemy.append(pygame.image.load('bots.png'))
    ene_x.append(random.randint(20,400))
    ene_y.append(random.randint(35,50))
    x_ene.append(0.5)
    y_ene.append(20)

bullet = pygame.image.load('bullet.png')
bul_x = 0
bul_y = 350
bul_speed = 2
bul_state = 'ready'

score = 0

font = pygame.font.SysFont('monteserate',30,True)

def Ship(x,y):
    screen.blit(ship ,(x, y))

def Enemy(x,y,i):
    screen.blit(enemy[i],(x, y))
    
def Bullet(x,y):
    global bul_state
    bul_state = 'fire'
    screen.blit(bullet,(x+9, y+14))

def Boss(x,y):
    screen.blit(boss, (x, y))

def Score():
    text = font.render('Score:'+str(score), 1, (0,255,0))
    screen.blit(text,(390,10))
def message():
    text = font.render('YOU WIN',1,(255,255,255))
    screen.blit(text,(220,190))

    
done = False


while not done:
    # --- Main event loop
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.8

            if event.key == pygame.K_RIGHT:
                x_change = 0.8

            if event.key == pygame.K_SPACE:
                if bul_state is 'ready':
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bul_x = pos_x
                    Bullet(bul_x,bul_y)             
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_change = 0        

    pos_x += x_change
  
# position of ship
    if pos_x <=0:
        pos_x = 0
    elif pos_x >= 450:
        pos_x = 450


#position of enemy
    for i in range(no_ene):
        ene_x[i] += x_ene[i]    
        if ene_x[i] <=0:
            x_ene[i] = 0.5
            ene_y[i] += y_ene[i]
            
        elif ene_x[i] >=470:
            x_ene[i] = -0.5
            ene_y[i] += y_ene[i]

            
        if bul_y >= ene_y[i] and bul_y<= ene_y[i]+5 and bul_x >= ene_x[i]-26 and bul_x <= ene_x[i]+10 :
            bul_y = 350
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bul_state = 'ready'
            score +=1
            no_ene -= 1
            
            
        Enemy(ene_x[i],ene_y[i],i)

    if no_ene <= 0:
        if health >0:
            Boss(boss_x,boss_y)
            pygame.draw.rect(screen,(255,0,0),(boss_x,boss_y-20,100,5))
            pygame.draw.rect(screen,(0,255,0),(boss_x,boss_y-20,100-(5 *(20 - health)),5))
            if bul_y >= boss_y and bul_y <= boss_y+50 and bul_x >= boss_x-25 and bul_x <= boss_x+75 :
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bul_y = 350
                bul_state = 'ready'
                health -=1
                
        boss_x += boss_speed
        if boss_x >= 400:
            boss_speed = -1 
        elif boss_x <=0:
            boss_speed = 1
        
    if bul_y <= 0:
        bul_y = 350
        bul_state = 'ready'
        bull_c -=1 
        
    if bul_state is 'fire':
        Bullet(bul_x,bul_y)
        
        bul_y -= bul_speed
         
    Ship(pos_x,pos_y)
    Score()
    pygame.display.update()



pygame.quit()
