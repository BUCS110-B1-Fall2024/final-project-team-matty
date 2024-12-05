import pygame
from src.sample_controller import controller


def main():
    pygame.init()
    control= controller()
    #Create an instance on your controller object
    control.mainloop()

    #Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
