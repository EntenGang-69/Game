############################ PREPERATION SECTION ############################
# IMPORT LIBRARIES
import pygame
import sys
import math
import random
import string

# INITIALIZE PYGAME
pygame.init()

# INITIAL SETUP OF WINDOW
window_height = 420
window_length = window_height/9*16
window = pygame.display.set_mode((window_length, window_height), pygame.RESIZABLE, pygame.SCALED)

# INITIALIZE mixer
pygame.mixer.init()

# IMPORT IMAGES
vapor_logo = pygame.image.load('CookieClicker/images/vapor_logo.png')
cum_inc_logo = pygame.image.load('CookieClicker/images/cum_inc_logo.png')
background_img = pygame.image.load('CookieClicker/images/cookie_clicker_background.png')
store_background_img = pygame.image.load('CookieClicker/images/cookie_clicker_store_background.png')
oreo = pygame.image.load('CookieClicker/images/oreo.png')
cookie_img = pygame.image.load('CookieClicker/images/cookie.png')
upgrades_bg = pygame.image.load('CookieClicker/images/black.jpg')
audio_play_img = pygame.image.load('CookieClicker/images/play.png')
audio_pause_img = pygame.image.load('CookieClicker/images/pause.png')
npc_dialog_black = pygame.image.load('CookieClicker/images/black2.png')
npc_dialog_white = pygame.image.load('CookieClicker/images/white.png')
npc_cookie_monster = pygame.image.load('CookieClicker/images/cookie_monster.png')
npc_cookie_monster_cookies = pygame.image.load('CookieClicker/images/cookie_monster_cookies.png')
npc_cookie_monster_cookies = pygame.image.load('CookieClicker/images/cookie_monster_cookies.png')
npc_shrek_cookie = pygame.image.load('CookieClicker/images/shrek_cookie.png')
jumpscare_cookie = pygame.image.load('CookieClicker/images/jumpscare_cookie.png')
golden_cookie_pic = pygame.image.load('CookieClicker/images/golden_cookie.png')
wooden_bar_horizontal = pygame.image.load('CookieClicker/images/wooden_bar_horizontal.png')
wooden_bar_vertical = pygame.image.load('CookieClicker/images/wooden_bar_vertical.png')
milk = pygame.image.load('CookieClicker/images/milk.png')
black_fade_full = pygame.image.load('CookieClicker/images/black_fade_full.png')
black_fade_half = pygame.image.load('CookieClicker/images/black_fade_half.png')

# IMPORT AUDIO
awm = pygame.mixer.Sound('CookieClicker/audio/awm.mp3')
upgrade_sound = pygame.mixer.Sound('CookieClicker/audio/8-Bit_Upgrade-Sound.mp3')
golden_cookie_sound = pygame.mixer.Sound('CookieClicker/audio/8-Bit_Golden-Cookie-Sound.mp3')
key_press = pygame.mixer.Sound('CookieClicker/audio/key_press.mp3')
minecraft_hit = pygame.mixer.Sound('CookieClicker/audio/minecraft_hit.mp3')
elixir = pygame.mixer.Sound('CookieClicker/audio/elixir.mp3')
hog_rider = pygame.mixer.Sound('CookieClicker/audio/hog_rider.mp3')
augh = pygame.mixer.Sound('CookieClicker/audio/augh.mp3')
cookie_monster_sound = pygame.mixer.Sound('CookieClicker/audio/Hom_nom_nom_nom_nom.mp3')
jumpscare_cookie_scream = pygame.mixer.Sound('CookieClicker/audio/augh.mp3')

# SET DEFAULT COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)
GREEN = (198, 134, 123)
BLUE = (51, 60, 75)

# STANDARD CURSOR SETUP
# import img
custom_default_cursor_img = pygame.image.load('CookieClicker/images/custom_default_cursor.png')
# scale img
custom_default_cursor_img =pygame.transform.scale(custom_default_cursor_img, (20, 20))
# set cursor
standard_cursor = pygame.cursors.Cursor((8, 0), custom_default_cursor_img)
pygame.mouse.set_cursor(standard_cursor)

# SETUP TITLE
template = "{} - {}"
CAPTION = "Cookie Clicker THE ORIGINAL"
version = " Version 1.0 "
pygame.display.set_caption(template.format(CAPTION, version.capitalize()))

# SETUP WINDOW ICON
pygame.display.set_icon(cookie_img)

############################ CLASS SECTION ############################
# CLASS FOR THE BIG CLICKABLE COOKIE
class MainCookie:
    # INITIAL SETUP OF COOKIE
    def __init__(self):
        self.animation_state = 0
        self.hit = False
        self.starting_frame = 0
        self.image = cookie_img

    # DRAW COOKIE
    def draw(self):
        # ANIMATINION STATES CHANGE OF COOKIE SIZE
        # when hit
        if self.animation_state > 0:
            cookie_img_scaled = pygame.transform.scale(self.image, ( int(1.1*x_size_cookie), int(1.1*x_size_cookie) ))
            window.blit(cookie_img_scaled, (cookie_img_scaled.get_rect(center =( x_pos_cookie, y_pos_cookie) )))
            self.animation_state -= 1
        # default
        else:
            cookie_img_scaled = pygame.transform.scale(self.image, ( int(1*x_size_cookie), int(1*x_size_cookie) ))
            window.blit(cookie_img_scaled, (cookie_img_scaled.get_rect(center =( x_pos_cookie, y_pos_cookie) )))

    # DEFINING COLLIDER / HITBOX
    def collidepoint(self):
        x_distance = x_pos_cookie - pygame.mouse.get_pos()[0]
        y_distance = y_pos_cookie - pygame.mouse.get_pos()[1]
        if x_distance < 0:
            x_distance = x_distance*-1
        if y_distance < 0:
            y_distance = y_distance*-1
        distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
        if distance <= (x_size_cookie*0.48):
            return True

