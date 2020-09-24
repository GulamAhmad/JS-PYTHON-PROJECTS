import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600,400))

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.e = pygame.image.load('bots.png')
        self.delete = False
    def show(self):
        screen.blit(self.e,(self.x, self.y))
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,32,32),2)
    def disappear(self):
        self.delete = True

class Ship:
    def __init__(self):
        self.x = 268
        self.y = 300
        self.s = pygame.image.load('spaceship.png')
        self.speed = 0

    def show(self):
        screen.blit(self.s,(self.x,self.y))
    
    
class Bullets:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.b = pygame.image.load('bullet.png')
    def show(self):
        screen.blit(self.b,(self.x,self.y))
    def move(self):
        self.y -= 0.2
            
done = False
enemys = []
bullet = []
ship = Ship()
no_enemy = 6


for i in range(no_enemy):
    enemy = Enemy(i*80+80,50)
    enemys.append(enemy)
while not done:
    # --- Main event loop
    screen.fill((0,0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.speed -= 0.1

            if event.key == pygame.K_RIGHT:
                ship.speed += 0.1 

            if event.key == pygame.K_SPACE:
                bullets = Bullets(ship.x+10,ship.y)
                bullet.append(bullets)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                ship.speed = 0

    ship.x += ship.speed            
    for i in range(no_enemy):
        enemys[i].show()
    for i in range(len(bullet)):
        bullet[i].show()
        bullet[i].move()
        for j in range(len(enemys)):
            if bullet[i].y <= enemys[j].y+32 and bullet[i].y >= enemys[j].y and bullet[i].x >= enemys[j].x-16 and  bullet[i].x <= enemys[j].x+20:
                enemys[i].disappear()

    for i in range(len(enemys)):
        if(enemys[i].delete):
            enemys.remove(enemys[i])

      

                
    ship.show()
    pygame.display.update()
pygame.quit()
    
