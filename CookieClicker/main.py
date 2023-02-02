# IMPORT LIBRARIES
import pygame
import sys
import math
import random

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
cookie_img = pygame.image.load('CookieClicker/images/keks.png')
upgrades_bg = pygame.image.load('CookieClicker/images/black.jpg')
leiste = pygame.image.load('CookieClicker/images/leiste.png')
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
chocolate_milk = pygame.image.load('CookieClicker/images/chocolate_milk.png')
milk = pygame.image.load('CookieClicker/images/milk.png')
black_fade_full = pygame.image.load('CookieClicker/images/black_fade_full.png')
black_fade_half = pygame.image.load('CookieClicker/images/black_fade_half.png')

# IMPORT AUDIO
awm = pygame.mixer.Sound('CookieClicker/audio/awm.mp3')
upgrade_sound = pygame.mixer.Sound('CookieClicker/audio/8-Bit_Upgrade-Sound.mp3')
golden_cookie_sound = pygame.mixer.Sound('CookieClicker/audio/8-Bit_Golden-Cookie-Sound.mp3')
key_press = pygame.mixer.Sound('CookieClicker/audio/key_press.mp3')
cookie_monster_sound = pygame.mixer.Sound('CookieClicker/audio/Hom_nom_nom_nom_nom.mp3')
jumpscare_cookie_scream = pygame.mixer.Sound('CookieClicker/audio/jumpscare_cookie_scream.mp3')

# SET DEFAULT COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)
GREEN = (198, 134, 123)
BLUE = (51, 60, 75)

# STANDARD CURSOR SETUP
#
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

class MainCookie:
    # INITIAL SETUP OF COOKIE
    def __init__(self, x_pos_cookie, y_pos_cookie, x_size_cookie):
        self.x = x_pos_cookie
        self.y = y_pos_cookie
        self.length = x_size_cookie
        self.height = x_size_cookie

        self.animation_state = 0

    # DRAW COOKIE
    def draw(self):
        # ANIMATINION STATES
        # while hit
        if self.animation_state > 0:
            cookie_img_scaled = pygame.transform.scale(cookie_img, ( int(1.1*x_size_cookie), int(1.1*x_size_cookie) ))
            window.blit(cookie_img_scaled, (cookie_img_scaled.get_rect(center =( x_pos_cookie, y_pos_cookie) )))
            self.animation_state -= 1
        # default
        else:
            cookie_img_scaled = pygame.transform.scale(cookie_img, ( int(1*x_size_cookie), int(1*x_size_cookie) ))
            window.blit(cookie_img_scaled, (cookie_img_scaled.get_rect(center =( x_pos_cookie, y_pos_cookie) )))

    # DEFINING COLLIDER / HITBOX
    def collidepoint(self, mouse_pos):
        return pygame.Rect(x_pos_cookie-x_size_cookie/2, y_pos_cookie-x_size_cookie/2, x_size_cookie, x_size_cookie).collidepoint(mouse_pos)

class ScoreDisplay():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 100
        self.height = 100

    def draw(self, x_pos_score, y_pos_score):
        font = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 24)
        small_font = pygame.font.Font('CookieClicker/Font/Kavoon-Regular.ttf', 26)

        SCORE = small_font.render('{} cookies'.format(format_number ( int(user.score))), True, WHITE)
        CPS = font.render('per second: {}'.format(format_number ( user.cps)), True, WHITE)
        window.blit(SCORE, (SCORE.get_rect( center=( int(x_pos_score), int(y_pos_score) ) )))
        window.blit(CPS, (CPS.get_rect(center=(int(x_pos_score), int(y_pos_score)+20 ) )))
class card:
    # INITIAL STATIC SETUP OF CARD (TEMPORARILY)
    def __init__(self, name, index_x, index_y, image, base_cost, increase_per_purchase, cps):
        self.name = name
        self.cursor = cursor
        self.index_x = index_x
        self.index_y = index_y
        self.length = 200
        self.height = 280

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

        # DRAW TO SCREEN
        window.blit(self.image, (pos_x, pos_y))
        window.blit(cost, (pos_x + 160 - cost_length, pos_y + self.height -40))
        window.blit(quantity, (pos_x + 170 - quantity_length, pos_y + 7))
        window.blit(black_overlay_scaled, (pos_x, pos_y))

