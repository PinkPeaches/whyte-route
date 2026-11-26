"""Scenes 11-20."""
import math
from lib import *
import lib
from animals_a import feet, arms


def body(rx=92, ry=108, cy=-115, belly=True):
    ell(0, cy, rx, ry)
    if belly:
        ell(0, cy - 8, rx * .58, ry * .68, lw=LW_FINE)


def flakes(extra=()):
    snowflake(-205, 190, 34)
    snowflake(210, 230, 26)
    snow_dots([(-215, 60), (215, 90), (-150, 290), (150, 300)] + list(extra))


# 11 ------------------------------------------------------------ elephant wrapped in lights
def elephant():
    body(100, 112, -112)
    arms(92, -50, -165, 28, 8)
    for s in (-1, 1):
        ell(s * 60, -210, 40, 24)
        for k in (-1, 0, 1):
            line(s * 60 + k * 14, -214, s * 60 + k * 14, -202, lw=3.5)
    # ears
    for s in (-1, 1):
        blob([(s * 90, 120), (s * 170, 170), (s * 235, 120), (s * 235, 40), (s * 175, -10), (s * 110, 30)], lw=LW)
        blob([(s * 120, 100), (s * 175, 130), (s * 205, 100), (s * 200, 55), (s * 160, 30), (s * 125, 50)], lw=4)
    ell(0, 85, 112, 98)
    # trunk
    blob([(-34, 70), (-36, 0), (-34, -50), (-10, -88), (36, -92), (62, -62), (44, -40), (30, -58),
          (12, -56), (4, -20), (34, 70)], lw=LW)
    for yy in (30, -5):
        line(-35, yy, 15, yy, lw=3.5)
    # tusks
    for s in (-1, 1):
        blob([(s * 48, 30), (s * 62, -4), (s * 58, -24), (s * 40, -4)], lw=4.5)
    eyes(0, 118, 52, 12)
    cheeks(0, 82, 80, 11)
    for s in (-1, 1):   # forehead wrinkle
        pass
    curve([(-14, 168), (0, 180), (14, 168)], lw=4)
    # garland of lights across the top of the page
    lights([(-235, 290), (-170, 262), (-100, 252), (-30, 268), (40, 292), (110, 296), (180, 272), (240, 262)], 10)
    ornament(-150, -150, 22, 2) if False else None
    gift(130, -250, 110, 95, pattern=1)
    star(-185, -215, 34, lw=5)
    flakes()


# 12 ------------------------------------------------------------ lion cub with holly crown
def lion():
    # tail
    curve([(70, -170), (150, -160), (190, -110), (180, -60)], lw=9)
    ell(182, -48, 20, 26, lw=5)
    body(88, 105, -118)
    arms(80, -50, -165, 26, 5)
    feet(-208, 50)
    # mane tufts
    pts = []
    n = 18
    for i in range(n):
        a = math.radians(i * 360 / n)
        r = 160 if i % 2 == 0 else 128
        pts.append((r * math.cos(a), 62 + r * math.sin(a) * .95))
    poly(pts, lw=LW)
    # ears
    for s in (-1, 1):
        ell(s * 82, 148, 30, lw=LW)
        ell(s * 82, 148, 13, lw=3.5)
    ell(0, 55, 92, 82)
    # muzzle
    ell(-24, 5, 32, 24, lw=LW_FINE + 1)
    ell(24, 5, 32, 24, lw=LW_FINE + 1)
    nose_tri(0, 28, 13)
    line(0, 22, 0, 8, lw=4)
    arc(-14, 6, 14, 12, 200, 140, lw=4.5)
    arc(14, 6, 14, 12, 200, 140, lw=4.5)
    eyes(0, 72, 40, 12)
    curve([(-60, 98), (-40, 108), (-20, 100)], lw=4) if False else None
    # holly crown
    holly(-62, 138, .75, 25)
    holly(62, 138, .75, -25)
    holly(0, 140, .0001, 0) if False else None
    ornament(-175, 120, 22, 0) if False else None
    flakes()
    gift(-250, -260, 100, 90)