#CLASS FOR ANIMATON OF SMALL COOKIES AND NUMBERS WENN THE BIG COOKIE IS CLICKED
class CookieHitAnimation:
    # INITIAL SETUP
    def __init__(self):
        self.starting_frame = total_frames_drawn
        self.hit_location = pygame.mouse.get_pos()
        self.animation_frame = 0
        self.animation_speed = random.randint(-7, 7)
        self.hit_opacity = 255
        self.font = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', int(current_window_height*0.03))
        self.image = cookie_img

    # DRAWS THE ANIMATION
    def animate(self):
        if total_frames_drawn < (self.starting_frame + FPS * 0.3):
            if total_frames_drawn != self.starting_frame:
                if total_frames_drawn < (self.starting_frame + FPS * 0.2):
                    self.hit_opacity -= 30
                self.animation_frame += 1
                self.hit_location = (self.hit_location[0] + current_window_height*self.animation_frame*0.0001*self.animation_speed, self.hit_location[1] - current_window_height*0.01)
            cookie_hit_img = pygame.transform.scale(self.image, (current_window_height*0.06, current_window_height*0.06))
            cookie_hit_img.set_alpha(self.hit_opacity)
            window.blit(cookie_hit_img, (self.hit_location[0] - cookie_hit_img.get_width()/2, self.hit_location[1] - cookie_hit_img.get_height()/2))
            CPH = self.font.render('+{}'.format(format_number ( user.total_cph)), True, WHITE)
            CPH.set_alpha(self.hit_opacity)
            window.blit(CPH, (CPH.get_rect(center=(int(self.hit_location[0])+int(current_window_height*0.03)*0.3, int(self.hit_location[1])+int(current_window_height*0.03)*0.3 ) )))

# CLASS FOR THE DISPLAY OF THE COOKIE SCORE AND COOKIES PER SECOND    
class ScoreDisplay():
    # INITIAL SETUP
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 100
        self.height = 100

    # DRAWS THE DISPLAY 
    def draw(self, x_pos_score, y_pos_score):
        font = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 24)
        small_font = pygame.font.Font('CookieClicker/Font/Kavoon-Regular.ttf', 26)

        SCORE = small_font.render('{} cookies'.format(format_number ( int(user.score))), True, WHITE)
        CPS = font.render('per second: {}'.format(format_number ( user.cps)), True, WHITE)
        window.blit(SCORE, (SCORE.get_rect( center=( int(x_pos_score), int(y_pos_score) ) )))
        window.blit(CPS, (CPS.get_rect(center=(int(x_pos_score), int(y_pos_score)+20 ) )))

# CASS FOR THE CARDS OF THE SHOP, WHICH ADD COOKIES PER SECOND
class Card:
    # INITIAL STATIC SETUP OF CARD (TEMPORARILY)
    def __init__(self, name, index_x, index_y, image, base_cost, increase_per_purchase, cps, sound):
        self.name = name
        self.index_x = index_x
        self.index_y = index_y
        self.length = 200
        self.height = 280

        self.sound = sound

        self.image = pygame.transform.scale(image, (self.length, self.height))
        self.base_cost = base_cost
        self.increase_per_purchase = increase_per_purchase
        self.cps = cps

        self.max_card_count = 100

        self.quantity = 0
        self.created = 0

    # DEFINING COLLIDER / HITBOX
    def collidepoint(self, mouse_pos):
        pos_x = x_pos_store + (self.card_index_x * (self.length + 10))
        pos_y = y_pos_store + (self.card_index_y * (self.height + 10))
        return pygame.Rect(pos_x, pos_y, self.length, self.height).collidepoint(mouse_pos)

    # DEFINING TOTAL COST AFTER PRICE INCREASE
    def getTotalCost(self):
        return self.base_cost * self.increase_per_purchase**(self.quantity)

    # DRAW THE CARD
    def draw(self, card_index_x, card_index_y, solid = True):
        # DEFINING VARIABLES
        store_cost_font = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 14)
        store_quantity_cost = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 20)
        cost = store_cost_font.render('{}'.format( format_number(int(self.getTotalCost()) ) ), True, GREEN)
        cost_length = cost.get_rect().width
        quantity = store_quantity_cost.render('{}'.format(self.quantity), True, BLUE)
        quantity_length = quantity.get_rect().width
        black_overlay_scaled = pygame.transform.scale(black_fade_full, (self.length, self.height))

        # SET / CHECK: PARTIALLY TRANSLUCENT
        if solid == False:
            self.image.set_alpha(170)
        else:
            self.image.set_alpha(255)
        
        # SET POSITION
        pos_x = x_pos_store + (card_index_x * (self.length + 10))
        pos_y = y_pos_store + (card_index_y * (self.height + 10))

        # SET INDEX
        self.card_index_x = card_index_x
        self.card_index_y = card_index_y

        # DRAW CARD
        window.blit(self.image, (pos_x, pos_y))
        window.blit(cost, (pos_x + 160 - cost_length, pos_y + self.height -40))
        window.blit(quantity, (pos_x + 170 - quantity_length, pos_y + 7))
        window.blit(black_overlay_scaled, (pos_x, pos_y))
    
    # UPGRADE SOUND
    def upgradeSound(self):
        pygame.mixer.Sound.play(self.sound, 0)

# CLASS FOR THE CURSORS OF THE CURSOR SHOP, ABOVE THE CARDS SHOP, WHICH ADD COOKIES PER HIT
class Cursor:
    # INITIAL SETUP OF CURSOR
    def __init__(self, name, index_x, index_y, image, cost, cph, condition_id, sound):
        self.name = name
        self.index_x = index_x
        self.index_y = index_y
        self.length = 100
        self.height = 100

        self.sound = sound

        self.image = pygame.transform.scale(image, (self.length, self.height))
        self.cost = cost
        self.cph = cph
        self.condition_id = condition_id

        self.max_card_count = 1

        self.quantity = 0
        self.created = 0

        self.cursor_image = pygame.transform.scale(image.convert(), (20, 20))
    
    # DEFINING COLLIDER / HITBOX
    def collidepoint(self, mouse_pos):
        pos_x = x_pos_store + (self.cursor_index_x * (self.length + 10))
        pos_y = wooden_bar_width + (self.cursor_index_y * (self.height + 10))
        return pygame.Rect(pos_x, pos_y, self.length, self.height).collidepoint(mouse_pos)

    # DRAW THE CARD
    def draw(self, cursor_index_x, cursor_index_y, solid = True):
        # DEFINING VARIABLES
        store_cost_font = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 14)
        store_quantity_cost = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 20)
        cost = store_cost_font.render('{}'.format( format_number(int(self.cost) ) ), True, GREEN)
        cost_length = cost.get_rect().width
        quantity = store_quantity_cost.render('{}'.format(self.quantity), True, BLUE)

        # SET / CHECK: PARTIALLY TRANSLUCENT
        if solid == False:
            self.image.set_alpha(170)
        else:
            self.image.set_alpha(255)
        
        # SET POSITION
        pos_x = x_pos_store + (cursor_index_x * (self.length + current_window_width * 0.01))
        pos_y = wooden_bar_width + (cursor_index_y * (self.height + current_window_width * 0.01))

        # SET INDEX
        self.cursor_index_x = cursor_index_x
        self.cursor_index_y = cursor_index_y

        # DRAW TO SCREEN
        window.blit(self.image, (pos_x, pos_y))
        window.blit(cost, (pos_x + 80 - cost_length, pos_y + 80))
    
    # CHANGE CURSOR
    def setCursor(self):
        # black to transparent
        self.cursor_image.set_colorkey((0, 0, 0))

        # set cursor
        cursor = pygame.cursors.Cursor((8, 0), self.cursor_image)
        pygame.mouse.set_cursor(cursor)

    # CHECK FOR DISPLAY CONDITION
    def checkCondition(self):
        if list_of_cards[self.condition_id].quantity >= 5:
            return True
        else:
            return False

    # HIT SOUND
    def hitSound(self):
        pygame.mixer.Sound.play(self.sound, 0)

