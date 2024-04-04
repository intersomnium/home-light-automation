import pygame
import threading
pygame.init()

#  window display stuff
window_width = 800
window_height = 600
gameDisplay = pygame.display.set_mode((window_width, window_height))
background_image = pygame.image.load("StanResized.jpg").convert()

#  naslov na proektot
pygame.display.set_caption('Light Logic')

#  boi
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
dimmedYellow = (255, 255, 180)

#  pocetna pozicija i golemina na player
lead_x = int(window_width / 1.54807692308)
lead_y = int(window_height / 5)
block_size = 10

# some other stuff I need
clock = pygame.time.Clock()
FPS = 15
gameExit = False

#  promenlivi sho kje mi trebaat vo programata
collisionLevo = collisionDesno = collisionUp = collisionDown = 0

velocityL = velocityU = velocityR = velocityD = 1
positionL = positionR = positionU = positionD = 0

collisionVrata = 0

LightPretsobje = LightSopche = LightGolemoWC = LightMaloWC = LightHodnikWC = LightKujna1 = LightKujna2 = 0
LightHodnik = LightSpalna = LightSpalnaL1 = LightSpalnaL2 = LightSpalnaL3 = LightTrpezarija = LightTerasaDnevna = 0
LightDnevna = LightDnevnaL1 = LightDnevnaL2 = LightDnevnaL3 = LightDnevnaL4 = LightDnevnaL5 = LightDnevnaL6 = 0
LightDnevnaL7 = LightDnevnaL8 = LightDnevnaL9 = LightRabotna = LightRabotnaL1 = LightRabotnaL2 = LightRabotnaL3 = 0
LightRabotnaL4 = LightRabotnaL5 = LightRabotnaL6 = LightTerasaRabotna = 0

sensor0 = sensor1 = sensor2 = sensor3 = sensor4 = sensor5 = sensor6 = sensor7 = sensor8 = sensor9 = sensor10 = 0
sensor11 = sensor12 = sensor13 = sensor14 = sensor15 = sensor16 = sensor17 = sensor18 = sensor19 = sensor20 = 0
sensor21 = sensor22 = sensor23 = sensor24 = sensor25 = 0

DmLightSpalnaL1 = DmLightSpalnaL2 = 0
DmLightSpalnaL3 = DmLightDnevnaL1 = DmLightDnevnaL2 = DmLightDnevnaL3 = DmLightDnevnaL4 = DmLightDnevnaL5 = 0
DmLightDnevnaL6 = DmLightDnevnaL7 = DmLightDnevnaL8 = DmLightDnevnaL9 = DmLightRabotnaL1 = DmLightRabotnaL2 = 0
DmLightRabotnaL3 = DmLightRabotnaL4 = DmLightRabotnaL5 = DmLightRabotnaL6 = 0

global DmLightHodnik
DmLightHodnik = 0
def offHodnik():
    global DmLightHodnik
    DmLightHodnik = 0
    global timerNotActiveHodnik
    timerNotActiveHodnik = True
    return 0

global DmLightHodnikWC
DmLightHodnikWC = 0

def offHodnikWC():
    global DmLightHodnikWC
    DmLightHodnikWC = 0
    global timerNotActiveHodnikWC
    timerNotActiveHodnikWC = True
    return 0
#  timerHodnikWC = threading.Timer(5.0, offHodnikWC)

global DmLightKujna
DmLightKujna = 0

def offKujna():
    global DmLightKujna
    DmLightKujna = 0
    global timerNotActiveKujna
    timerNotActiveKujna = True
    return 0
# timerKujna = threading.Timer(5.0, offKujna)

def offSpalna():
    DmLightSpalnaL1 = DmLightSpalnaL2 = DmLightSpalnaL3 = 0
timerSpalna = threading.Timer(5.0, offSpalna)

global DmLightDnevna
DmLightDnevna = 0

def offDnevna():
    global DmLightDnevna
    DmLightDnevna = 0
    global timerNotActiveDnevna
    timerNotActiveDnevna = True
    return 0
# timerDnevna = threading.Timer(5.0, offDnevna)

def offRabotna():
    DmLightRabotnaL1 = DmLightRabotnaL2 = DmLightRabotnaL3 = 0
    DmLightRabotnaL4 = DmLightRabotnaL5 = DmLightRabotnaL6 = 0
timerRabotna = threading.Timer(5.0, offRabotna)


