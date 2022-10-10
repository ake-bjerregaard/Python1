import random

import pygame as pg

from game_constants import *


class Player(pg.sprite.Sprite):
    """Representing the player as a moon buggy type car."""

    speed = 10
    bounce = 24
    gun_offset = -11
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top

class OtherEnemies(pg.sprite.Sprite):
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.image = pg.transform.scale(self.image, (100, 150))
        self.rect = pg.Rect(10, 10, 100, 150)
        # self.rect = pg.Rect.inflate(self.rect, 2, 2)
        
    def update(self):
        self.rect.move_ip(1, 0)
        

class Alien(pg.sprite.Sprite):
    """An alien space ship. That slowly moves down the screen."""

    speed = 1
    animcycle = 12
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]

class AlienOtherDirection(Alien):
    
    speed = -10
    def __init__(self):
        super().__init__()
        self.facing = AlienOtherDirection.speed

class Explosion(pg.sprite.Sprite):
    """An explosion. Hopefully the Alien and not the player!"""

    defaultlife = 12
    animcycle = 3
    images = []

    def __init__(self, actor):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        """called every time around the game loop.

        Show the explosion surface for 'defaultlife'.
        Every game tick(update), we decrease the 'life'.

        Also we animate the explosion.
        """
        self.life = self.life - 1
        self.image = self.images[self.life // self.animcycle % 2]
        if self.life <= 0:
            self.kill()


class Shot(pg.sprite.Sprite):
    """a bullet the Player sprite fires."""

    speed = -11
    images = []

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        # self.rect = self.image.get_rect(midbottom=pos)
        self.image = self.images[0]
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = pg.Rect(pos[0], pos[1], 50, 50)

    def update(self):
        """called every time around the game loop.

        Every tick we move the shot upwards.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


class Bomb(pg.sprite.Sprite):
    """A bomb the aliens drop."""

    speed = 9
    images = []

    def __init__(self, alien):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=alien.rect.move(0, 5).midbottom)

    def update(self):
        """called every time around the game loop.

        Every frame we move the sprite 'rect' down.
        When it reaches the bottom we:

        - make an explosion.
        - remove the Bomb.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()


class Score(pg.sprite.Sprite):
    """to keep track of the score."""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = "white"
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        """We only update the score in update() when it has changed."""
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)


#behöver då en repeterande bild
class BackgroundKlass(pg.sprite.Sprite):

    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.image = pg.transform.scale(self.image, (SCREENRECT.width, SCREENRECT.height*2))
        self.rect = pg.Rect(0, 0, SCREENRECT.width, SCREENRECT.height*2)

    def update(self):
        self.rect.move_ip(0, 10)
        if(self.rect.y > 0):
            self.rect.y = -self.rect.height//2
        
class Boll(pg.sprite.Sprite):

    images = []
    velocity = [4, 4]
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.velocity = Boll.velocity

    def update(self):
        self.rect.move_ip(self.velocity[0], self.velocity[1])

    def bounce(self):
        self.velocity[1] = -self.velocity[1]

class StartKnapp(pg.sprite.Sprite):
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def nedtryckt(self):
        self.image = self.images[1]

    def upptryckt(self):
        self.image = self.images[0]  

class TextField(pg.sprite.Sprite):
    """to keep track of the score."""

    updatera = False

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 20)
        self.font.set_italic(0)
        self.color = "white"
        self.updatera = True
        self.text = "Här ska vi skriva"
        self.update()
        self.rect = self.image.get_rect().move(10, 450)


    def update(self):
        """We only update the score in update() when it has changed."""
        # if self.updatera:
        self.image = self.font.render(self.text, 0, self.color)
        self.updatera = False

    def läggtilltext(self, extra_text):
        self.text += extra_text
        self.updatera = True
        

# class ExplosionSpritesheet(pg.sprite.Sprite):
    
#     images = []
#     image = None

#     def __init__(self, image):
#         pg.sprite.Sprite.__init__(self, self.containers)
#         self.image = image
#         self.images = [self.image_at(self, pg.Rect(0,0,222,222))]
        

    
#     def imageToSpriteImages(image):
#         local_images = [] 

#         return local_images

#     def images_at(self, rects, colorkey = None):
#         "Loads multiple images, supply a list of coordinates" 
#         return [self.image_at(rect, colorkey) for rect in rects]

#     def image_at(self, rectangle, colorkey = None):
#         "Loads image from x,y,x+offset,y+offset"
#         rect = pg.Rect(rectangle)
#         image = pg.Surface(rect.size).convert()
#         image.blit(self.sheet, (0, 0), rect)
#         if colorkey is not None:
#             if colorkey is -1:
#                 colorkey = image.get_at((0,0))
#             image.set_colorkey(colorkey, pg.RLEACCEL)
#         return image

#     def load_strip(self, rect, image_count):
#         for x in range(image_count):
#             tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
#             for x in range(image_count)]
#         return self.images_at(tups)

#############

# class spritesheet(object):
#     def __init__(self, filename):
#         try:
#             self.sheet = pygame.image.load(filename).convert()
#         except pygame.error, message:
#             print 'Unable to load spritesheet image:', filename
#             raise SystemExit, message
#     # Load a specific image from a specific rectangle
#     def image_at(self, rectangle, colorkey = None):
#         "Loads image from x,y,x+offset,y+offset"
#         rect = pygame.Rect(rectangle)
#         image = pygame.Surface(rect.size).convert()
#         image.blit(self.sheet, (0, 0), rect)
#         if colorkey is not None:
#             if colorkey is -1:
#                 colorkey = image.get_at((0,0))
#             image.set_colorkey(colorkey, pygame.RLEACCEL)
#         return image
#     # Load a whole bunch of images and return them as a list
#     def images_at(self, rects, colorkey = None):
#         "Loads multiple images, supply a list of coordinates" 
#         return [self.image_at(rect, colorkey) for rect in rects]
#     # Load a whole strip of images
#     def load_strip(self, rect, image_count, colorkey = None):
#         "Loads a strip of images and returns them as a list"
#         tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
#                 for x in range(image_count)]
#         return self.images_at(tups, colorkey)