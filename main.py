import pygame
import time
import random

pygame.init()

pygame.display.set_caption("Thrill Chaser")

robot_img = pygame.image.load('robot.png')
rock_img = pygame.image.load('rock.png')
monster_img = pygame.image.load('monster.png')
door_img = pygame.image.load('door.png')
coin_img = pygame.image.load('coin.png')

#some constants
coin_robot_x = coin_img.get_width() + robot_img.get_width()
coin_robot_y = coin_img.get_height() + robot_img.get_height()
rock_robot_x = rock_img.get_width() + robot_img.get_width()
rock_robot_y = rock_img.get_height() + robot_img.get_height()
monster_robot_x = monster_img.get_width() + robot_img.get_width()
monster_robot_y = monster_img.get_height() + robot_img.get_height()

gameDisplay = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

#from here until class Button2 prepare for menu selection.

startImg = pygame.image.load("starticon.png")
quitImg = pygame.image.load("quiticon.png")
clickStartImg = pygame.image.load("clickedStartIcon.png")
clickQuitImg = pygame.image.load("clickedQuitIcon.png")
titleImg = pygame.image.load("titleicon.png")

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, parms, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                playerparms.append(parms[0])
                playerparms.append(parms[1])
                playerparms.append(parms[2])
                playerparms.append(parms[3])
                playerparms.append(parms[4])
                playerparms.append(parms[5])
                playerparms.append(parms[6])
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))


class Player:

    def __init__(self,robot_img,speedIn,robot_x,robot_y, healthy_bar):
        self.speed = speedIn
        self.robot_x = robot_x
        self.robot_y = robot_y
        self.robot_img = robot_img
        # self.robot_hit_x = robot_hit_x
        # self.robot_hit_y = robot_hit_y
        self.healthy_bar = healthy_bar

class Gameobject:

    def __init__(self, gameobject_img, speed, coord_x, coord_y, gameobject_hit_x, gameobject_hit_y):
        self.gameobject_img = gameobject_img
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.gameobject_hit_x = gameobject_hit_x
        self.gameobject_hit_y = gameobject_hit_y

class Random_harm_rock():

    def __init__(self, rock_img):
        self.pos_x = random.randrange(1, 640-rock_img.get_width())
        self.pos_y = random.randrange(1, 480-rock_img.get_height())
        self.velocity = [2, 2]
        self.rock_img = rock_img

    def move(self):
        
        self.pos_x += self.velocity[0]
        self.pos_y += self.velocity[1]

        if self.pos_x + rock_img.get_width() > 640 or self.pos_x < 0:
            self.velocity[0] = -self.velocity[0]
            #self.pos_x = random.randrange(1, 640-rock_img.get_width())
        if self.pos_y + rock_img.get_height() > 480 or self.pos_y < 0:
            self.velocity[1] = -self.velocity[1]
            #self.pos_y = random.randrange(1, 480-rock_img.get_height())

        #gameDisplay.blit(self.rock_img, (self.pos_x, self.pos_y))

def scorecounter(count, healthy_bar):
    
    pygame.draw.rect(gameDisplay, (220, 247, 230), pygame.Rect(150, 25, 150, 20)) 
    print('pointcoutner')
    font = pygame.font.SysFont("Arial", 20)
    text = font.render("Points:" + str(count), True, (255, 0, 0))
    gameDisplay.blit(text, (460, 0))
    if healthy_bar > 0:
        text1 = font.render("Healthy Value:" + str(healthy_bar), True, (255, 0, 0))
        gameDisplay.blit(text1, (150, 0))
        pygame.draw.rect(gameDisplay, (255,0,0), pygame.Rect(150, 25, 150-healthy_bar*1.5, 20))
    else:
        pygame.draw.rect(gameDisplay, (255,0,0), pygame.Rect(150, 25, 150, 20)) 
        text1 = font.render("Healthy Value:" + "0", True, (255, 0, 0))
        gameDisplay.blit(text1, (150, 0))
        pygame.time.wait(2000)
        screen_display('Game over!')
    

