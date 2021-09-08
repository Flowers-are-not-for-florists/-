import pygame
from numpy import random
import math

#初始化
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("逆行者-给医院配送口罩")
bgimg=pygame.image.load('bg.png')

#音乐
pygame.mixer.music.load('bgmusic.wav')
pygame.mixer.music.play(-1)

#玩家
playerimg=pygame.image.load('player.png')
playerx=339
playery=742
playerxstep=0
playerystep=0

#玩家移动
def moveplayer():
    global playerx,playery
    playerx +=playerxstep
    playery +=playerystep
    if playerx>739:
        playerx=739
    elif playerx<0:
        playerx=0
    elif playery>742:
        playery=742
    elif playery<0:
        playery=0

#感染者
infecteds=[]
infectednumber=10
class infected():
    def __init__(self):
        self.img=pygame.image.load("infected.png")
        self.x=random.randint(0,800)
        self.y=random.randint(50,500)
        self.xstep=random.uniform(0.2,0.4)

for i in range(infectednumber):
    infecteds.append(infected())

def showinfected():
    global checkmask,beinfected,playerimg
    for a in infecteds:
        screen.blit(a.img,(a.x,a.y))
        a.x+=a.xstep
        if a.x>710 or a.x<0:
            a.xstep=-a.xstep
            a.y+=20
        if distance(a.x,a.y,playerx,playery)<90:
            if checkmask==False:
                beinfected=True
                infecteds.clear()
            if checkmask==True:
                checkmask=False
                playerimg=pygame.image.load('player.png')
                infecteds.remove(a)

        
#距离
def distance(x1,y1,x2,y2):
    a=x1-x2
    b=y1-y2
    return math.sqrt(a*a+b*b)

#医院
def showhospital():
    global victory,checkmask
    himg=pygame.image.load('hospital.png')
    screen.blit(himg, (660,0))
    if checkmask==True:
        if distance(660,0,playerx,playery)<100:
            victory=True
            infecteds.clear()

#游戏结束
beinfected=False
victory=False
font=pygame.font.Font("freesansbold.ttf",64)
def checkbeinfected():
    if beinfected==True:
        text='Beinfected'
        beinfected1=font.render(text,True,(255,0,0))
        screen.blit(beinfected1, (250,350))
def checkvictory():
    if victory==True:
        text="Victory"
        victory1=font.render(text,True,(255,0,0))
        screen.blit(victory1,(300,330))

#口罩
checkmask=False
xm=random.randint(0,200)
ym=random.randint(300,500)
def mask():
    mimg=pygame.image.load('mask.png')
    screen.blit(mimg, (xm,ym))
    if distance(xm,ym,playerx,playery)<70:
        global playerimg,checkmask
        checkmask=True
        playerimg=pygame.image.load('playermask.jpg')
        
#游戏运行主程序
runing=True
while runing:
    screen.blit(bgimg, (0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                playerxstep=0.3
            elif event.key==pygame.K_LEFT:
                playerxstep=-0.3
            elif event.key==pygame.K_UP:
                playerystep=-0.3
            elif event.key==pygame.K_DOWN:
                playerystep=0.3
        if event.type==pygame.KEYUP:
            playerxstep=0
            playerystep=0
    screen.blit(playerimg,(playerx, playery))
    moveplayer()
    showinfected()
    showhospital()
    mask()
    checkbeinfected()
    checkvictory()
    pygame.display.update()