# CLASS FOR DEBUFFS, WHICH REDUCE PLAYER VALUES AFTER ACTIVATION THROUGH NPC 
class Debuff:
    # INITIAL SETUP OF DEBUFF
    def __init__(self, name, image, score_reduce, cps_reduce, cph_reduce, sound):
        self.name = name
        self.length = 200
        self.height = 280

        self.sound = sound

        self.image = pygame.transform.scale(image, (self.length, self.height))
        self.score_reduce = score_reduce
        self.cps_reduce = cps_reduce
        self.cph_reduce = cph_reduce

        self.max_card_count = 100

        self.quantity = 0
        self.created = 0

    # REDUCE PLAYER VALUES
    def reduce(self):
        user.score -= user.score * self.score_reduce
        user.cps -= user.cps * self.cps_reduce
        user.cph -= user.cph * self.cph_reduce
        user.updateTotalCPS()
        user.updateTotalCPH()
    
    # DRAW DEBUFF CARD 
    def draw(self):
        window.blit(self.image, (current_window_width*0.6, current_window_height*0.5))

# CLASS FOR PLAYER STATISTICS  (COOKIE SCORE, CLICKS PER SECOND, COOKIES PER HIT)
class Player:
    # INITIAL SETUP OF PLAYER
    def __init__(self):
        self.score = float(0)
        # cookies per second (AUTOMATICALLY GENERATED COOKIES)
        self.cps = float(0)
        # cookies per hit (MANUALLY GENERATED COOKIES)
        self.cph = 1
        self.cph_multiplier = 1
        self.total_cph = self.cph * self.cph_multiplier

    #  UPDATE THE TOTAL CLICKS-PER-SECOND
    def updateTotalCPS(self):
        self.cps = 0
        for card in list_of_cards:
            self.cps += card.cps * card.quantity
    
    #  UPDATE THE TOTAL CLICKS-PER-HIT
    def updateTotalCPH(self):
        self.cph = 1
        for card in list_of_cursors:
            self.cph += card.cph * card.quantity
        self.total_cph = self.cph * self.cph_multiplier

# CLASS FOR THE BACKGROUND MUSIC
class Music():
    # INITIAL SETUP OF MUSIC PLAYER
    def __init__(self):        
        self.volume = 0.3
        pygame.mixer.music.set_volume(self.volume)
        
        self.play = True

    # DEFINING COLLIDER / HITBOX
    def collidepoint(self, mouse_pos):
        return pygame.Rect(x_pos_music_play_pause, y_pos_music_play_pause, x_size_music_play_pause, x_size_music_play_pause).collidepoint(mouse_pos)

    # DRAW TO FRAME
    def draw(self):
        audio_play_img_scaled = pygame.transform.scale(audio_play_img, (x_size_music_play_pause, x_size_music_play_pause))
        audio_pause_img_scaled = pygame.transform.scale(audio_pause_img, (x_size_music_play_pause, x_size_music_play_pause))
        if self.play == False:
            window.blit(audio_play_img_scaled, (x_pos_music_play_pause, y_pos_music_play_pause))
        else:
            window.blit(audio_pause_img_scaled, (x_pos_music_play_pause, y_pos_music_play_pause))

# CLASS FOR NOT PLAYER CHARACTERS, WHICH POP UP AT CERTAIN EVENTS AND ACTIVATES A DEBUFF CARD
class NPC():
    # INITIAL SETUP OF NPC
    def __init__(self, text, NPC_pic_in, NPC_pic_out, sound, sound_volume):
        self.text = text
        self.NPC_pic_in = NPC_pic_in
        self.NPC_pic_out = NPC_pic_out
        self.NPC_audio_volume = sound_volume
        self.was_activ = False
        self.NPC_pop = False
        self.NPC_pop_stay = False
        self.NPC_pop_return = False
        self.once_activ = False
        self.time = 0
        self.counter = 0
        self.sound = sound

        self.time_until_pop_return = 5000
        self.NPC_cookie_steal = user.score*0.5

    # DRAW NPC DIALOG WINDOW IN ANIMATION TO FRAME
    def draw(self):
        # load and scale images and text
        self.display_dialog_speed = current_window_height * 0.02

        npc_dialog_black_scaled = pygame.transform.scale(npc_dialog_black, (x_pos_leiste, npc_dialog_height))
        npc_dialog_black_scaled.set_alpha(200)            
        npc_dialog_white_top = pygame.transform.scale(npc_dialog_white, (x_pos_leiste, 15))
        npc_dialog_white_bottom = pygame.transform.scale(npc_dialog_white, (15, npc_dialog_height))
        npc_in = pygame.transform.scale(self.NPC_pic_in, (npc_dialog_height, npc_dialog_height))
        npc_out = pygame.transform.scale(self.NPC_pic_out, (npc_dialog_height, npc_dialog_height))

        dialog_text = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 20)
        dialog_text_rendert = dialog_text.render(self.text, True, (255, 255, 255))

        # ANIMATES THE WINDOW POPING UP
        if self.NPC_pop == True:
            if not self.counter >= int(y_pos_npc_dialog * 0.5) or self.counter == 0:
                self.counter += self.display_dialog_speed

                if self.counter >= int(y_pos_npc_dialog * 0.5):
                    self.NPC_pop_stay = True
            else:
                self.NPC_pop = False
                self.counter = 0

            if self.counter < int(y_pos_npc_dialog * 0.5) and not self.NPC_pop_stay == True:
                window.blit(npc_in, (0, current_window_height - y_pos_npc_dialog * 0.5 - self.counter))
                window.blit(npc_dialog_black_scaled, (0, current_window_height - self.counter ))
                window.blit(npc_dialog_white_top, (0, current_window_height - 15 - self.counter))
                window.blit(npc_dialog_white_bottom, (x_pos_leiste - 15, current_window_height - self.counter))
                window.blit(dialog_text_rendert, (dialog_text_rendert.get_rect(center =(x_pos_leiste/2, current_window_height + npc_dialog_text_pos - self.counter))))

        # KEEPS THE WINDOW IN THE POPED POSITON
        if self.NPC_pop_stay == True:
            if self.time == 0 and self.sound != None:
                pygame.mixer.Sound.set_volume(self.sound, self.NPC_audio_volume)
                pygame.mixer.Sound.play(self.sound, 1)
                selector = (random.randint(1, len(list_of_debuffs)-1))
                self.debuff = list_of_debuffs[selector]

            window.blit(npc_in, (0, y_pos_npc_dialog * 0.5))
            window.blit(npc_dialog_black_scaled, (0, y_pos_npc_dialog))
            window.blit(npc_dialog_white_top, (0, y_pos_npc_dialog - 15))
            window.blit(npc_dialog_white_bottom, (x_pos_leiste - 15, y_pos_npc_dialog))
            window.blit(dialog_text_rendert, (dialog_text_rendert.get_rect(center =(x_pos_leiste/2, current_window_height - npc_dialog_text_pos))))
            self.time += Clock.get_time()
            self.debuff.draw()

        # ANIMATES THE WINDOW POPING DOWN
        if self.NPC_pop_return == True:
            self.NPC_pop_stay = False
            if not self.counter >= int(y_pos_npc_dialog * 0.5):
                self.counter += self.display_dialog_speed
            else:
                self.NPC_pop_return = False

            if self.counter < int(y_pos_npc_dialog * 0.5) and not self.NPC_pop_stay == True:
                window.blit(npc_out, (0, y_pos_npc_dialog * 0.5 + self.counter))
                window.blit(npc_dialog_black_scaled, (0, y_pos_npc_dialog + self.counter ))
                window.blit(npc_dialog_white_top, (0, y_pos_npc_dialog - 15 + self.counter))
                window.blit(npc_dialog_white_bottom, (x_pos_leiste - 15, y_pos_npc_dialog + self.counter))            
                window.blit(dialog_text_rendert, (dialog_text_rendert.get_rect(center =(x_pos_leiste/2, current_window_height - npc_dialog_text_pos + self.counter))))

        if self.time > self.time_until_pop_return and self.once_activ == False:
            user.score = float(user.score*0.5)
            self.NPC_pop_return = True
            self.once_activ = True

