def on_player2_button_a_pressed():
    global dart2
    if info.player2.has_life():
        dart2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
                . . 3 3 3 3 3 3 3 3 3 3 3 3 . .
                . . 1 1 1 1 1 1 1 1 1 1 1 1 . .
                . . 1 1 1 1 1 1 1 1 1 1 1 1 . .
                . . 3 3 3 3 3 3 3 3 3 3 3 3 . .
                . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            player2,
            200,
            0)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player4_life_zero():
    game.set_dialog_text_color(1)
    game.set_dialog_frame(img("""
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        """))
    if not (info.player1.has_life()) and (not (info.player2.has_life()) and not (info.player3.has_life())):
        game.show_long_text("Player 4 Wins!", DialogLayout.BOTTOM)
        game.over(True)
    else:
        game.show_long_text("Player 4 is out :-(", DialogLayout.BOTTOM)
        player4.destroy()
info.player4.on_life_zero(on_player4_life_zero)

def on_player3_life_zero():
    game.set_dialog_text_color(1)
    game.set_dialog_frame(img("""
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        """))
    if not (info.player1.has_life()) and (not (info.player2.has_life()) and not (info.player4.has_life())):
        game.show_long_text("Player 3 Wins!", DialogLayout.BOTTOM)
        game.over(True)
    else:
        game.show_long_text("Player 3 is out :-(", DialogLayout.BOTTOM)
        player3.destroy()
info.player3.on_life_zero(on_player3_life_zero)

def on_player4_button_a_pressed():
    global dart4
    if info.player4.has_life():
        dart4 = sprites.create_projectile_from_sprite(img("""
                . . . . . b b b b b b . . . . .
                . . . b b 9 9 9 9 9 9 b b . . .
                . . b b 9 9 9 9 9 9 9 9 b b . .
                . b b 9 d 9 9 9 9 9 9 9 9 b b .
                . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
                b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
                b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
                b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
                b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
                b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
                b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
                . b 5 3 3 3 d 9 9 9 9 d d 5 b .
                . b d 5 3 3 3 3 3 3 3 d 5 b b .
                . . b d 5 d 3 3 3 3 5 5 b b . .
                . . . b b 5 5 5 5 5 5 b b . . .
                . . . . . b b b b b b . . . . .
                """),
            player4,
            200,
            0)
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player1_button_a_pressed():
    global dart1
    if info.player1.has_life():
        dart1 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . c c c . . . . . .
                . . . . . . a b a a . . . . . .
                . . . . . c b a f c a c . . . .
                . . . . c b b b f f a c c . . .
                . . . . b b f a b b a a c . . .
                . . . . c b f f b a f c a . . .
                . . . . . c a a c b b a . . . .
                . . . . . . c c c c . . . . . .
                . . . . . . . c . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            player1,
            200,
            0)
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player1_life_zero():
    game.set_dialog_text_color(1)
    game.set_dialog_frame(img("""
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        """))
    if not (info.player2.has_life()) and (not (info.player3.has_life()) and not (info.player4.has_life())):
        game.show_long_text("Player 1 Wins!", DialogLayout.BOTTOM)
        game.over(True)
    else:
        game.show_long_text("Player 1 is out :-(", DialogLayout.BOTTOM)
        player1.destroy()
info.player1.on_life_zero(on_player1_life_zero)

