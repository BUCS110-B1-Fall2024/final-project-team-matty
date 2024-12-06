import pygame
from src.sample_controller import controller


def main():
    pygame.init()
    control= controller()
    control.mainloop()



    

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