def prepare_coins(num):
    coins = []#stay still and waiting for robot player to score
    for i in range(num):
        coins.append(Gameobject(coin_img, random.randrange(1, 4), random.randrange(10, 620), random.randrange(50, 470), 40, 40))
    
    return coins

def screen_display(text):

    font = pygame.font.SysFont("Arial", 20)
    text_to_display = font.render(text, True, (88, 136, 166))
    print('text_to_display', text_to_display)
    gameDisplay.blit(text_to_display, (150, 240)) 


def quitgame():
    pygame.quit()
    quit()

def render_multi_line(text, x, y, fsize):
    font = pygame.font.SysFont("calibri", 20)
    lines = text.splitlines()
    for i, l in enumerate(lines):
        gameDisplay.blit(font.render(l, 0, (82, 62, 7)), (x, y + fsize*i))

def before_start():

    before_display = True

    while before_display: 
        # gameDisplay.fill((52, 247, 124))
        # screen_display('you have 60 seconds to collects as much coins as possible,\n try not to get hurt by random running rocks and tailing monsters \n ofc you can take a break by hidding near the door \n press S to start play')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((255, 255, 255))

        text= '                        welcome to "Thrill Chaser"\n\n\nyou have 30 seconds to collects as much coins as possible\n\ntry not to get hurt by random running rocks and tailing monsters\n\nofc you can take a break by hidding near the door\n\n\n                                enjoy chasing!'
        render_multi_line(text, 30, 40, 15)
        gameDisplay.blit(robot_img, (80, 300))
        gameDisplay.blit(monster_img, (200, 300))
        gameDisplay.blit(rock_img, (300, 320))
        gameDisplay.blit(coin_img, (400, 320))
        gameDisplay.blit(door_img, (500, 300))
        startButton = Button(startImg,190,420,60,20,clickStartImg,195,418,game_loop)
        quitButton = Button(quitImg,400,420,60,20,clickQuitImg,405,418,quitgame)

        pygame.display.update()
        clock.tick(15)

def result_display(score, time, healthy_bar):

    result = True
    while result:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill((52, 247, 124))
        lost_healthy_value = 100 - healthy_bar
        text=f'Your game result:\n\nwithin {time} seconds\n\nyou scored {score} points\n\nsuffered {lost_healthy_value} healthy value loss'
        render_multi_line(text, 30, 100, 15)
        gameDisplay.blit(robot_img, (500, 100))
        startButton = Button(startImg,190,420,60,20,clickStartImg,195,418,game_loop)
        quitButton = Button(quitImg,400,420,60,20,clickQuitImg,405,418,quitgame)
        pygame.display.update()
        clock.tick(15)