def on_player3_button_a_pressed():
    global dart3
    if info.player3.has_life():
        dart3 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 4 5 5 4 4 4 . . . .
                . . . 3 3 3 3 4 4 4 4 4 4 . . .
                . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                . . 3 3 3 3 3 2 2 2 1 1 5 4 . .
                . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 .
                . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 .
                . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                . . . 4 2 2 2 2 2 2 2 2 4 . . .
                . . . . 4 4 2 2 2 2 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . 3 .
                . . . . . . . . . . . . . . . .
                """),
            player3,
            200,
            0)
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

def on_player2_life_zero():
    game.set_dialog_text_color(1)
    game.set_dialog_frame(img("""
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f
        """))
    if not (info.player1.has_life()) and (not (info.player3.has_life()) and not (info.player4.has_life())):
        game.show_long_text("Player 2 Wins!", DialogLayout.BOTTOM)
        game.over(True)
    else:
        game.show_long_text("Player 2 is out :-(", DialogLayout.BOTTOM)
        player2.destroy()
info.player2.on_life_zero(on_player2_life_zero)

def on_on_overlap(sprite, otherSprite):
    if sprite == dart1:
        info.player1.change_score_by(1)
    elif sprite == dart2:
        info.player2.change_score_by(1)
    elif sprite == dart3:
        info.player3.change_score_by(1)
    else:
        info.player4.change_score_by(1)
    sprite.destroy()
    otherSprite.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    if sprite2 == player1:
        info.player1.change_life_by(-1)
        scene.camera_shake(4, 200)
    elif sprite2 == player2:
        info.player2.change_life_by(-1)
        scene.camera_shake(4, 200)
    elif sprite2 == player3:
        info.player3.change_life_by(-1)
        scene.camera_shake(4, 200)
    else:
        info.player4.change_life_by(-1)
        scene.camera_shake(4, 200)
    otherSprite2.destroy(effects.fire, 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
dart3: Sprite = None
dart1: Sprite = None
dart4: Sprite = None
dart2: Sprite = None
player4: Sprite = None
player3: Sprite = None
player2: Sprite = None
player1: Sprite = None
game.splash("Ask your friends to join", "Then press A")
scene.set_background_image(img("""
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f
    """))
effects.star_field.start_screen_effect()
player1 = sprites.create(img("""
        . . . . . . . . . . . . .
        . . . f f f f f f . . . .
        . f f f f f f f f f . . .
        . f f f f f f c f f f . .
        f f f f c f f f c f f f .
        f c f f c c f f f c c f f
        f c c f f f f e f f f f f
        f f f f f f f e e f f f .
        f f e e f b f e e f f . .
        . f e 4 e 1 f 4 4 f f . .
        . f f f e e 4 4 4 f . . .
        . . f e 4 4 e e f f . . .
        . . f e 4 4 e 7 7 f . . .
        . f f f e e f 6 6 f f . .
        . f f f f f f f f f f . .
        . . f f . . . f f f . . .
        """),
    SpriteKind.player)
player1.set_position(20, 15)
player1.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
controller.move_sprite(player1, 200, 200)
info.player1.set_life(3)
info.player1.set_score(0)
player2 = sprites.create(img("""
        .......ff...............
        ....ffff2ff.............
        ..ffeeeef2ff............
        .ffeeeeef22ff...........
        .feeeeffeeeef...........
        .fffffee2222ef..........
        fffe222ffffe2f..........
        ffffffffeeefff..........
        fefe44ebf44eef..........
        .fee4d4bfddef...........
        ..feee4dddee.c..........
        ...f2222eeddeccccccc....
        ...f444e44ddecddddd.....
        ...fffffeeee.ccccc......
        ..ffffffff...c..........
        ..fff..ff...............
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        """),
    SpriteKind.player)
player2.set_position(20, 45)
player2.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
controller.player2.move_sprite(player2, 200, 200)
info.player2.set_life(3)
info.player2.set_score(0)
player3 = sprites.create(img("""
        ........................
        ............cc..........
        ............ccc.........
        ........cc..ccccccc.....
        ........ccccc555555cc...
        ........ccb5555555555c..
        .....cc..b555555555555c.
        .....cccb555555ff155555c
        ......cb55555555ff55d55c
        ......b5555555555555555c
        ...cc.b555dd5555bb13bbc.
        ...cccd55ddddd555b3335c.
        ....ccdd5ddddddd55b335c.
        .....bddddb55bdddd5555c.
        ..cccdddddb55bbbbbcccc..
        .ccccddddddb5555cbcccc..
        .cdccdddddddc555cbc55c..
        .cdddddddddddcccbbc5c...
        .cbddddddd55dbbbbccc....
        .ccbdddddd555dbbbcbc....
        ..cccddbbbd555bbccc.....
        ....ccbbbbbd555cc.......
        ......ccccbddddbc.......
        ..........cd5555dc......
        """),
    SpriteKind.player)
player3.set_position(20, 75)
player3.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
controller.player3.move_sprite(player3, 200, 200)
info.player3.set_life(3)
info.player3.set_score(0)
player4 = sprites.create(img("""
        . . . . . . . . . . . . . .
        . . . . . c c c f f f . . .
        . . . f f 5 5 5 5 5 5 f f .
        . . f 5 5 5 5 5 5 5 5 5 f .
        . c 5 5 5 5 5 5 5 5 5 5 5 f
        c 5 5 5 5 5 5 5 5 d b 5 5 f
        f 5 5 5 5 5 5 5 b 4 4 d 5 f
        f 5 5 5 5 5 c c 4 4 4 b 5 f
        f b 5 5 5 b c b c 4 4 f f .
        c b b b b b e 1 c d d f . .
        c b b b b e e d d d d c . .
        . c b b 4 d d e 4 4 4 c . .
        . . c c e d d e 9 9 9 c . .
        . . c b b e e b b b b b c .
        . . . c b 3 3 3 b 3 b 3 c .
        . . . . c c c b b c c c . .
        """),
    SpriteKind.player)
player4.set_position(20, 105)
player4.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
controller.player4.move_sprite(player4, 200, 200)
info.player4.set_life(3)
info.player4.set_score(0)

def on_update_interval():
    global bogey
    if True:
        bogey = sprites.create(img("""
                ........................
                ........................
                ........................
                ........................
                .........fffff..........
                ........f11111ff........
                .......fb111111bf.......
                .......f1111111dbf......
                ......fd111111dddf......
                ......fd11111ddddf......
                ......fd11dddddddf......
                ......f111dddddddf......
                ......f11fcddddddf......
                .....fb1111bdddbf.......
                .....f1b1bdfcfff........
                .....fbfbffffffff.......
                ......fffffffffff.ff....
                ...........ffffffff.....
                ........f1b1bffffff.....
                ........fbfbffffff......
                ........................
                ........................
                ........................
                ........................
                """),
            SpriteKind.enemy)
        bogey.set_velocity(-50, 0)
        bogey.set_position(180, randint(0, 120))
    else:
        pass
game.on_update_interval(500, on_update_interval)
