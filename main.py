
import pygame as pg
from sprites import * # importerer alt fra sprites.py fil
 
class Game():
    def __init__(self): # kjører når vi starter spillet
        pg.init()
 
        pg.mixer.init()
        self.soundPowerUp = pg.mixer.Sound('sounds/powerup.wav')
        screenWidth = 720
        screenHeight = 420
 
        self.screen = pg.display.set_mode((screenWidth, screenHeight)) # lager spill vinduet
        orange = (255, 165, 0) # RGB 
 
        self.comicSans30 = pg.font.SysFont("Comic Sans MS", 30)
 
        self.bgImg = pg.image.load("img/Background.png")
        self.bgImg = pg.transform.scale(self.bgImg,(screenWidth, screenHeight))
 
        self.clock = pg.time.Clock()
 
        self.new()
 
    def new(self): # kode for å starte en ny runde/etter game over 
        self.score = 0
     
        self.foodGroup = pg.sprite.Group()
        self.allSprites = pg.sprite.Group()
        self.enemyGroup = pg.sprite.Group()
        self.playerProjectiles = pg.sprite.Group()
 
        self.hero = Player(self) # oppretter player
        self.allSprites.add(self.hero) # legger til hero i allsprites gruppen
 
        self.burgerTimer = 0
        self.enemyTimer = 0
 
        self.scoreText = self.comicSans30.render(f"Score: {self.score}", False, ("red"))
        
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
            
 
            hit = pg.sprite.spritecollide(self.hero, self.enemyGroup, True)
            if hit: # når vi kolliderer med enemy
                self.score -= 20
                # lydeffekt
                self.hero.size -= 50
                self.hero.changeSize()
 
            hit = pg.sprite.spritecollide(self.hero, self.foodGroup, True)
            if hit: # når vi kolliderer med burger
                self.soundPowerUp.play()
                self.score += 1
                self.scoreText = self.comicSans30.render(f"Score: {self.score}", False, ("red"))
                self.hero.size += 1
                self.hero.changeSize()
 
            self.screen.blit(self.scoreText, (10,0))
            
            # burger spawner
            if self.burgerTimer <= 0:
                burger = Burger()
                self.foodGroup.add(burger)
                self.allSprites.add(burger) # legger til burger i allSprites
                self.burgerTimer = 10
                
 
            # enemy timer
            if self.enemyTimer <= 0:
                enemy = Enemy(self.hero)
                self.allSprites.add(enemy)
                self.enemyGroup.add(enemy)
                self.enemyTimer = 100
 
            self.burgerTimer -= 1
            self.enemyTimer -= 1
 
            self.allSprites.draw(self.screen) # allSprites gruppen tegnes til screen
            pg.display.update() # oppdaterer screen
 
g = Game()
