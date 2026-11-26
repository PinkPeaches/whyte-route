"""Scenes 21-30."""
import math
from lib import *
import lib
from animals_a import feet, arms
from animals_b import body, flakes


# 21 ------------------------------------------------------------ seal pup balancing a bauble
def seal():
    # tail flippers
    for s in (-1, 1):
        blob([(s * 20, -190), (s * 90, -215), (s * 120, -250), (s * 60, -245), (s * 15, -225)], lw=LW)
    # body
    blob([(0, 120), (90, 100), (130, 20), (130, -90), (95, -175), (0, -215), (-95, -175), (-130, -90),
          (-130, 20), (-90, 100)], lw=LW)
    ell(0, -105, 70, 80, lw=LW_FINE)
    # flippers
    for s in (-1, 1):
        blob([(s * 118, -10), (s * 190, -60), (s * 200, -110), (s * 150, -100), (s * 112, -60)], lw=LW)
        for k in (0, 1, 2):
            line(s * (180 + k * 6), -78 - k * 12, s * (192 + k * 6), -84 - k * 12, lw=3) if False else None
    # head
    ell(0, 75, 105, 88)
    ell(0, 52, 52, 36, lw=LW_FINE + 1)
    nose_round(0, 64, 14, 10)
    line(0, 56, 0, 44, lw=4)
    smile(0, 44, 13)
    eyes(0, 95, 46, 12)
    for s in (-1, 1):
        for k in (-1, 0, 1):
            dot(s * 30 + k * 7, 48 + k * 5, 2.8)
    whiskers(0, 48, 56, 12, 50)
    # bauble on nose
    ornament(0, 205, 52, 0)
    # little ice bump
    flakes()
    ground(0, -262, 470, 6)


# 22 ------------------------------------------------------------ otter floating with a gift
def otter():
    # waves
    for yy, off in ((-130, 0), (-190, 40)):
        pts = [(-260 + i * 52, yy + (10 if (i % 2) else -10)) for i in range(11)]
        curve(pts, lw=5)
    # tail
    blob([(150, -10), (230, -30), (255, -10), (230, 20), (150, 25)], lw=LW)
    # body
    blob([(-150, 30), (-60, 70), (60, 66), (160, 40), (170, -20), (120, -70), (0, -80), (-120, -60), (-165, -10)], lw=LW)
    ell(20, -5, 100, 46, lw=LW_FINE)
    # back feet up
    for dy in (-35, 35):
        blob([(150, dy + 8), (195, dy + 24), (215, dy + 4), (190, dy - 14)], lw=LW) if False else None
    # head (looking up)
    ell(-170, 80, 92, 82)
    for s in (-1, 1):
        ell(-170 + s * 70, 150, 22, lw=LW)
    eyes(-170, 100, 38, 11)
    ell(-170, 62, 44, 30, lw=LW_FINE + 1)
    nose_round(-170, 74, 13, 9)
    smile(-170, 50, 12)
    whiskers(-170, 56, 46, 10, 40)
    santa_hat(-165, 146, 120, tilt=-14)
    # paws holding the gift on belly
    gift(-50, -10, 110, 90)
    for s in (-1, 1):
        ell(-50 + (0 if s < 0 else 110), 25, 24, 20)
    snowflake(-180, 280, 34)
    snowflake(130, 230, 28)
    snow_dots([(-60, 230), (230, 140), (-250, 190), (50, 290)])