# 13 ------------------------------------------------------------ giraffe calf
def giraffe():
    # legs
    for x in (-62, 62):
        rrect(x - 22, -250, 44, 140, r=14, lw=LW)
        rrect(x - 26, -262, 52, 26, r=12, lw=LW)
    # neck
    blob([(-48, -40), (-44, 40), (-40, 130), (-40, 200), (40, 200), (40, 130), (44, 40), (48, -40)], lw=LW)
    # body
    ell(0, -90, 118, 80)
    # spots
    for (x, y, r) in ((-72, -75, 18), (30, -110, 15), (82, -60, 16), (-24, -50, 12), (-22, 20, 14), (18, 80, 13), (-20, 140, 12)):
        ell(x, y, r, r * .85, lw=4, rot=20)
    # tail
    curve([(115, -70), (150, -60), (158, -110)], lw=6)
    ell(158, -120, 10, 16, lw=4)
    # ossicones + ears
    for s in (-1, 1):
        line(s * 26, 262, s * 30, 296, lw=7)
        ell(s * 30, 302, 12, lw=4.5)
        blob([(s * 54, 232), (s * 120, 248), (s * 122, 222), (s * 62, 208)], lw=LW)
    # head
    ell(0, 225, 66, 56)
    ell(0, 198, 46, 32, lw=LW_FINE + 1)
    for s in (-1, 1):
        dot(s * 14, 204, 4)
    eyes(0, 240, 34, 11)
    arc(-9, 184, 9, 8, 200, 140, lw=4)
    arc(9, 184, 9, 8, 200, 140, lw=4)
    scarf(0, 100, 130, 100, side=1)
    star(-185, 250, 38, lw=5)
    snowflake(195, 200, 34)
    snow_dots([(-200, 80), (200, 60), (-190, -80), (200, -150)])
    ground(0, -266, 440, 6)


# 14 ------------------------------------------------------------ koala with gift
def koala():
    body(92, 108, -115)
    # big fluffy ears
    for s in (-1, 1):
        ell(s * 112, 98, 56, lw=LW)
        ell(s * 112, 98, 32, lw=4)
        for k in (-1, 0, 1):
            curve([(s * 112 + k * 12, 118), (s * 112 + k * 12 + 3, 98), (s * 112 + k * 12, 78)], lw=3) if False else None
    ell(0, 55, 100, 88)
    # nose
    blob([(-26, 55), (-30, 28), (0, 14), (30, 28), (26, 55), (0, 64)], lw=LW)
    dot(0, 40, 12)
    white_dot(4, 44, 3.5)
    arc(-10, 4, 10, 9, 200, 140, lw=4.5)
    arc(10, 4, 10, 9, 200, 140, lw=4.5)
    line(0, 24, 0, 8, lw=4) if False else None
    eyes(0, 82, 46, 11)
    cheeks(0, 30, 74, 10) if False else None
    elf_hat(10, 125, 120, tilt=8)
    feet(-208, 52)
    # gift in lap
    gift(-60, -170, 120, 95)
    for s in (-1, 1):
        ell(s * 62, -122, 28, 26)
    # eucalyptus leaves
    for (x, y, rt) in ((-190, -150, 30), (-170, -210, -10)):
        blob([(x, y), (x + 20, y + 30), (x + 70, y + 40), (x + 25, y + 10)], lw=4.5)
    flakes()


# 15 ------------------------------------------------------------ mouse in a mug
def mouse():
    # ears
    for s in (-1, 1):
        ell(s * 92, 190, 62, lw=LW)
        ell(s * 92, 190, 38, lw=4)
    # head
    ell(0, 105, 100, 90)
    eyes(0, 125, 40, 12)
    nose_round(0, 98, 11, 8)
    line(0, 90, 0, 80, lw=4)
    smile(0, 80, 13)
    whiskers(0, 90, 62, 10, 45)
    cheeks(0, 82, 76, 10) if False else None
    # paws on rim
    for s in (-1, 1):
        ell(s * 56, 5, 30, 24)
        for k in (-1, 1):
            line(s * 56 + k * 8, 2, s * 56 + k * 8, 14, lw=3.5)
    # candy cane in mug
    candy_cane(90, -60, 210, lean=18, w=16)
    # tail
    curve([(-120, -230), (-210, -250), (-245, -200), (-215, -160)], lw=8)
    mug(-10, -250, 250, 230)
    # mug decoration
    holly(-10, -125, 1.1)
    for x in (-95, 80):
        star(x, -70, 20, lw=3.5)
    snowflake(-205, 215, 34)
    snowflake(205, 245, 26)
    snow_dots([(-220, 90), (220, 150), (-140, 290)])


