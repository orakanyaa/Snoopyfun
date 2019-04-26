import arcade.key
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
 
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) }
class Snoopy:
    
    MOVE_WAIT = 0.2

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
        self.wait_time = 0
        self.direction = DIR_RIGHT

    def update(self, delta):
        self.wait_time += delta
 
        if self.wait_time < Snoopy.MOVE_WAIT:
            return
 
        if self.x > self.world.width:
            self.x = 0
        direction = DIR_OFFSET[self.direction]
        self.x += 16*direction[0]
        self.y += 16*direction[1]
        self.wait_time = 0
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.snoopy = Snoopy(self, width // 2, height // 2)
 
 
    def update(self, delta):
        self.snoopy.update(delta) 

    def on_key_press(self, key, key_modifiers):

        if(key == 65362):
            self.snoopy.direction = DIR_UP
        elif(key == 65364):
            self.snoopy.direction = DIR_DOWN
        elif( key == 65361):
            self.snoopy.direction = DIR_LEFT
        else:
            self.snoopy.direction = DIR_RIGHT
