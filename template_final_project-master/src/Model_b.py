class fire:
    def __init__(self,x,y,speed,img_file,type=0):
        self.x=x+speed
        self.y=y+speed
        self.speed=speed
        self.type=type
        self.img_file=img_file

