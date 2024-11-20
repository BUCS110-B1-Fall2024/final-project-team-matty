class char:
    def __init__(self,x,y,img_file):
        self.x=x
        self.y=y
        self.img_file=img_file
        
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