# 23 ------------------------------------------------------------ raccoon hugging an ornament
def raccoon():
    # ringed tail
    blob([(60, -170), (150, -150), (215, -80), (232, 10), (185, 5), (150, -50), (90, -100)], lw=LW)
    for (x, y, rt) in ((120, -118, -38), (165, -75, -55), (200, -25, -70)):
        C = lib.C
        C.saveState()
        C.translate(x, y)
        C.rotate(rt)
        line(-26, 0, 26, 0, lw=4.5)
        C.restoreState()
    body(88, 106, -115)
    arms(78, -50, -165, 25, 5)
    feet(-208, 48, 38, 22)
    # ears
    for s in (-1, 1):
        ell(s * 82, 140, 34, lw=LW)
        ell(s * 82, 140, 14, lw=3.5)
    ell(0, 55, 108, 86)
    # mask
    blob([(-98, 70), (-60, 98), (-20, 78), (0, 72), (20, 78), (60, 98), (98, 70), (86, 38), (40, 34), (0, 48), (-40, 34), (-86, 38)], lw=LW_FINE + 1)
    eyes(0, 68, 46, 12)
    # muzzle
    ell(0, 14, 40, 30, lw=LW_FINE + 1)
    nose_round(0, 28, 13, 9)
    line(0, 20, 0, 8, lw=4)
    smile(0, 8, 13)
    # holly headband
    holly(-52, 140, .7, 20)
    holly(52, 140, .7, -20)
    # big ornament held in front
    ornament(0, -110, 66, 1)
    for s in (-1, 1):
        ell(s * 62, -95, 25, 21)
    flakes()


# 24 ------------------------------------------------------------ fawn with wreath
def fawn():
    body(88, 106, -115, belly=False)
    # white spots
    for (x, y) in ((-48, -58), (-16, -100), (36, -62), (58, -112), (-60, -128), (6, -148), (-20, -190)):
        ell(x, y, 11, 9, lw=3.5)
    arms(80, -50, -165, 24, 5)
    for s in (-1, 1):
        ell(s * 50, -212, 34, 22)
        line(s * 50, -226, s * 50, -200, lw=4)
    # ears
    for s in (-1, 1):
        blob([(s * 78, 110), (s * 160, 150), (s * 185, 110), (s * 130, 50), (s * 86, 60)], lw=LW)
        blob([(s * 100, 105), (s * 150, 128), (s * 160, 108), (s * 124, 78)], lw=4)
    ell(0, 55, 100, 90)
    # white spots on head top
    for (x, y) in ((-30, 120), (0, 132), (30, 120)):
        ell(x, y, 8, 6, lw=3.5)
    ell(0, 12, 46, 34, lw=LW_FINE + 1)
    nose_round(0, 26, 13, 9)
    line(0, 18, 0, 6, lw=4)
    smile(0, 6, 12)
    eyes(0, 72, 44, 13)
    # wreath collar
    for k in range(-4, 5):
        a = math.radians(270 + k * 18)
        mx, my = 80 * math.cos(a) * 1.1, -26 + 38 * math.sin(a)
        blob([(mx - 14, my), (mx, my + 12), (mx + 14, my), (mx, my - 12)], lw=3.5)
    holly(0, -62, .8, 0)
    tree(-185, -245, 200)
    tree(200, -245, 160, star_top=True)
    snowflake(-60, 290, 30) if False else None
    snow_dots([(-215, 150), (215, 120), (-110, 295), (140, 295)])
    snowflake(-190, 200, 28)
    snowflake(200, 235, 28)