# CLASS FOR JUMPSCARES AT CERTAIN EVENTS
class Jumpscare():
    # INITIAL SETUP OF JUMPSCARE
    def __init__(self, pic, time_shown, sound, volume):
        self.action = False
        self.jumpscare_pic = pic
        self.time = time_shown
        self.sound = sound
        self.audio_volume = volume

        self.once_activ = False
        self.timer = 0

    # DRAWS JUMPSCARE ON TOP OF THE SCREEN AND PLAYS SOUND
    def draw(self):
        jumpscare_pic_scaled = pygame.transform.scale(self.jumpscare_pic, (current_window_height, current_window_height))

        if self.action == True and self.timer < self.time:
            self.timer += 1
            window.blit(jumpscare_pic_scaled, (jumpscare_pic_scaled.get_rect(center =( current_window_center) )))
            if self.once_activ == False:
                pygame.mixer.Sound.set_volume(self.sound, self.audio_volume)
                pygame.mixer.Sound.play(self.sound, 0)
                self.once_activ = True

# CLASS FOR THE GOLDEN COOKIE, WHICH FALLS DOWN AT REANDOM POSITONS OF THE SCREEN. IT CAN BE CLICKED TO OPTAIN COOKIES
class GoldenCookie():
    # INITIAL SETUP OF JUMPSCARE
    def __init__(self):
        self.action = False
        self.random_pos = 0
        self.random_speed = 0
        self.counter = 0

        self.boost_starting_frame = 0
        self.boost_status = False
        self.boost_duration =  0
        
    # DEFINING COLLIDER / HITBOX
    def collidepoint(self, mouse_pos):
        return pygame.Rect(self.random_pos, self.counter, x_size_cookie*0.1, x_size_cookie*0.1).collidepoint(mouse_pos)

    # DRAW THE GOLDEN COOKIE IN AN ANIMATION FALLING FROM THE TOP OF THE DISPLAY TO THE BOTTOM
    def draw(self):
        golden_cookie_scaled = pygame.transform.scale(golden_cookie_pic, (x_size_cookie*0.1, x_size_cookie*0.1))

        if self.action == True and self.counter < current_window_height:
            self.counter += self.random_speed
            window.blit(golden_cookie_scaled, (self.random_pos, self.counter))
        else:
            self.random_pos = random.randint(20, int(x_pos_leiste) - 40)
            self.random_speed = random.randint(5, 20)
            self.counter = 0
            self.action = False

    # COOKIE BOOST FROM GOLDEN COOKIE
    def boost(self):
        if self.boost_status == True:
            # START BOOST
            if total_frames_drawn == self.boost_starting_frame:
                cookie.image = oreo
                user.cph_multiplier = 2
                self.boost_duration = FPS * 5
                user.updateTotalCPH()
            # MILK ANIMATION
            elif total_frames_drawn < (self.boost_starting_frame+self.boost_duration):
                milk_scaled = pygame.transform.scale(milk, (milk_width+10, milk_width/4*3))
                global milk_pos
                for i in range(milk_build):
                    if (milk_pos[0] + i*milk_width) >= x_pos_leiste+milk_width:
                        milk_pos = (0, milk_pos[1])
                    x_pos_milk = milk_pos[0] + (i-1)*milk_width
                    window.blit(milk_scaled, (x_pos_milk - 5, (current_window_height - milk_scaled.get_height())))
            # END BOOST
            elif total_frames_drawn == (self.boost_starting_frame+self.boost_duration):
                cookie.image = cookie_img
                user.cph_multiplier = 1
                user.updateTotalCPH()
                self.boost_status = False
                
############################ OBJEKT SECTION ############################
# SETUP COOKIE (ONLY TEMPORARY VALUES FOR POSITION AND SIZE)
cookie = MainCookie()

# SETUP SCORE-BOARD (ONLY TEMPORARY VALUES FOR POSITION AND SIZE)
score_display = ScoreDisplay(360, 0)

# SETUP PLAYER
user = Player()

# SETUP MUSIC
theme = Music()

# SETUP NPC 
cookie_monster = NPC("You have got some cookies there, may I have some?", npc_cookie_monster, npc_cookie_monster_cookies, cookie_monster_sound, 0.3)
shrek_cookie = NPC("Eyyyy what are you doing? You can not use those!", npc_shrek_cookie, npc_shrek_cookie, cookie_monster_sound, 0.3)

