from machine import Pin, I2C, PWM
import sh1106
import time
import random
import framebuf


i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # zkusíme pomaleji
time.sleep_ms(200)
oled = sh1106.SH1106_I2C(128, 64, i2c, addr=0x3C)
oled.flip(True)

hra = 0



oled.fill(0)  
#oled.text("PicoBox v1.0", 5, 6)
oled.text("### # # #  # # #", 0, 5)
oled.text("# # # # ## # ##", 0, 12)
oled.text("### # # # ## ##", 0, 19)
oled.text("#   ### #  # # #"  , 0, 26)
oled.text("    STATION"  , 0, 38)

#oled.rect(0, 0, 128, 20 , 1)



oled.show()
time.sleep(3)



def SnackRider():
    
    
    monster1 = bytearray([
        0b00111001,  
        0b00111001, 
        0b11111111, 
        0b00010001, 
        0b01111101, 
        0b01000110, 
        0b11000000   
    ])
        
    monster1_mov = bytearray([
        0b00111000,  
        0b10111001, 
        0b01111101,  
        0b00010001,  
        0b01111101, 
        0b11000101,  
        0b00000110  
    ])

    
    monster2 = bytearray([
        0b00000000,  
        0b00000000, 
        0b00000000, 
        0b00111000, 
        0b01010100, 
        0b10000010, 
        0b00000000   
    ])
        
    monster2_mov = bytearray([
        0b00000000,  
        0b10000010, 
        0b01000100, 
        0b00111000, 
        0b00010000, 
        0b00000000, 
        0b00000000   
    ])
    
    stone = bytearray([
        0b11101111, 
        0b11101111, 
        0b00000000,  
        0b01111111, 
        0b01111111, 
        0b01111111, 
        0b00000000  
    ])
        
    water = bytearray([
        0b00000000,  
        0b10011001,  
        0b01100110,  
        0b00000000, 
        0b00111000, 
        0b11000110,  
        0b00000000  
    ])
 
    clear = bytearray([
         0b00000000,  
         0b00000000, 
         0b00000000,  
         0b00000000,  
         0b00000000,  
         0b00000000,  
         0b00000000   
    ])
    
    hero_right = bytearray([
         0b01110000,  
         0b01110000, 
         0b00000011,  
         0b01111100,  
         0b10110000,  
         0b01001000,  
         0b11001100   
    ])
    
    hero_left = bytearray([
         0b00011100,  
         0b00011100, 
         0b00000000,  
         0b11111100,  
         0b00011011,  
         0b00100100,  
         0b11000110   
    ])
  
    hero_down = bytearray([
         0b00011100,  
         0b00011101, 
         0b11000001,  
         0b00111110,  
         0b00011100,  
         0b11100010,  
         0b00000011   
    ])
    
    hero_up = bytearray([
         0b00011100,  
         0b00011100, 
         0b01100011,  
         0b00111100,  
         0b00011000,  
         0b00100100,  
         0b01100110   
    ])
    
        
    blade = bytearray([
         0b01000100,  
         0b01000100, 
         0b11111111,  
         0b11111111,  
         0b00000000,  
         0b00000000,  
         0b00000000   
    ])
    
    hero_death = bytearray([
         0b01000110,  
         0b11000111, 
         0b11111111,  
         0b00000000,  
         0b11000111,  
         0b10111011,  
         0b00111100  
    ])
    
    
    blade_mov = bytearray([
         0b00000000, 
         0b00000000,  
         0b11111111,  
         0b11111111,  
         0b00000000,
         0b00000000,
         0b00000000
    ])
    
    health = bytearray([
         0b11111111, 
         0b10000001,  
         0b10011001,  
         0b10111101,  
         0b10011001,
         0b10000001,
         0b11111111
    ])
    
    heart = bytearray([
         0b11111111,
         0b11111111, 
         0b11011101,  
         0b10001000,  
         0b10000000,  
         0b10000000,
         0b11000001,
         0b11100011,
         0b11110111,
         0b11111111
    ])
             
    monster1 = framebuf.FrameBuffer(monster1, 8, 7, framebuf.MONO_HLSB)
    monster1_mov = framebuf.FrameBuffer(monster1_mov, 8, 7, framebuf.MONO_HLSB)
    stone = framebuf.FrameBuffer(stone, 8, 7, framebuf.MONO_HLSB)
    water = framebuf.FrameBuffer(water, 8, 7, framebuf.MONO_HLSB)
    clear = framebuf.FrameBuffer(clear, 8, 7, framebuf.MONO_HLSB)
    hero_right = framebuf.FrameBuffer(hero_right, 8, 7, framebuf.MONO_HLSB)
    hero_left = framebuf.FrameBuffer(hero_left, 8, 7, framebuf.MONO_HLSB)
    hero_down = framebuf.FrameBuffer(hero_down, 8, 7, framebuf.MONO_HLSB)
    hero_up = framebuf.FrameBuffer(hero_up, 8, 7, framebuf.MONO_HLSB)
    blade = framebuf.FrameBuffer(blade, 8, 7, framebuf.MONO_HLSB)
    blade_mov = framebuf.FrameBuffer(blade_mov, 8, 7, framebuf.MONO_HLSB)
    monster2 = framebuf.FrameBuffer(monster2, 8, 7, framebuf.MONO_HLSB)
    monster2_mov = framebuf.FrameBuffer(monster2_mov, 8, 7, framebuf.MONO_HLSB)
    health = framebuf.FrameBuffer(health, 8, 7, framebuf.MONO_HLSB)
    hero_death = framebuf.FrameBuffer(hero_death, 8, 7, framebuf.MONO_HLSB)
    heart = framebuf.FrameBuffer(heart, 8, 10, framebuf.MONO_HLSB)
    
    # ===== stav hry =====
    movie = 1
    movie2 = 1
    movie3 = 0
    smer = 1
    room = 0
    col = 0
    maz = 1

    # ===== hrdina =====
    x_hero = 8
    y_hero = 35
    x_hero_old = 0
    y_hero_old = 0
    jump = 0
    pad = 0
    up = 0
    lives = 9

    # ===== scroll mapy =====
    x_roll = 0
    y_roll = 0

    # ===== pomocné =====
    tlac = 1
    line = 0
    next_x = 0
    fix = 0

    # ===== nepřátelé a překážky =====
    blade1_x = []
    blade1_y = []
    blade1_count = 0

    monster1_x = []
    monster1_y = []
    monster1_x_old = []
    monster1_y_old = []
    monster1_count = 0
    monster1_move = []
    
    
    monster2_x = []
    monster2_y = []
    monster2_x_old = []
    monster2_y_old = []
    monster2_count = 0
    monster2_move = []

    # ===== mapa =====
    mapa = [       

        "###########################################################################",
        "#       #     P #               #            #                            #",
        "#       #                                    #                            #",
        "#       #                                    #       #                    #",
        "#     P                                      #       #                    #",
        "#     #  M  M #        P                     #       #                    #",
        "####  #########   L    #                     #       #                    #",
        "####  #       #####H#  #     P               #       #                    #",
        "####HH#       #######        ####    P       #       #                    #",
        "#######                              #       #       #                    #",
        "#                                            #       #                    #",
        "#                                            #       #                    #",
        "#                                            #       #                    #",
        "#                                            #       #                    #",
        "#                                            #       #                    #",
        "#                                           ##       #                    #",
        "#     # M  #                                 #      ##                    #",
        "#     ######                                 #       #                    #",
        "#             ###  #   ##       P            #       #                    #",
        "#              ##      ##    #M #            #      ##                    #",
        "#  #                         ####            #       #                    #",
        "## #VVVVVVVVVVVVVVVVVVVVVVVVV#####VVVVVVVVV###       #                    #",
        "## ###########################################      ##                    #",
        "## ###########################################       #                    #",
        "## ###########################################      L#                    #",
        "##                                           #      ##                    #",
        "##                                           #       #                    #",
        "##       P  P                                        #                    #",
        "#####VV#H#VV#VV###VV#VV###VVHVV####VVHVV##H####VVVVV##",
        "##########################################################################",
        "##########################################################################",
        "##########################################################################",
    ]

    # ===== hardware =====
    tlacitko_right = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko_left = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko_end = Pin(4, Pin.IN, Pin.PULL_UP)
    tlacitko_up = Pin(3, Pin.IN, Pin.PULL_UP)
    tlacitko_down = Pin(11, Pin.IN, Pin.PULL_UP)

    buzzer = PWM(Pin(16))
    shift = 0
    
    def draw():
        
        for i in 57:
            if monster2_x[i] == x_hero and monster2_y[i] == y_hero:
                oled.blit(hero_death, x_hero, y_hero)
                lives = lives - 1
        
        return

    # ===== pomocné funkce =====
    def reset_room():
        nonlocal monster1_x_old, monster1_y_old
        nonlocal monster1_x, monster1_y
        nonlocal monster2_x_old, monster2_y_old
        nonlocal monster2_x, monster2_y
        nonlocal blade1_x, blade1_y, livesblok
        nonlocal monster1_move, monster1_count, blade1_count
        nonlocal monster2_move, monster2_count

        monster1_x_old = []
        monster1_y_old = []
        monster1_x = []
        monster1_y = []
        
        monster2_x_old = []
        monster2_y_old = []
        monster2_x = []
        monster2_y = []
        
        blade1_x = []
        blade1_y = []
        
        monster1_move = []
        monster1_count = 0
        
        monster2_move = []
        monster2_count = 0
        livesblok = 0
        
        blade1_count = 0
        return

    # ===== hlavní smyčka =====
    while True:
        movie = -movie
        movie3 = movie3 + 1
        if movie3 > 10:
            movie3 = 0

        x_hero_old = x_hero
        y_hero_old = y_hero

        # --- konec ---
        if not tlacitko_end.value():
            return

        # --- vstup ---
        if not tlacitko_right.value():
            oled.fill_rect(x_hero,y_hero,8,7, 0)
            smer = 1
            x_hero += 8
            tlac = 1
            movie2 = -movie2
            

        if not tlacitko_left.value():
            oled.fill_rect(x_hero,y_hero,8,7, 0)
            smer = 2
            x_hero -= 8
            tlac = 1
            movie2 = -movie2
            

        if not tlacitko_up.value():
            oled.fill_rect(x_hero_old,y_hero_old,8,7, 0)
           
            tlac = 1
            if jump == 0 and pad == 0:
                jump = 1

        # --- skok ---
        if jump <= 4 and jump > 0 :
            
  
            y_hero -= 7
            jump += 1
        elif jump > 4:
            
            y_hero += 7
            jump += 1

        if jump > 8:
            jump = 0

        # --- kolize ---
        colision = mapa[y_hero // 7 + y_roll][x_hero // 8 + x_roll : x_hero // 8 + 1 + x_roll]
        fix = mapa[y_hero // 7 + y_roll + 1][x_hero // 8 + x_roll : x_hero // 8 + 1 + x_roll]

        if (fix == " " or fix == "S" or fix == "M" or fix == "P" or fix == "L") and jump == 0:
            y_hero += 7
            pad = 1
            up = 2
        else:
            pad = 0
            up = 1

        if colision != " " and colision != "S" and colision != "M" and colision != "P" and colision != "L":
            y_hero = y_hero_old
            x_hero = x_hero_old
            col = 1
        else:
            col = 0
            
        if colision == "L" and livesblok==0:
            lives = 9
            livesblok=1

        # --- přechod roomazovky ---
        if x_hero // 8 >= 16 and smer == 1:
            x_roll += 16
            x_hero = 0
            smer = 0
            room = 0
            reset_room()

        if x_hero // 8 <= 0 and smer == 2:
            x_roll -= 16
            x_hero = 120
            smer = 0
            room = 0
            reset_room()

        if y_hero // 7 >= 8 and up == 2:
            y_roll += 7
            y_hero = 0
            up = 0
            room = 0
            reset_room()

        if y_hero // 7 <= 0 and up == 1:
            y_roll -= 7
            y_hero = 42
            up = 0
            room = 0
            reset_room()

        # --- kreslení hráče ---
       
      
        if smer == 0:
            oled.blit(hero_up, x_hero, y_hero)
        elif smer == 1 or smer == 2:
            if movie2 == 1:
                oled.blit(hero_left, x_hero, y_hero)
            else:
                oled.blit(hero_right, x_hero, y_hero)
        elif smer == 3:
            oled.blit(hero_up, x_hero, y_hero)
        elif smer == 4:
            oled.blit(hero_down, x_hero, y_hero)

        # --- pohyb monster1 ---
        for i in range(monster1_count):
            oled.fill_rect(monster1_x[i],monster1_y[i],8,7, 0)
            monster1_x[i] += monster1_move[i]
            

            colision3 = mapa[monster1_y[i] // 7 + y_roll][monster1_x[i] // 8 + x_roll : monster1_x[i] // 8 + 1 + x_roll]

            if colision3 != " " and colision3 != "S" and colision3 != "M" and colision3 != "P":
                monster1_y[i] = monster1_y_old[i]
                monster1_x[i] = monster1_x_old[i]
                monster1_move[i] = -monster1_move[i]

            monster1_y_old[i] = monster1_y[i]
            monster1_x_old[i] = monster1_x[i]
            
        # --- pohyb monster2 ---
        for i in range(monster2_count):
            oled.fill_rect(monster2_x[i],monster2_y[i],8,7, 0)
            monster2_y[i] += monster2_move[i]       

            colision4 = mapa[monster2_y[i] // 7 + y_roll][monster2_x[i] // 8 + x_roll : monster2_x[i] // 8 + 1 + x_roll]

            if colision4 != " " and colision4 != "S" and colision4 != "M" and colision4 != "P":
                monster2_y[i] = monster2_y_old[i]
                monster2_x[i] = monster2_x_old[i]
                monster2_move[i] = -monster2_move[i]

            monster2_y_old[i] = monster2_y[i]
            monster2_x_old[i] = monster2_x[i]

        # --- kreslení monster ---
        for i in range(monster1_count):
            if movie == 1:
                oled.blit(monster1, monster1_x[i], monster1_y[i])
            else:
                oled.blit(monster1_mov, monster1_x[i], monster1_y[i])
        
                # --- kreslení monster ---
        for i in range(monster2_count):
            if movie == 1:
                oled.blit(monster2, monster2_x[i], monster2_y[i])
            else:
                oled.blit(monster2_mov, monster2_x[i], monster2_y[i])

        # --- kreslení blade ---
        for i in range(blade1_count):
            if movie3 > 5:
                oled.fill_rect(blade1_x[i],blade1_y[i],8,7, 0)
                oled.blit(blade, blade1_x[i], blade1_y[i])
            else:
                oled.fill_rect(blade1_x[i],blade1_y[i],8,7, 0)
                oled.blit(blade_mov, blade1_x[i], blade1_y[i])

        # --- načtení roomazovky ---
        if room == 0:
            oled.fill(0)

            line = 0
            next_x = 0

            for i in range(144):
                read = mapa[line + y_roll][x_roll + next_x : x_roll + next_x + 1]

                if read == '#':
                    oled.blit(stone, next_x * 8, line * 7)

                if read == 'L':
                    oled.blit(health, next_x * 8, line * 7)

                if read == 'V':
                    oled.blit(water, next_x * 8, line * 7)
                    
                if read == 'B':
                    oled.blit(gate, 0, 0)

                if read == 'H':
                    blade1_count += 1
                    blade1_x.append(next_x * 8)
                    blade1_y.append(line * 7)

                if read == 'M':
                    monster1_count += 1
                    monster1_x.append(next_x * 8)
                    monster1_y.append(line * 7)
                    monster1_x_old.append(next_x * 8)
                    monster1_y_old.append(line * 7)
                    monster1_move.append(8)
                    
                if read == 'P':
                    monster2_count += 1
                    monster2_x.append(next_x * 8)
                    monster2_y.append(line * 7)
                    monster2_x_old.append(next_x * 8)
                    monster2_y_old.append(line * 7)
                    monster2_move.append(7)

                next_x += 1

                if next_x == 16:
                    line += 1
                    next_x = 0

                if line == 9:
                    line = 0
                    next_x = 0
                    room = 1
                    
        for i in range(monster1_count):
            if monster1_x[i] == x_hero and monster1_y[i] == y_hero:
                oled.blit(hero_death, x_hero, y_hero)
                lives = lives - 1
                
                
        for i in range(monster2_count):
            if monster2_x[i] == x_hero and monster2_y[i] == y_hero:
                oled.blit(hero_death, x_hero, y_hero)
                lives = lives - 1
                
        if fix == "H" and movie3 > 5:
            oled.blit(hero_death, x_hero, y_hero)
            lives = lives - 1
            
                 
        if fix == "V" :
            oled.blit(hero_death, x_hero, y_hero)
            lives = lives - 1
        
        if lives <= 0 :
            oled.fill_rect(28, 23, 80, 10, 1)
            oled.text("GAME OVER", 30, 25, 0)
            oled.show()
            time.sleep(3)
            dungeon()
        
        oled.fill_rect(118,0,128,10, 1)
        oled.blit(heart, 110, 0)
        oled.text(str(lives), 119, 1, 0)
        oled.fill_rect(8,0,48,10, 1)
       
        oled.show()
        time.sleep(0.1)

        # --- mazání sprite ---
        if jump > 0 or pad == 1 or col == 1:
            oled.fill_rect(x_hero,y_hero,8,7, 0)
        
        
        
       

        #for i in range(monster1_count):
        #    oled.blit(clear, monster1_x[i], monster1_y[i])
        
    

        oled.show()        



#########################################################################################################################
# Game:  space ---------------------------------------------------------------------------------------

def game_space():
    

    tlacitko = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko2 = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(3, Pin.IN, Pin.PULL_UP)
    tlacitko4 = Pin(4, Pin.IN, Pin.PULL_UP)
    buzzer = PWM(Pin(16))
    reset = 1

    while True:
        if reset == 1:
            x_star2 = 0
            x = 1
            x_star=1
            ran = 2
            ran2 = 0
            x_hero = 0
            tilt = 0
            score = 1
            shield = 100
            shot = 0
            ran3 = 0
            ran4 = 0
            ran5 = 0
            s = 1
            block = 1
            block2 = 0
            oprava = 1
            r = 0
            dest = 0
            boom = 0
            hit = 0
            flash_shield = 0
            flash_count = 0
            flash_spaceship = 1
            reset = 0
            sound=0
            
        
        
        if flash_count >= 1:
            flash_count = flash_count+1
            flash_spaceship = flash_spaceship+1 

        if flash_spaceship == 2:
            flash_spaceship = 0

        if flash_count >= 5:
            flash_count = 0
    
        oled.fill(0) 
        tilt = 0
        
        if not tlacitko4.value():  
           return
        
        # move spaceship

        if not tlacitko.value():  
            x_hero = x_hero + 4
            tilt = 4 
  
        if not tlacitko2.value():  
            x_hero = x_hero - 4
            tilt = -4
        
        # shot from your spaceship
            
        if not tlacitko3.value():  
            shot = 1
            block = block + 1
               
            
        if shot == 1 and block == 0:
            shot = 0
            oled.line(60 + x_hero, 45 , 60 + x_hero + tilt, 15, 1)
            sound=1
             
        if block >= 1:
            block=0   
            
       
        
        # flash shield
        
        flash_shield = flash_shield + 1 

        if flash_shield == 2:
            flash_shield = 0   
        
        # star cluster
        
        oled.rect(62 - x_star , 25 - x_star , 1, 1, 1)
        oled.rect(68 + x_star, 30+x_star, 1, 1, 1)
        oled.rect(70 + x_star2, 28 - x_star2, 1, 1, 1)
        oled.rect(60 - x_star2 , 32 + x_star2 , 1, 1, 1)
        oled.rect(85 + x_star2 + ran, 13 - x_star2 , ran, ran, 1)
        oled.rect(45 - x_star2 , 47 + x_star2 , 1, 1, 1)
        oled.rect(62 - x_star , 25 ,1, 1, 1)
        oled.rect(68 + x_star, 22, 1, 1, 1)
        oled.rect(32 - x_star, 25 , 1, 1, 1)
        oled.rect(98 + x_star, 22, ran, ran, 1)
        
        x_star=x_star+r
        x_star2=x_star2+r
        
        if x_star2 >= 15:
            x_star2=0
        if x_star >= 30:
            x_star=0
            ran = random.randint(1, 2)
        
        # alien
            
        if x >= 15 and oprava < 5:
            
            oled.rect( 58 + ran2, 3 + x + dest, 4, 4, 1)
            oled.rect( 55 + ran2 - dest, 2 + x + dest, 1, 7, 1)
            oled.rect( 64 + ran2 + dest, 2 + x + dest, 1, 7, 1)
            oled.rect( 56 + ran2 , 5 + x + dest * 2, 9, 1, 1)
        else:
            oled.rect( 58 + ran2 , 3 + x, 4, 2, 1)
           
        if x >= 15 and oprava == 5:
            oled.rect( 58 + ran2 , 3 + x, 6, 6, flash_shield)
            oled.rect( 60 + ran2, 5 + x, 2, 2, flash_shield)
    
        # informations
         
        oled.text("score:" + str(score), 65 , 57)
        oled.rect( 0, 58, 6, 6, 1)
        oled.rect( 2, 60, 2, 2, 1)
        oled.text(str(shield) + "%", 10, 57)
        
        # alien move
        
        x = x + r
        r = round(s)
            
        # alien random shot
         
        if x == 16 and ran4 == 1 and oprava < 5 and boom==0:
            
            
            oled.line(58 + ran3, 55 , 62 + ran2, 5 + x , 1)

            sound = 1
            
        # alien hit your spaceship
        
        if x_hero < ran3 + 8 and x_hero > ran3-8 and  x == 16 and ran4 == 1 and boom==0:
         
            flash_count = 1
            shield = shield - 10
        
        # game over
        
        if  shield < 1:
            oled.text("GAME OVER", 25, 26)
            reset = 1        
            oled.show()
            time.sleep(2)
        
        # shield catch
    
        if x_hero < ran2 + 8 and x_hero > ran2-8 and x >= 36 and oprava == 5:
            
            shield = shield + 10
            sound = 1
            boom = 0
        
        # your bad hit to alien
        
        if x >= 36:
            if hit == 0 and oprava < 5:
                oled.line(60 + x_hero, 55 , 65 + ran2, 5 + x , 1)
                # oled.rect( 33 + x_hero , 50, 55, 5, 1)
                flash_count = 1
                shield = shield - 10
                sound = 1
            dest = 0
            x = 0
            
            ran2 = random.randint(-10, 10)
            ran3 = random.randint(-10, 10)
            ran4 = random.randint(1, 2)
            oprava = random.randint(1, 5)
            ran2 = ran2 * 4
            ran3 = ran3 * 4
            s=s+0.05
            boom = 0
            hit = 0
            block2 = 0
        
        # successful hit to alien 
        
        if x_hero < ran2 + 8 and x_hero > ran2-8 and x >= 14 and shot == 1 and oprava < 5 and block2 == 0:
           
            boom = 1
            block2=1
            hit = 1
            score = score + 1
            sound=1
            
        if boom == 1:
            dest = dest - 4
        
        # beep
        
        if sound==1:
            sound=0
            buzzer.freq(50)
            buzzer.duty_u16(32768)
            time.sleep(0.05)
            buzzer.duty_u16(0)
            buzzer.deinit()
    

        # your spaceship

        oled.line(60 + x_hero, 47 , 70 + x_hero, 55 + tilt, flash_spaceship)
        oled.line(60 + x_hero, 47, 50 + x_hero, 55 - tilt , flash_spaceship)
        oled.line(60 + x_hero, 52 , 70 + x_hero, 55 + tilt, flash_spaceship)
        oled.line(60 + x_hero, 52, 50 + x_hero, 55 - tilt , flash_spaceship)

        
        
        time.sleep(0.1)
        
        oled.show()
        
# Game:  Pong ---------------------------------------------------------------------------------------


def game_pong():

    x_hero = 2
    direction = 0
    ran = 1
    direction2 = 1
    direction3 = 1
    x_hero_old = 2
    y_hero_old = 2
    score = 0
    tlacitko = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko2 = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(4, Pin.IN, Pin.PULL_UP)
    buzzer = PWM(Pin(16))
    shift = 0
    sound = 0

    while True:


        if not tlacitko3.value():  
            return

        if not tlacitko.value():  
            x_hero = x_hero + 2  
  
        if not tlacitko2.value():  
            x_hero = x_hero - 2 

        
        oled.fill(0)  
        oled.text("Score " + str(score), 0, 0)
   

        # bat
        oled.rect(x_hero, 58, 10, 2, 1)

        # ball
        oled.rect(x_hero_old + 5 , 56 - y_hero_old, 2, 2, 1)
   

        if shift == 0:
            x_hero_old = x_hero_old + ran 
            y_hero_old = y_hero_old + direction3

    
        if x_hero_old <= 0 or x_hero_old >= 116:  
            direction2 = -direction2
            ran = -ran
            sound = 1
       
        if x_hero <= x_hero_old + 8 and x_hero >= x_hero_old - 8 and y_hero_old == 0:   
            shift = 0
            ran = random.randint(1, 3)
            score = score + 1
            sound = 1

        elif y_hero_old == 0 :       
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2) 
            x_hero = 2
            direction = 0
            ran = 1
            direction2 = 1
            direction3 = 1
            x_hero_old = 2
            y_hero_old = 2
            score = 0
   
    
        if y_hero_old <= 0 or y_hero_old >= 54:  
            direction3 = -direction3
            sound = 1
        

        oled.show()


        if sound == 1:
            buzzer.freq(200)
            buzzer.duty_u16(32768)
            time.sleep(0.02)
            buzzer.duty_u16(0)
            sound = 0
            buzzer.deinit()
        else:
            time.sleep(0.02)



# Game: Lunar module ---------------------------------------------------------------------------------------

def game_modul():

    
    level = 1
    x_hero = 2
    direction = 0
    ran = 1
    direction2 = 1
    direction3 = 1
    x_hero_old = 2
    y_hero_old = 2
    gravity= 1
    fuel = 25
    fire = 0
    
    tlacitko2 = Pin(20, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(4, Pin.IN, Pin.PULL_UP)
    shift = 0

    while True:


        if not tlacitko3.value():  
           return
    
        if not tlacitko2.value():
            fire = 1
            gravity = gravity - 5
            fuel = fuel - 1 

  
        oled.fill(0)  
        oled.text("Fuel " + str(fuel), 0, 55)
        oled.text("m/s " + str(gravity), 80, 1)
    
   
        # Lunar modul
        
        oled.rect(6 + x_hero_old, 3 + y_hero_old, 5, 5, 1)
        oled.vline(5 + x_hero_old, 5 + y_hero_old, 5, 1)
        oled.vline(11 + x_hero_old, 5 + y_hero_old, 5, 1)
        oled.rect(7 + x_hero_old, 1 + y_hero_old, 3, 4 , 1)

        # landing area
        oled.rect(100, 62, 14, 2, 1)
        
        if fire == 1:
            oled.vline(8 + x_hero_old, 11 + y_hero_old, 8, 1)
            fire = 0

        x_hero_old = x_hero_old + ran 
        y_hero_old = y_hero_old + direction3
        y_hero_old = y_hero_old +  1 + gravity // 10
        gravity = gravity + 1
       
        if x_hero_old > 90 and x_hero_old < 110 and y_hero_old >=  56 and gravity < 4:
            oled.text("Landing OK!", 25, 20)
            level = level + 1
            oled.text("Level " + str(level), 25, 30)
            oled.show()
            time.sleep(2) 
            x_hero = 2
            direction = 0
            gravity = 1
            ran = ran + 1
            direction2 = 1
            direction3 = 1
            x_hero_old = 2
            y_hero_old = 2
            fuel = 25

        elif y_hero_old >=  56 or fuel < 1:       
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2) 
            x_hero = 2
            direction = 0
            gravity = 1
            ran = 1
            direction2 = 1
            direction3 = 1
            x_hero_old = 2
            y_hero_old = 2
            fuel = 25
            level = 1
   

        oled.show()

        time.sleep(0.1)


# Game: Full speed ---------------------------------------------------------------------------------------

def game_moto():
    x = 1
    y = 1
    prekazka = 1
    ran = 0
    direction3 = 1
    x_hero = 2
    tilt = 0
    score = 1
    speed= 1
    acceleration = 1
    level = 1
    y_rival = 0
    crasch = 0

    tlacitko = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko2 = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(4, Pin.IN, Pin.PULL_UP)



    while True:
    
        oled.fill(0) 
        tilt = 0
        if not tlacitko3.value():  
           return

        if not tlacitko.value():  
            x_hero = x_hero + 2
            tilt = 4 
  
        if not tlacitko2.value():  
            x_hero = x_hero - 2
            tilt = -4
    
        y_rival = ran + y
        oled.text("Score:" + str(score), 0, 0)
        oled.text(str(score * 5) + " km/h", 70, 0)
    
        x = x + 1
        y = y + direction3
        prekazka = prekazka + speed

    
        # horizont
        oled.line(20 + y // 5, 35 + y // 10 , 9 + y // 4 , 39 + y // 10, 1)
        oled.line(20 + y // 5, 35 + y // 10, 29 + y // 4, 39 + y // 10, 1)
        
        # road
    
    
        oled.rect(0, 40 + y //10, 128, 2, 1)

        oled.line(50 + y, 40 + y // 10, 30 , 50, 1)
        oled.line(70 + y , 40 + y // 10, 90, 50, 1)
    
        oled.line(30, 50, 10, 63, 1)
        oled.line(90, 50, 118, 63, 1)
    
        oled.rect(0, 42 + x//2, 128, 4, 0)
    
        oled.rect(0, 52 + x, 128, 8, 0)
    
        # your moto
        oled.rect(60 + x_hero, 58, 2, 4, 1)
        oled.rect(59  + x_hero + tilt // 2, 55, 5, 4, 1)

        oled.rect(60 + x_hero + tilt, 52, 2, 2, 1)

        # rival
        if prekazka > 10: 
            oled.rect(60 + ran + y, 38 + prekazka , 2, 4, 1)
            oled.rect(59 + y // 20  + ran + y, 35 + prekazka, 5, 4, 1)

            oled.rect(60 + y // 10  + ran + y, 32 + prekazka, 2, 2, 1)
        
        if prekazka <= 10: 
            oled.rect(60 + ran + y, 38 + prekazka , 2, 4, 1)
    
        oled.show()
    
        if x== 4:  
            x = 0

        if prekazka >= 30:  
            ran = random.randint(-5, 5)
            ran = ran * 2
            prekazka = 0
            score = score + 1
            acceleration = acceleration + 0.05
            speed = round(acceleration)
    

        if y <= -35  or y >= 25:  
            direction3 = -direction3

        if y <= -15:  
            x_hero = x_hero + 2
        
        if y > 15 :  
            x_hero = x_hero - 2
            
        if x_hero >=  46 or x_hero < -46:       
            crasch = 1

        if x_hero <= y_rival + 4  and x_hero >= y_rival - 4 and prekazka >= 15:       
            crasch = 1


        if  crasch ==  1:  
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2)
            x = 1
            y = 1
            prekazka = 1
            ran = 0
            direction3 = 1
            x_hero = 2
            tilt = 0
            score = 1
            speed= 1
            acceleration = 1
            level = 1
            y_rival = 0
            crasch = 0

        time.sleep(0.1)


# Menu  ---------------------------------------------------------------------------------------

def main_menu():
    
    while True:
        
        
        oled.fill(0)  
        oled.text(" Snack Rider", 18, 25)
        oled.show()
        time.sleep(2)
        SnackRider()
        
        oled.fill(0)  
        oled.text("King of Space", 18, 25)
        oled.show()
        time.sleep(2)
        game_space() 
       
        oled.fill(0)  
        oled.text("   Pong  ", 18, 25)
        oled.show()
        time.sleep(2)
        game_pong() 

        oled.fill(0)  
        oled.text("Lunar Module", 18, 25)
        oled.show()
        time.sleep(2)
        game_modul()         

        oled.fill(0)  
        oled.text(" Full Speed", 18, 25)
        oled.show()
        time.sleep(2)
        game_moto()
        
     
        
main_menu()







