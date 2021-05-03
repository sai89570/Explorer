import pygame
import time
import random
pygame.init()
white=(255,255,255)
yellow=(255,255,102)
black=(0,0,0)
red=(213,50,80)
green=(0,255,0)
blue=(50,153,213)
dis_width=600
dis_height=400
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('snake game by vamshi')
clock=pygame.time.clock()
snake_block=10
snake_speed=15
font_style=pygame.font.SysFont("bahnscrift",25)
score_font=pygame.font.SysFont("comicsansms",35)

def your_score(score):
    Value=score_font.render("your_score:"+str(score),True,yellow)
    dis.blit(value,[0,0])

def our_snake(snake_block,snake_list):
    for x in snale_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])
def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/3])
def gameloop():
    game_over=False
    game_close=False
    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_list=[]
    length_of_snake=1
    foodX=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foodY=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0

    while not game_over:
        while game_close==True:
            dis.fill(blue)
            message("You Lost!Press C-play Again or Q-Quit",red)
            your_score(length_of_snake+1)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_Q:
                    game_over=True
                    game_close=False
                if event.key==pygame.K_C:
                    gameloop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True
        x1+=x1_change
        y1+=y1_change

        dis.fill(blue)
        pygame.draw.rect(dis,green,[foodX,foodY,snake_block,snake_block])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list)>length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_Head:
                game_close=True
        our_snake(snake_block,snake_list)
        your_score(length_of_snake-1)
        pygame.display.update()
        if x1==foodX and y1==foodY:
            foodX=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
            foodY=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
            length_of_snake+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameloop()
        
                    
                    
                
            
