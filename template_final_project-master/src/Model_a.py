

class fire:
    def __init__(self,x=250,y=250,speed=0.25,width=15,height=15,color=[1,0,0]):
        self.speed=speed
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.color=color

class player:
    def __init__(self,x=150,y=150,width=15,height=15,speed=0.25,color=[0,0,225]):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed=speed
        self.color=color        
class Right:
    def __init__(self,x,speed):
        self.x=x
        self.speed=speed
    def right(self,x,speed):
        self.x = speed+x
        return self.x
class Left:
    def __init__(self,x,speed):
        self.x=x
        self.speed=speed
    def right(self,x,speed):
        self.x = x-speed
        return self.x
class Up:
        
    def __init__(self,y,speed):
        self.y=y
        self.speed=speed
    def right(self,y,speed):
        self.y = speed+y
        return self.y
class Down:
    def __init__(self,y,speed):
        self.y=y
        self.speed=speed
    def right(self,y,speed):
        self.y = y-speed
        return self.y