# 25 ------------------------------------------------------------ chick hatching from ornament
def chick():
    # chick body + head (drawn first; the broken bauble covers its lower half)
    for s in (-1, 1):   # wings
        blob([(s * 78, 20), (s * 150, 50), (s * 162, -8), (s * 108, -30)], lw=LW)
    ell(0, 20, 108, 96)
    ell(0, 140, 98, 90)
    curve([(-12, 224), (-4, 262), (8, 230)], lw=6)
    curve([(10, 228), (26, 258), (30, 226)], lw=6)
    eyes(0, 160, 42, 12)
    blob([(-24, 130), (0, 140), (24, 130), (0, 100)], lw=5)
    line(-22, 128, 22, 128, lw=3.5)
    cheeks(0, 122, 72, 10)
    # bauble bottom half, clipped under a zig-zag break line
    zz = [(-176, -10)]
    for i in range(1, 11):
        zz.append((-176 + i * 35.2, -10 if i % 2 == 0 else 40))
    C = lib.C
    C.saveState()
    p = C.beginPath()
    p.moveTo(*zz[0])
    for q in zz[1:]:
        p.lineTo(*q)
    p.lineTo(176, -400)
    p.lineTo(-176, -400)
    p.close()
    C.clipPath(p, stroke=0, fill=0)
    ell(0, -110, 170, 165, lw=LW + 0.5)
    C.restoreState()
    poly(zz, lw=LW + 0.5, closed=False)
    for yy in (-95, -150):
        arc(0, yy, 150, 38, 200, 140, lw=4.5)
    for k in range(-3, 4):
        star(k * 44, -215 if k % 2 == 0 else -230, 13, lw=3.2) if False else None
    # shell scraps
    poly([(-230, -230), (-195, -205), (-215, -180), (-250, -200)], lw=5)
    poly([(215, -240), (250, -220), (225, -195)], lw=5)
    snowflake(-210, 215, 34)
    snowflake(215, 230, 26)
    snow_dots([(-225, 80), (225, 90), (-150, 295), (160, 300)])
    ground(0, -290, 470, 6)


# 26 ------------------------------------------------------------ frog on a gift
def frog():
    # gift under the frog
    gift(-150, -255, 300, 130, bow=False)
    # back legs
    for s in (-1, 1):
        ell(s * 120, -100, 56, 50, rot=s * -20)
        blob([(s * 80, -125), (s * 160, -125), (s * 180, -135), (s * 160, -150), (s * 85, -145)], lw=LW) if False else None
        # toes
        for k in (-1, 0, 1):
            ell(s * 150 + k * 22, -138, 12, 15, lw=4.5)
    body(105, 100, -45)
    arms(80, -20, -95, 24, 10)
    for s in (-1, 1):
        for k in (-1, 0, 1):
            ell(s * 88 + k * 18, -108, 11, 14, lw=4.5)
    # head with eye bumps
    for s in (-1, 1):
        ell(s * 62, 130, 40, lw=LW)
    ell(0, 62, 130, 80)
    for s in (-1, 1):
        ell(s * 62, 132, 40, lw=LW)
        dot(s * 62, 134, 17)
        white_dot(s * 62 + 6, 141, 6)
    # wide mouth
    curve([(-100, 40), (-50, 14), (0, 8), (50, 14), (100, 40)], lw=LW)
    dot(-14, 56, 3.5)
    dot(14, 56, 3.5)
    cheeks(0, 30, 96, 12) if False else None
    for s in (-1, 1):
        ell(s * 92, 28, 12, 9, lw=3.5)
    # holly bow tie
    holly(0, -2, .9, 0)
    # lights around
    lights([(-230, 270), (-150, 235), (-70, 255), (20, 285), (110, 258), (190, 232), (245, 260)], 10)
    snowflake(-210, 140, 30) if False else None
    snow_dots([(-215, 195), (215, 190), (-240, 0), (240, -10)])