# 16 ------------------------------------------------------------ squirrel with bauble
def squirrel():
    # big tail behind
    blob([(60, -170), (150, -170), (215, -90), (225, 10), (200, 110), (150, 170), (110, 120), (130, 50),
          (110, -20), (70, -80)], lw=LW)
    curve([(165, 120), (180, 50), (170, -30)], lw=4) if False else None
    for yy in (-60, 0, 60, 110):
        curve([(150, yy), (175, yy + 18)], lw=3.5)
    body(86, 105, -118)
    arms(78, -50, -150, 25, 5)
    feet(-208, 48, 38, 22)
    # ears with tufts
    for s in (-1, 1):
        blob([(s * 52, 125), (s * 80, 220), (s * 112, 140), (s * 110, 112)], lw=LW)
        curve([(s * 80, 220), (s * 82, 245)], lw=5)
    ell(0, 55, 108, 86)
    ell(0, 15, 40, 30, lw=LW_FINE + 1)
    nose_round(0, 28, 11, 8)
    line(0, 20, 0, 10, lw=4)
    smile(0, 10, 13, open_mouth=True)
    # buck teeth
    eyes(0, 72, 46, 12)
    cheeks(0, 28, 76, 12)
    holly(-60, 118, .7, 25)
    # bauble held up
    ornament(60, -90, 38, 0)
    ell(40, -112, 22, 18)
    ell(80, -112, 22, 18)
    flakes()
    snowflake(-200, -80, 22)


# 17 ------------------------------------------------------------ duckling in a wreath
def duckling():
    # body & wing
    ell(0, -80, 110, 112)
    blob([(-95, -40), (-140, -90), (-120, -160), (-70, -150), (-60, -90)], lw=LW)
    blob([(95, -40), (140, -90), (120, -160), (70, -150), (60, -90)], lw=LW)
    # head
    ell(0, 105, 96, 86)
    # head tuft
    curve([(-8, 188), (0, 215), (12, 190)], lw=6)
    eyes(0, 125, 38, 12)
    # beak
    blob([(-48, 92), (-40, 74), (0, 64), (40, 74), (48, 92), (0, 100)], lw=LW)
    line(-36, 82, 36, 82, lw=3.5)
    cheeks(0, 88, 76, 9) if False else None
    # feet
    for s in (-1, 1):
        blob([(s * 30, -180), (s * 90, -196), (s * 100, -214), (s * 60, -218), (s * 20, -208)], lw=LW)
        for k in (0, 1):
            line(s * (50 + k * 26), -198, s * (52 + k * 28), -216, lw=3.5)
    # wreath ring around the little duck
    ell(0, -10, 205, 215, fill=False, lw=LW + 1)
    ell(0, -10, 168, 178, fill=False, lw=LW + 1)
    for k in range(18):
        a = math.radians(k * 20 + 10)
        mx, my = 186 * math.cos(a), -10 + 196 * math.sin(a)
        blob([(mx - 14, my), (mx, my + 16), (mx + 14, my), (mx, my - 16)], lw=3.5)
    # bow at the bottom
    by = -205
    blob([(0, by), (-50, by + 28), (-62, by - 8), (-14, by - 14)], lw=5)
    blob([(0, by), (50, by + 28), (62, by - 8), (14, by - 14)], lw=5)
    ell(0, by + 2, 14, lw=5)
    for (x, y) in ((-150, 130), (155, 110), (-110, -170)):
        ell(x, y, 12, lw=4.5)
    snowflake(-235, 230, 22) if False else None
    snow_dots([(-240, 270), (240, 285), (-250, 20), (250, -90)])


