
import pygame as pg
from sprites import * # importerer alt fra sprites.py fil
 
class Game():
    def __init__(self): # kjører når vi starter spillet
        pg.init()
 
        pg.mixer.init()
        screenWidth = 720
        screenHeight = 420
 
        self.screen = pg.display.set_mode((screenWidth, screenHeight)) # lager spill vinduet
 
        self.comicSans30 = pg.font.SysFont("Comic Sans MS", 30)
 
        self.bgImg = pg.image.load("img/Background.png")
        self.bgImg = pg.transform.scale(self.bgImg,(screenWidth, screenHeight))
 
        self.clock = pg.time.Clock()
 
        self.new()
 
    def new(self): # kode for å starte en ny runde/etter game over 

     
    
        self.allSprites = pg.sprite.Group()
 
      
        
        self.run()
 
    def run(self): # game loop
        playing = True
        while playing:
            self.clock.tick(120)
            #print("playing")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False
 
            self.screen.blit(self.bgImg,(0,0))
 
            self.allSprites.update() 
          

            self.allSprites.draw(self.screen) # allSprites gruppen tegnes til screen
            pg.display.update() # oppdaterer screen
 
g = Game()