class cursor:
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

class Player:
    # INITIAL SETUP OF PLAYER
    def __init__(self):
        self.score = float(0)
        self.click_multiplier = 1
        # cookies per second (AUTOMATICALLY GENERATED COOKIES)
        self.cps = float(0)
        # cookies per hit (MANUALLY GENERATED COOKIES)
        self.cph = 1

    #  UPDATE THE TOTAL CLICKS-PER-SECOND
    def updateTotalCPS(self, list_of_cards):
        self.cps = 0
        for card in list_of_cards:
            self.cps += card.cps * card.quantity
    
    #  UPDATE THE TOTAL CLICKS-PER-SECOND
    def updateTotalCPH(self, list_of_cursors):
        self.cph = 0
        for card in list_of_cursors:
            self.cph += card.cph * card.quantity

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
        self.display_dialog_speed = current_window_height * 0.02

        npc_dialog_black_scaled = pygame.transform.scale(npc_dialog_black, (x_pos_leiste, npc_dialog_height))
        npc_dialog_black_scaled.set_alpha(200)            
        npc_dialog_white_top = pygame.transform.scale(npc_dialog_white, (x_pos_leiste, 15))
        npc_dialog_white_bottom = pygame.transform.scale(npc_dialog_white, (15, npc_dialog_height))
        npc_in = pygame.transform.scale(self.NPC_pic_in, (npc_dialog_height, npc_dialog_height))
        npc_out = pygame.transform.scale(self.NPC_pic_out, (npc_dialog_height, npc_dialog_height))

        dialog_text = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 20)
        dialog_text_rendert = dialog_text.render(self.text, True, (255, 255, 255))

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

        if self.NPC_pop_stay == True:
            if self.time == 0 and self.sound != None:
                pygame.mixer.Sound.set_volume(self.sound, self.NPC_audio_volume)
                pygame.mixer.Sound.play(self.sound, 1)

            window.blit(npc_in, (0, y_pos_npc_dialog * 0.5))
            window.blit(npc_dialog_black_scaled, (0, y_pos_npc_dialog))
            window.blit(npc_dialog_white_top, (0, y_pos_npc_dialog - 15))
            window.blit(npc_dialog_white_bottom, (x_pos_leiste - 15, y_pos_npc_dialog))
            window.blit(dialog_text_rendert, (dialog_text_rendert.get_rect(center =(x_pos_leiste/2, current_window_height - npc_dialog_text_pos))))
            self.time += Clock.get_time()

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

class Jumpscare ():
    def __init__(self, pic, time_shown, sound, volume):
        self.action = False
        self.jumpscare_pic = pic
        self.time = time_shown
        self.sound = sound
        self.audio_volume = volume

        self.once_activ = False
        self.timer = 0

    def draw(self):
        jumpscare_pic_scaled = pygame.transform.scale(self.jumpscare_pic, (current_window_height, current_window_height))

        if self.action == True and self.timer < self.time:
            self.timer += 1
            window.blit(jumpscare_pic_scaled, (jumpscare_pic_scaled.get_rect(center =( current_window_center) )))
            if self.once_activ == False:
                pygame.mixer.Sound.set_volume(self.sound, self.audio_volume)
                pygame.mixer.Sound.play(self.sound, 0)
                self.once_activ = True

class golden_cookie ():
    def __init__(self):
        self.action = False
        self.random_pos = 0
        self.random_speed = 0
        self.counter = 0

    def collidepoint(self, mouse_pos):
        return pygame.Rect(self.random_pos, self.counter, x_size_cookie*0.1, x_size_cookie*0.1).collidepoint(mouse_pos)

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

# SETUP COOKIE (ONLY TEMPORARY VALUES FOR POSITION AND SIZE)
cookie = MainCookie(300, 240, 200)

# SETUP SCORE-BOARD (ONLY TEMPORARY VALUES FOR POSITION AND SIZE)
score_display = ScoreDisplay(360, 0)

# SETUP PLAYER
user = Player()

