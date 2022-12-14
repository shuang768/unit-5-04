import pygame
from pygame import display, Color, draw
import time
import random
pygame.init()
display_width=700
display_height=560
block_size=20
fps=15

gamedisplay = display.set_mode((display_width,display_height))
display.set_caption('hello')
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,25)

img=pygame.image.load('picture/snakehead.png')
def snake(block_size,snakelist):
  gamedisplay.blit(img,(snakelist[-1][0],snakelist[-1][1]))
  for xny in snakelist[:-1]:
    draw.rect(gamedisplay,Color('green'), [xny[0], xny[1], block_size,block_size])
    
def text_object(text,color):
  textsurface=font.render(text,True,color)
  return textsurface, textsurface.get_rect()
  
def message_to_screen(msg,color):
  textsurf,textrect=text_object(msg,color)
#  screen_text = font.render(msg,True,color)
#  gamedisplay.blit(screen_text,[display_width/2*0.5,display_height/2-0.5])
  textrect.center=(display_width/2), (display_height/2)
  gamedisplay.blit(textsurf,textrect)
  
def gameloop():
  exit=False
  gameover=False
  
  lead_x=display_width/2
  lead_y=display_height/2
  
  lead_x_change=0
  lead_y_change=0
  
  snakelist=[]
  snakelength=1
  
  applex=round(random.randrange(10,display_width-block_size))#/10.0)*10.0
  appley=round(random.randrange(10,display_height-block_size))#/10.0)*10.0
  while not exit:
      while gameover==True:
        gamedisplay.fill(Color('white'))
        message_to_screen('Game over, press C to play again or Q to quit',Color('red'))
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
          elif event.key==pygame.K_RIGHT:
            lead_x_change=block_size
            lead_y_change=0
          elif event.key==pygame.K_UP:
            lead_y_change=-block_size
            lead_x_change=0
          elif event.key==pygame.K_DOWN:
            lead_y_change=block_size
            lead_x_change=0
        #if event.type==pygame.KEYUP:
         # if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
          #  lead_x_change=0
          #elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
           # lead_y_change=0
      
      lead_x+=lead_x_change
      lead_y+=lead_y_change
      if lead_x >= display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
        gameover=True
      applethick=30
      gamedisplay.fill(Color('blue'))
      draw.rect(gamedisplay,Color('red'), [applex,appley,applethick,applethick])
      draw.rect(gamedisplay,Color('green'), [lead_x, lead_y, block_size,block_size])
      
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
      display.update()
      

#      if lead_x>=applex and lead_x<=applex+applethick:
#        if lead_y>=appley and lead_y<=appley+applethick:
#          applex=round(random.randrange(10,display_width-block_size))#/10.0)*10.0
#          appley=round(random.randrange(10,display_height-block_size))#/10.0)*10.0
#          snakelength+=1
      if lead_x >applex and lead_x <applex+applethick or lead_x+block_size>applex and lead_x+block_size<applex+applethick:
        if lead_y >appley and lead_y <appley+applethick:
          applex=round(random.randrange(10,display_width-block_size))
          appley=round(random.randrange(10,display_height-block_size))
          snakelength+=1 
        elif lead_y+block_size>appley and lead_y+block_size<appley+applethick:
          applex=round(random.randrange(10,display_width-block_size))
          appley=round(random.randrange(10,display_height-block_size))
          snakelength+=1
      clock.tick(fps)
    
  quit()
gameloop()