# 18 ------------------------------------------------------------ lamb
def lamb():
    # fluffy body
    pts = []
    n = 16
    for i in range(n):
        a = math.radians(i * 360 / n)
        r = 126 if i % 2 == 0 else 112
        pts.append((r * 1.0 * math.cos(a), -110 + r * 1.05 * math.sin(a)))
    blob(pts, lw=LW)
    for s in (-1, 1):
        ell(s * 52, -218, 36, 24)
        line(s * 52, -232, s * 52, -206, lw=4)
    arms(78, -60, -160, 24, 6)
    # ears sideways
    for s in (-1, 1):
        blob([(s * 60, 90), (s * 140, 100), (s * 168, 76), (s * 130, 52), (s * 70, 56)], lw=LW)
        blob([(s * 84, 84), (s * 130, 88), (s * 142, 76), (s * 118, 64)], lw=4)
    ell(0, 55, 82, 92)
    # woolly forehead tuft
    pts = [(-70, 120), (-44, 150), (-20, 130), (0, 158), (22, 130), (46, 150), (70, 120), (40, 110), (0, 114), (-40, 110)]
    blob(pts, lw=LW)
    eyes(0, 72, 36, 12)
    ell(0, 14, 40, 30, lw=LW_FINE + 1)
    nose_tri(0, 28, 10)
    line(0, 22, 0, 8, lw=4)
    arc(-9, 6, 10, 9, 200, 140, lw=4.5)
    arc(9, 6, 10, 9, 200, 140, lw=4.5)
    holly(-45, 138, .65, 30)
    holly(45, 138, .65, -30)
    # bell collar
    blob([(-52, -32), (0, -48), (52, -32), (50, -18), (0, -32), (-50, -18)], lw=5)
    bell(0, -56, 14)
    flakes()
    ground(0, -250, 440, 6)


# 19 ------------------------------------------------------------ piglet with gingerbread cookie
def piglet():
    # curly tail
    curve([(80, -170), (130, -160), (140, -120), (110, -110), (118, -90)], lw=7)
    body(92, 108, -115)
    arms(80, -50, -160, 26, 5)
    feet(-208, 50, 38, 22)
    # ears
    for s in (-1, 1):
        poly([(s * 52, 125), (s * 128, 190), (s * 130, 95)], lw=LW)
        poly([(s * 72, 132), (s * 112, 168), (s * 112, 118)], lw=4)
    ell(0, 55, 112, 92)
    # snout
    ell(0, 22, 52, 36, lw=LW)
    for s in (-1, 1):
        ell(s * 18, 22, 8, 12, lw=4)
    eyes(0, 82, 46, 12)
    arc(-0, 6, 20, 14, 205, 130, lw=4.5)
    cheeks(0, 38, 84, 12) if False else None
    elf_hat(0, 138, 110, tilt=-8) if False else None
    # elf hat
    elf_hat(0, 130, 120, tilt=0)
    # cookie in hand
    cookie_person(125, -95, 1.15)
    ell(88, -100, 24, 20)
    flakes()


# 20 ------------------------------------------------------------ polar bear cub on a sled
def polar_bear():
    sled(0, -250, 380)
    body(95, 100, -150, belly=False)
    arms(98, -85, -170, 26, 10)
    # feet over sled
    for s in (-1, 1):
        ell(s * 72, -205, 44, 24)
        for k in (-1, 1):
            line(s * 72 + k * 12, -208, s * 72 + k * 12, -196, lw=3.5)
    # ears small
    for s in (-1, 1):
        ell(s * 92, 138, 30, lw=LW)
        ell(s * 92, 138, 13, lw=3.5)
    # earmuff band
    curve([(-96, 128), (-60, 205), (60, 205), (96, 128)], lw=9)
    ell(0, 48, 112, 92)
    for s in (-1, 1):
        ell(s * 108, 82, 34, lw=LW)         # muffs
    # snout
    ell(0, 18, 50, 38, lw=LW_FINE + 1)
    nose_round(0, 32, 14, 10)
    line(0, 24, 0, 8, lw=4)
    smile(0, 8, 14)
    eyes(0, 66, 42, 11)
    # gifts on sled
    gift(110, -210, 100, 85)
    gift(-215, -210, 80, 70, pattern=1)
    snowflake(-205, 215, 34)
    snowflake(205, 230, 26)
    snow_dots([(-215, 90), (215, 110), (-130, 290), (140, 295)])


SCENES_B = [
    ("Baby elephant wrapped in lights", elephant),
    ("Lion cub with holly crown", lion),
    ("Giraffe calf with a scarf", giraffe),
    ("Koala in an elf hat with a gift", koala),
    ("Mouse in a mug with candy cane", mouse),
    ("Squirrel holding a bauble", squirrel),
    ("Duckling in a wreath", duckling),
    ("Lamb with holly and a bell", lamb),
    ("Piglet with a gingerbread cookie", piglet),
    ("Polar bear cub on a sled", polar_bear),
]