# SETUP MUSIC
theme = Music()

# SETUP NPC 
cookie_monster = NPC("You have got some cookies there, may I have some?", npc_cookie_monster, npc_cookie_monster_cookies, cookie_monster_sound, 0.3)
shrek_cookie = NPC("Eyyyy what are you doing? You can not use those!", npc_shrek_cookie, npc_shrek_cookie, None, None )

# SETUP JUMPSCARE
cookie_scream = Jumpscare(jumpscare_cookie, 200, jumpscare_cookie_scream, 1)

# SETUP GOLDEN_COOKIE
golden_cookie_objekt = golden_cookie()

# SET UPGRADE-STORE POSITION (ONLY TEMPORARY VALUES)
store_y = 20
store_x = 830

# CREATE CARDS FROM CLASS
# create list
list_of_cards = []
########################################################################
# ROW1 : get image
# ROW2 : create card from class, set values
# ROW3 : append to list
########################################################################
# NORMAL CARDS
card_slaves_img = pygame.image.load('CookieClicker/images/card_slaves.png')
card_slaves = card("Slaves", 0, 0 , card_slaves_img, base_cost=15, increase_per_purchase=1.15, cps=0.1)
list_of_cards.append(card_slaves)

card_turbo_img = pygame.image.load('CookieClicker/images/card_turbo.png')
card_turbo = card("Turbo", 0, 0 , card_turbo_img, base_cost=100, increase_per_purchase=1.15, cps=1)
list_of_cards.append(card_turbo)

card_chump_hat_img = pygame.image.load('CookieClicker/images/card_chump_hat.png')
card_chump_hat = card("Chump Hat", 0, 0 , card_chump_hat_img, base_cost=1100, increase_per_purchase=1.15, cps=8)
list_of_cards.append(card_chump_hat)

card_nuclearreactor_img = pygame.image.load('CookieClicker/images/card_nuclearreactor.png')
card_nuclearreactor = card("Nuclear Reactor", 0, 0 , card_nuclearreactor_img, base_cost=12000, increase_per_purchase=1.15, cps=47)
list_of_cards.append(card_nuclearreactor)

card_nestle_img = pygame.image.load('CookieClicker/images/card_nestle.png')
card_nestle = card("Nestle", 0, 0 , card_nestle_img, base_cost=130000, increase_per_purchase=1.15, cps=260)
list_of_cards.append(card_nestle)

card_oil_img = pygame.image.load('CookieClicker/images/card_oil.png')
card_oil = card("Oil", 0, 0 , card_oil_img, base_cost=1400000, increase_per_purchase=1.15, cps=1400)
list_of_cards.append(card_oil)

card_cookie_collector_img = pygame.image.load('CookieClicker/images/card_cookie_collector.png')
card_cookie_collector = card("Cookie Collector", 0, 0 , card_cookie_collector_img, base_cost=20000000, increase_per_purchase=1.15, cps=7800)
list_of_cards.append(card_cookie_collector)

card_cookie_drill_img = pygame.image.load('CookieClicker/images/card_cookie_drill.png')
card_cookie_drill = card("Cookie Drill", 0, 0 , card_cookie_drill_img, base_cost=330000000, increase_per_purchase=1.15, cps=44000)
list_of_cards.append(card_cookie_drill)

card_cookie_mine_img = pygame.image.load('CookieClicker/images/card_cookie_mine.png')
card_cookie_mine = card("Cookie Mine", 0, 0 , card_cookie_mine_img, base_cost=5100000000, increase_per_purchase=1.15, cps=260000)
list_of_cards.append(card_cookie_mine)
########################################################################
list_of_cursors = []
# CURSORS
cursor_wooden_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_wooden_pickaxe.png')
cursor_wooden_pickaxe = cursor("Wooden Pickaxe", 0, 0 , cursor_wooden_pickaxe_img, cost=100, cph=2, condition_id=0, sound=key_press)
list_of_cursors.append(cursor_wooden_pickaxe)

cursor_golden_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_golden_pickaxe.png')
cursor_golden_pickaxe = cursor("Golden Pickaxe", 0, 0 , cursor_golden_pickaxe_img, cost=500, cph=8, condition_id=1, sound=key_press)
list_of_cursors.append(cursor_golden_pickaxe)

