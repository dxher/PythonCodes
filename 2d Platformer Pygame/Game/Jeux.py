
"""

Jeux Sommative
Auteur: Anthony, dahant17@ecolecatholique.ca
Date: 11 juin, 2020

"""

import pygame
import pgzrun
import random


#Demension de l'ecran
WIDTH = 1000
HEIGHT = 600


#couleur
blue = 0
blueforward = True
groundcolour = 0, 0, 255


#Sprite - mc
mush = Actor('mush1', (500,250))
mush_x_velocity = 0
mush_y_velocity = 0


#graviter
gravity = 1
jumping = False
jumped = False
allowx = True
timer = [] #list


#temps
elapsed_time = 0


#Plancher 
floor = Rect ((0,580), (1000,20)) #placher
platform1 = Rect((450,500),(100,10)) #milieu
platform2 = Rect((300,400),(100,10)) #gauche
platform3 = Rect((600,400),(100,10)) #droite
platform4 = Rect((0,350),(100,10)) #gauche haut
platform5 = Rect((900,350),(100,10)) #droite haut
plat61_x = 200 #Location 'x' du platform gauche qui bouge
plat62_x = 700 #Location 'x' du platform droite qui bouge
platform61 = Rect((plat61_x, 200),(100,10)) #Platform milieu gauche qui bouge
platform62 = Rect((plat62_x,200),(100,10)) #Platform milieu droite qui bouge
platform6 = Rect((0,100),(100,10)) #haut gauche
platform7 = Rect((900,100),(100,10)) #haut droite
platforms = [floor, platform1, platform2, platform3, platform4, platform5, platform6, platform7, platform61, platform61] #list of platforms
plat61left = True
plat62left = False


#Argent
cash_x = [950,50,650,350,500,50,950]
cash_y = [320,320,370,370,470,70,70]
c_xy = random.randint(0,6)
cash = Actor('cash', (cash_x[c_xy], cash_y[c_xy]))
points = 0


#Music
pygame.mixer.pre_init(22050, -16, 2, 1024) #lower buffer size
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
sounds.theme.play(-1)

             
def draw():
    global platform61, platform62
    screen.fill((173,216,blue))#Couleur du derriere plan
    screen.blit('henesysgrass', (0,0))#scene
    platform61 = Rect((plat61_x, 200),(100,10))#platform qui bouge gauche
    platform62 = Rect((plat62_x,200),(100,10))#platform qui bouge droit
    platforms[8] = platform61
    platforms[9] = platform62
    for i in platforms:
        screen.draw.filled_rect(i, groundcolour)#Dessine tous les platforms
    mush.draw()#Caractere
    cash.draw()#Argent
    screen.draw.text("Loot:", center = (50, 540), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")#Score
    screen.draw.text(str(points), center = (100, 540), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")#Pointage
    screen.draw.text(str(elapsed_time) + " seconds", midtop = (84,552), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")#temps

    
def update(dt): #Applique tous les definitions dessous
    backgroundcolourfade()
    platform_mover()
    mush_move(dt)
    

def mush_move(ticks):
    global mush_x_velocity, mush_y_velocity, jumping, gravity, jumped, allowx, timer, points, c_xy

    #front facing caracter model
    if mush_x_velocity == 0 and not jumped:
        mush.image = 'mush1'


    #graviter
    if collidecheck(): # si on touche le plancher, graviter = normale
        gravity = 1
        mush.y -= 1
        allowx = True
        timer = []
    if not collidecheck(): # si nous somme dans l'air, gagne la vitesse vers le plancher
        mush.y += gravity
        if gravity <= 20:
            gravity += 0.5
        timer.append(ticks)#temps duree dans l'air
        if len(timer) > 5 and not jumped:
            allowx = False
            mush.image = 'mush4'
            if len(timer) > 20:
                mush.image = 'mush5'
                if len(timer) > 30:
                    mush.image = 'mush2' #animation tomber


    #movement gauche et droit
    if (keyboard.left) and allowx:
        if (mush.x > 40) and (mush_x_velocity > -8):#condition pour controller la vitesse et ne pas sortir des bordures - gauche
            mush_x_velocity -= 2 #vitesse
            mush.image = 'mush3' #sprite
            if (keyboard.left) and jumped: #sprite lorsqu'on saute
                mush.image = 'mush4'

    if (keyboard.right) and allowx : #condition pour controller la vitesse et ne pas sortir des bordures - droite
        if (mush.x < 960) and (mush_x_velocity < 8):
            mush_x_velocity += 2 #vitesse
            mush.image = 'mush6'#sprite
            if (keyboard.right) and jumped:#sprite lorsqu'on saute
                mush.image = 'mush7'
            
    mush.x += mush_x_velocity #bouger

    
    #velocity
    if mush_x_velocity > 0:
        mush_x_velocity -= 1 #baisser la vitesse
    if mush_x_velocity < 0:
        mush_x_velocity += 1 #augmenter la vitesse

    if mush.x < 50 or mush.x > 950: #Limite de l'ecran
        mush_x_velocity = 0


    #jumping
    if (keyboard.space or keyboard.up) and collidecheck() and not jumped: #click espace ou haut pour sauter
        sounds.jump.play() #sound
        jumping = True 
        jumped = True
        clock.schedule_unique(jumpedrecently, 0.5) #jump breaktime
        mush.image = "mush4" #changer sprite
        mush_y_velocity = 95 #vitesse
    if jumping and mush_y_velocity > 25:
        mush_y_velocity = mush_y_velocity - ((100 - mush_y_velocity)/2)#limite du saut
        mush.y -= mush_y_velocity / 3.2 #jump height
    else:#pas sauter constanement
        mush_y_velocity = 0
        jumping = False


    #coin collision - system de pointage
    if mush.colliderect(cash):
        points += 1 #augmente point
        sounds.coin.play() #sound
        old_c_xy = c_xy
        c_xy = random.randint(0,6)
        while old_c_xy == c_xy: #Eviter que sa spawn dans le meme location
            c_xy = random.randint(0,6)
        cash.x = cash_x[c_xy]
        cash.y = cash_y[c_xy]


def platform_mover():
    global plat61_x, plat62_x, plat61left, plat62left

    #platform gauche - bouger droite et gauche
    if plat61left:
        plat61_x += 2
        if plat61_x == 400:
            plat61left = False
        if mush.colliderect(platform61):
            mush.x += 2
    else:
        plat61_x -= 2
        if plat61_x == 200:
            plat61left = True
        if mush.colliderect(platform61):
            mush.x -= 2

            
    #platform droite - bouger droite et gauche
    if plat62left:
        plat62_x += 2
        if plat62_x == 700:
            plat62left = False
        if mush.colliderect(platform62):
            mush.x += 2
    else:
        plat62_x -= 2
        if plat62_x == 500:
            plat62left = True
        if mush.colliderect(platform62):
            mush.x -= 2

    
def collidecheck(): # code pour collision avec les planchers
    collide = False
    for i in platforms:
        if mush.colliderect(i):
            collide = True
    return collide


def jumpedrecently():#Eviter un 'spam' de saut
    global jumped
    jumped = False


def backgroundcolourfade(): #Lentement changer le couleur du derriere plan
    global blue, blueforward
    if blue < 255 and blueforward:
        blue += 1
    else:
        blueforward = False
    if blue > 130 and not blueforward:
        blue -= 1
    else:
        blueforward = True


def update_timer(): #temps
    global elapsed_time
    elapsed_time +=1
    

clock.schedule_interval(update_timer, 1.0)   


pgzrun.go()
