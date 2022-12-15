import pygame
from pygame import display, Color, draw
import time
import random
pygame.init()
display_width=700
display_height=560
block_size=20
fps=15
direction="right"
applethick=30


green=(0,155,0)
gamedisplay = display.set_mode((display_width,display_height))
display.set_caption('hello')
icon=pygame.image.load('picture/apple.png')
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)

def highscore(score):
  if highscore>score:
    text=smallfont.render("highscore: "+str(highscore),True,Color('black'))
    gamedisplay.blit(text,[0,10])
  if highscore<score:
    highscore=score
    text=smallfont.render("highscore: "+str(highscore),True,Color('black'))
    gamedisplay.blit(text,[0,10])
def score(score):
  text=smallfont.render("score: "+str(score),True,Color('black'))
  gamedisplay.blit(text,[0,0])
  

def rand_apple():
  applex=round(random.randrange(10,display_width-applethick))
  appley=round(random.randrange(10,display_height-applethick))
  return applex,appley
  
def game_intro():
  intro=True
  while intro:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        quit()
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_c:
          intro=False
        if event.key==pygame.K_q:
          pygame.quit()
          quit()
    
    gamedisplay.fill(Color('white'))
    message_to_screen("welcome to slither",Color('green'), y_displace=-100, size="large")
    message_to_screen("the objective of the game is to read apple", Color('black'), -30, 'small')
    message_to_screen("the more apple you eat the longer you get",Color('black'), 10, size="small")
    message_to_screen("if you run into your self or the edges, you die", Color('black'), 50, 'small')
    message_to_screen("press C to play or Q to quit", Color('black'), 120, 'small')
    pygame.display.update()
    clock.tick(5)
img=pygame.image.load('picture/snakehead.png')
appleimg=pygame.image.load('picture/apple.png')
def snake(block_size,snakelist):
  if direction=="right":
    head=pygame.transform.rotate(img,270)
  if direction=="left":
    head=pygame.transform.rotate(img,90)
  if direction=="up":
    head=img
  if direction=="down":
    head=pygame.transform.rotate(img,180)
  gamedisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
  for xny in snakelist[:len(snakelist)-1]:
    draw.rect(gamedisplay,green, [xny[0], xny[1], block_size,block_size])
    
def text_object(text,color,size):
  if size=="small":
    textsurface=smallfont.render(text,True,color)
  elif size=="medium":
    textsurface=medfont.render(text,True,color)
  elif size=="large":
    textsurface=largefont.render(text,True,color)
  return textsurface, textsurface.get_rect()
  
def message_to_screen(msg,color, y_displace=0, size="small"):
  textsurf,textrect=text_object(msg,color,size)
  textrect.center=(display_width/2), (display_height/2)+y_displace
  gamedisplay.blit(textsurf,textrect)
  
def gameloop():
  global direction
  direction='right'
  exit=False
  gameover=False
  
  lead_x=display_width/2
  lead_y=display_height/2
  
  lead_x_change=10
  lead_y_change=0
  
  snakelist=[]
  snakelength=1
  
  applex,appley=rand_apple()
  while not exit:
      while gameover==True:
        gamedisplay.fill(Color('white'))
        message_to_screen('Game over',Color('red'),y_displace=-50, size="large")
        message_to_screen('press C to play again, press Q to quit',Color('black'),50, size="medium")
        display.update()
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            exit=True
            gameover=False
          if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
              exit=True
              gameover=False
            if event.key==pygame.K_c:
              gameloop()
           
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          exit=True
        if event.type == pygame.KEYDOWN:
          if event.key==pygame.K_LEFT:
            lead_x_change=-block_size
            lead_y_change=0
            direction="left"
          elif event.key==pygame.K_RIGHT:
            lead_x_change=block_size
            lead_y_change=0
            direction="right"
          elif event.key==pygame.K_UP:
            lead_y_change=-block_size
            lead_x_change=0
            direction="up"
          elif event.key==pygame.K_DOWN:
            lead_y_change=block_size
            lead_x_change=0
            direction="down"
        #if event.type==pygame.KEYUP:
         # if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
          #  lead_x_change=0
          #elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
           # lead_y_change=0
      
      lead_x+=lead_x_change
      lead_y+=lead_y_change
      if lead_x >= display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
        gameover=True
        
      gamedisplay.fill(Color('white'))
      gamedisplay.blit(appleimg,(applex,appley))
    
      snakehead=[]
      snakehead.append(lead_x)
      snakehead.append(lead_y)
      snakelist.append(snakehead)
    
      if len(snakelist)>snakelength:
        del snakelist[0]
        
      for eachsegment in snakelist[:-1]:
        if eachsegment==snakehead:
          gameover=True
          
      snake(block_size,snakelist)
      score(snakelength-1)
      highscore(score)
      display.update()
      

      if lead_x >applex and lead_x <applex+applethick or lead_x+block_size>applex and lead_x+block_size<applex+applethick:
        if lead_y >appley and lead_y <appley+applethick:
          applex,appley=rand_apple()
          snakelength+=1 
        elif lead_y+block_size>appley and lead_y+block_size<appley+applethick:
          applex,appley=rand_apple()
          snakelength+=1
      clock.tick(fps)
    
  quit()
game_intro()
gameloop()