# SETUP JUMPSCARE
cookie_scream = Jumpscare(jumpscare_cookie, 25, jumpscare_cookie_scream, 1)

# SETUP GOLDEN_COOKIE
golden_cookie = GoldenCookie()

# SET UPGRADE-STORE POSITION (ONLY TEMPORARY VALUES)
store_y = 20
store_x = 830

# SETUP CARDS
# create list
list_of_cards = []
########################################################################
# ROW1 : get image
# ROW2 : create object from class, set values
# ROW3 : append to list
########################################################################
# slave card
card_slaves_img = pygame.image.load('CookieClicker/images/card_slaves.png')
card_slaves = Card("Slaves", 0, 0 , card_slaves_img, base_cost=15, increase_per_purchase=1.15, cps=0.1, sound=upgrade_sound)
list_of_cards.append(card_slaves)
# turbo card
card_turbo_img = pygame.image.load('CookieClicker/images/card_turbo.png')
card_turbo = Card("Turbo", 0, 0 , card_turbo_img, base_cost=100, increase_per_purchase=1.15, cps=1, sound=upgrade_sound)
list_of_cards.append(card_turbo)
#chump hat card
card_chump_hat_img = pygame.image.load('CookieClicker/images/card_chump_hat.png')
card_chump_hat = Card("Chump Hat", 0, 0 , card_chump_hat_img, base_cost=1100, increase_per_purchase=1.15, cps=8, sound=upgrade_sound)
list_of_cards.append(card_chump_hat)
# nuclearreactr card
card_nuclearreactor_img = pygame.image.load('CookieClicker/images/card_nuclearreactor.png')
card_nuclearreactor = Card("Nuclear Reactor", 0, 0 , card_nuclearreactor_img, base_cost=12000, increase_per_purchase=1.15, cps=47, sound=upgrade_sound)
list_of_cards.append(card_nuclearreactor)
# nestle card
card_nestle_img = pygame.image.load('CookieClicker/images/card_nestle.png')
card_nestle = Card("Nestle", 0, 0 , card_nestle_img, base_cost=130000, increase_per_purchase=1.15, cps=260, sound=upgrade_sound)
list_of_cards.append(card_nestle)
# oil card
card_oil_img = pygame.image.load('CookieClicker/images/card_oil.png')
card_oil = Card("Oil", 0, 0 , card_oil_img, base_cost=1400000, increase_per_purchase=1.15, cps=1400, sound=upgrade_sound)
list_of_cards.append(card_oil)
# cookie collector card
card_cookie_collector_img = pygame.image.load('CookieClicker/images/card_cookie_collector.png')
card_cookie_collector = Card("Cookie Collector", 0, 0 , card_cookie_collector_img, base_cost=20000000, increase_per_purchase=1.15, cps=7800, sound=elixir)
list_of_cards.append(card_cookie_collector)
# cookie drill card
card_cookie_drill_img = pygame.image.load('CookieClicker/images/card_cookie_drill.png')
card_cookie_drill = Card("Cookie Drill", 0, 0 , card_cookie_drill_img, base_cost=330000000, increase_per_purchase=1.15, cps=44000, sound=elixir)
list_of_cards.append(card_cookie_drill)
# cookie mine card
card_cookie_mine_img = pygame.image.load('CookieClicker/images/card_cookie_mine.png')
card_cookie_mine = Card("Cookie Mine", 0, 0 , card_cookie_mine_img, base_cost=5100000000, increase_per_purchase=1.15, cps=260000, sound=elixir)
list_of_cards.append(card_cookie_mine)
# hog rider card
card_hog_rider_img = pygame.image.load('CookieClicker/images/card_hog_rider.png')
card_hog_rider = Card("Hog Rider", 0, 0 , card_hog_rider_img, base_cost=75000000000, increase_per_purchase=1.15, cps=5000000, sound=hog_rider)
list_of_cards.append(card_hog_rider)

# SETUP CURSORS
# create list
list_of_cursors = []
###########################################
# ROW1 : get image
# ROW2 : create cursor from class, set values
# ROW3 : append to list
############################################
# wooden pickaxe cursor
cursor_wooden_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_wooden_pickaxe.png')
cursor_wooden_pickaxe = Cursor("Wooden Pickaxe", 0, 0 , cursor_wooden_pickaxe_img, cost=100, cph=2, condition_id=0, sound=minecraft_hit)
list_of_cursors.append(cursor_wooden_pickaxe)
# golden pickaxe cursor
cursor_golden_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_golden_pickaxe.png')
cursor_golden_pickaxe = Cursor("Golden Pickaxe", 0, 0 , cursor_golden_pickaxe_img, cost=500, cph=8, condition_id=1, sound=minecraft_hit)
list_of_cursors.append(cursor_golden_pickaxe)
# diamond pickaxe cursor
cursor_diamond_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_diamond_pickaxe.png')
cursor_diamond_pickaxe = Cursor("Diamond Pickaxe", 0, 0 , cursor_diamond_pickaxe_img, cost=10000, cph=69, condition_id=2, sound=minecraft_hit)
list_of_cursors.append(cursor_diamond_pickaxe)
# netherite pickaxe cursor
cursor_netherite_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_netherite_pickaxe.png')
cursor_netherite_pickaxe = Cursor("Netherite Pickaxe", 0, 0 , cursor_netherite_pickaxe_img, cost=1000000, cph=112, condition_id=3, sound=minecraft_hit)
list_of_cursors.append(cursor_netherite_pickaxe)
# scope cursor
cursor_scope_img = pygame.image.load('CookieClicker/images/scope.png')
cursor_scope = Cursor("AWM", 0, 0 , cursor_scope_img, cost=10000000, cph=1000, condition_id=4, sound=awm)
list_of_cursors.append(cursor_scope)

# SETUP DEBUFFS
# create list
list_of_debuffs = []
###########################################
# ROW1 : get image
# ROW2 : create debuff from class, set values
# ROW3 : append to list
############################################
# bad code debuff
card_bad_code_img = pygame.image.load('CookieClicker/images/card_bad_code.png')
card_bad_code = Debuff("Bad Code", card_bad_code_img, score_reduce=0.1, cps_reduce=0.1, cph_reduce=0.1, sound=upgrade_sound)
list_of_debuffs.append(card_bad_code)
# teachers dream debuff
card_teachers_dream_img = pygame.image.load('CookieClicker/images/card_teachers_dream.png')
card_teachers_dream = Debuff("Teachers Dream", card_teachers_dream_img, score_reduce=0.5, cps_reduce=0.2, cph_reduce=0.3, sound=upgrade_sound)
list_of_debuffs.append(card_teachers_dream)
# math debuff
card_math_img = pygame.image.load('CookieClicker/images/card_math.png')
card_math = Debuff("Math", card_math_img, score_reduce=1, cps_reduce=1, cph_reduce=1, sound=upgrade_sound)
list_of_debuffs.append(card_math)