cursor_diamond_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_diamond_pickaxe.png')
cursor_diamond_pickaxe = cursor("Diamond Pickaxe", 0, 0 , cursor_diamond_pickaxe_img, cost=10000, cph=69, condition_id=2, sound=key_press)
list_of_cursors.append(cursor_diamond_pickaxe)

cursor_netherite_pickaxe_img = pygame.image.load('CookieClicker/images/cursor_netherite_pickaxe.png')
cursor_netherite_pickaxe = cursor("Netherite Pickaxe", 0, 0 , cursor_netherite_pickaxe_img, cost=1000000, cph=112, condition_id=3, sound=key_press)
list_of_cursors.append(cursor_netherite_pickaxe)

cursor_scope_img = pygame.image.load('CookieClicker/images/scope.png')
cursor_scope = cursor("AWM", 0, 0 , cursor_scope_img, cost=10000000, cph=1000, condition_id=4, sound=awm)
list_of_cursors.append(cursor_scope)
########################################################################
# DEBUFFS
card_bad_code_img = pygame.image.load('CookieClicker/images/card_bad_code.png')
card_bad_code = card("Bad Code", 0, 0 , card_bad_code_img, base_cost=15, increase_per_purchase=1.15, cps=1)
# CURRENTLY NOT IMPLEMENTED
# list_of_cards.append(card_bad_code)

card_teachers_dream_img = pygame.image.load('CookieClicker/images/card_teachers_dream.png')
card_teachers_dream = card("Teachers Dream", 0, 0 , card_teachers_dream_img, base_cost=15, increase_per_purchase=1.15, cps=1)
# CURRENTLY NOT IMPLEMENTED
# list_of_cards.append(card_teachers_dream)

# FUNCTION TO FORMAT NUMBERS INTO TEXT
def format_number(n):
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

    # COOKIE
    cookie.draw()

    #GOLDEN COOKIE
    golden_cookie_objekt.draw()

    # SCORE BOARD
    score_display.draw(x_pos_score, y_pos_score)

    # MUSIC CONTROL
    theme.draw()

    # NPC
    cookie_monster.draw()
    shrek_cookie.draw()

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

    if total_frames_drawn < (FPS * 5):
        # DRAW VAPOR LOGO
        vapor_logo_scaled = pygame.transform.scale(vapor_logo, (current_window_width * 0.1, current_window_width * 0.1))
        window.blit(vapor_logo_scaled, (current_window_center[0] - vapor_logo_scaled.get_width()/2, current_window_center[1] - vapor_logo_scaled.get_height()/2))
    elif total_frames_drawn < (FPS * 10):
        cum_inc_logo_scaled = pygame.transform.scale(cum_inc_logo, (current_window_width * 0.1, current_window_width * 0.1))
        logo_background = pygame.Surface((cum_inc_logo_scaled.get_width(), cum_inc_logo_scaled.get_height()))
        logo_background.fill((255, 255, 255))
        window.blit(logo_background, (current_window_center[0] - cum_inc_logo_scaled.get_width()/2, current_window_center[1] - cum_inc_logo_scaled.get_height()/2))
        window.blit(cum_inc_logo_scaled, (current_window_center[0] - cum_inc_logo_scaled.get_width()/2, current_window_center[1] - cum_inc_logo_scaled.get_height()/2))
    elif total_frames_drawn < (FPS * 15):
        main_title = pygame.font.Font(None, 40)
        secondary_title = pygame.font.Font(None, 20)
        main_title_surface = main_title.render("Cookie Clicker", True, (255, 255, 255))
        secondary_title_surface = secondary_title.render("THE ORIGINAL", True, (255, 255, 255))
        
        window.blit(main_title_surface, (current_window_center[0] - main_title_surface.get_width()/2, current_window_center[1] - main_title_surface.get_height()))
        window.blit(secondary_title_surface, (current_window_center[0] - secondary_title_surface.get_width()/2, current_window_center[1] + secondary_title_surface.get_height()))
    elif total_frames_drawn < (FPS * 17):
        main_title = pygame.font.Font(None, 40)
        secondary_title = pygame.font.Font(None, 20)
        main_title_surface = main_title.render("- Music by -", True, (255, 255, 255))
        secondary_title_surface = secondary_title.render("Fesliyan Studios", True, (255, 255, 255))
        
        window.blit(main_title_surface, (current_window_center[0] - main_title_surface.get_width()/2, current_window_center[1] - main_title_surface.get_height()))
        window.blit(secondary_title_surface, (current_window_center[0] - secondary_title_surface.get_width()/2, current_window_center[1] + secondary_title_surface.get_height()))
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

