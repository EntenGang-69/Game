import pygame

pygame.init()

window_length = 1750
window_height = 1000
window = pygame.display.set_mode((window_length, window_height))

background_img = pygame.image.load('images/grey.jpg')

cookie_img = pygame.image.load('images/keks.png')

'''Buildings'''
turbo = pygame.image.load('images/turbo.png')
bardello = pygame.image.load('images/bardello.png')
slaves = pygame.image.load('images/slaves.png')
chump_hat = pygame.image.load('images/chump_hat.png')
nuclear_reactor = pygame.image.load('images/nuclearreactor.png')

'''Details'''

upgrades_bg = pygame.image.load('images/black.jpg')
leiste = pygame.image.load('images/leiste.png')
building_display_background = pygame.image.load('images/grey.jpg')


'''Colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)
GREEN = (0, 255, 0)
BLUE = (51, 90, 144)


class MainCookie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 250
        self.height = 250

        self.animation_state = 0
    def draw(self):
        if self.animation_state > 0:
            cookie_img_scaled = pygame.transform.scale(cookie_img, ( int(1.9*self.length), int(1.9*self.height) ))
            window.blit(cookie_img_scaled, (cookie_img_scaled.get_rect(center =( int(self.x + self.length/2), int(self.y + self.height/2) ) )))
            self.animation_state -= 1
        else:
            window.blit(cookie_img, (cookie_img.get_rect(center=( int(self.x + self.length/2), int(self.y + self.height/2) ) )))
    def collidepoint(self, mouse_pos):
        return pygame.Rect(self.x-100, self.y-100, self.length+200, self.height+200).collidepoint(mouse_pos)

class ScoreDisplay():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 100
        self.height = 100

    def draw(self):
        font = pygame.font.Font('Font/SemiSweet-Bold-italic.ttf', 24)
        small_font = pygame.font.Font('Font/Kavoon-Regular.ttf', 26)

        SCORE = small_font.render('{} cookies'.format(format_number ( int(user.score) )), True, WHITE)
        CPS = font.render('per second: {}'.format(int(user.cps)), True, WHITE)
        window.blit(SCORE, (SCORE.get_rect( center=( int(self.x + self.length/2), int(self.y + self.height/2) ) )))
        window.blit(CPS, (CPS.get_rect(center=(int(self.x + self.length / 2), int(self.y + self.height / 2)+20 ) )))
class Building:
    def __init__(self, name, x, y, image, icon, base_cost, increase_per_purchase, cps):
        self.name = name
        self.x = x
        self.y = y
        self.length = 300
        self.height = 64

        self.image = image
        self.icon = icon
        self.base_cost = base_cost
        self.increase_per_purchase = increase_per_purchase
        self.cps = cps

        self.quantity = 0
        self.created = 0

    def collidepoint(self, mouse_pos):
        return pygame.Rect(self.x+10, self.y, self.length-120, self.height+200).collidepoint(mouse_pos)

    def getTotalCost(self):
        return self.base_cost * self.increase_per_purchase**(self.quantity)

    def draw(self, solid = True):
        store_cost_font = pygame.font.Font('Font/SemiSweet-Bold-italic.ttf', 14)
        store_quantity_cost = pygame.font.Font('Font/SemiSweet-Bold-italic.ttf', 20)



        icon = self.image
        cost = store_cost_font.render('{}'.format( format_number(int(self.getTotalCost()) ) ), True, GREEN)
        quantity = store_quantity_cost.render('{}'.format(self.quantity), True, BLUE)





        if solid == False:
            icon.set_alpha(100)
        else:
            icon.set_alpha(255)
        window.blit(icon, (self.x, self.y))
        window.blit(cost, (self.x +110, self.y + self.height +175))
        window.blit(quantity, (self.x + self.length -155, self.y + self.height -56))

 #       def drawDisplayBox(self):
#          building_font = pygame.font.Font('Font/SemiSweet-Bold-italic.ttf', 20)
#            building_title = building_font.render('{}'.format(self.name), True, WHITE)
#
 #           discribe_font = pygame.font.Font('Font/SemiSweet-Bold-italic.ttf', 20)
  #          production = discribe_font.render('Each {} produces {:.lf} cookies per second'.format(self.name, self.cps), True, WHITE)
   #         quantity = building_font.render('You have {} {}s producing {:.lf} cookies per second'.format(self.quantity, self.name, self.cps*self.quantity),True, WHITE)
    #        created = building_font.render('{}s have created {} cookies so far'. format(self.name, math.floor(self.created)), True, WHITE)
#
 #           x_pos = self.x - 400
  #          y_pos = pygame.mouse.get_pos()[1] - 72
#
 #           window.blit(building_display_background, (x_pos, y_pos))
  #          window.blit(self.icon, (x_pos + 3, y_pos + 3))
   #         window.blit(building_title, (x_pos + 43, y_pos + 50))
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

    def updateTotalCPS(self, list_of_buildings):
        self.cps = 0
        for building in list_of_buildings:
            self.cps += building.cps * building.quantity


'''pos1 = x, pos2 = y'''
cookie = MainCookie(550, 300)

score_display = ScoreDisplay(630, 0)
user = Player()

'''Buildings'''
store_y = 412
store_x = 1145

slaves = Building("Slaves", store_x, store_y , slaves, slaves, base_cost=15, increase_per_purchase=1.15, cps=0.1)
Bardell = Building('Turbo', store_x+200*1, store_y, turbo, turbo, base_cost=125, increase_per_purchase=1.18, cps=100)
Bardell1 = Building('Bardelli', store_x+200*2, store_y, bardello, bardello, base_cost=2500, increase_per_purchase=1.185, cps=105)
chump_hat = Building('Chumphat', store_x, store_y+280*1, chump_hat, chump_hat, base_cost=80000, increase_per_purchase=1.15, cps=1000)
nuclear_reactor = Building('Nuclear-Reactor', store_x+200*1, store_y+280*1, nuclear_reactor, nuclear_reactor, base_cost=1000000, increase_per_purchase=3.15, cps=1000)
Bardell4 = Building('Bardelli', store_x+200*2, store_y+280*1, bardello, bardello, base_cost=1000000, increase_per_purchase=300.15, cps=10000)


list_of_buildings = [slaves, Bardell, Bardell1, chump_hat, nuclear_reactor, Bardell4]


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

    window.blit(upgrades_bg, (1130, 0))
    window.blit(leiste, (1120, 0))

    '''Draw Cookie & ScoreDisplay'''

    cookie.draw()
    score_display.draw()

    '''Draw buildings'''
    for building in list_of_buildings:
        if user.score >= building.getTotalCost():
            building.draw(solid=True)
        else:
            building.draw(solid=False)


        '''ADD cookies made trough buildings'''
        user.score += building.quantity * building.cps * .025
        building.created += building.quantity * building.cps * .01


        '''Draw Display Box'''
 #       if building.collidepoint(pygame.mouse.get_pos()):
  #          building.drawDisplayBox



    pygame.display.update()


main = True
while main == True:

    pygame.time.delay(10)


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            '''CLick Cookie'''
            if cookie.collidepoint(mouse_pos):
                user.score += 1
                cookie.animation_state = 1

            for building in list_of_buildings:
                if building.collidepoint(mouse_pos) and user.score >= building.getTotalCost():
                    user.score -= building.getTotalCost()
                    building.quantity += 1
                    user.updateTotalCPS(list_of_buildings)

        if event.type == pygame.QUIT:
            main = False



    draw()

pygame.quit()