############################ FUNKTION SECTION ############################
# FUNCTION TO FORMAT NUMBERS INTO TEXT
def format_number(n):
    n = round(float(n), 2)
    if n >= 1000000000000000000:
        if (n / 1000000000000000000) % 1 == 0:
            n = '{:.0f} quintillion'.format(n / 1000000000000000000)
        else:
            n = '{:.2f} quintillion'.format(n / 1000000000000000000)
    elif n >= 1000000000000000:
        if (n / 1000000000000000) % 1 == 0:
            n = '{:.0f} quadrillion'.format(n / 1000000000000000)
        else:
            n = '{:.2f} quadrillion'.format(n / 1000000000000000)
    elif n >= 1000000000000:
        if (n / 1000000000000) % 1 == 0:
            n = '{:.0f} trillion'.format(n / 1000000000000)
        else:
            n = '{:.2f} trillion'.format(n / 1000000000000)
    elif n >= 1000000000:
        if (n / 1000000000) % 1 == 0:
            n = '{:.0f} billion'.format(n / 1000000000)
        else:
            n = '{:.2f} billion'.format(n / 1000000000)
    elif n >= 1000000:
        if (n / 1000000) % 1 == 0:
            n = '{:.0f} million'.format(n / 1000000)
        else:
            n = '{:.2f} million'.format(n / 1000000)
    elif n >= 1000:
        if (n / 1000) % 1 == 0:
            n = '{:.0f} k'.format(n / 1000)
        else:
            n = '{:.2f} k'.format(n / 1000)
    return n