def createVariables(current_window_width, current_window_height, set_width_to_two):
    # CREATING GLOBAL VARIABLES FOR DYNAMIC LAYOUT
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

# UPGRADE SOUND
def upgradeSound():
    pygame.mixer.Sound.play(upgrade_sound, 0)

# STANDARD HIT SOUND
def hitSound():
    pygame.mixer.Sound.play(key_press, 0)

# SOUND MIXER
pygame.mixer.Sound.set_volume(awm, 0.3)
pygame.mixer.Sound.set_volume(upgrade_sound, 1)
pygame.mixer.Sound.set_volume(golden_cookie_sound, 1)

# SETUP MAIN-LOOP
main = True
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
global intro_music
intro_music = False
global main_music
main_music = False
global intro
intro = False
global current_cursor
current_cursor = -1

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

    # DRAW FRAME
    #
    # intro
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
    # game
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
                if cookie.collidepoint(mouse_pos):
                    if current_cursor >= 0:
                        list_of_cursors[current_cursor].hitSound()
                    else:
                        hitSound()
                    user.score += user.cph
                    cookie.animation_state = 1
                
                # HIT GOLDEN COOKIE
                if golden_cookie_objekt.collidepoint(mouse_pos):
                    user.score += user.score
                    pygame.mixer.Sound.set_volume(golden_cookie_sound, 1)
                    pygame.mixer.Sound.play(golden_cookie_sound, 0)
                    golden_cookie_objekt.action = False

                # HIT CURSOR CARD
                cursor_id = 0
                for _cursor in list_of_cursors:
                    if _cursor.checkCondition():
                        if _cursor.collidepoint(mouse_pos) and user.score >= _cursor.cost and _cursor.quantity < 1:
                            _cursor.setCursor()
                            upgradeSound()
                            user.score -= _cursor.cost
                            _cursor.quantity += 1
                            user.updateTotalCPH(list_of_cursors)
                            current_cursor = cursor_id
                    cursor_id +=1

                # HIT CARD
                for _card in list_of_cards:
                    if _card.collidepoint(mouse_pos) and user.score >= _card.getTotalCost() and _card.quantity < _card.max_card_count:
                        upgradeSound()
                        user.score -= _card.getTotalCost()
                        _card.quantity += 1
                        user.updateTotalCPS(list_of_cards)

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
            
            # MUTE AUDIO
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m and music == True:
                pygame.mixer.music.pause()
                theme.play = False
                music = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m and music == False :
                pygame.mixer.music.unpause()
                theme.play = True
                music = True

            # EXIT BUTTON
            if event.type == pygame.QUIT:
                main = False
        
        # DRAW NPC
        if user.cps >= 100 and cookie_monster.was_activ == False:
            cookie_monster.NPC_pop = True
            cookie_monster.was_activ = True

        if user.cps >= 1000 and shrek_cookie.was_activ == False:
            shrek_cookie.NPC_pop = True
            shrek_cookie.was_activ = True

        # DRAW JUMPSCARE
        if user.cps > 666:
            cookie_scream.action = True

        # DRAW GOLDEN_COOKIE
        if random.randint(0, 1000) == 1:
            golden_cookie_objekt.action = True
                
        # DRAW NEW FRAME
        draw()
    
    if data == True:
        print(pygame.mouse.get_pos(), relative_scroll)

    # CLEAR EVENT QUEUE (INACTIVE DUE TO READOUT ERROR)
    # pygame.event.clear()

    # TOTAL FRAMES DRAWN
    total_frames_drawn +=1

pygame.quit()
sys.exit()