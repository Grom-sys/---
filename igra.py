from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,picimage, sx,sy):
        super().__init__()
        self.image = transform.scale(image.load(picimage),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = sx 
        self.rect.y = sy
    def reset(self):
        scr.blit(self.image, (self.rect.x,self.rect.y))


scr = display.set_mode((700,500))
background = transform.scale(image.load("фон.jpg"),(700,500))
hero = transform.scale(image.load("plat.png"),(100,100))
hero2 = transform.scale(image.load("plat.png"),(100,100))
ball = GameSprite("gem.png",450,450)
game = True
clock = time.Clock()
FPS = 60
x1 = 150
y1= 150

dx = 5
dy = 3
while game:
    ball.rect.x += dx
    ball.rect.y -= dy
    if ball.rect.x > 650:
        dx *= -1
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > 450:
        dy *= -1
    if sprite.collide_rect(ball,hero):
        dx *= -1

    #scr.fill((50,50,150))
    scr.blit(background,(0,0))
    scr.blit(hero,(x1,y1))
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        y1 -= 5
    if keys_pressed[K_DOWN]:
        y1 += 5
    display.update()
    clock.tick(FPS)
