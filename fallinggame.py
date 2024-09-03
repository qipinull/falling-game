
import pygame
import random
import math
import os

# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()

# Dimension of the display
CharDisplayX = 400
CharDisplayY = 600

# create the display surface object  
# of specific dimension.  
win = pygame.display.set_mode((CharDisplayX, CharDisplayY))

# set the pygame window name 
pygame.display.set_caption("Rainy Window")

# colours
bg_colour = 25, 25, 25
WHITE = (255,255,255)

# time
clock = pygame.time.Clock()
basetime = 6000
seconds_ht = basetime / 100
seconds = math.floor(seconds_ht)
mins = 0
hours = 0
done = False

# score
score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

# object current co-ordinates 
x = (CharDisplayX / 2)
y = (CharDisplayY / 2)
tempX = (random.randrange(20,CharDisplayX - 20))
tempY = (random.randrange(20,CharDisplayY - 20))
goldX = (random.randrange(20,CharDisplayY - 20))
goldY = (random.randrange(20,CharDisplayY - 20))

# dimensions of the object 
size = 20
Psize = 20
width = size
height = size
Pwidth = Psize
Pheight = Psize

jumping = False

#variables
gold_collectable = False
gold1 = random.randrange(1,100)
gold2 = random.randrange(1,100)
pause = False
start = True
gamemode = ("Timed")
gameover = False
strip = r"\n"

# highscores
file_name = r'highscore.txt'
my_local_file = os.path.join(os.path.dirname(__file__), (file_name))
with open(my_local_file) as file:
    hs1 = file.readline()
    hs2 = file.readline()
    timed_highscore = hs1.rstrip('\r\n')
    infinite_highscore = hs2.rstrip('\r\n')
    int(timed_highscore)
    int(infinite_highscore)
    file.close
    mode_highscore = timed_highscore

# enemy
enemy_hit = 0
badY = 0
badY2 = 0
badY3 = 0
badY4 = 0
badX = (random.randrange(0,CharDisplayY))
badX2 = (random.randrange(0,CharDisplayY))
badX3 = (random.randrange(0,CharDisplayY))
badX4 = (random.randrange(0,CharDisplayY))
enemyspeed = random.randrange(2,10)
enemyspeed2 = random.randrange(2,10)
enemyspeed3 = random.randrange(2,10)
enemyspeed4 = random.randrange(2,10)

# gravity
Ygravity = 1
# jump hight
jumphight = 20
# y velocity
Yvelocity = jumphight

# velocity / speed of movement
vel = 3

# Indicates pygame is running
run = True
  
# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
      
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False


    # stores keys pressed 
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_ESCAPE]:
        pause = True
    