# 27 ------------------------------------------------------------ hippo with antlers
def hippo():
    body(105, 105, -110)
    arms(98, -45, -160, 28, 8)
    feet(-208, 60, 40, 24)
    for s in (-1, 1):
        for k in (-1, 0, 1):
            pass
    # antlers headband
    for s in (-1, 1):
        curve([(s * 40, 155), (s * 70, 215), (s * 90, 262)], lw=10)
        curve([(s * 62, 205), (s * 110, 210)], lw=8)
        curve([(s * 80, 245), (s * 52, 262)], lw=8)
    curve([(-95, 150), (0, 178), (95, 150)], lw=8)
    # ears
    for s in (-1, 1):
        ell(s * 96, 140, 26, lw=LW)
        ell(s * 96, 140, 11, lw=3.5)
    ell(0, 62, 125, 98)
    # big muzzle
    blob([(-95, 32), (-85, 62), (0, 70), (85, 62), (95, 32), (80, -26), (0, -48), (-80, -26)], lw=LW_FINE + 1)
    for s in (-1, 1):
        ell(s * 38, 42, 12, 9, lw=4)
    arc(-22, -4, 22, 16, 200, 140, lw=4.5)
    arc(22, -4, 22, 16, 200, 140, lw=4.5)
    for s in (-1, 1):
        rrect(s * 28 - 8, -26, 16, 18, r=3, lw=3.5) if False else None
    eyes(0, 108, 52, 12)
    cheeks(0, 20, 108, 10) if False else None
    # bell collar
    blob([(-80, -28), (0, -48), (80, -28), (76, -10), (0, -30), (-76, -10)], lw=5)
    bell(0, -56, 16)
    gift(-250, -260, 100, 90, pattern=1) if False else None
    flakes()
    ground(0, -250, 440, 6)


# 28 ------------------------------------------------------------ monkey with baubles
def monkey():
    # tail
    curve([(70, -170), (150, -180), (205, -130), (200, -60), (160, -20), (130, -50)], lw=9)
    body(88, 104, -115)
    arms(78, -45, -140, 25, 5)
    feet(-208, 50, 40, 22)
    # ears
    for s in (-1, 1):
        ell(s * 118, 55, 40, lw=LW)
        ell(s * 118, 55, 20, lw=4)
    ell(0, 62, 108, 92)
    # face mask (heart-ish)
    blob([(0, 100), (40, 118), (80, 100), (88, 55), (60, 5), (0, -22), (-60, 5), (-88, 55), (-80, 100), (-40, 118)], lw=LW_FINE + 1)
    eyes(0, 70, 38, 12)
    dot(-8, 40, 4)
    dot(8, 40, 4)
    arc(-0, 14, 26, 18, 205, 130, lw=4.5)
    # baubles held up
    ornament(-150, -72, 34, 2)
    ornament(150, -72, 34, 0)
    ell(-118, -108, 22, 18)
    ell(118, -108, 22, 18)
    # garland of stars across top
    curve([(-235, 250), (-120, 215), (0, 250), (120, 215), (235, 250)], lw=4)
    for (x, y) in ((-170, 240), (-60, 232), (60, 232), (170, 240)):
        star(x, y - 16, 20, lw=4)
    snow_dots([(-215, 130), (215, 140), (-240, -20), (240, -20)])
    snowflake(-205, 80, 24)
    snowflake(210, 60, 24) if False else None


# 29 ------------------------------------------------------------ tiger cub in a sweater
def tiger():
    # tail
    blob([(70, -170), (150, -176), (205, -130), (212, -55), (190, -40), (176, -85), (150, -122), (70, -128)], lw=LW)
    for (x, y, r) in ((118, -148, 80), (160, -146, 60), (192, -110, 20), (196, -70, 5)):
        lib.C.saveState(); lib.C.translate(x, y); lib.C.rotate(r)
        line(-4, -18, -4, 16, lw=5)
        lib.C.restoreState()
    body(90, 106, -115, belly=False)
    # sweater band
    blob([(-88, -60), (-40, -48), (40, -48), (88, -60), (86, -150), (0, -176), (-86, -150)], lw=LW_FINE + 1)
    star(0, -112, 26, lw=4.5)
    for k in (-2, -1, 1, 2):
        ell(k * 40, -112 + (14 if abs(k) == 1 else -14), 6, lw=3.5)
    arms(80, -50, -165, 26, 5)
    feet(-208, 50)
    for s in (-1, 1):  # arm stripes
        line(s * 70, -80, s * 96, -86, lw=4)
        line(s * 70, -110, s * 96, -116, lw=4)
    # ears
    for s in (-1, 1):
        ell(s * 92, 140, 32, lw=LW)
        ell(s * 92, 140, 14, lw=3.5)
    ell(0, 55, 112, 92)
    # forehead stripes
    for dx in (-26, 0, 26):
        line(dx, 140, dx, 122 if dx else 116, lw=5)
    for s in (-1, 1):
        line(s * 100, 62, s * 76, 68, lw=5)
        line(s * 104, 38, s * 80, 44, lw=5)
        line(s * 98, 86, s * 76, 90, lw=5)
    # muzzle
    ell(0, 12, 52, 32, lw=LW_FINE + 1)
    nose_tri(0, 28, 12)
    line(0, 22, 0, 8, lw=4)
    arc(-12, 6, 12, 10, 200, 140, lw=4.5)
    arc(12, 6, 12, 10, 200, 140, lw=4.5)
    eyes(0, 72, 44, 12)
    flakes()
    gift(-250, -260, 100, 90) if False else None
    snow_dots([(-215, -100), (220, -20)])


