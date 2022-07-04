#(to use this program enter the number of data points you would like to be sorted and then press enter)
import pygame
from sys import exit
from random import shuffle
from time import sleep
pygame.init()
#visual constatns
baseFont = pygame.font.Font(None, 32)
white=255,255,255
black=0,0,0
green=0,255,0
red=255,0,0

#screen 
Sdims=Swidth,Shight=1000,500
screen=pygame.display.set_mode(Sdims)

#user input box
IBW,IBH=200,25
inputBoxRect=pygame.Rect(0.5*(Swidth-IBW),Shight*0.9,IBW,IBH)
IBactive=False
userInput=''

#sortables
data=[]
def createBars(UI):
    global data,Swidth,Shight
    data=[]
    try:
        numBars=int(UI)
        for i in range(numBars):
            dataPoint=0.9*((i+1)/numBars)
            data.append(dataPoint)
    except ValueError:
        pass
    shuffle(data)
    print(data)
    drawBars(numBars)
    sleep(3)
    bubbleSort(numBars)

def drawBars(numBars):
    global data
    screen.fill(black)
    for i in range(len(data)):
        barWidth=Swidth/numBars
        barHeight=Shight*0.9*data[i]    
        rect=pygame.Rect(barWidth*i,(Shight*0.9)-barHeight,barWidth,barHeight)
        pygame.draw.rect(screen,white,rect)
    pygame.display.flip()

def bubbleSort(numBars):
    global data
    sorted=False
    while not sorted:
        sorted=True
        try:
            for i in range(len(data)):
                if data[i]>data[i+1]:
                    sorted=False
                    temp=data[i+1]
                    data[i+1]=data[i]
                    data[i]=temp
                drawBars(numBars)
        except IndexError:
            pass
            


#game loop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inputBoxRect.collidepoint(event.pos):
                IBactive = True
            else:
                IBactive = False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                userInput=userInput[:-1]
            elif event.key==pygame.K_RETURN:
                createBars(userInput)
                userInput=''
            else:
                userInput+=event.unicode 
    
    #render input box
    inputBox=pygame.draw.rect(screen,white,inputBoxRect)
    textSurface=baseFont.render(userInput,True,black)
    screen.blit(textSurface,(inputBoxRect.x+5,inputBoxRect.y+5))
    pygame.display.flip()