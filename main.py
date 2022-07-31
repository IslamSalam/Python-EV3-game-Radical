#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
import urandom
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

while True:
    ev3 = EV3Brick() #  ev3.speaker.beep()

    x1 = []  # создание списка для хранения координат
    x2 = []
    y1 = [] 
    y2 = []
    width = 5 # ширина линий

    x_igrok = 80  # координаты игрока, скорость игрока, скорость линий
    y_igrok = 90
    speed_igrok = 8
    speed_line = width


    y = -65  # расстояние между линиями
    j = 1
    g = 0
    k = 0
    total = 0  # счет
    game_over = False

    # создать список координат
    for i in range(100):
        for i in range(urandom.randint(1, 2)):
                
            x1.append(1)
            x2.append(urandom.randint(70, 110))
            xx2 = x2[k]
            k += 2
                    
            x1.append(xx2+30)
            x2.append(175)
        for i in range(urandom.randint(1, 2)):
                
            x1.append(1)
            x2.append(urandom.randint(1, 30))
            xx2 = x2[k]
            k += 2
                    
            x1.append(xx2+30)
            x2.append(175)

    for i in range(100):
        y1.append(y*i)
        y2.append(y*i)
        


    while game_over == False:
        
        # вывести на экран линии
        ev3.screen.draw_line(175, 1,  175, 125, width)
        ev3.screen.draw_line(1, 1,  1, 125, width)
        
        ev3.screen.draw_line(x1[0], y1[0],  x2[0], y2[0], width)  
        ev3.screen.draw_line(x1[1], y1[0],  x2[1], y2[0], width)
        
        ev3.screen.draw_line(x1[2], y1[1],  x2[2], y2[1], width)
        ev3.screen.draw_line(x1[3], y1[1],  x2[3], y2[1], width)
        
        ev3.screen.draw_line(x1[4], y1[2],  x2[4], y2[2], width)
        ev3.screen.draw_line(x1[5], y1[2],  x2[5], y2[2], width)
        
        ev3.screen.draw_line(x1[6], y1[3],  x2[6], y2[3], width)
        ev3.screen.draw_line(x1[7], y1[3],  x2[7], y2[3], width)
    
        ev3.screen.draw_line(x1[8], y1[4],  x2[8], y2[4], width)
        ev3.screen.draw_line(x1[9], y1[4],  x2[9], y2[4], width)

        ev3.screen.draw_line(x1[10], y1[5],  x2[10], y2[5], width)
        ev3.screen.draw_line(x1[11], y1[5],  x2[11], y2[5], width)
        
        ev3.screen.draw_line(x1[12], y1[6],  x2[12], y2[6], width)
        ev3.screen.draw_line(x1[13], y1[6],  x2[13], y2[6], width)
        
        ev3.screen.draw_line(x1[14], y1[7],  x2[14], y2[7], width)
        ev3.screen.draw_line(x1[15], y1[7],  x2[15], y2[7], width)
        
        ev3.screen.draw_line(x1[16], y1[8],  x2[16], y2[8], width)
        ev3.screen.draw_line(x1[17], y1[8],  x2[17], y2[8], width)
    
        ev3.screen.draw_line(x1[18], y1[9],  x2[18], y2[9], width)
        ev3.screen.draw_line(x1[19], y1[9],  x2[19], y2[9], width)

        ev3.screen.draw_line(x1[20], y1[10],  x2[20], y2[10], width)
        ev3.screen.draw_line(x1[21], y1[10],  x2[21], y2[10], width)
        
        ev3.screen.draw_line(x1[22], y1[11],  x2[22], y2[11], width)
        ev3.screen.draw_line(x1[23], y1[11],  x2[23], y2[11], width)
        
        ev3.screen.draw_line(x1[24], y1[12],  x2[24], y2[12], width)
        ev3.screen.draw_line(x1[25], y1[12],  x2[25], y2[12], width)
        
        ev3.screen.draw_line(x1[26], y1[13],  x2[26], y2[13], width)
        ev3.screen.draw_line(x1[27], y1[13],  x2[27], y2[13], width)
    
        ev3.screen.draw_line(x1[28], y1[14],  x2[28], y2[14], width)
        ev3.screen.draw_line(x1[29], y1[14],  x2[29], y2[14], width)

        ev3.screen.draw_line(x1[30], y1[15],  x2[30], y2[15], width)
        ev3.screen.draw_line(x1[31], y1[15],  x2[31], y2[15], width)
        
        ev3.screen.draw_line(x1[32], y1[16],  x2[32], y2[16], width)
        ev3.screen.draw_line(x1[33], y1[16],  x2[33], y2[16], width)
        
        ev3.screen.draw_line(x1[34], y1[17],  x2[34], y2[17], width)
        ev3.screen.draw_line(x1[35], y1[17],  x2[35], y2[17], width)
        
        ev3.screen.draw_line(x1[36], y1[18],  x2[36], y2[18], width)
        ev3.screen.draw_line(x1[37], y1[18],  x2[37], y2[18], width)
    
        ev3.screen.draw_line(x1[38], y1[19],  x2[38], y2[19], width)
        ev3.screen.draw_line(x1[39], y1[19],  x2[39], y2[19], width)

        ev3.screen.draw_line(x1[40], y1[20],  x2[40], y2[20], width)
        ev3.screen.draw_line(x1[41], y1[20],  x2[41], y2[20], width)
        
        ev3.screen.draw_line(x1[42], y1[21],  x2[42], y2[21], width)
        ev3.screen.draw_line(x1[43], y1[21],  x2[43], y2[21], width)
        
        ev3.screen.draw_line(x1[44], y1[22],  x2[44], y2[22], width)
        ev3.screen.draw_line(x1[45], y1[22],  x2[45], y2[22], width)
        
        ev3.screen.draw_line(x1[46], y1[23],  x2[46], y2[23], width)
        ev3.screen.draw_line(x1[47], y1[23],  x2[47], y2[23], width)
    
        ev3.screen.draw_line(x1[48], y1[24],  x2[48], y2[24], width)
        ev3.screen.draw_line(x1[49], y1[24],  x2[49], y2[24], width)

        ev3.screen.draw_line(x1[50], y1[25],  x2[50], y2[25], width)
        ev3.screen.draw_line(x1[51], y1[25],  x2[51], y2[25], width)
        
        ev3.screen.draw_line(x1[52], y1[26],  x2[52], y2[26], width)
        ev3.screen.draw_line(x1[53], y1[26],  x2[53], y2[26], width)
        
        ev3.screen.draw_line(x1[54], y1[27],  x2[54], y2[27], width)
        ev3.screen.draw_line(x1[55], y1[27],  x2[55], y2[27], width)
        
        ev3.screen.draw_line(x1[56], y1[28],  x2[56], y2[28], width)
        ev3.screen.draw_line(x1[57], y1[28],  x2[57], y2[28], width)
    
        ev3.screen.draw_line(x1[58], y1[29],  x2[58], y2[29], width)
        ev3.screen.draw_line(x1[59], y1[29],  x2[59], y2[29], width)


        ev3.screen.draw_circle(x_igrok, y_igrok, 5, fill=True)

        ev3.screen.draw_text(84, 1, total)

        # чтобы линии двигались вниз
        y1[0] += speed_line
        y2[0] += speed_line
        y1[1] += speed_line
        y2[1] += speed_line
        y1[2] += speed_line
        y2[2] += speed_line
        y1[3] += speed_line
        y2[3] += speed_line
        y1[4] += speed_line
        y2[4] += speed_line
        y1[5] += speed_line
        y2[5] += speed_line
        y1[6] += speed_line
        y2[6] += speed_line
        y1[7] += speed_line
        y2[7] += speed_line
        y1[8] += speed_line
        y2[8] += speed_line
        y1[9] += speed_line
        y2[9] += speed_line
        y1[10] += speed_line
        y2[10] += speed_line
        y1[11] += speed_line
        y2[11] += speed_line
        y1[12] += speed_line
        y2[12] += speed_line
        y1[13] += speed_line
        y2[13] += speed_line
        y1[14] += speed_line
        y2[14] += speed_line
        y1[15] += speed_line
        y2[15] += speed_line
        y1[16] += speed_line
        y2[16] += speed_line
        y1[17] += speed_line
        y2[17] += speed_line
        y1[18] += speed_line
        y2[18] += speed_line
        y1[19] += speed_line
        y2[19] += speed_line    
        y1[20] += speed_line
        y2[20] += speed_line
        y1[21] += speed_line
        y2[21] += speed_line
        y1[22] += speed_line
        y2[22] += speed_line
        y1[23] += speed_line
        y2[23] += speed_line
        y1[24] += speed_line
        y2[24] += speed_line
        y1[25] += speed_line
        y2[25] += speed_line
        y1[26] += speed_line
        y2[26] += speed_line
        y1[27] += speed_line
        y2[27] += speed_line
        y1[28] += speed_line
        y2[28] += speed_line
        y1[29] += speed_line
        y2[29] += speed_line
        y1[30] += speed_line
        y2[30] += speed_line
        y1[31] += speed_line
        y2[31] += speed_line
        y1[32] += speed_line
        y2[32] += speed_line
        y1[33] += speed_line
        y2[33] += speed_line
        y1[34] += speed_line
        y2[34] += speed_line
        y1[35] += speed_line
        y2[35] += speed_line
        y1[36] += speed_line
        y2[36] += speed_line
        y1[37] += speed_line
        y2[37] += speed_line
        y1[38] += speed_line
        y2[38] += speed_line
        y1[39] += speed_line
        y2[39] += speed_line
        y1[40] += speed_line
        y2[40] += speed_line
        y1[41] += speed_line
        y2[41] += speed_line
        y1[42] += speed_line
        y2[42] += speed_line
        y1[43] += speed_line
        y2[43] += speed_line
        y1[44] += speed_line
        y2[44] += speed_line
        y1[45] += speed_line
        y2[45] += speed_line
        y1[46] += speed_line
        y2[46] += speed_line
        y1[47] += speed_line
        y2[47] += speed_line
        y1[48] += speed_line
        y2[48] += speed_line
        y1[49] += speed_line
        y2[49] += speed_line
        
        
        # проверка проигрыша
        if  (y_igrok in y1) and ((x_igrok-4 in range(x1[g], x2[g])) or (x_igrok+4 in range(x1[j], x2[j]))) or ((x_igrok in range(1, 9) or (x_igrok in range(168, 175))) and (y_igrok in range(1, 125))):  
            ev3.speaker.beep(300,300)
            game_over = True
        
            
        if 105 in y1 and game_over == False: # если прошел одну линию увеличиваем счет, и если это не проигрыш
                    
            total +=1
            g += 2
            j += 2
           
        


        if Button.RIGHT in (ev3.buttons.pressed()):  # управление игроком
            x_igrok += speed_igrok
        
        if Button.LEFT in (ev3.buttons.pressed()):
            x_igrok -= speed_igrok
        
        
        
        
        
        if total == 30 or game_over == True:  # если выиграл или проиграл
            if total == 30:
                ev3.screen.draw_text(40,50, "Bravooo!!!")
                ev3.speaker.beep(700,300)
                ev3.speaker.play_file(SoundFile.CHEERING)
                game_over = True
                  
            else:
                ev3.screen.draw_text(40,50, "Game Over")
                ev3.speaker.play_file(SoundFile.CRYING)  
            
            while not Button.CENTER in (ev3.buttons.pressed()):
                if Button.LEFT in(ev3.buttons.pressed()):
                    sys.exit() #вырубить всю программу
        
        wait(100)
        ev3.screen.clear()    
        
    ev3.screen.clear()
    ev3.speaker.play_file(SoundFile.CONFIRM)