# FUNCTION TO GENERATE A RANDOM VARIABLE NAME
def generate_random_variable_name(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# FUNCTION TO DRAW A NEW FRAME
def draw():
    # SET CURRENT MUSIC STATE
    global main_music
    main_music = True

    # IMPORT & SCALE IMAGES
    wooden_bar_vertical_scaled = pygame.transform.scale(wooden_bar_vertical, (wooden_bar_width, current_window_height))
    wooden_bar_horizontal_scaled = pygame.transform.scale(wooden_bar_horizontal, (current_window_width - (x_pos_leiste + wooden_bar_width), wooden_bar_width))
    background_img_scaled = pygame.transform.scale(background_img, (current_window_width, current_window_height))
    store_background_img_scaled = pygame.transform.scale(store_background_img, (current_window_height/9*16, current_window_height))
    upgrade_store_background_img_scaled = pygame.transform.scale(upgrades_bg, (current_window_width - x_pos_upgradeBackground, y_pos_store_divider))

    # BACKGROUND
    window.blit(background_img_scaled, (0,0))

    # DRAW COOKIE HIT ANIMATION
    global new_cookie_animation
    # check for event start
    if new_cookie_animation == True:
        # generate random name
        random_variable_name = generate_random_variable_name()
        # create variable from class
        globals()[random_variable_name] = CookieHitAnimation()
        # append to list
        animated_cookies.append(globals()[random_variable_name])
        # reset event
        new_cookie_animation = False
    
    # MILK ANIMATION AND CPH BOOST
    golden_cookie.boost()

    # COOKIE
    cookie.draw()

    # check for animations
    if len(animated_cookies) != 0:
        # draw animations from list
        for animation_id in range(len(animated_cookies)):
            # oreo image
            if golden_cookie.boost_status == True:
                animated_cookies[animation_id].image = oreo
            # standard image
            else:
                animated_cookies[animation_id].image = cookie_img
            # draw
            animated_cookies[animation_id].animate()

    #GOLDEN COOKIE
    golden_cookie.draw()

    # SCORE BOARD
    score_display.draw(x_pos_score, y_pos_score)

    # MUSIC CONTROL
    theme.draw()

    # STORE BACKGROUND
    window.blit(store_background_img_scaled, (x_pos_upgradeBackground, 0))

    # CARDS
    card_index_x = 0
    card_index_y = 0
    for card in list_of_cards:
        if user.score >= card.getTotalCost():
            card.draw(card_index_x, card_index_y, solid=True)
        else:
            card.draw(card_index_x, card_index_y, solid=False)
        if card_index_x == (cards_per_row - 1):
            card_index_x = 0
            card_index_y += 1
        else:
            card_index_x += 1

        # ADD COOKIES THAT WERE MADE TROUGH UPGRADE
        user.score += card.quantity * card.cps * .025
        card.created += card.quantity * card.cps * .01

    # CURSOR STORE
    window.blit(upgrade_store_background_img_scaled, (x_pos_upgradeBackground, 0))

    # CURSORS
    cursor_index_x = 0
    cursor_index_y = 0
    for cursor in list_of_cursors:
        if cursor.quantity < 1 and cursor.checkCondition():
            if user.score >= cursor.cost:
                cursor.draw(cursor_index_x, cursor_index_y, solid=True)
            else:
                cursor.draw(cursor_index_x, cursor_index_y, solid=False)
            if cursor_index_x == (cursors_per_row - 1):
                cursor_index_x = 0
                cursor_index_y += 1
            else:
                cursor_index_x += 1

    # DIVIDERS
    window.blit(wooden_bar_vertical_scaled, (x_pos_leiste, 0))
    window.blit(wooden_bar_horizontal_scaled, (x_pos_leiste + wooden_bar_width, y_pos_store_divider))

    # NPC
    cookie_monster.draw()
    shrek_cookie.draw()

    # JUMPSCARE
    cookie_scream.draw()

    # UPDATE FRAME
    pygame.display.update()

# FUNCTION TO DRAW A NEW FRAME (INTRO)
def drawIntro():
    # SET CURRENT MUSIC STATE
    global intro_music
    intro_music = True

    # DRAW BACKGROUND
    intro_background = pygame.Surface((current_window_width, current_window_height))
    intro_background.fill((0, 0, 0))
    window.blit(intro_background, (0, 0))

    # DRAW VAPOR LOGO
    if total_frames_drawn < (FPS * 5):
        vapor_logo_scaled = pygame.transform.scale(vapor_logo, (current_window_width * 0.1, current_window_width * 0.1))
        window.blit(vapor_logo_scaled, (current_window_center[0] - vapor_logo_scaled.get_width()/2, current_window_center[1] - vapor_logo_scaled.get_height()/2))

    #DRAW CUM INC LOGO 
    elif total_frames_drawn < (FPS * 10):
        cum_inc_logo_scaled = pygame.transform.scale(cum_inc_logo, (current_window_width * 0.1, current_window_width * 0.1))
        logo_background = pygame.Surface((cum_inc_logo_scaled.get_width(), cum_inc_logo_scaled.get_height()))
        logo_background.fill((255, 255, 255))
        window.blit(logo_background, (current_window_center[0] - cum_inc_logo_scaled.get_width()/2, current_window_center[1] - cum_inc_logo_scaled.get_height()/2))
        window.blit(cum_inc_logo_scaled, (current_window_center[0] - cum_inc_logo_scaled.get_width()/2, current_window_center[1] - cum_inc_logo_scaled.get_height()/2))
    
    #DRAW TITLE
    elif total_frames_drawn < (FPS * 15):
        main_title = pygame.font.Font(None, 40)
        secondary_title = pygame.font.Font(None, 20)
        main_title_surface = main_title.render("Cookie Clicker", True, (255, 255, 255))
        secondary_title_surface = secondary_title.render("THE ORIGINAL", True, (255, 255, 255))
        
        window.blit(main_title_surface, (current_window_center[0] - main_title_surface.get_width()/2, current_window_center[1] - main_title_surface.get_height()))
        window.blit(secondary_title_surface, (current_window_center[0] - secondary_title_surface.get_width()/2, current_window_center[1] + secondary_title_surface.get_height()))
    
    #DRAW MUSICIAN
    elif total_frames_drawn < (FPS * 17):
        main_title = pygame.font.Font(None, 40)
        secondary_title = pygame.font.Font(None, 20)
        main_title_surface = main_title.render("- Music by -", True, (255, 255, 255))
        secondary_title_surface = secondary_title.render("Fesliyan Studios", True, (255, 255, 255))
        
        window.blit(main_title_surface, (current_window_center[0] - main_title_surface.get_width()/2, current_window_center[1] - main_title_surface.get_height()))
        window.blit(secondary_title_surface, (current_window_center[0] - secondary_title_surface.get_width()/2, current_window_center[1] + secondary_title_surface.get_height()))
    
    #DRAW KEYMAP
    else:
        main_title = pygame.font.Font(None, 40)
        secondary_title = pygame.font.Font(None, 20)
        row_1_surface = main_title.render("KEYMAP", True, (255, 255, 255))
        row_2_surface = secondary_title.render("LELFT MOUSE BUTTON: interact", True, (255, 255, 255))
        row_3_surface = secondary_title.render("MOUSE SCROLL: scroll trough Upgrade Store", True, (255, 255, 255))
        row_4_surface = secondary_title.render("M: mute/unmute music", True, (255, 255, 255))
        row_5_surface = secondary_title.render("T: activate Terminal debugging output", True, (255, 255, 255))
        

        window.blit(row_1_surface, (20, 20))
        window.blit(row_2_surface, (26, 50))
        window.blit(row_3_surface, (26, 70))
        window.blit(row_4_surface, (26, 90))
        window.blit(row_5_surface, (26, 110))

    # UPDATE FRAME
    pygame.display.update()

# FUNKTION TO CREATE GLOBAL VARIABLES FOR DYNAMIC LAYOUT
def createVariables(current_window_width, current_window_height, set_width_to_two):
    global card_length
    card_length = 200
    global card_height
    card_height = 280
    global total_card_length
    total_card_length = card_length + 10
    global cursor_card_length
    cursor_card_length = 100
    global cursor_card_height
    cursor_card_height = 100
    global total_cursor_card_length
    total_cursor_card_length = cursor_card_length + 10
    global x_pos_leiste
    if set_width_to_two == "TRUE":
        x_pos_leiste = current_window_width - 36 - ( total_card_length * 2 )
    elif set_width_to_two == "FALSE":
        x_pos_leiste = current_window_width * 2/3
    global x_pos_cookie
    x_pos_cookie = x_pos_leiste * 0.5
    global y_pos_cookie
    y_pos_cookie = current_window_height * 0.5
    global x_size_cookie
    x_size_cookie = x_pos_leiste * 0.4
    global x_pos_score
    x_pos_score = x_pos_leiste * 0.5
    global y_pos_score
    y_pos_score = current_window_height * 0.1
    global wooden_bar_width
    wooden_bar_width = current_window_width * 0.01
    global y_pos_store_divider
    y_pos_store_divider = current_window_height * 0.25
    global x_pos_store
    x_pos_store = x_pos_leiste + wooden_bar_width * 2
    global y_pos_store
    y_pos_store = (- relative_scroll[1] * 20) + y_pos_store_divider + wooden_bar_width*2
    global x_pos_upgradeBackground
    x_pos_upgradeBackground = x_pos_leiste + wooden_bar_width
    global store_width
    store_width = current_window_width - x_pos_upgradeBackground
    global cards_per_row
    cards_per_row = math.floor(store_width / total_card_length)
    global card_rows
    card_rows = math.ceil(len(list_of_cards) / cards_per_row)
    global cursors_per_row
    cursors_per_row = math.floor(store_width / total_cursor_card_length)
    global x_pos_music_play_pause
    x_pos_music_play_pause = 30
    global y_pos_music_play_pause
    y_pos_music_play_pause = 30
    global x_size_music_play_pause
    x_size_music_play_pause = 30
    global current_window_center
    current_window_center = [current_window_width/2, current_window_height/2]
    global y_pos_npc_dialog
    y_pos_npc_dialog = current_window_height * 2/3
    global npc_dialog_height
    npc_dialog_height = current_window_height * 1/3
    global npc_dialog_text_pos
    npc_dialog_text_pos = abs(y_pos_npc_dialog - current_window_height)/2
    global milk_count
    milk_count = 4
    global milk_build
    milk_build = milk_count + 1
    global milk_width
    milk_width = x_pos_leiste / milk_count
    global milk_pos
    milk_pos = (milk_pos[0] + milk_width/FPS, milk_pos[1])

# INTRO MUSIC
def playIntroMusic():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('CookieClicker/audio/8-Bit_Intro.mp3')
    pygame.mixer.music.play(0)

# MAIN GAME MUSIC
def playMainMusic():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('CookieClicker/audio/8-Bit_Game.mp3')
    pygame.mixer.music.play(-1)

# STANDARD HIT SOUND
def hitSound():
    pygame.mixer.Sound.play(key_press, 0)

# SOUND MIXER
pygame.mixer.Sound.set_volume(awm, 0.3)
pygame.mixer.Sound.set_volume(hog_rider, 0.3)
pygame.mixer.Sound.set_volume(upgrade_sound, 1)
pygame.mixer.Sound.set_volume(golden_cookie_sound, 1)

############################ MAIN LOOP SECTION ############################
# SETUP MAIN-LOOP
main = True

# CONTROLL GAME
global intro_music
intro_music = False
global main_music
main_music = False
global intro
intro = True

# INITIAL VARIABLE SETUP
FPS = 60
Clock = pygame.time.Clock()
global relative_scroll
relative_scroll = [0, 0]
global mouse_pos
mouse_pos = 0
global data
data = False
music = False
global total_frames_drawn
total_frames_drawn = 0
global current_cursor
current_cursor = -1
global milk_pos
milk_pos = (0, 0)
global new_cookie_animation
new_cookie_animation = False
global animated_cookies
animated_cookies = []

# START MAIN-LOOP
while main == True:
    # FPS / Delay
    Clock.tick(FPS)

    # GET WINDOW SIZE
    current_window_width = pygame.display.get_surface().get_width()
    current_window_height = pygame.display.get_surface().get_height()

    # CREATE VARIABLES FOR DYNAMIC LAYOUT
    set_width_to_two = "FALSE"
    createVariables(current_window_width, current_window_height, set_width_to_two)
    if cards_per_row < 2:
        set_width_to_two = "TRUE"
        createVariables(current_window_width, current_window_height, set_width_to_two)

    # INTRO
    if total_frames_drawn < (FPS * 30) and intro == True:
        # START MUSIC
        if intro_music == False:
            playIntroMusic()

        # EVENT LISTENERS
        for event in pygame.event.get():
            # MOUSE-CLICK -- LINKE MOUSTASTE
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
            # EXIT BUTTON
            if event.type == pygame.QUIT:
                main = False

        # DRAW FRAME
        drawIntro()
    # GAME
    else:
        # SRART MUSIC
        if main_music == False:
            playMainMusic()

        # EVENT LISTENERS
        for event in pygame.event.get():
            
            # MOUSE-CLICK -- LINKE MOUSTASTE
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                # HIT COOKIE
                if cookie.collidepoint():
                    if current_cursor >= 0:
                        list_of_cursors[current_cursor].hitSound()
                    else:
                        hitSound()
                    user.score += user.total_cph
                    cookie.animation_state = 1
                    cookie.hit = True
                    cookie.starting_frame = total_frames_drawn
                    new_cookie_animation = True
                
                # HIT GOLDEN COOKIE
                if golden_cookie.collidepoint(mouse_pos):
                    golden_cookie.boost_status = True
                    golden_cookie.boost_starting_frame = total_frames_drawn
                    pygame.mixer.Sound.set_volume(golden_cookie_sound, 1)
                    pygame.mixer.Sound.play(golden_cookie_sound, 0)
                    golden_cookie.action = False

                # HIT CURSOR CARD
                cursor_id = 0
                for cursor in list_of_cursors:
                    if cursor.checkCondition():
                        if cursor.collidepoint(mouse_pos) and user.score >= cursor.cost and cursor.quantity < 1:
                            cursor.setCursor()
                            cursor.hitSound()
                            user.score -= cursor.cost
                            cursor.quantity += 1
                            user.updateTotalCPH()
                            current_cursor = cursor_id
                    cursor_id +=1

                # HIT CARD
                for card in list_of_cards:
                    if card.collidepoint(mouse_pos) and user.score >= card.getTotalCost() and card.quantity < card.max_card_count:
                        card.upgradeSound()
                        user.score -= card.getTotalCost()
                        card.quantity += 1
                        user.updateTotalCPS()

                # Hit PAUSE AND PLAY
                if theme.collidepoint(mouse_pos) and music == True:
                    pygame.mixer.music.pause()
                    theme.play = False
                    music = False
                elif theme.collidepoint(mouse_pos) and music == False :
                    pygame.mixer.music.unpause()
                    theme.play = True
                    music = True
            
            # MOUSE-SCROLL
            if event.type == pygame.MOUSEWHEEL:
                relative_scroll[0] += event.x
                relative_scroll[1] -= event.y
                if relative_scroll[1] < 0:
                    relative_scroll[1] = 0
                elif relative_scroll[1] > (card_rows * (card_height + 10))/20:
                    relative_scroll[1] = (card_rows * (card_height + 10))/20

            # INPUT DATA TO CONSOLE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                if data == True:
                    data = False
                else:
                    data = True

            # HIDDEN FUNCTION TO INCREASE USER-SCORE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                user.score += 1000000
            
            # MUTE AUDIO VIA "M" KEY
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m and music == True:
                pygame.mixer.music.pause()
                theme.play = False
                music = False
            # UNMUTE AUDIO VIA "M" KEY
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m and music == False :
                pygame.mixer.music.unpause()
                theme.play = True
                music = True

            # EXIT BUTTON
            if event.type == pygame.QUIT:
                main = False
        
        # DRAW NPC UNDER CONDITION
        if user.cps >= 100 and cookie_monster.was_activ == False:
            cookie_monster.NPC_pop = True
            cookie_monster.was_activ = True

        if user.cps >= 1000 and shrek_cookie.was_activ == False:
            shrek_cookie.NPC_pop = True
            shrek_cookie.was_activ = True

        # DRAW JUMPSCARE UNDER CONDITION
        if user.cps > 666:
            cookie_scream.action = True

        # DRAW GOLDEN_COOKIE AND DEFINE FREQUENCY
        if random.randint(0, 1000) == 1 and golden_cookie.boost_status == False:
            golden_cookie.action = True
                
        # DRAW NEW FRAME
        draw()
    
    # TERMINAL OUTPUT OF SENSORS
    if data == True:
        print(pygame.mouse.get_pos(), relative_scroll)

    # TOTAL FRAMES DRAWN
    total_frames_drawn +=1
    
    # SCORE TO/FROM FILE
    # read highscore
    high_score_file_read = open("CookieClicker/files/highscore.txt", "r")
    # check if current score is higher than saved highscore
    if float(high_score_file_read.read()) < user.score:
        # write current score as highscore
        high_score_file_write = open("CookieClicker/files/highscore.txt", "w")
        high_score_file_write.write(str(user.score))
        high_score_file_write.close()
    # write current score as last score
    last_score_file_write = open("CookieClicker/files/last_score.txt", "w")
    last_score_file_write.write(str(user.score))

# EXIT
pygame.quit()
sys.exit()