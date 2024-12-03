import pygame
import pygame_menu


width = 500
height = 500
bg_color = "black" 

class Controller:
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

        char_x = 0
        char_y = 0
        char_width=25 
        char_height = 25
        char_speed=0.25
        char_color="Blue"

        fire_x= 50 
        fire_y = 25
        fire_width=25
        fire_height =25
        fire_speed=0.25
        fire_color="Red"

        running = True
        while running:
            self.screen.fill(bg_color)  
            
            
            char = pygame.Rect(char_x, char_y, char_width, char_height)
            pygame.draw.rect(self.screen, char_color, char)
            fire = pygame.Rect(fire_x, fire_y, fire_width, fire_height)
            pygame.draw.rect(self.screen, fire_color, fire)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if char.colliderect (fire):
                  print('touch')
             

            keys = pygame.key.get_pressed() 
            if keys[pygame.K_LEFT] and char_x >= 0:
              char_x-= char_speed
            if keys[pygame.K_RIGHT] and char_x <= 475:
              char_x+= char_speed        
            if keys[pygame.K_DOWN] and char_y <= 475:
              char_y+= char_speed
            if keys[pygame.K_UP] and char_y>=0:
              char_y-= char_speed          
            if keys[pygame.K_ESCAPE]:
              self.endloop()
        
            pygame.display.update()

        self.state = "End"  

    def endloop(self):
        self.menu.clear()  
        self.menu.add.label("You lost!", font_size=16)
        self.menu.add.button("Back to menu", self.start_loop)
        self.menu.draw(self.screen)
        pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        exit()  

if __name__ == '__main__':
    controller = Controller()
    controller.mainloop()
