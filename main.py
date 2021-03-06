@namespace
class SpriteKind:
    prof = SpriteKind.create()
    traner = SpriteKind.create()

def on_a_pressed():
    if violet.overlaps_with(prof_maple):
        game.splash("as you know I am prof", "maple and are you ready")
        game.splash("to be embrace by the word", "of pokemon ")
        game.splash("pokemon are all around us", "in the sky in the sea ")
        game.splash("and on the ground ")
        game.splash("everyone can do anything  ", "whit pokemon ")
        game.splash("I myself i am a pokmon", "professor of pokemon ")
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

prof_maple: Sprite = None
violet: Sprite = None
violet = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
prof_maple = sprites.create(img("""
        . . . . f f f f . . . . 
            . . f f e e e e f f . . 
            . f f e e e e e e f f . 
            f f f f 4 4 4 4 f f f f 
            f f f 4 4 4 4 4 f f f f 
            f f f f f f f f f f f f 
            f 4 f 1 1 1 1 1 1 f 4 f 
            f 4 f 1 1 1 1 1 1 f 4 f 
            f e f f f f f f f f e f 
            . f e d d b b d d e f . 
            . f f e b 4 4 b e f f . 
            e 4 f b 1 1 1 1 b f 4 e 
            4 d f 1 1 1 1 1 1 f d 4 
            4 4 f 6 6 6 6 6 6 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . .
    """),
    SpriteKind.prof)
controller.move_sprite(violet)
scene.camera_follow_sprite(violet)
tiles.set_tilemap(tilemap("""
    level1
"""))
prof_maple.set_position(122, 107)
mySprite3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . 2 2 2 2 2 e . . . 
            . . . . . . 2 2 2 2 d 2 2 e . . 
            . . . . . e 2 2 2 2 2 2 2 e . . 
            . . . . . e 2 2 2 2 2 2 2 e . . 
            . . . . . e 2 2 2 2 2 e f f c c 
            . . . . . e e 2 2 e f f f f b c 
            . . . e e e f e 2 2 b f f f d c 
            . . e e 2 2 d f e 2 1 1 1 1 b c 
            . . e e 2 2 d f e e e c c c . . 
            . . b 1 1 d e 2 2 e e c . . . . 
            . . . f f f d d 2 2 f d d . . . 
            . . . . f f d d e e f d d . . . 
            . . . . . f f f f f . . . . . . 
            . . . . e e e f f . . . . . . . 
            . . . . e e e e f f . . . . . .
    """),
    SpriteKind.traner)
game.splash("come here ", "it is your .prof maple")
game.show_long_text("walk over to .prof maple and press A", DialogLayout.BOTTOM)
mySprite3.set_position(105, 40)
violet.set_position(140, 250)
nom = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            f f f f f f f f f f f f f f f f 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
nom.set_position(135, 2)

def on_forever():
    if violet.overlaps_with(nom):
        tiles.set_tilemap(tilemap("""
            level6
        """))
forever(on_forever)