# 30 ------------------------------------------------------------ llama with festive blanket
def llama():
    # legs
    for x in (-50, 50):
        rrect(x - 22, -255, 44, 130, r=14, lw=LW)
        rrect(x - 26, -266, 52, 26, r=12, lw=LW)
    # neck first
    blob([(-52, -20), (-50, 60), (-42, 150), (42, 150), (50, 60), (52, -20)], lw=LW)
    # fluffy body
    ell(0, -92, 128, 84)
    for k in range(-2, 3):
        arc(k * 44, -34, 24, 16, 200, 140, lw=4) if False else None
    # festive blanket
    rrect(-80, -128, 160, 60, r=10, lw=LW_FINE + 1)
    for k in range(-3, 4):
        poly([(k * 22 - 10, -128), (k * 22, -142), (k * 22 + 10, -128)], lw=3.5) if False else None
    for k in range(-3, 4):
        star(k * 22, -98, 8, lw=3) if k % 2 == 0 else ell(k * 22, -98, 5, lw=3)
    for k in range(-3, 4):
        line(k * 22 - 10, -128, k * 22 - 10, -140, lw=3.5)
    # ears
    for s in (-1, 1):
        blob([(s * 30, 240), (s * 70, 316), (s * 96, 296), (s * 76, 236)], lw=LW)
    # head tuft + head
    ell(0, 215, 68, 70)
    pts = [(-52, 262), (-30, 292), (-8, 270), (14, 294), (34, 268), (56, 288), (60, 258), (30, 246), (-30, 246)]
    blob(pts, lw=LW)
    ell(0, 180, 44, 32, lw=LW_FINE + 1)
    nose_tri(0, 192, 9)
    smile(0, 178, 10)
    eyes(0, 226, 28, 11)
    # bell collar
    blob([(-50, 148), (0, 138), (50, 148), (50, 164), (0, 156), (-50, 164)], lw=4.5)
    bell(0, 126, 14)
    holly(-70, 40, .0001, 0) if False else None
    # tail
    curve([(110, -80), (140, -60), (138, -110)], lw=7) if False else None
    snowflake(-195, 190, 34)
    snowflake(200, 230, 28)
    snow_dots([(-210, 40), (210, 60), (-150, 295), (150, 305), (-200, -80), (200, -120)])
    ground(0, -272, 440, 6)
    holly(160, -240, .8, -10)


SCENES_C = [
    ("Seal pup balancing a bauble", seal),
    ("Otter floating with a gift", otter),
    ("Raccoon hugging a big ornament", raccoon),
    ("Fawn with wreath collar", fawn),
    ("Chick hatching from an ornament", chick),
    ("Frog on a gift", frog),
    ("Hippo calf with antlers", hippo),
    ("Monkey with baubles", monkey),
    ("Tiger cub in a Christmas sweater", tiger),
    ("Llama with festive blanket", llama),
]