#  definiranje lista na vrati
doors = []
doors.append(pygame.Rect(335, 160, 30, 2))  # 0 horizontalen1 vece malo out 1
doors.append(pygame.Rect(335, 138, 30, 2))  # 1 horizontalen1 vece malo in 2
doors.append(pygame.Rect(180, 325, 30, 2))  # 2 horizontalen3 trpez - kujna 1
doors.append(pygame.Rect(180, 303, 30, 2))  # 3 horizontalen3 kujna - trpez 2
doors.append(pygame.Rect(385, 325, 40, 2))  # 4 horizontalen3 dnevna - hodnik 1
doors.append(pygame.Rect(385, 303, 40, 2))  # 5 horizontalen3 hodnik - dnevna 2
doors.append(pygame.Rect(530, 325, 30, 2))  # 6 horizontalen3 rab - hod 1
doors.append(pygame.Rect(530, 303, 30, 2))  # 7 horizontalen3 hod - rab 2
doors.append(pygame.Rect(570, 195, 100, 2))  # 8 horizontalen4 blue rabotna - terasa 1
doors.append(pygame.Rect(540, 495, 30, 2))  # 9 horizontalen4 blue terasa - rabotna 2
doors.append(pygame.Rect(410, 188, 40, 2))  # 10 horizontalen7 vlez2 out 1
doors.append(pygame.Rect(410, 210, 40, 2))  # 11 horizontalen7 vlez2 in 2
doors.append(pygame.Rect(90, 188, 30, 2))  # 12 horizontalen7 sopche out 1
doors.append(pygame.Rect(90, 210, 30, 2))  # 13 horizontalen7 sopche in 1
doors.append(pygame.Rect(340, 210, 30, 2))  # 14 horizontalen7 hodnik - hodnik vece 1
doors.append(pygame.Rect(340, 188, 30, 2))  # 15 horizontalen7 hodnik vece - hodnik 2
doors.append(pygame.Rect(530, 265, 30, 2))  # 16 horizontalen8 hod - spalna 1
doors.append(pygame.Rect(530, 243, 30, 2))  # 17 horizontalen8 spalna - hod 2
doors.append(pygame.Rect(510, 110, 2, 30))  # 18 vertikalen9  vlez out 1
doors.append(pygame.Rect(488, 110, 2, 30))  # 19 vertikalen9  vlez in 2
doors.append(pygame.Rect(290, 390, 2, 80))  # 20 vertikalen13  dnevna - trpezarija
doors.append(pygame.Rect(280, 390, 2, 80))  # 21 vertikalen13 trpezarija - dnevna
doors.append(pygame.Rect(310, 160, 2, 30))  # 22 vertikalen21 hodnik vece - golemo vece 1
doors.append(pygame.Rect(288, 160, 2, 30))  # 23 vertikalen21 golemo vece - hodnik vece 2
doors.append(pygame.Rect(340, 260, 2, 30))  # 24 vertikalen22 hodnik - kujna 1
doors.append(pygame.Rect(318, 260, 2, 30))  # 25 vertikalen22 kujna - hodnik 2

#  definiranje lista na zidovi
walls = []
walls.append(pygame.Rect(60, 90, 430, 20))  # horizontalen0
walls.append(pygame.Rect(290, 140, 80, 20))  # horizontalen1
walls.append(pygame.Rect(490, 140, 250, 20))  # horizontalen2
walls.append(pygame.Rect(60, 305, 680, 20))  # horizontalen3
walls.append(pygame.Rect(530, 475, 140, 20))  # horizontalen4
walls.append(pygame.Rect(280, 535, 230, 20))  # horizontalen5
walls.append(pygame.Rect(125, 475, 155, 20))  # horizontalen6
walls.append(pygame.Rect(80, 190, 425, 20))  # horizontalen7
walls.append(pygame.Rect(505, 245, 75, 20))  # horizontalen8
walls.append(pygame.Rect(490, 90, 20, 60))  # vertikalen9
walls.append(pygame.Rect(720, 160, 20, 165))  # vertikalen10
walls.append(pygame.Rect(670, 325, 20, 170))  # vertikalen11
walls.append(pygame.Rect(510, 325, 20, 230))  # vertikalen12
walls.append(pygame.Rect(280, 475, 20, 60))  # vertikalen13
walls.append(pygame.Rect(125, 305, 20, 190))  # vertikalen14
walls.append(pygame.Rect(60, 90, 20, 215))  # vertikalen15
walls.append(pygame.Rect(505, 160, 20, 85))  # vertikalen16
walls.append(pygame.Rect(560, 265, 20, 40))  # vertikalen17
walls.append(pygame.Rect(130, 110, 20, 80))  # vertikalen18
walls.append(pygame.Rect(270, 110, 20, 50))  # vertikalen19
walls.append(pygame.Rect(370, 110, 20, 80))  # vertikalen20
walls.append(pygame.Rect(290, 160, 20, 30))  # vertikalen21
walls.append(pygame.Rect(320, 210, 20, 95))  # vertikalen22
walls.append(pygame.Rect(282, 325, 8, 150))  # vertikalen23
# timerHodnik.start()
global timerNotActiveHodnik
timerNotActiveHodnik = True
global timerNotActiveHodnikWC
timerNotActiveHodnikWC = True
global timerNotActiveKujna
timerNotActiveKujna = True
global timerNotActiveDnevna
timerNotActiveDnevna = True

