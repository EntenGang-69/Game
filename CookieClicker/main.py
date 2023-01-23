import pygame
import sys
import math

pygame.init()

window_height = 420
window_length = window_height/9*16
window = pygame.display.set_mode((window_length, window_height), pygame.RESIZABLE, pygame.SCALED)
current_window_width, _ = pygame.display.get_surface().get_size()

background_img = pygame.image.load('CookieClicker/images/grey.jpg')

cookie_img = pygame.image.load('CookieClicker/images/keks.png')

'''cards'''
<<<<<<< HEAD
# turbo = pygame.image.load('CookieClicker/images/turbo.png')
# bardello = pygame.image.load('CookieClicker/images/bardello.png')
# slaves = pygame.image.load('CookieClicker/images/slaves.png')
# chump_hat = pygame.image.load('CookieClicker/images/chump_hat.png')
# nuclear_reactor = pygame.image.load('CookieClicker/images/nuclearreactor.png')
=======
turbo = pygame.image.load('CookieClicker/images/turbo.png')
bardello = pygame.image.load('CookieClicker/images/bardello.png')
slaves = pygame.image.load('CookieClicker/images/slaves.png')
chump_hat = pygame.image.load('CookieClicker/images/chump_hat.png')
nuclear_reactor = pygame.image.load('CookieClicker/images/nuclearreactor.png')
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3

'''Details'''
upgrades_bg = pygame.image.load('CookieClicker/images/black.jpg')
leiste = pygame.image.load('CookieClicker/images/leiste.png')
card_display_background = pygame.image.load('CookieClicker/images/grey.jpg')

