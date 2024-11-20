import pygame
import Model_a
import Model_b

class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen=pygame.display.set_mode()
    size_list = pygame.display.get_window_size(width, height)
    width = size_list[0]
    height = size_list[1]
    self.char = []
                           
    #setup pygame data
    #sets the size of the screen, and sets up which character to use
    
  def mainloop(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.CONTROLLER_BUTTON_DPAD_UP:
          up=True
        
          
          
        
    #select state loop
    #setting up eventing for the controls and collision for objects
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop
      #main menu where you select character, difficulty, click to play or exit

      #update data

      #redraw
      
  def gameloop(self):
      #event loop
      #starts the game events so you play the game

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop
      #stops gameplay and tells you the time, and if you want to retry or go back to menu

      #update data

      #redraw
