import pygame
from spriteloader import spritesheet
from os.path import dirname, basename, isfile, join
from iter_game import iter_game
from sample import snake_game
from new_game import checkers_game
###import more game classes from files ####

#setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#data passed between games
class data(object):
    def __init__(self):
        self.score = 0
        self.log = ""
        self.status = -1
        self.game_num = 0
        def up_score(val):
            self.score+=val
        def up_log(text):
            self.log +=text+"\n"

#basic game (can be deleted later)
class mini_game(iter_game):
    def ok(self):
        print("ok")

#menu like game to choose between games (include more later)
class overworld_game(iter_game):
    def __init__(self):
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.locations = [(20,20),(140,50),(60,280),(790,120),(790,120)]
        self.ss = spritesheet('guy10.png')
        self.ss.load_strip(1,colorkey=(0,0,0))
        self.ss.iter()
        self.image = self.ss.next(0)

    def next(self,pygame,events,screen,dt,data):
        x = self.player_pos[0]
        y = self.player_pos[1]
        bounds = 50
        screen.fill("purple")

        screen.blit(self.image, self.player_pos)
        for i in range(len(games)):
            if i==0:
                continue
            pygame.draw.circle(screen, "red", self.locations[i], 16)
            if(x+bounds>self.locations[i][0] and x-bounds<self.locations[i][0] and y+bounds>self.locations[i][1] and y-bounds<self.locations[i][1]):
                print("collision" + str(self.locations[i][0]))
                data.game_num = i
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * dt
        pygame.display.flip()
        self.image = self.ss.next(dt)
dobj = data()
#### Insert games to be included below ####


#games = [overworld_game(),snake_game(),checkers_game(),mini_game(),mini_game()]
game_num = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    games[game_num].next(pygame,events,screen,dt,dobj)
    game_num = dobj.game_num
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()