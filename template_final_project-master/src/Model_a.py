class char:
    def __init__(self,x,y,width,height,speed):
        self.width = 25
        self.height = 25
        self.x = width
        self.y = height
        self.speed = 5
        
class right:
    def __init__(self,x):
        self.x=x

class left:
    def __init__(self,x):
        self.x=-x

class up:
    def __init__(self,y):
        self.y=y

class down:
    def __init__(self,y):
        self.y=-y
        
class fire:
    def __init__(self,speed,width,height):
        self.speed=3
        self.width=15
        self.height=15
        