while not gameExit:
    pygame.time.delay(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.blit(background_image, [0, 0])
    keys = pygame.key.get_pressed()
    player = pygame.draw.rect(gameDisplay, white, (lead_x, lead_y, block_size, block_size))
    if player.collidelist(doors) != -1 and collisionVrata == 0:
        collisionVrata = 1
    if player.collidelist(doors) != -1 and collisionVrata == 1 and player.collidelist(walls) == -1:
        collisionVrata = 0
        sensor0 = sensor1 = sensor2 = sensor3 = sensor4 = sensor5 = sensor6 = sensor7 = sensor8 = sensor9 = sensor10 = 0
        sensor11 = sensor12 = sensor13 = sensor14 = sensor15 = sensor16 = sensor17 = sensor18 = sensor19 = sensor20 = 0
        sensor21 = sensor22 = sensor23 = sensor24 = sensor25 = 0

    if keys[pygame.K_LEFT] and lead_x > (0+block_size):
        if player.collidelist(walls) == -1 or collisionVrata == 1:
            lead_x -= velocityL
            positionL = lead_x
        if player.collidelist(walls) >= 9 and player.collidelist(walls) <= 23 and collisionDesno == 0:
            collisionLevo = 1
            lead_x = positionL
        if collisionDesno == 1 and player.collidelist(walls) >= 9 and player.collidelist(walls) <= 23:
            lead_x -= velocityL
            collisionDesno = 0

    if keys[pygame.K_RIGHT] and lead_x < window_width - (block_size + block_size/2):
        if player.collidelist(walls) == -1 or collisionVrata == 1:
            lead_x += velocityR
            positionR = lead_x
        if collisionLevo == 0 and player.collidelist(walls) >= 9 and player.collidelist(walls) <= 23:
            collisionDesno = 1
            lead_x = positionR
        if collisionLevo == 1 and player.collidelist(walls) >= 9 and player.collidelist(walls) <= 23:
            lead_x += velocityR
            collisionLevo = 0

    if keys[pygame.K_UP] and lead_y > (0+block_size):
        if player.collidelist(walls) == -1 or collisionVrata == 1:
            lead_y -= velocityU
            positionU = lead_y
        if collisionDown == 0 and player.collidelist(walls) >= 0 and player.collidelist(walls) <= 8:
            collisionUp = 1
            lead_y = positionU
        if collisionDown == 1 and player.collidelist(walls) >= 0 and player.collidelist(walls) <= 8:
            lead_y -= velocityU
            collisionDown = 0

    if keys[pygame.K_DOWN] and lead_y < window_height - (block_size + block_size/2):
        if player.collidelist(walls) == -1 or collisionVrata == 1:
            lead_y += velocityD
            positionD = lead_y
        if collisionUp == 0 and player.collidelist(walls) >= 0 and player.collidelist(walls) <= 8:
            collisionDown = 1
            lead_y = positionD
        if collisionUp == 1 and player.collidelist(walls) >= 0 and player.collidelist(walls) <= 8:
            lead_y += velocityD
            collisionUp = 0

    #  ON PRETSOBJE (od nadvor vleguvame vnatre)
    if player.collidelist(doors) == 18 and sensor19 == 0:
        sensor18 = 1
    if player.collidelist(doors) == 19 and sensor18 == 1:
        LightPretsobje = 1
    if LightPretsobje == 1:
        pygame.draw.circle(gameDisplay, yellow, (435, 145), 10)  # pretsobje
    #  OFF PRETSOBJE (od vnatre izleguvame nadvor)
    if player.collidelist(doors) == 19 and sensor18 == 0:
        sensor19 = 1
    if player.collidelist(doors) == 18 and sensor19 == 1:
        LightPretsobje = 0
    #  OFF PRETSOBJE ON HODNIK
    if player.collidelist(doors) == 10 and LightPretsobje == 1:
        sensor10 = 1
    if player.collidelist(doors) == 11 and sensor10 == 1:
        LightPretsobje = 0
        if timerNotActiveHodnik is False:
            timerHodnik.cancel()
            timerNotActiveHodnik = True
            DmLightHodnik = 0
        LightHodnik = 1
    if LightHodnik == 1:
        pygame.draw.circle(gameDisplay, yellow, (410, 260), 10)  # hodnik
    #  OFF HODNIK ON PRETSOBJE
    if player.collidelist(doors) == 11 and sensor10 == 0:
        sensor11 = 1
    if sensor11 == 1 and player.collidelist(doors) == 10:
        LightPretsobje = 1
        LightHodnik = 0
        DmLightHodnik = 1
    if DmLightHodnik == 1:
        pygame.draw.circle(gameDisplay, dimmedYellow, (410, 260), 10)  # dimmed hodnik
    # timerHodnik.cancel()
    # if timerHodnik.is_alive() is False and DmLightHodnik == 1:
    # print(DmLightHodnik)
    if DmLightHodnik == 1 and timerNotActiveHodnik:
        # print(DmLightHodnik)
        timerHodnik = threading.Timer(5.0, offHodnik)
        DmLightHodnik = timerHodnik.start()
        timerNotActiveHodnik = False
    #  OFF HODNIK ON HODNIKWC (14 i 15)
    if player.collidelist(doors) == 14 and LightHodnik == 1:
        sensor14 = 1
    if player.collidelist(doors) == 15 and sensor14 == 1:
        LightHodnik = 0
        LightHodnikWC = 1
        DmLightHodnik = 1
    if LightHodnikWC == 1:
        pygame.draw.circle(gameDisplay, yellow, (345, 175), 10)  # hodnik vecinja
        # timerHodnik.cancel()
        # if timerHodnik.is_alive() is False and DmLightHodnik == 1:
        # print(DmLightHodnik)
    #  OFF HODNIKWC ON HODNIK
    if LightHodnikWC == 1 and player.collidelist(doors) == 15:
        sensor15 = 1
    if sensor15 == 1 and player.collidelist(doors) == 14:
       LightHodnikWC = 0
       if timerNotActiveHodnik is False:
           timerHodnik.cancel()
           timerNotActiveHodnik = True
           DmLightHodnik = 0
       LightHodnik = 1
    #  OFF HODNIKWC ON GOLEMOWC 22 i 23
    if player.collidelist(doors) == 22 and LightHodnikWC == 1:
        sensor22 = 1
    if player.collidelist(doors) == 23 and sensor22 == 1:
        LightHodnikWC = 0
        LightGolemoWC = 1
        DmLightHodnikWC = 1
    if DmLightHodnikWC == 1:
        pygame.draw.circle(gameDisplay, dimmedYellow, (345, 175), 10)  # hodnik vecinja
    if DmLightHodnikWC == 1 and timerNotActiveHodnikWC:
        timerHodnikWC = threading.Timer(5.0, offHodnikWC)
        DmLightHodnikWC = timerHodnikWC.start()
        timerNotActiveHodnikWC = False
    if LightGolemoWC == 1:
        pygame.draw.circle(gameDisplay, yellow, (215, 150), 10)  # golemo vece
    #  ON HODNIKWC OFF GOLEMOWC 22 i 23
    if LightGolemoWC == 1 and player.collidelist(doors) == 23:
        sensor23 = 1
    if sensor23 == 1 and player.collidelist(doors) == 22:
       LightGolemoWC = 0
       if timerNotActiveHodnikWC is False:
           timerHodnikWC.cancel()
           timerNotActiveHodnikWC = True
           DmLightHodnikWC = 0
       LightHodnikWC = 1
    #  OFF HODNIKWC ON MALOWC 0 i 1
    if LightHodnikWC == 1 and player.collidelist(doors) == 0:
        sensor0 = 1
    if sensor0 == 1 and player.collidelist(doors) == 1:
       LightMaloWC = 1
       LightHodnikWC = 0
       DmLightHodnikWC = 1
    if LightMaloWC == 1:
       pygame.draw.circle(gameDisplay, yellow, (330, 120), 10)  # malo vece
    #  ON HODNIKWC OFF MALOWC 0 i 1
    if LightMaloWC == 1 and player.collidelist(doors) == 1:
        sensor1 = 1
    if sensor1 == 1 and player.collidelist(doors) == 0:
       LightMaloWC = 0
       if timerNotActiveHodnikWC is False:
           timerHodnikWC.cancel()
           timerNotActiveHodnikWC = True
           DmLightHodnikWC = 0
       LightHodnikWC = 1
    #  OFF HODNIK ON KUJNA 24 i 25
    if sensor25 == 0 and player.collidelist(doors) == 24:
        sensor24 = 1
    if sensor24 == 1 and player.collidelist(doors) == 25:
        LightHodnik = 0
        LightKujna1 = LightKujna2 = 1
        DmLightHodnik = 1
        if timerNotActiveKujna is False:
            timerKujna.cancel()
            timerNotActiveKujna = True
            DmLightKujna = 0
    if LightKujna1 and LightKujna2 == 1:
        pygame.draw.circle(gameDisplay, yellow, (185, 260), 10)  # kujna 1
        pygame.draw.circle(gameDisplay, yellow, (265, 260), 10)  # kujna 2

    #  OFF KUJNA ON HODNIK 24 i 25
    if sensor24 == 0 and player.collidelist(doors) == 25:
        sensor25 = 1
    if player.collidelist(doors) == 24 and sensor25 == 1:
        LightKujna2 = LightKujna1 = 0
        DmLightKujna = 1
        LightHodnik = 1
        if timerNotActiveHodnik is False:
            timerHodnik.cancel()
            timerNotActiveHodnik = True
            DmLightHodnik = 0
    if DmLightKujna == 1:
        pygame.draw.circle(gameDisplay, dimmedYellow, (185, 260), 10)  # kujna 1
        pygame.draw.circle(gameDisplay, dimmedYellow, (265, 260), 10)  # kujna 2
    if DmLightKujna == 1 and timerNotActiveKujna:
        timerKujna = threading.Timer(5.0, offKujna)
        DmLightKujna = timerKujna.start()
        timerNotActiveKujna = False
    # ON SOPCHE 13 i 12 (dodeka sum vo sopche ne sakam da se gasi vo kujna)
    if player.collidelist(doors) == 13 and sensor12 == 0:
        sensor13 = 1
    if player.collidelist(doors) == 12 and sensor13 == 1:
        LightSopche = 1
    if LightSopche == 1:
        pygame.draw.circle(gameDisplay, yellow, (105, 155), 10)  # sopche
    # OFF SOPCHE 13 i 12 (dodeka sum vo sopche ne sakam da se gasi vo kujna)
    if player.collidelist(doors) == 12 and sensor13 == 0:
        sensor12 = 1
    if sensor12 == 1 and player.collidelist(doors) == 13:
        LightSopche = 0
    # OFF HODNIK ON SPALNA 16 i 17
    if sensor17 == 0 and player.collidelist(doors) == 16:
        sensor16 = 1
    if sensor16 == 1 and player.collidelist(doors) == 17:
        LightSpalna = 1
        LightHodnik = 0
        DmLightHodnik = 1
    if LightSpalna == 1:
        pygame.draw.circle(gameDisplay, yellow, (650, 230), 10)  # spalna

    # ON HODNIK OFF SPALNA 16 i 17
    if sensor16 == 0 and player.collidelist(doors) == 17:
        sensor17 = 1
    if sensor17 == 1 and player.collidelist(doors) == 16:
        LightSpalna = 0
        LightSpalnaL1 = LightSpalnaL2 = LightSpalnaL3 = 0
        if timerNotActiveHodnik is False:
            timerHodnik.cancel()
            timerNotActiveHodnik = True
            DmLightHodnik = 0
        LightHodnik = 1

    # OFF HODNIK ON RABOTNA 7 i 6
    if sensor6 == 0 and player.collidelist(doors) == 7:
        sensor7 = 1
    if sensor7 == 1 and player.collidelist(doors) == 6:
        LightHodnik = 0
        LightRabotnaL1 = LightRabotnaL2 = LightRabotnaL3 = LightRabotnaL4 = LightRabotnaL5 = LightRabotnaL6 = 1
        DmLightHodnik = 1
    if LightRabotnaL1 == LightRabotnaL2 == LightRabotnaL3 == LightRabotnaL4 == LightRabotnaL5 == LightRabotnaL6 == 1:
        pygame.draw.circle(gameDisplay, yellow, (540, 335), 5)  # rabotna l1
        pygame.draw.circle(gameDisplay, yellow, (540, 360), 5)  # rabotna l2
        pygame.draw.circle(gameDisplay, yellow, (540, 385), 5)  # rabotna l3
        pygame.draw.circle(gameDisplay, yellow, (540, 410), 5)  # rabotna l4
        pygame.draw.circle(gameDisplay, yellow, (540, 436), 5)  # rabotna l5
        pygame.draw.circle(gameDisplay, yellow, (540, 462), 5)  # rabotna l6
    # ON HODNIK OFF RABOTNA 7 i 6
    if sensor7 == 0 and player.collidelist(doors) == 6:
        sensor6 = 1
    if sensor6 == 1 and player.collidelist(doors) == 7:
        LightHodnik = 1
        if timerNotActiveHodnik is False:
            timerHodnik.cancel()
            timerNotActiveHodnik = True
            DmLightHodnik = 0
        LightRabotnaL1 = LightRabotnaL2 = LightRabotnaL3 = LightRabotnaL4 = LightRabotnaL5 = LightRabotnaL6 = 0
    # ON DNEVNA OFF HODNIK (5 i 4)
    if sensor4 == 0 and player.collidelist(doors) == 5:
        sensor5 = 1
    if sensor5 == 1 and player.collidelist(doors) == 4:
        LightHodnik = 0
        LightDnevna = LightDnevnaL1 = LightDnevnaL2 = LightDnevnaL3 = LightDnevnaL4 = LightDnevnaL5 = LightDnevnaL6 = 1
        LightDnevnaL7 = LightDnevnaL8 = LightDnevnaL9 = 1
        DmLightHodnik = 1
    if LightDnevna == 1:
        pygame.draw.circle(gameDisplay, yellow, (380, 435), 10)  # dnevna
    if LightDnevnaL1 == 1:
        pygame.draw.circle(gameDisplay, yellow, (495, 415), 5)  # dnevna l1
        pygame.draw.circle(gameDisplay, yellow, (495, 437), 5)  # dnevna l2
        pygame.draw.circle(gameDisplay, yellow, (495, 459), 5)  # dnevna l3
        pygame.draw.circle(gameDisplay, yellow, (495, 481), 5)  # dnevna l4
        pygame.draw.circle(gameDisplay, yellow, (495, 503), 5)  # dnevna l5
        pygame.draw.circle(gameDisplay, yellow, (495, 525), 5)  # dnevna l6
        pygame.draw.circle(gameDisplay, yellow, (472, 525), 5)  # dnevna l7
        pygame.draw.circle(gameDisplay, yellow, (449, 525), 5)  # dnevna l8
        pygame.draw.circle(gameDisplay, yellow, (426, 525), 5)  # dnevna l9
    # DNEVNA OFF HODNIK ON 5 i 4
    if sensor5 == 0 and player.collidelist(doors) == 4:
        sensor4 = 1
    if sensor4 == 1 and player.collidelist(doors) == 5:
        LightDnevna = 0
        LightDnevnaL1 = LightDnevnaL2 = LightDnevnaL3 = LightDnevnaL4 = LightDnevnaL5 = LightDnevnaL6 = 0
        LightDnevnaL7 = LightDnevnaL8 = LightDnevnaL9 = 0
        LightHodnik = 1
        DmLightDnevna = 1
        if timerNotActiveHodnik is False:
            timerHodnik.cancel()
            timerNotActiveHodnik = True
            DmLightHodnik = 0
    if DmLightDnevna == 1:
        pygame.draw.circle(gameDisplay, dimmedYellow, (495, 415), 5)  # dnevna l1
        pygame.draw.circle(gameDisplay, dimmedYellow, (495, 437), 5)  # dnevna l2
        pygame.draw.circle(gameDisplay, dimmedYellow, (495, 459), 5)  # dnevna l3
        pygame.draw.circle(gameDisplay, dimmedYellow, (495, 481), 5)  # dnevna l4
        pygame.draw.circle(gameDisplay, dimmedYellow, (495, 503), 5)  # dnevna l5
        pygame.draw.circle(gameDisplay, dimmedYellow, (495, 525), 5)  # dnevna l6
        pygame.draw.circle(gameDisplay, dimmedYellow, (472, 525), 5)  # dnevna l7
        pygame.draw.circle(gameDisplay, dimmedYellow, (449, 525), 5)  # dnevna l8
        pygame.draw.circle(gameDisplay, dimmedYellow, (426, 525), 5)  # dnevna l9
    if DmLightDnevna == 1 and timerNotActiveDnevna:
        timerDnevna = threading.Timer(5.0, offDnevna)
        DmLightDnevna = timerDnevna.start()
        timerNotActiveDnevna = False

    # KUJNA OFF TRPEZARIJA ON 3 i 2
    if sensor2 == 0 and player.collidelist(doors) == 3:
        sensor3 = 1
    if sensor3 == 1 and player.collidelist(doors) == 2:
        LightTrpezarija = 1
        LightKujna2 = LightKujna1 = 0
        DmLightKujna = 1
        LightDnevnaL1 = LightDnevnaL2 = LightDnevnaL3 = LightDnevnaL4 = LightDnevnaL5 = LightDnevnaL6 = 1
        LightDnevnaL7 = LightDnevnaL8 = LightDnevnaL9 = 1
        if timerNotActiveDnevna is False:
            timerDnevna.cancel()
            timerNotActiveDnevna = True
            DmLightDnevna = 0
    if LightTrpezarija == 1:
        pygame.draw.circle(gameDisplay, yellow, (220, 410), 10)  # trpezarija
    # KUJNA ON TRPEZARIJA OFF 3 i 2
    if sensor3 == 0 and player.collidelist(doors) == 2:
        sensor2 = 1
    if sensor2 == 1 and player.collidelist(doors) == 3:
        LightTrpezarija = 0
        LightKujna2 = LightKujna1 = 1
        DmLightDnevna = 1
        if LightDnevna == 1 or LightDnevnaL1 == 1:
            LightDnevna = 0
            LightDnevnaL1 = LightDnevnaL2 = LightDnevnaL3 = LightDnevnaL4 = LightDnevnaL5 = LightDnevnaL6 = 0
            LightDnevnaL7 = LightDnevnaL8 = LightDnevnaL9 = 0
    # TRPEZARIJA ON (DNEVNA ostanuva ON) 20 i 21
    if sensor21 == 0 and player.collidelist(doors) == 20:
        sensor20 = 1
    if sensor20 == 1 and player.collidelist(doors) == 21:
        LightTrpezarija = 1
    # TRPEZARIJA OFF DNEVNA ON 20 i 21
    if sensor20 == 0 and player.collidelist(doors) == 21:
        sensor21 = 1
    if sensor21 == 1 and player.collidelist(doors) == 20:
        LightTrpezarija = 0
        LightDnevna = 1
        LightDnevnaL1 = LightDnevnaL2 = LightDnevnaL3 = LightDnevnaL4 = LightDnevnaL5 = LightDnevnaL6 = 1
        LightDnevnaL7 = LightDnevnaL8 = LightDnevnaL9 = 1
    # Easter Egg za toj shto actually kje go prochita kodov :) (spalna nad krevet)
    if player.collidelist(doors) == 8:
        LightSpalna = 0
        LightSpalnaL1 = LightDnevnaL2 = LightSpalnaL3 = 1
    if LightSpalnaL1 == 1: # manuelno se gasat ovie so minuvanje na raka pred mal senzor nad krevetot (ili so napustane na prostorijata)
        pygame.draw.circle(gameDisplay, yellow, (595, 305), 5)  # spalna l1
        pygame.draw.circle(gameDisplay, yellow, (630, 305), 5)  # spalna l2
        pygame.draw.circle(gameDisplay, yellow, (665, 305), 5)  # spalna l3

##### SIJALICI

    # pygame.draw.circle(gameDisplay, yellow, (105, 155), 10)  # sopche
    # pygame.draw.circle(gameDisplay, yellow, (215, 150), 10)  # golemo vece
    # pygame.draw.circle(gameDisplay, yellow, (330, 120), 10)  # malo vece
    # pygame.draw.circle(gameDisplay, yellow, (345, 175), 10)  # hodnik vecinja
    # pygame.draw.circle(gameDisplay, yellow, (435, 145), 10)  # LightPretsobje
    # pygame.draw.circle(gameDisplay, yellow, (185, 260), 10)  # kujna 1
    # pygame.draw.circle(gameDisplay, yellow, (265, 260), 10)  # kujna 2
    # pygame.draw.circle(gameDisplay, yellow, (410, 260), 10)  # hodnik
    # pygame.draw.circle(gameDisplay, yellow, (650, 230), 10)  # spalna
    # pygame.draw.circle(gameDisplay, yellow, (595, 305), 5)  # spalna l1
    # pygame.draw.circle(gameDisplay, yellow, (630, 305), 5)  # spalna l2
    # pygame.draw.circle(gameDisplay, yellow, (665, 305), 5)  # spalna l3
    # pygame.draw.circle(gameDisplay, yellow, (220, 410), 10)  # trpezarija
    # pygame.draw.circle(gameDisplay, yellow, (205, 530), 10)  # terasa dnevna
    # pygame.draw.circle(gameDisplay, yellow, (380, 435), 10)  # dnevna
    # pygame.draw.circle(gameDisplay, yellow, (495, 415), 5)  # dnevna l1
    # pygame.draw.circle(gameDisplay, yellow, (495, 437), 5)  # dnevna l2
    # pygame.draw.circle(gameDisplay, yellow, (495, 459), 5)  # dnevna l3
    # pygame.draw.circle(gameDisplay, yellow, (495, 481), 5)  # dnevna l4
    # pygame.draw.circle(gameDisplay, yellow, (495, 503), 5)  # dnevna l5
    # pygame.draw.circle(gameDisplay, yellow, (495, 525), 5)  # dnevna l6
    # pygame.draw.circle(gameDisplay, yellow, (472, 525), 5)  # dnevna l7
    # pygame.draw.circle(gameDisplay, yellow, (449, 525), 5)  # dnevna l8
    # pygame.draw.circle(gameDisplay, yellow, (426, 525), 5)  # dnevna l9
    # pygame.draw.circle(gameDisplay, yellow, (600, 400), 10)  # rabotna
    # pygame.draw.circle(gameDisplay, yellow, (540, 335), 5)  # rabotna l1
    # pygame.draw.circle(gameDisplay, yellow, (540, 360), 5)  # rabotna l2
    # pygame.draw.circle(gameDisplay, yellow, (540, 385), 5)  # rabotna l3
    # pygame.draw.circle(gameDisplay, yellow, (540, 410), 5)  # rabotna l4
    # pygame.draw.circle(gameDisplay, yellow, (540, 436), 5)  # rabotna l5
    # pygame.draw.circle(gameDisplay, yellow, (540, 462), 5)  # rabotna l6
    # pygame.draw.circle(gameDisplay, yellow, (605, 520), 10)  # terasa rabotna

##### DIMMED SIJALICI

    # pygame.draw.circle(gameDisplay, dimmedYellow, (345, 175), 10)  # hodnik vecinja
    # pygame.draw.circle(gameDisplay, dimmedYellow, (185, 260), 10)  # kujna 1
    # pygame.draw.circle(gameDisplay, dimmedYellow, (265, 260), 10)  # kujna 2
    # pygame.draw.circle(gameDisplay, dimmedYellow, (410, 260), 10)  # hodnik
    # pygame.draw.circle(gameDisplay, dimmedYellow, (595, 305), 5)  # spalna l1
    # pygame.draw.circle(gameDisplay, dimmedYellow, (630, 305), 5)  # spalna l2
    # pygame.draw.circle(gameDisplay, dimmedYellow, (665, 305), 5)  # spalna l3
    # pygame.draw.circle(gameDisplay, dimmedYellow, (495, 415), 5)  # dnevna l1
    # pygame.draw.circle(gameDisplay, dimmedYellow, (495, 437), 5)  # dnevna l2
    # pygame.draw.circle(gameDisplay, dimmedYellow, (495, 459), 5)  # dnevna l3
    # pygame.draw.circle(gameDisplay, dimmedYellow, (495, 481), 5)  # dnevna l4
    # pygame.draw.circle(gameDisplay, dimmedYellow, (495, 503), 5)  # dnevna l5
    # pygame.draw.circle(gameDisplay, dimmedYellow, (495, 525), 5)  # dnevna l6
    # pygame.draw.circle(gameDisplay, dimmedYellow, (472, 525), 5)  # dnevna l7
    # pygame.draw.circle(gameDisplay, dimmedYellow, (449, 525), 5)  # dnevna l8
    # pygame.draw.circle(gameDisplay, dimmedYellow, (426, 525), 5)  # dnevna l9
    # pygame.draw.circle(gameDisplay, dimmedYellow, (540, 335), 5)  # rabotna l1
    # pygame.draw.circle(gameDisplay, dimmedYellow, (540, 360), 5)  # rabotna l2
    # pygame.draw.circle(gameDisplay, dimmedYellow, (540, 385), 5)  # rabotna l3
    # pygame.draw.circle(gameDisplay, dimmedYellow, (540, 410), 5)  # rabotna l4
    # pygame.draw.circle(gameDisplay, dimmedYellow, (540, 436), 5)  # rabotna l5
    # pygame.draw.circle(gameDisplay, dimmedYellow, (540, 462), 5)  # rabotna l6

    ########  VRATI

    # pygame.draw.rect(gameDisplay, white, [335, 160, 30, 2])  # 0 horizontalen1 vece malo out 1
    # pygame.draw.rect(gameDisplay, white, [335, 138, 30, 2])  # 1 horizontalen1 vece malo in 2
    # pygame.draw.rect(gameDisplay, white, [180, 325, 30, 2])  # 2 horizontalen3 trpez - kujna 1
    # pygame.draw.rect(gameDisplay, white, [180, 303, 30, 2])  # 3 horizontalen3 kujna - trpez 2
    # pygame.draw.rect(gameDisplay, white, [385, 325, 40, 2])  # 4horizontalen3 dnevna - hodnik 1
    # pygame.draw.rect(gameDisplay, white, [385, 303, 40, 2])  # 5horizontalen3 hodnik - dnevna 2
    # pygame.draw.rect(gameDisplay, white, [530, 325, 30, 2])  # 6horizontalen3 rab - hod 1
    # pygame.draw.rect(gameDisplay, white, [530, 303, 30, 2])  # 7horizontalen3 hod - rab 2
    # pygame.draw.rect(gameDisplay, white, [570, 195, 100, 2])  # 8horizontalen4 spalna nad krevet
    # # VISHAK E OVA pygame.draw.rect(gameDisplay, white, [540, 495, 30, 2])  # 9horizontalen4 blue terasa - rabotna 2
    # pygame.draw.rect(gameDisplay, white, [410, 188, 40, 2])  # 10horizontalen7 pretsobje - hodnik out 1
    # pygame.draw.rect(gameDisplay, white, [410, 210, 40, 2])  # 11horizontalen7 hodnik - pretsobje in 2
    # pygame.draw.rect(gameDisplay, white, [90, 188, 30, 2])  # 12horizontalen7 sopche out 1
    # pygame.draw.rect(gameDisplay, white, [90, 210, 30, 2])  # 13horizontalen7 sopche in 1
    # pygame.draw.rect(gameDisplay, white, [340, 210, 30, 2])  # 14horizontalen7 hodnik - hodnik vece 1
    # pygame.draw.rect(gameDisplay, white, [340, 188, 30, 2])  # 15horizontalen7 hodnik vece - hodnik 2
    # pygame.draw.rect(gameDisplay, white, [530, 265, 30, 2])  # 16horizontalen8 hod - spalna 1
    # pygame.draw.rect(gameDisplay, white, [530, 243, 30, 2])  # 17horizontalen8 spalna - hod 2
    # pygame.draw.rect(gameDisplay, white, [510, 110, 2, 30])  # 18vertikalen9  vlez out 1
    # pygame.draw.rect(gameDisplay, white, [488, 110, 2, 30])  # 19vertikalen9  vlez in 2
    # pygame.draw.rect(gameDisplay, white, [290, 390, 2, 80])  # 20vertikalen13 dnevna - trpezarija
    # pygame.draw.rect(gameDisplay, white, [280, 390, 2, 80])  # 21vertikalen13 trpezarija - dnevna
    # pygame.draw.rect(gameDisplay, white, [310, 160, 2, 30])  # 22vertikalen21 hodnik vece - golemo vece 1
    # pygame.draw.rect(gameDisplay, white, [288, 160, 2, 30])  # 23vertikalen21 golemo vece - hodnik vece 2
    # pygame.draw.rect(gameDisplay, white, [340, 260, 2, 30])  # 24vertikalen22 hodnik - kujna 1
    # pygame.draw.rect(gameDisplay, white, [318, 260, 2, 30])  # 25vertikalen22 kujna - hodnik 2

    ########  ZIDOVI

    # pygame.draw.rect(gameDisplay, black, [80, 90, 410, 20]) # horizontalen0
    # pygame.draw.rect(gameDisplay, black, [290, 140, 80, 20]) # horizontalen1
    # pygame.draw.rect(gameDisplay, (255, 0, 0), [490, 140, 250, 20]) # horizontalen2 red
    # pygame.draw.rect(gameDisplay, (0, 255, 0), [60, 305, 680, 20]) # horizontalen3 green
    # pygame.draw.rect(gameDisplay, (0, 0, 255), [530, 475, 140, 20]) # horizontalen4 blue rabotna prema terasa
    # pygame.draw.rect(gameDisplay, (0, 255, 255), [280, 535, 230, 20]) # horizontalen5 blue
    # pygame.draw.rect(gameDisplay, (255, 0, 255), [125, 475, 155, 20]) # horizontalen6 magenta
    # pygame.draw.rect(gameDisplay, (255, 255, 0), [80, 190, 425, 20]) # horizontalen7 yellow
    # pygame.draw.rect(gameDisplay, (100, 100, 255), [505, 245, 75, 20]) # horizontalen8 blue spalna levo
    # pygame.draw.rect(gameDisplay, (255, 100, 255), [490, 90, 20, 50]) # vertikalen9 magenta vlez
    # pygame.draw.rect(gameDisplay, (100, 255, 255), [720, 160, 20, 165]) # vertikalen10 blue spalna
    # pygame.draw.rect(gameDisplay, (100, 255, 255), [670, 325, 20, 170])  # vertikalen11 blue rabotna
    # pygame.draw.rect(gameDisplay, (255, 255, 100), [510, 325, 20, 230]) # vertikalen12 zolta dnevna desno
    # pygame.draw.rect(gameDisplay, (255, 255, 100), [280, 475, 20, 60])  # vertikalen13 zolta dnevna levo
    # pygame.draw.rect(gameDisplay, (100, 255, 100), [125, 325, 20, 170]) # vertikalen14 zelena trpezarija
    # pygame.draw.rect(gameDisplay, (100, 255, 255), [60, 90, 20, 215]) # vertikalen15 blue levo
    # pygame.draw.rect(gameDisplay, (255, 255, 100), [505, 160, 20, 85]) # vertikalen16 yellow spalna
    # pygame.draw.rect(gameDisplay, (100, 100, 100), [560, 265, 20, 40]) # vertikalen17 siv spalna
    # pygame.draw.rect(gameDisplay, (200, 100, 100), [130, 110, 20, 80]) # vertikalen18 praska sopche
    # pygame.draw.rect(gameDisplay, (200, 200, 100), [270, 110, 20, 50]) # vertikalen19 zolt vece
    # pygame.draw.rect(gameDisplay, (200, 200, 200), [370, 110, 20, 80]) # vertikalen20 sivo bel vece
    # pygame.draw.rect(gameDisplay, (100, 100, 200), [290, 160, 20, 30]) # vertikalen21 blue vece
    # pygame.draw.rect(gameDisplay, (100, 200, 100), [320, 210, 20, 95]) # vertikalen22 green kujna
    # pygame.draw.rect(gameDisplay, (50, 100, 200), [282, 325, 8, 150]) # vertikalen23 blue dnev - trpez toj sho shtrchi
    pygame.display.update()

pygame.quit()
quit()