def game_loop():

    # before_start()
    
    #bg music and sound effects,multiple channels 
    pygame.mixer.init()
    bg_song = pygame.mixer.Sound('music.mp3')
    coin_collecting_sound = pygame.mixer.Sound('snap.mp3')
    rock_hit_sound = pygame.mixer.Sound('rockhit.flac')
    monster_hit_sound = pygame.mixer.Sound('monsterhit.mp3')
    bg_song.play()

    #set time counter
    counter, text = 30, '30'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    #load all sprites
    robot=Player(robot_img, 2, 320, 480-robot_img.get_height(), 100)

    monsters = []# to follow robot player
    for i in range(2):
        monsters.append(Gameobject(monster_img, random.randrange(1, 4), random.randrange(10, 630), random.randrange(10, 470), 40, 40))

    #rocks need to be randomly one-time moving and hurt robot player 
    rocks = []
    for i in range(5):
        rocks.append(Random_harm_rock(rock_img))

    #set coins ready
    coins = prepare_coins(5)

    #x_change=0
    score = 0
    counter_increase = 0

    while True:

        #fill bg
        #before_start()
        gameDisplay.fill((52, 247, 124))
        
        #all events!!!!

        #monsters tailing robot player here
        for event in pygame.event.get():

            if event.type == pygame.USEREVENT: 
                
                if counter == 0:
                    result_display(score, counter_increase, robot.healthy_bar)
                    #before_start()
                counter -= 1
                counter_increase += 1
                text = str(counter).rjust(3) if counter > 0 else 'Times up'

            if pygame.mouse.get_pressed()[0]:

                if event.type == pygame.MOUSEMOTION:
                    robot.robot_x = event.pos[0]-robot.robot_img.get_width()/2
                    robot.robot_y = event.pos[1]-robot.robot_img.get_height()/2

            if event.type == pygame.QUIT:
                exit(0)

        #monsters only following no damage inflicted upon robot
        
        for i in range(len(monsters)):
            if monsters[i].coord_x > robot.robot_x:
                monsters[i].coord_x -= 1
            if monsters[i].coord_x < robot.robot_x:
                monsters[i].coord_x += 1
            if monsters[i].coord_y > robot.robot_y:
                monsters[i].coord_y -= 1
            if monsters[i].coord_y < robot.robot_y:
                monsters[i].coord_y += 1

        #blit scoring coins
        for i in range(len(coins)):
            gameDisplay.blit(coins[i].gameobject_img, (coins[i].coord_x, coins[i].coord_y))
        
        
        #blit tailing monsters
        for j in range(len(monsters)):
            gameDisplay.blit(monster_img, (monsters[j].coord_x, monsters[j].coord_y))

        #randome damaging ROCKS
        # accelerating when coins gets collected

        for l in range(len(rocks)):
            rocks[l].move()
        for a in range(len(rocks)):
            gameDisplay.blit(rocks[a].rock_img, (rocks[a].pos_x, rocks[a].pos_y))

        gameDisplay.blit(door_img, (640-door_img.get_width(), 0))

        gameDisplay.blit(robot.robot_img, (robot.robot_x, robot.robot_y))

        gameDisplay.blit(font.render(text, True, (0, 0, 0)), (0, 0))

        #draw_health_bar()
        scorecounter(score, robot.healthy_bar)
        #handling all events below
        for i in range(len(coins)):
            #if robot.robot_y < rocks[i].coord_y + rocks[i].rock_hit_y and robot.robot_y > rocks[i].coord_y or robot.robot_y + robot.robot_hit_y > rocks[i].coord_y and robot.robot_y + robot.robot_hit_y < rocks[i].coord_y + rocks[i].rock_hit_y:
            if abs(robot.robot_x - coins[i].coord_x) < coin_robot_x/3 and abs(robot.robot_y - coins[i].coord_y) < coin_robot_y/3:
                #pygame.mixer.init()
                coin_collecting_sound.play()
                coins[i].coord_x = random.randrange(10, 620)
                coins[i].coord_y = random.randrange(50, 470)
                score += 1
                #robot.healthy_bar -= 1
                for j in range(len(rocks)):
                #if abs(robot.robot_x - rocks[j].pos_x) < rock_robot_x/5 and abs(robot.robot_y - rocks[j].pos_y) < rock_robot_y/5:
                    #robot.healthy_bar -= 0.5
                    rocks[j].velocity[0] *= 1.02
                    rocks[j].velocity[1] *= 1.02

        for j in range(len(rocks)):
            if abs(robot.robot_x - rocks[j].pos_x) < rock_robot_x/5 and abs(robot.robot_y - rocks[j].pos_y) < rock_robot_y/5:
                robot.healthy_bar -= 0.5
                rock_hit_sound.play()
                # rocks[j].velocity[0] += 1
                # rocks[j].velocity[1] += 1
        
        #monster causes demage
        for m in range(len(monsters)):
            if abs(robot.robot_x - monsters[m].coord_x) < monster_robot_x/3 and abs(robot.robot_y - monsters[m].coord_y) < monster_robot_y/3:
                robot.healthy_bar -= 1
                monster_hit_sound.play()

        #healthy_bar run out before times up
        if robot.healthy_bar == 0:
            result_display(score, counter_increase, robot.healthy_bar)
        #how to halt execution once condition is met?? this solution is not good
        if 640-door_img.get_width() < robot.robot_x < 640 and robot.robot_y < door_img.get_height():
            if pygame.mouse.get_pressed()[0] == False:
                pygame.time.wait(2000)
                continue
            screen_display('Take a break huh? Smart!')
            #return 

        pygame.display.update()
        
        clock.tick(60)

before_start()
game_loop()


    

    