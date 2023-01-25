# IMPORT LIBRARIES
import pygame
import pygame_menu
import sys
import math
from playsound import playsound
import threading

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
background_img = pygame.image.load('CookieClicker/images/grey.jpg')
cookie_img = pygame.image.load('CookieClicker/images/keks.png')
upgrades_bg = pygame.image.load('CookieClicker/images/black.jpg')
leiste = pygame.image.load('CookieClicker/images/leiste.png')
audio_play_img = pygame.image.load('CookieClicker/images/play.png')
audio_pause_img = pygame.image.load('CookieClicker/images/pause.png')


# IMPORT AUDIO
awm = pygame.mixer.Sound('CookieClicker/audio/awm.mp3')
upgrade_sound = pygame.mixer.Sound('CookieClicker/audio/8-Bit_Upgrade-Sound.mp3')
key_press = pygame.mixer.Sound('CookieClicker/audio/key_press.mp3')

# SET DEFAULT COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)
GREEN = (0, 255, 0)
BLUE = (51, 90, 144)

# CUSTOM CURSOR SETUP
#
# import img
custom_default_cursor_img = pygame.image.load('CookieClicker/images/custom_default_cursor.png').convert()
# scale img
custom_default_cursor_img =pygame.transform.scale(custom_default_cursor_img, (20, 20))
# black to transparent
custom_default_cursor_img.set_colorkey((0, 0, 0))
# set cursor
cursor = pygame.cursors.Cursor((8, 0), custom_default_cursor_img)
pygame.mouse.set_cursor(cursor)

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

        SCORE = small_font.render('{} cookies'.format(format_number ( int(user.score) )), True, WHITE)
        CPS = font.render('per second: {}'.format(int(user.cps)), True, WHITE)
        window.blit(SCORE, (SCORE.get_rect( center=( int(x_pos_score), int(y_pos_score) ) )))
        window.blit(CPS, (CPS.get_rect(center=(int(x_pos_score), int(y_pos_score)+20 ) )))
class card:
    # INITIAL STATIC SETUP OF CARD (TEMPORARILY)
    def __init__(self, name, index_x, index_y, image, base_cost, increase_per_purchase, cps):
        self.name = name
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

        # SET / CHECK: PARTIALLY TRANSLUCENT
        if solid == False:
            self.image.set_alpha(100)
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
        window.blit(cost, (pos_x + 170 - cost_length, pos_y + 10))
        window.blit(quantity, (pos_x + self.length -45 - quantity_length, pos_y + self.height -47))

class Player:
    # INITIAL SETUP OF PLAYER
    def __init__(self):
        self.score = 0
        self.click_multiplier = 1
        self.cps = 0

    #  UPDATE THE TOTAL CLICKS-PER-SECOND
    def updateTotalCPS(self, list_of_cards):
        self.cps = 0
        for card in list_of_cards:
            self.cps += card.cps * card.quantity

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


# SETUP COOKIE (ONLY TEMPORARY VALUES FOR POSITION AND SIZE)
cookie = MainCookie(300, 240, 200)

# SETUP SCORE-BOARD (ONLY TEMPORARY VALUES FOR POSITION AND SIZE)
score_display = ScoreDisplay(360, 0)

# SETUP PLAYER
user = Player()

# SETUP MUSIC
theme = Music()

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
card_slaves = card("Slaves", 0, 0 , card_slaves_img, base_cost=15, increase_per_purchase=1.15, cps=1)
list_of_cards.append(card_slaves)

card_turbo_img = pygame.image.load('CookieClicker/images/card_turbo.png')
card_turbo = card("Turbo", 0, 0 , card_turbo_img, base_cost=100, increase_per_purchase=1.15, cps=20)
list_of_cards.append(card_turbo)

card_chump_hat_img = pygame.image.load('CookieClicker/images/card_chump_hat.png')
card_chump_hat = card("Chump Hat", 0, 0 , card_chump_hat_img, base_cost=1100, increase_per_purchase=1.15, cps=300)
list_of_cards.append(card_chump_hat)

card_nuclearreactor_img = pygame.image.load('CookieClicker/images/card_nuclearreactor.png')
card_nuclearreactor = card("Nuclear Reactor", 0, 0 , card_nuclearreactor_img, base_cost=12000, increase_per_purchase=1.15, cps=3000)
list_of_cards.append(card_nuclearreactor)
########################################################################
# PICKAXES
card_wooden_pickaxe_img = pygame.image.load('CookieClicker/images/card_wooden_pickaxe.png')
card_wooden_pickaxe = card("Wooden Pickaxe", 0, 0 , card_wooden_pickaxe_img, base_cost=130000, increase_per_purchase=1.15, cps=20000)
list_of_cards.append(card_wooden_pickaxe)

