#!/usr/bin/env python
""" pygame.examples.aliens

Shows a mini game where you have to defend against aliens.

What does it show you about pygame?

* pg.sprite, the difference between Sprite and Group.
* dirty rectangle optimization for processing for speed.
* music with pg.mixer.music, including fadeout
* sound effects with pg.Sound
* event processing, keyboard handling, QUIT handling.
* a main loop frame limited with a game clock from pg.time.Clock
* fullscreen switching.


Controls
--------

* Left and right arrows to move.
* Space bar to shoot
* f key to toggle between fullscreen.

"""

import random
import os

# import basic pygame modules
import pygame as pg

from klasser import *


# see if we can load more than standard BMP
if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")





def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()


def load_sound(file):
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


# Each type of game object gets an init and an update function.
# The update function is called once per frame, and it is when each object should
# change its current position and state.
#
# The Player object actually gets a "move" function instead of update,
# since it is passed extra information about the keyboard.





def main(winstyle=0):
    # Initialize pygame
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None

    fullscreen = False
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    img = load_image("player1.gif")
    Player.images = [img, pg.transform.flip(img, 1, 0)]
    img = load_image("explosion1.gif")
    Explosion.images = [img, pg.transform.flip(img, 1, 1)]
    Alien.images = [load_image(im) for im in ("chimp.png", "chimp.png", "chimp.png")]
    AlienOtherDirection.images = [load_image(im) for im in ("alien1.gif", "alien2.gif", "alien3.gif")]
    OtherEnemies.images = [load_image(im) for im in ("nedladdning.jfif", "chimp.png", "chimp.png")]
    Bomb.images = [load_image("bomb.gif")]
    Shot.images = [load_image("nedladdning.jfif")]
    img = load_image("TileVertical.png")
    BackgroundKlass.images = [load_image("TileVertical.png")]
    Boll.images = [load_image("asprite.bmp")]

    StartKnapp.images = [load_image("menu/Menu_Green_01.png"), load_image("menu/Menu_Red_03.png")]


    # decorate the game window
    icon = pg.transform.scale(Alien.images[0], (32, 32))
    pg.display.set_icon(icon)
    pg.display.set_caption("Pygame Tysenator")
    pg.mouse.set_visible(True)

    # create the background, tile the bgd image
    bgdtile = load_image("background.gif")
    background = pg.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pg.display.flip()

    # load the sound effects
    boom_sound = load_sound("boom.wav")
    shoot_sound = load_sound("car_door.wav")
    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = pg.sprite.Group()
    shots = pg.sprite.Group()
    bombs = pg.sprite.Group()
    bollar = pg.sprite.Group()
    all = pg.sprite.RenderUpdates()
    lastalien = pg.sprite.GroupSingle()

    # assign default groups to each sprite class
    Player.containers = all
    Alien.containers = aliens, all, lastalien
    OtherEnemies.containers = aliens, all
    Shot.containers = shots, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    BackgroundKlass.containers = all
    Score.containers = all
    Boll.containers = all, bollar

    menu = pg.sprite.Group()
    StartKnapp.containers = menu

    # Create Some Starting Values
    global score
    alienreload = ALIEN_RELOAD
    clock = pg.time.Clock()

    # initialize our starting sprites
    global SCORE
    BackgroundKlass()
    player = Player()
    Alien()  # note, this 'lives' because it goes into a sprite group
    AlienOtherDirection()
    Boll()
    
    OtherEnemies()
    if pg.font:
        all.add(Score())

    start_knapp = StartKnapp()
    start_game = False
    while not start_game:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                start_game = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if(start_knapp.rect.collidepoint(pg.mouse.get_pos())):
                    start_knapp.nedtryckt()
                    # start_game = True
            elif event.type == pg.MOUSEBUTTONUP:
                start_knapp.upptryckt()
                if(start_knapp.rect.collidepoint(pg.mouse.get_pos())):
                    start_game = True
                

        pg.display.flip()
        dirty = menu.draw(screen)
        pg.display.update(dirty)
    pg.mouse.set_visible(False)    

    # Run our main loop whilst the player is alive.
    while player.alive():

        # get input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        print("Changing to FULLSCREEN")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle | pg.FULLSCREEN, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    else:
                        print("Changing to windowed mode")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    pg.display.flip()
                    fullscreen = not fullscreen

        keystate = pg.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # handle player input
        direction = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]
        player.move(direction)
        firing = keystate[pg.K_SPACE]
        if not player.reloading and firing and len(shots) < MAX_SHOTS:
            Shot(player.gunpos())
            if pg.mixer:
                shoot_sound.play()
        player.reloading = firing

        # Create new alien
        if alienreload:
            alienreload = alienreload - 1
        elif not int(random.random() * ALIEN_ODDS):
            if(random.randint(0, 1) == 0):
                Alien()
            else:
                AlienOtherDirection()
            alienreload = ALIEN_RELOAD

        # Drop bombs
        if lastalien and not int(random.random() * BOMB_ODDS):
            Bomb(lastalien.sprite)

        # Detect collisions between aliens and players.
        for alien in pg.sprite.spritecollide(player, aliens, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(alien)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()

        for boll in pg.sprite.spritecollide(player, bollar, False):
            boll.bounce()

        # See if shots hit the aliens.
        for alien in pg.sprite.groupcollide(aliens, shots, 1, 1).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(alien)
            SCORE = SCORE + 1

        # See if alien boms hit the player.
        for bomb in pg.sprite.spritecollide(player, bombs, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(player)
            Explosion(bomb)
            player.kill()

        # draw the scene
        dirty = all.draw(screen)
        pg.display.update(dirty)

        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(40)

    if pg.mixer:
        pg.mixer.music.fadeout(1000)
    pg.time.wait(1000)


# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()
