import pygame
import time
import random
#import subprocess
#import os

pygame.init()  
  
gameDisplay = pygame.display.set_mode()
pygame.display.set_caption('Get Over Here Mr.Mike!!!')
clock = pygame.time.Clock()
 
def blitImg(img, x, y):
    gameDisplay.blit(pygame.image.load(str(img)),(x,y))

def read_file(filename):
    f = open(filename,'r')
    line = f.readline()
    f.close()
    return line

troublemaker = read_file('Settings.txt') 
#print(player)
player = pygame.image.load(str(troublemaker))
gameIcon = pygame.image.load('icon1.png')
pygame.display.set_icon(gameIcon)
black = (0,0,0)
white = (255,255,255)
brown = (160,113,69)
red = (200,0,0)
green  = (0,200,0)
yellow = (255,255,0)
gold = (255,215,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
dark_grey = (200,200,200)
grey = (215,215,215)
bright_grey = (225,225,225)
first = True

class Mr:
    Mike = "MR.MIKE GET OVER HERE"

cryForHelp = Mr.Mike
#print(cryForHelp)

##def readyPlayerOne():
##    # os.system('open '+ "/Users/ian.ault/Desktop/MR.MIKE/TextFile1.sh")
##    # subprocess.call("/Users/ian.ault/Desktop/MR.MIKE/TextFile1.sh")
##    pass

def Credits():
    Credit = True
    while Credit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("Raleway-Medium.ttf",90)
        TextSurf, TextRect = text_objects(('Made By: Keith Farr and'),largeText)
        TextRect.center = ((640),(200))
        gameDisplay.blit(TextSurf, TextRect)
        largeText = pygame.font.Font("Raleway-Medium.ttf",90)
        TextSurf, TextRect = text_objects(('Ibrahim Dabarani'),largeText)
        TextRect.center = ((640),(280))
        gameDisplay.blit(TextSurf, TextRect)

        button("Back",490,500,300,100,red,bright_red,main)

        pygame.display.update()
        clock.tick(15)
    
def quitgame():
    pygame.quit()
    quit()

def imgButton(msg,x,y,w,h,ic,ac,func,params,action=None,paramsSecond=None):
    (params1,params2,params3) = params
    (params4,params5) = paramsSecond
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h >mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            # pygame.draw.rect(gameDisplay, bright_green,(x,y,w,h))
            # time.sleep(.5)
            if params2 != None:
                action(params4,params5)
            else:
                action()
            main()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("Raleway-Medium.ttf",45)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    func(params1,params2,params3)

def button(msg,x,y,w,h,ic,ac,action=None,params=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h >mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if params != None:
                (params1, params2) = params
                action(params1,params2)
            else:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("Raleway-Medium.ttf",45)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def quad(color,x,y,w,h,t):
    pygame.draw.rect(gameDisplay,color,(x,y,w,h),t)

def line(color,closed,points,t):
    pygame.draw.lines(gameDisplay,color,closed,points,t)
    
def write_file(filename,text):
    f = open(filename,'w')
    f.write(text)
    f.close()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text(msg, x, y, size=100):
    largeText = pygame.font.Font("Raleway-Medium.ttf", size)
    TextSurf, TextRect = text_objects((msg), largeText)
    TextRect.center = ((x),(y))
    gameDisplay.blit(TextSurf, TextRect)

def mobBoss():
    while True:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        blitImg("MobBoss.png",640,0)
        text("Complete the Campaign to Unlock", 640, 300, 70)
        button("Back",490,500,300,100,red,bright_red,playerSelect)

        pygame.display.update()
        clock.tick(120)

def playerSelect():
    global first
    first = False
    nameSize = 25
    quoteSize = 18
    while True:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Title
        text('Select Your Trouble Maker!',650, 60, 90)
        
        # Player1
        imgButton('', 95, 115, 260,310, white, grey, blitImg,
            ('player1.png', 100, 120), write_file,
            ('Settings.txt','player1.png'))
        text('Ibrahim Dabarani:', 220, 460, nameSize)
        text('"Gimme your lunch money!"', 220, 490, quoteSize)
        
        # Player2
        imgButton('', 375, 115, 260,310, white, grey, blitImg,
            ('player2.png', 380, 120), write_file,
            ('Settings.txt','player2.png'))
        text('Keith Farr:', 500, 460, nameSize)
        text('"Keith was here"', 500, 490, quoteSize)
        
        # Player3
        imgButton('', 655, 115, 260,310, white, grey, blitImg,
            ('player3.png', 660, 120), write_file,
            ('Settings.txt','player3.png'))
        text('Kaden Chin-Massey:', 780, 460, nameSize)
        text('"I will take your juice box!"', 780, 490, quoteSize)
        
        # Player4
        imgButton('', 935, 115, 260,310, white, grey, blitImg,
            ('player4.png', 940, 120), write_file,
            ('Settings.txt','player4.png'))
        text('Mohamud Hassan:', 1060, 460, nameSize)
        text('"Can you gimme my bak-pak."', 1060, 490, quoteSize)
        
        # Mob Boss
        button('Mob Boss',275,580,300,100,dark_grey,grey,mobBoss)
        button("Back",725,580,300,100,red,bright_red,main)
        troublemaker = read_file('Settings.txt')
        
#the banana was orange so I decided to not eat it after all. in the end I gave it to demitri and he threw it at kaden!
        
        pygame.display.update()
        clock.tick(30)

def main():
    time.sleep(.2)
    while True:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

##        button("Start!",275,450,300,100,green,bright_green,readyPlayerOne)
##        button("Quit",725,450,300,100,red,bright_red,quitgame)
##        button("Select Player",275,575,300,100,gold,yellow,playerSelect)
##        button("Credits",725,575,300,100,dark_grey,grey)
        button("Select Player",275,450,300,100,gold,yellow,playerSelect)
        button("Credits",725,450,300,100,dark_grey,grey,Credits)
        button("Start!",275,575,300,100,green,bright_green,loop)
        button("Quit",725,575,300,100,red,bright_red,quitgame)
        text(cryForHelp, 640, 200)

        pygame.display.update()
        clock.tick(120)

def win():
##    def dance(num):
##        blitImg("dance"+str(num+1)+".jpg",0,0)
    gameDisplay.fill(white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for i in range(16):
            time.sleep(.1)
            blitImg("dance"+str(i+1)+".jpg",0,0)
    
        pygame.display.update()
        clock.tick(30)

    
    

def loop():
    global first
    first = True
    troublemaker = read_file('Settings.txt')
    up,down,left,right,b,a = 0,0,0,0,0,0
##    Start Cordinates
    mikeX, mikeY = 700,200
    car1X, car1Y = 100,200
    car2X, car2Y = 300,200
    car3X, car3Y = 500,200
    

    if troublemaker == "player1.png":
        player = "face1.png"
    elif troublemaker == "player2.png":
        player = "face2.png"
    elif troublemaker == "player3.png":
        player = "face3.png"
    elif troublemaker == "player4.png":
        player = "face4.png"
    else:
        player = "icon1.png"

    time.sleep(.2)
    

    while True:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            ## Controls
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mikeY += 10
                    up += 1
                if event.key == pygame.K_DOWN:
                    mikeY -= 10 
                    down += 1
                if event.key == pygame.K_LEFT:
                    mikeX -= 10
                    left += 1
                if event.key == pygame.K_RIGHT:
                    right += 1
                if event.key == pygame.K_b:
                    b += 1
                if event.key == pygame.K_a:
                    a += 1
        if up == 2 and down == 2 and left == 2 and right == 2 and b == 1 and a == 1:
            mikeX,mikeY = random.randint(0,1280),random.randint(0,720)
            win()
##            if event.type == pygame.KEYUP:
##                pass
            ##if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            ##                    x_change = (-4 - (dodged * 0.09)) * 1.2






            
        # Mike car
        mike = blitImg("Lamboveiw1.png",mikeX,mikeY)
        blitImg(player,mikeX+75,mikeY+40)
        # Ibrahim car
        blitImg("Car1.png",car1X,car1Y)
        blitImg(player,car1X+70,car1Y+75)
        # Keith car
        blitImg("Car2.png",car2X,car2Y)
        blitImg(player,car2X+75,car2Y+48)
        # Kden car
        blitImg("Car3.png",car3X,car3Y)
        blitImg(player,car3X+72,car3Y+55)
        # Mohamud
        button("Back",725,580,300,100,red,bright_red,main)
        line(black,False,[(640,0),(640,1.1234e9)],10)

        
            

        pygame.display.update()
        clock.tick(30)

main()
pygame.quit()
quit()