card_golden_pickaxe_img = pygame.image.load('CookieClicker/images/card_golden_pickaxe.png')
card_golden_pickaxe = card("Golden Pickaxe", 0, 0 , card_golden_pickaxe_img, base_cost=1400000, increase_per_purchase=1.15, cps=100000)
list_of_cards.append(card_golden_pickaxe)

card_diamond_pickaxe_img = pygame.image.load('CookieClicker/images/card_diamond_pickaxe.png')
card_diamond_pickaxe = card("Diamond Pickaxe", 0, 0 , card_diamond_pickaxe_img, base_cost=20000000, increase_per_purchase=1.15, cps=3000000)
list_of_cards.append(card_diamond_pickaxe)

card_netherite_pickaxe_img = pygame.image.load('CookieClicker/images/card_netherite_pickaxe.png')
card_netherite_pickaxe = card("Netherite Pickaxe", 0, 0 , card_netherite_pickaxe_img, base_cost=330000000, increase_per_purchase=1.15, cps=20000000)
list_of_cards.append(card_netherite_pickaxe)
########################################################################
# DEBUFFS
card_bad_code_img = pygame.image.load('CookieClicker/images/card_bad_code.png')
card_bad_code = card("Bad Code", 0, 0 , card_bad_code_img, base_cost=15, increase_per_purchase=1.15, cps=1)
list_of_cards.append(card_bad_code)

card_teachers_dream_img = pygame.image.load('CookieClicker/images/card_teachers_dream.png')
card_teachers_dream = card("Teachers Dream", 0, 0 , card_teachers_dream_img, base_cost=15, increase_per_purchase=1.15, cps=1)
list_of_cards.append(card_teachers_dream)

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
    return n

# FUNCTION TO DRAW A NEW FRAME
def draw():
    # SET CURRENT MUSIC STATE
    global main_music
    main_music = True

    # BACKGROUND AND DIVIDER
    window.blit(background_img, (0,0))
    window.blit(upgrades_bg, (x_pos_upgradeBackground, 0))
    window.blit(leiste, (x_pos_leiste, 0))

    # COOKIE
    cookie.draw()

    # SCORE BOARD
    score_display.draw(x_pos_score, y_pos_score)

    # MUSIC CONTROL
    theme.draw()

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
        row_4_surface = secondary_title.render("T: activate Terminal debugging output", True, (255, 255, 255))
        

        window.blit(row_1_surface, (20, 20))
        window.blit(row_2_surface, (26, 50))
        window.blit(row_3_surface, (26, 70))
        window.blit(row_4_surface, (26, 90))

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
    global x_pos_leiste
    if set_width_to_two == "TRUE":
        x_pos_leiste = current_window_width - 36 - ( total_card_length * 2 )
    elif set_width_to_two == "FALSE":
        x_pos_leiste = current_window_width * 2/3
    global x_pos_upgradeBackground
    x_pos_upgradeBackground = x_pos_leiste + 10
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
    global x_pos_store
    x_pos_store = x_pos_leiste + 36
    global y_pos_store
    y_pos_store = 20 - (relative_scroll[1] * 20)
    global store_width
    store_width = current_window_width - x_pos_upgradeBackground
    global cards_per_row
    cards_per_row = math.floor(store_width / total_card_length)
    global x_pos_music_play_pause
    x_pos_music_play_pause = 30
    global y_pos_music_play_pause
    y_pos_music_play_pause = 30
    global x_size_music_play_pause
    x_size_music_play_pause = 30
    global current_window_center
    current_window_center = [current_window_width/2, current_window_height/2]

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

# HIT SOUND
def hitSound():
    pygame.mixer.Sound.play(key_press, 0)

# UPGRADE SOUND
def upgradeSound():
    pygame.mixer.Sound.play(upgrade_sound, 0)

# SOUND MIXER
pygame.mixer.Sound.set_volume(awm, 0.3)
pygame.mixer.Sound.set_volume(upgrade_sound, 1)


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
    if total_frames_drawn < (FPS * 30):
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
                    hitSound()
                    user.score += 1
                    cookie.animation_state = 1

                # HIT CARD
                for card in list_of_cards:
                    if card.collidepoint(mouse_pos) and user.score >= card.getTotalCost() and card.quantity < card.max_card_count:
                        upgradeSound()
                        user.score -= card.getTotalCost()
                        card.quantity += 1
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
            
            if event.type == pygame.KEYDOWN and pygame.K_t:
                if data == True:
                    data = False
                else:
                    data = True

            # EXIT BUTTON
            if event.type == pygame.QUIT:
                main = False
                
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