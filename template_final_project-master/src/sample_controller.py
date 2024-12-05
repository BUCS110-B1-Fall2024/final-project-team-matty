import pygame
import pygame_menu
from src.Model_a import *



width = 500
height = 500
bg_color = (0,0,0) 


class controller:
    def __init__ (self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Fireball_Survival")
        self.state = "Start"
        self.menu = pygame_menu.Menu("Fireball Survival", width, height)
    
    def start_game(self):
        self.state = "Game"  
    
    def mainloop(self):
        while True:
            if self.state == "Start":
                self.start_loop()
            elif self.state == "Game":
                self.gameloop()
            elif self.state == "End":
                self.endloop()

    def start_loop(self):
        self.menu.clear() 
        self.menu = pygame_menu.Menu("Fireball Survival", width, height)
        self.menu.add.label("Begin Game?", font_size=16)
        self.menu.add.button("Start", self.gameloop) 
        self.menu.add.button("Quit", self.quit_game)  
        self.menu.mainloop(self.screen) 


    def gameloop(self):
        running = True
        while running:
            self.screen.fill(bg_color)  
            person=player()
            enemy=fire()
            


            gamer = pygame.Rect(person.x, person.y, person.width, person.height)
            pygame.draw.rect(self.screen, person.color, gamer)
            fireball = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            pygame.draw.rect(self.screen, enemy.color, fireball)



            keys = pygame.key.get_pressed() 
            for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                if keys[pygame.K_LEFT] and person.x >= 0:
                  person.x -= person.speed
            if keys[pygame.K_RIGHT] and person.x <= 475:
              person.x += person.speed
            if keys[pygame.K_DOWN] and person.y <= 475:
              person.y -= person.speed
            if keys[pygame.K_UP] and person.y>=0:
              person.y += person.speed         
            if keys[pygame.K_ESCAPE]:
              self.endloop()
        
            pygame.display.update()


             

    def endloop(self):
        self.menu.clear()  
        self.menu = pygame_menu.Menu("Game Over", width, height) 
        self.menu.add.label("You lost!", font_size=16)
        self.menu.add.button("Back to menu", self.start_loop)
        self.menu.draw(self.screen)
        pygame.display.flip()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
            if running == False:
                  pygame.quit()
            if gamer.colliderect(fireball):
                  print('touch')
             
    def quit_game(self):
        pygame.quit()
        exit()  
        
        