# start menu
    while start == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys_pressed = pygame.key.get_pressed()

            win.fill((100, 100, 100))
            if keys_pressed[pygame.K_SPACE]:
                if gamemode == ("Timed"):
                    basetime = 6000
                score = 0
                start = False
            if keys_pressed[pygame.K_1]:
                basetime = 6000
                score = 0
                gamemode = ("Timed")
                mode_highscore = timed_highscore
            if keys_pressed[pygame.K_2]:
                basetime = 0
                score = 0
                gamemode = ("Infinite")
                mode_highscore = infinite_highscore
            if keys_pressed[pygame.K_y]:
                pygame.quit()
                quit()
            text =  game_font.render(f"Highcore: {mode_highscore}",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 105,CharDisplayX / 2))
            
            text =  game_font.render(f"press SPACE to start",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 160,(CharDisplayY / 2) -  60))
            
            text =  game_font.render(f"Mode:",False,WHITE)
            win.blit(text,((0,0 + 5)))

            text =  game_font.render(f"{gamemode}",False,WHITE)
            win.blit(text,((0),(30) + 10))
            
            pygame.display.update()

    # pause menu
    while pause == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys_pressed = pygame.key.get_pressed()

            win.fill((100, 100, 100))
            if keys_pressed[pygame.K_SPACE]:
                pause = False
            if keys_pressed[pygame.K_r]:
                score = 0
                basetime = 0
                enemy_hit = 0
                pause = False
            if keys_pressed[pygame.K_y]:
                pause = False
                start = True
            text =  game_font.render(f"score: {score}",False,WHITE)
            win.blit(text,((0),(CharDisplayX / 2)-70))
            
            text =  game_font.render(f"time: {seconds}",False,WHITE)
            win.blit(text,((0),(CharDisplayX / 2) -35))
            
            text =  game_font.render(f"press SPACE to resume",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 180,(CharDisplayY / 2) -  60))
            
            text =  game_font.render(f"press R to restart",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 130,(CharDisplayY / 2) - 20))

            text =  game_font.render(f"press Y for menu",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 130,(CharDisplayY / 2) + 20))
            
            pygame.display.update()
    
    # gameover
    while gameover == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys_pressed = pygame.key.get_pressed()
            if score >= int(timed_highscore) and gamemode == ("Timed"):
                timed_highscore = score
            win.fill((100, 100, 100))
            if keys_pressed[pygame.K_r]:
                score = 0
                basetime =  6000
                enemy_hit = 0
                gameover = False
            if keys_pressed[pygame.K_y]:
                score = 0
                basetime =  6000
                enemy_hit = 0
                gameover = False
                start = True
            text =  game_font.render(f"score: {score}",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 150,CharDisplayX / 2))
                
            text =  game_font.render(f"enemies hit: {enemy_hit}",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 150,(CharDisplayX / 2) - 40))
            
            text =  game_font.render(f"Well Done!",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 180,(CharDisplayY / 2) -  60))
                
            text =  game_font.render(f"press R to restart",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 130,(CharDisplayY / 2) - 20))

            text =  game_font.render(f"press Y for menu",False,WHITE)
            win.blit(text,((CharDisplayX / 2) - 130,(CharDisplayY / 2) + 20))

            if int(timed_highscore) <= score:
                timed_highscore = score

            saving = open(my_local_file, "w")
            saving.write(str(timed_highscore)+"\n")
            saving.write(str(infinite_highscore)+"\n")
            saving.close()

            pygame.display.update()

    # if up arrow key or w is pressed
    if keys_pressed[pygame.K_w] and y>0 or keys_pressed[pygame.K_UP] and y>0:
          
        # move up
        y -= vel
          
    # if right arrow key or d is pressed
    if keys_pressed[pygame.K_d] and x<CharDisplayX-Pwidth or keys_pressed[pygame.K_RIGHT] and x<CharDisplayX-Pwidth:
          
        # move right
        x += vel
    
        # if left arrow key or a is pressed
    if keys_pressed[pygame.K_a] and x>0 or keys_pressed[pygame.K_LEFT] and x>0:
          
        # move left
        x -= vel
          
    # if down arrow key or s is pressed
    if keys_pressed[pygame.K_s] and y<CharDisplayY-Pwidth or keys_pressed[pygame.K_DOWN] and y<CharDisplayY-Pwidth:
          
        # move down
        y += vel
    
    if keys_pressed[pygame.K_SPACE] and y>0:
        jumping = True

    # collectables
    if  pygame.Rect.colliderect(pygame.draw.rect(win, (255, 0, 0), (x, y, Pwidth, Pheight)), pygame.draw.rect(win, (0, 255, 0), (tempX, tempY, width, height))):
        tempX = (random.randrange(20,CharDisplayX - 20))
        tempY = (random.randrange(20,CharDisplayY - 20))
        score = score + 1
        if gold_collectable is False:
            gold1 = random.randrange(1,100)
            gold2 = random.randrange(1,100)
            if gold1 == gold2:
                goldX = (random.randrange(20,CharDisplayX - 20))
                goldY = (random.randrange(20,CharDisplayY - 20))
                gold_collectable = True
    
    if pygame.Rect.colliderect(pygame.draw.rect(win, (255, 0, 0), (x, y, Pwidth, Pheight)), pygame.draw.rect(win, (200, 175, 0), (goldX, goldY, width, height))) and gold_collectable == True:
        score = score + 10
        gold_collectable = False
        
        
    # enemy
    if  pygame.Rect.colliderect(pygame.draw.rect(win, (255, 0, 0), (x, y, Pwidth, Pheight)), pygame.draw.rect(win, (0, 0, 255), (badX, badY, width, height))):
        enemyspeed = random.randrange(2,10)
        badX = (random.randrange(0,CharDisplayX - 20))
        badY = 0
        enemy_hit += 1
        if score >= 1:
            score = score - 1

        
    if  pygame.Rect.colliderect(pygame.draw.rect(win, (255, 0, 0), (x, y, Pwidth, Pheight)), pygame.draw.rect(win, (0, 0, 254), (badX2, badY2, width, height))):
        enemyspeed2 = random.randrange(2,10)
        badX2 = (random.randrange(0,CharDisplayX - 20))
        badY2 = 0
        enemy_hit += 1
        if score >= 1:
            score = score - 1
    
    if  pygame.Rect.colliderect(pygame.draw.rect(win, (255, 0, 0), (x, y, Pwidth, Pheight)), pygame.draw.rect(win, (0, 0, 253), (badX3, badY3, width, height))):
        enemyspeed3 = random.randrange(2,10)
        badX3 = (random.randrange(0,CharDisplayX - 20))
        badY3 = 0
        enemy_hit += 1
        if score >= 1:
            score = score - 1
    
    if  pygame.Rect.colliderect(pygame.draw.rect(win, (255, 0, 0), (x, y, Pwidth, Pheight)), pygame.draw.rect(win, (0, 0, 252), (badX4, badY4, width, height))):
        enemyspeed4 = random.randrange(2,10)
        badX4 = (random.randrange(0,CharDisplayX - 20))
        badY4 = 0
        enemy_hit += 1
        if score >= 1:
            score = score - 1


    # enemy move
    if badY >= CharDisplayY:
        enemyspeed = random.randrange(2,10)
        badX = (random.randrange(0,CharDisplayX - 20))
        badY = 0
    if badY2 >= CharDisplayY:
        enemyspeed2 = random.randrange(2,10)
        badX2 = (random.randrange(0,CharDisplayX - 20))
        badY2 = 0
    if badY3 >= CharDisplayY:
        enemyspeed3 = random.randrange(2,10)
        badX3 = (random.randrange(0,CharDisplayX - 20))
        badY3 = 0
    if badY4 >= CharDisplayY:
        enemyspeed4 = random.randrange(2,10)
        badX4 = (random.randrange(0,CharDisplayX - 20))
        badY4 = 0
    badY += enemyspeed
    badY2 += enemyspeed2
    badY3 += enemyspeed3
    badY4 += enemyspeed4
    pygame.draw.rect(win, (0, 0, 255), (badX, badY, width, height))
    pygame.draw.rect(win, (0, 0, 254), (badX2, badY2, width, height))
    pygame.draw.rect(win, (0, 0, 253), (badX3, badY3, width, height))
    pygame.draw.rect(win, (0, 0, 252), (badX4, badY4, width, height))

    if  x <= 0:
            x = 379
    if x >= 380:
            x = 1

    # completely fill the surface object  
    # with black colour  
    win.fill((bg_colour))
      
    # drawing object on screen which is rectangle here 
    pygame.draw.rect(win, (255, 0, 0), (x, y, Pwidth, Pheight))
    pygame.draw.rect(win, (0, 255, 0), (tempX, tempY, width, height))
    if gold_collectable is True:
        pygame.draw.rect(win, (200, 175, 0), (goldX, goldY, width, height))
        pass
    pygame.draw.rect(win, (0, 0, 255), (badX, badY, width, height))
    pygame.draw.rect(win, (0, 0, 254), (badX2, badY2, width, height))
    pygame.draw.rect(win, (0, 0, 253), (badX3, badY3, width, height))
    pygame.draw.rect(win, (0, 0, 252), (badX4, badY4, width, height))
    text =  game_font.render(f"score: {score}",False,WHITE)
    win.blit(text,(5,40))

    text =  game_font.render(f"time: {seconds}",False,WHITE)
    win.blit(text,(5,5))
    seconds_ht = basetime / 100
    seconds = math.floor(seconds_ht)
    if clock.tick(1000) and gamemode == ("Infinite"):
        basetime += 1
    if clock.tick(1000) and gamemode == ("Timed"):
        basetime -= 1
    if basetime <= 0 and gamemode == ("Timed"):
        gameover = True

    basefps = clock.get_fps()
    fps = math.floor(basefps)
    text =  game_font.render(f"FPS: {fps}",False,WHITE)
    win.blit(text,(CharDisplayX - (CharDisplayX / 3),5))

    if score >= int(infinite_highscore):
        if gamemode == ("Infinite"):
            infinite_highscore = score

    saving = open(my_local_file, "w")
    saving.write(str(timed_highscore)+"\n")
    saving.write(str(infinite_highscore)+"\n")
    saving.close()

    # it refreshes the window
    pygame.display.update() 
    
  
# closes the pygame window 
pygame.quit()