'''Colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)
GREEN = (0, 255, 0)
BLUE = (51, 90, 144)

<<<<<<< HEAD
# CUSTOM CURSOR SETUP
#
# import img
custom_default_cursor_img = pygame.image.load('CookieClicker/images/custom_default_cursor.png')
cursor_size = (int(8)), (int(8))
# hit point
hit_point = ( int( custom_default_cursor_img.get_width() * 0.5 ) ), (int( custom_default_cursor_img.get_height() * 0.1) )
# replace cursor
tuple = custom_default_cursor_img.get_rect()
pygame.mouse.set_cursor(cursor_size, hit_point, tuple, tuple)


=======
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3
class MainCookie:
    def __init__(self, x_pos_cookie, y_pos_cookie, x_size_cookie):
        self.x = x_pos_cookie
        self.y = y_pos_cookie
        self.length = x_size_cookie
        self.height = x_size_cookie

        self.animation_state = 0
    def draw(self):

        if self.animation_state > 0:
            cookie_img_scaled = pygame.transform.scale(cookie_img, ( int(1.3*x_size_cookie), int(1.3*x_size_cookie) ))
            window.blit(cookie_img_scaled, (cookie_img_scaled.get_rect(center =( x_pos_cookie, y_pos_cookie) )))
            self.animation_state -= 1
        else:
            cookie_img_scaled = pygame.transform.scale(cookie_img, ( int(1*x_size_cookie), int(1*x_size_cookie) ))
            window.blit(cookie_img_scaled, (cookie_img_scaled.get_rect(center =( x_pos_cookie, y_pos_cookie) )))
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
<<<<<<< HEAD
    def __init__(self, name, index_x, index_y, image, base_cost, increase_per_purchase, cps):
=======
    def __init__(self, name, index_x, index_y, image, icon, base_cost, increase_per_purchase, cps):
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3
        self.name = name
        self.index_x = index_x
        self.index_y = index_y
        self.length = 200
        self.height = 280

        self.image = pygame.transform.scale(image, (self.length, self.height))
        self.base_cost = base_cost
        self.increase_per_purchase = increase_per_purchase
        self.cps = cps

        self.quantity = 0
        self.created = 0

    def collidepoint(self, mouse_pos):
        pos_x = x_pos_store + (self.card_index_x * (self.length + 10))
        pos_y = y_pos_store + (self.card_index_y * (self.height + 10))
        return pygame.Rect(pos_x, pos_y, self.length, self.height).collidepoint(mouse_pos)

    def getTotalCost(self):
        return self.base_cost * self.increase_per_purchase**(self.quantity)

    def draw(self, card_index_x, card_index_y, solid = True):
        store_cost_font = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 14)
        store_quantity_cost = pygame.font.Font('CookieClicker/Font/SemiSweet-Bold-italic.ttf', 20)
<<<<<<< HEAD
=======

        icon = self.image
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3
        cost = store_cost_font.render('{}'.format( format_number(int(self.getTotalCost()) ) ), True, GREEN)
        cost_length = cost.get_rect().width
        quantity = store_quantity_cost.render('{}'.format(self.quantity), True, BLUE)
        quantity_length = quantity.get_rect().width

        if solid == False:
            self.image.set_alpha(100)
        else:
<<<<<<< HEAD
            self.image.set_alpha(255)
=======
            icon.set_alpha(255)
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3
        pos_x = x_pos_store + (card_index_x * (self.length + 10))
        pos_y = y_pos_store + (card_index_y * (self.height + 10))
        self.card_index_x = card_index_x
        self.card_index_y = card_index_y
<<<<<<< HEAD
        window.blit(self.image, (pos_x, pos_y))
=======
        window.blit(icon, (pos_x, pos_y))
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3
        window.blit(cost, (pos_x + 170 - cost_length, pos_y + 10))
        window.blit(quantity, (pos_x + self.length -45 - quantity_length, pos_y + self.height -47))

 #       def drawDisplayBox(self):
#          card_font = pygame.font.Font('Font/SemiSweet-Bold-italic.ttf', 20)
#            card_title = card_font.render('{}'.format(self.name), True, WHITE)
#
 #           discribe_font = pygame.font.Font('Font/SemiSweet-Bold-italic.ttf', 20)
  #          production = discribe_font.render('Each {} produces {:.lf} cookies per second'.format(self.name, self.cps), True, WHITE)
   #         quantity = card_font.render('You have {} {}s producing {:.lf} cookies per second'.format(self.quantity, self.name, self.cps*self.quantity),True, WHITE)
    #        created = card_font.render('{}s have created {} cookies so far'. format(self.name, math.floor(self.created)), True, WHITE)
#
 #           x_pos = self.x - 400
  #          y_pos = pygame.mouse.get_pos()[1] - 72
#
 #           window.blit(card_display_background, (x_pos, y_pos))
  #          window.blit(self.icon, (x_pos + 3, y_pos + 3))
   #         window.blit(card_title, (x_pos + 43, y_pos + 50))
#
 #           space_between_lines = 16
  #          window.blit(production, (x_pos + 18, y_pos + 50))
   #         window.blit(quantity, (x_pos + 18, y_pos + 50 + space_between_lines*1))
    #        window.blit(created, (x_pos + 18, y_pos + 50 + space_between_lines*2))
#

class Player:
    def __init__(self):
        self.score = 0
        self.click_multiplier = 1
        self.cps = 0

    def updateTotalCPS(self, list_of_cards):
        self.cps = 0
        for card in list_of_cards:
            self.cps += card.cps * card.quantity

'''pos1 = x, pos2 = y'''
cookie = MainCookie(300, 240, 200)

score_display = ScoreDisplay(360, 0)
user = Player()

'''cards'''
store_y = 20
store_x = 830

<<<<<<< HEAD
# slaves = card("Slaves", 0, 0 , slaves, slaves, base_cost=15, increase_per_purchase=1.15, cps=1)
# Turbo = card('Turbo', 1, 0, turbo, turbo, base_cost=100, increase_per_purchase=1.18, cps=20)
# Bardell1 = card('Bardelli', 2, 0, bardello, bardello, base_cost=2500, increase_per_purchase=1.185, cps=105)
# chump_hat = card('Chumphat', 0, 1, chump_hat, chump_hat, base_cost=80000, increase_per_purchase=1.15, cps=1000)
# nuclear_reactor = card('Nuclear-Reactor', 1, 1, nuclear_reactor, nuclear_reactor, base_cost=1000000, increase_per_purchase=3.15, cps=1000)
# Bardell4 = card('Bardelli', 2, 1, bardello, bardello, base_cost=1000000, increase_per_purchase=300.15, cps=10000)

# list_of_cards = [slaves, Bardell, Bardell1, chump_hat, nuclear_reactor, Bardell4]

# CREATE CARDS FROM CLASS
#
# create list
#
list_of_cards = []
#
# import images
card_bad_code_img = pygame.image.load('CookieClicker/images/card_bad_code.png')
card_bad_code = card("Slaves", 0, 0 , card_bad_code_img, base_cost=15, increase_per_purchase=1.15, cps=1)
list_of_cards.append(card_bad_code)
card_chump_hat_img = pygame.image.load('CookieClicker/images/card_chump_hat.png')
card_diamond_pickaxe_img = pygame.image.load('CookieClicker/images/card_diamond_pickaxe.png')
card_golden_pickaxe_img = pygame.image.load('CookieClicker/images/card_golden_pickaxe.png')
card_netherite_pickaxe_img = pygame.image.load('CookieClicker/images/card_netherite_pickaxe.png')
card_nuclearreactor_img = pygame.image.load('CookieClicker/images/card_nuclearreactor.png')
card_slaves_img = pygame.image.load('CookieClicker/images/card_slaves.png')
card_teachers_dream_img = pygame.image.load('CookieClicker/images/card_teachers_dream.png')
card_turbo_img = pygame.image.load('CookieClicker/images/card_turbo.png')
card_wooden_pickaxe_img = pygame.image.load('CookieClicker/images/card_wooden_pickaxe.png')
=======
slaves = card("Slaves", 0, 0 , slaves, slaves, base_cost=15, increase_per_purchase=1.15, cps=0.1)
Bardell = card('Turbo', 1, 0, turbo, turbo, base_cost=125, increase_per_purchase=1.18, cps=100)
Bardell1 = card('Bardelli', 2, 0, bardello, bardello, base_cost=2500, increase_per_purchase=1.185, cps=105)
chump_hat = card('Chumphat', 0, 1, chump_hat, chump_hat, base_cost=80000, increase_per_purchase=1.15, cps=1000)
nuclear_reactor = card('Nuclear-Reactor', 1, 1, nuclear_reactor, nuclear_reactor, base_cost=1000000, increase_per_purchase=3.15, cps=1000)
Bardell4 = card('Bardelli', 2, 1, bardello, bardello, base_cost=1000000, increase_per_purchase=300.15, cps=10000)

list_of_cards = [slaves, Bardell, Bardell1, chump_hat, nuclear_reactor, Bardell4]
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3

def format_number(n):
    if n >= 1000000000:
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

def draw():

    '''Draw Background'''
    window.blit(background_img, (0,0))

    window.blit(upgrades_bg, (x_pos_upgradeBackground, 0))
    window.blit(leiste, (x_pos_leiste, 0))

    '''Draw Cookie & ScoreDisplay'''

    cookie.draw()
    score_display.draw(x_pos_score, y_pos_score)

    '''Draw cards'''
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

        '''ADD cookies made trough cards'''
        user.score += card.quantity * card.cps * .025
        card.created += card.quantity * card.cps * .01

        '''Draw Display Box'''
 #       if card.collidepoint(pygame.mouse.get_pos()):
  #          card.drawDisplayBox

    pygame.display.update()

<<<<<<< HEAD
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
=======
def createVariables(current_window_width, current_window_height):
    # CREATING GLOBAL VARIABLES FOR DYNAMIC LAYOUT
    global x_pos_leiste
    x_pos_leiste = current_window_width * 2/3
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3
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
    y_pos_store = 20 - (relative_scroll_y * 20)
    global store_width
    store_width = current_window_width - x_pos_upgradeBackground
<<<<<<< HEAD
    global cards_per_row
    cards_per_row = math.floor(store_width / total_card_length)
=======
    global card_length
    card_length = 200
    global card_height
    card_height = 280
    global cards_per_row
    cards_per_row = math.floor(store_width / ( card_length + 10 ))
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3


# SETUP MAIN-LOOP
main = True
FPS = 60
Clock = pygame.time.Clock()
global relative_scroll_x
relative_scroll_x = 0
global relative_scroll_y
relative_scroll_y = 0

# START MAIN-LOOP
while main == True:

    # FPS / Delay
    Clock.tick(FPS)

    # GET WINDOW SIZE
    current_window_width = pygame.display.get_surface().get_width()
    current_window_height = pygame.display.get_surface().get_height()

    # CREATE VARIABLES FOR DYNAMIC LAYOUT
<<<<<<< HEAD
    set_width_to_two = "FALSE"
    createVariables(current_window_width, current_window_height, set_width_to_two)
    if cards_per_row < 2:
        set_width_to_two = "TRUE"
        createVariables(current_window_width, current_window_height, set_width_to_two)
=======
    createVariables(current_window_width, current_window_height)
>>>>>>> 1b92a7d50ae83da0cc0dc68458ba92c7b5b5ccc3

    # DRAW NEW FRAME
    draw()

    # EVENT LISTENERS
    for event in pygame.event.get():

        # MOUSE-CLICK -- LINKE MOUSTASTE
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            # HIT COOKIE
            if cookie.collidepoint(mouse_pos):
                user.score += 1
                cookie.animation_state = 1

            # HIT CARD
            for card in list_of_cards:
                if card.collidepoint(mouse_pos) and user.score >= card.getTotalCost():
                    user.score -= card.getTotalCost()
                    card.quantity += 1
                    user.updateTotalCPS(list_of_cards)
        
        # MOUSE-SCROLL
        if event.type == pygame.MOUSEWHEEL:
            relative_scroll_x += event.x
            relative_scroll_y -= event.y
            if relative_scroll_y < 0:
                relative_scroll_y = 0

        # EXIT BUTTON
        if event.type == pygame.QUIT:
            main = False
    
    # CLEAR EVENT QUEUE
    pygame.event.clear()

# EXIT PYGAME
pygame.quit()