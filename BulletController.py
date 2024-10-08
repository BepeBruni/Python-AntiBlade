from ursina import *
from EnemyController import Enemy
from ObstacleController import Obstacle

class bullet(Entity):
    def __init__(self,pose, **kwargs):
        super().__init__()
        self.speed = 3
        self.effect = "idk"
        self.power = 100
        self.rotation = (0, 0, 0)
        self.model = "cube"
        self.shooted = False
        self.path = Vec3(0,0,0)
        self.position = pose
        self.collider = 'box'
        self.hitted = False

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        if self.shooted == False:
            self.rotation = (0,0,Vec2(1,0).signedAngleDeg(Vec2(-mouse.x,mouse.y)))
            self.path = mouse.position
            self.shooted = True
        if self.shooted == True and not self.hitted:
            self.position += self.left *self.speed
        for thing in self.intersects().entities:
            if not self.hitted and (type(thing) == Enemy or type(thing) == Obstacle):
                if type(thing) == Enemy:
                    thing.getHit()
                print(thing.name)
                self.scale /= 1.5
                self.hitted = True
                destroy(self)
