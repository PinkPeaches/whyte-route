"""Scenes 1-10. Each scene draws around (0,0); roughly x in [-250,250], y in [-300,300]."""
import math
from lib import *
import lib


def feet(y=-212, dx=50, rx=38, ry=23, toe=True):
    for s in (-1, 1):
        ell(s * dx, y, rx, ry)
        if toe:
            for k in (-1, 1):
                line(s * dx + k * 11, y - 4, s * dx + k * 11, y + 9, lw=3.5)


def front_legs(dx=52, top=-70, bot=-205, w=30):
    for s in (-1, 1):
        blob([(s * (dx - w), top), (s * (dx + w), top), (s * (dx + w + 4), bot + 20),
              (s * dx, bot + 38), (s * (dx - w - 4), bot + 20)], lw=LW)


# 1 ------------------------------------------------------------- kitten in stocking
def kitten_stocking():
    # chest, then head, then stocking in front
    ell(0, 105, 75, 62)
    # ears
    for s in (-1, 1):
        poly([(s * 38, 215), (s * 118, 285), (s * 128, 190)], lw=LW)
        poly([(s * 62, 218), (s * 104, 256), (s * 108, 212)], lw=4)
    ell(0, 185, 128, 100)
    # forehead stripes
    for dx in (-22, 0, 22):
        line(dx, 275 if dx == 0 else 268, dx, 252 if dx == 0 else 247, lw=4.5)
    eyes(0, 195, 52, 13)
    nose_tri(0, 160, 10)
    line(0, 150, 0, 140, lw=4)
    smile(0, 140, 16)
    whiskers(0, 150, 82, 16, 50)
    cheeks(0, 150, 100, 11) if False else None
    stocking(0, 45, 1.65)
    for s in (-1, 1):   # paws resting on the cuff
        ell(s * 72, 100, 34, 26)
        line(s * 72 - 8, 96, s * 72 - 8, 108, lw=3.5)
        line(s * 72 + 8, 96, s * 72 + 8, 108, lw=3.5)
    # candy canes poking out? keep clean; gifts + snow on the ground
    gift(150, -285, 100, 85, pattern=1)
    ornament(-185, 10, 26, 1)
    snowflake(-195, 190, 34)
    snowflake(205, 120, 28)
    snow_dots([(-215, 105), (222, 215), (-130, 300), (160, 300)])


# 2 ------------------------------------------------------------- puppy in Santa hat
def puppy_santa():
    # tail
    curve([(70, -175), (140, -170), (170, -120), (150, -90)], lw=9)
    # body + haunch
    ell(0, -115, 92, 108)
    ell(-86, -172, 46, 52)
    ell(86, -172, 46, 52)
    front_legs(48, -70, -200, 28)
    feet(-205, 52)
    # collar + bell
    blob([(-70, -30), (0, -52), (70, -30), (66, -10), (0, -32), (-66, -10)], lw=5)
    bell(0, -58, 15)
    # ears behind head
    blob([(-95, 105), (-150, 80), (-172, 10), (-146, -35), (-105, 20)], lw=LW)
    blob([(95, 105), (150, 80), (172, 10), (146, -35), (105, 20)], lw=LW)
    ell(0, 55, 118, 98)
    # muzzle
    ell(0, 15, 56, 42)
    nose_round(0, 38, 14, 10)
    line(0, 28, 0, 14, lw=4)
    smile(0, 14, 16, open_mouth=True)
    eyes(0, 80, 46, 13)
    # brows
    arc(-46, 100, 18, 8, 30, 120, lw=4)
    arc(46, 100, 18, 8, 30, 120, lw=4)
    # spots
    santa_hat(-6, 130, 150, tilt=-12)
    gift(120, -250, 120, 100)
    snowflake(-200, 140, 34)
    snowflake(200, 215, 26)
    snow_dots([(-215, 40), (-130, 250), (210, 40)])


# 3 ------------------------------------------------------------- baby reindeer
def reindeer():
    # antlers behind head
    for s in (-1, 1):
        curve([(s * 50, 140), (s * 80, 200), (s * 112, 245), (s * 130, 300)], lw=11)
        curve([(s * 88, 215), (s * 140, 215), (s * 172, 245)], lw=9)
        curve([(s * 110, 250), (s * 90, 285)], lw=9)
    # body
    ell(0, -115, 92, 108)
    ell(0, -125, 55, 70)  # tummy
    front_legs(48, -70, -200, 27)
    for s in (-1, 1):  # hooves
        ell(s * 50, -212, 36, 22)
        line(s * 50, -228, s * 50, -200, lw=4)
    # ears
    for s in (-1, 1):
        blob([(s * 100, 70), (s * 170, 100), (s * 190, 60), (s * 140, 20), (s * 100, 35)], lw=LW)
        blob([(s * 118, 65), (s * 160, 82), (s * 166, 62), (s * 132, 45)], lw=4)
    ell(0, 55, 112, 98)
    # muzzle
    ell(0, 5, 62, 46)
    ell(0, 25, 24, 18, lw=5.5)   # big round nose
    smile(0, -8, 16)
    eyes(0, 80, 46, 13)
    # forehead tuft
    curve([(-12, 148), (0, 168), (12, 148)], lw=5)
    # jingle collar with holly
    blob([(-74, -28), (0, -50), (74, -28), (70, -8), (0, -30), (-70, -8)], lw=5)
    bell(0, -56, 16)
    holly(-48, -22, .5, -10)
    snowflake(-200, 190, 36)
    snowflake(210, 100, 30)
    snow_dots([(-215, 60), (215, 230), (-140, 280), (150, 300), (-220, -60)])
    ground(0, -245, 440, 6)


# 4 ------------------------------------------------------------- penguin chick, scarf
def penguin():
    # flippers behind
    for s in (-1, 1):
        blob([(s * 118, 40), (s * 175, -40), (s * 185, -120), (s * 140, -90), (s * 110, -20)], lw=LW)
    # body
    blob([(0, 200), (80, 175), (125, 90), (140, -30), (110, -140), (50, -205), (0, -215),
          (-50, -205), (-110, -140), (-140, -30), (-125, 90), (-80, 175)], lw=LW)
    # belly
    blob([(0, 70), (60, 20), (88, -60), (66, -150), (0, -190), (-66, -150), (-88, -60), (-60, 20)], lw=LW_FINE + 1)
    # feet
    for s in (-1, 1):
        blob([(s * 30, -212), (s * 88, -228), (s * 100, -250), (s * 60, -252), (s * 20, -240)], lw=LW)
        line(s * 52, -230, s * 52, -250, lw=3.5)
        line(s * 76, -234, s * 82, -250, lw=3.5)
    # face
    eyes(0, 140, 38, 13)
    # beak
    blob([(-24, 112), (0, 128), (24, 112), (0, 80)], lw=5)
    line(-22, 110, 22, 110, lw=3.5)
    cheeks(0, 100, 62, 10)
    # chest fluff tufts
    for dx, dy in ((-30, -40), (30, -60), (0, -100)):
        curve([(dx - 10, dy), (dx, dy - 10), (dx + 10, dy)], lw=3.5)
    scarf(0, 62, 190, 100, side=1)
    snowflake(-210, 190, 34)
    snowflake(205, 215, 28)
    snowflake(215, 60, 22)
    snow_dots([(-225, 80), (-165, 270), (170, 300), (-222, -80)])
    ground(0, -262, 470, 6)


# 5 ------------------------------------------------------------- bunny with candy cane
def bunny():
    # ears
    for s in (-1, 1):
        blob([(s * 45, 130), (s * 85, 215), (s * 90, 300), (s * 55, 325), (s * 22, 270), (s * 18, 160)], lw=LW)
        blob([(s * 55, 175), (s * 72, 230), (s * 68, 285), (s * 52, 280), (s * 40, 215)], lw=4)
    # tail puff
    ell(105, -180, 30, lw=LW)
    # body
    ell(0, -115, 92, 108)
    ell(0, -125, 55, 72, lw=LW_FINE)
    # big hind feet
    for s in (-1, 1):
        ell(s * 78, -215, 52, 26)
        for k in (-1, 0, 1):
            line(s * 78 + k * 16, -222, s * 78 + k * 16, -208, lw=3.5)
    # head
    ell(0, 55, 118, 98)
    eyes(0, 80, 46, 13)
    cheeks(0, 38, 68, 12)
    nose_tri(0, 52, 9)
    line(0, 44, 0, 32, lw=4)
    smile(0, 32, 16)
    # buck teeth
    rrect(-12, -6, 12, 22, r=3, lw=4)
    rrect(0, -6, 12, 22, r=3, lw=4)
    # whisker dots
    for s in (-1, 1):
        for k in (-1, 1):
            dot(s * 30 + k * 6, 40 + k * 4, 2.8)
    # candy cane held in paws
    candy_cane(112, -235, 270, lean=0, w=18)
    for s in (-1, 1):
        pass
    ell(76, -80, 34, 28)
    ell(112, -60, 34, 28)
    holly(-150, -200, .9, 20)
    snowflake(-200, 150, 34)
    snowflake(200, 235, 26)
    snow_dots([(-215, 40), (-160, 280), (215, -20)])


# 6 ------------------------------------------------------------- bear cub peeking from gift box
def bear_gift():
    # head
    for s in (-1, 1):
        ell(s * 105, 205, 44, lw=LW)
        ell(s * 105, 205, 22, lw=4)
    ell(0, 120, 128, 108)
    ell(0, 82, 56, 42)           # muzzle
    nose_round(0, 100, 17, 12)
    line(0, 90, 0, 76, lw=4)
    smile(0, 76, 17)
    eyes(0, 140, 50, 13)
    cheeks(0, 100, 92, 11)
    # paws on rim
    for s in (-1, 1):
        ell(s * 88, 5, 40, 30)
        for k in (-1, 0, 1):
            line(s * 88 + k * 14, 5, s * 88 + k * 14, 18, lw=3.5)
    # box (front)
    rrect(-170, -250, 340, 215, r=10, lw=LW + 0.5)
    rrect(-190, -50, 380, 55, r=12, lw=LW + 0.5)    # rim/lid band
    rrect(-24, -250, 48, 250, r=3, lw=4.5)          # ribbon
    for fx in (-120, -70, 70, 120):
        star(fx, -140, 20, lw=3.5)
    # bow at the front
    cy = -22
    blob([(0, cy), (-60, cy + 38), (-76, cy + 4), (-20, cy - 8)], lw=5)
    blob([(0, cy), (60, cy + 38), (76, cy + 4), (20, cy - 8)], lw=5)
    ell(0, cy + 3, 15, lw=5)
    # lid leaning on right
    snowflake(-210, 220, 34)
    snowflake(215, 120, 28)
    snow_dots([(-225, 100), (210, 250), (-160, 295)])


# 7 ------------------------------------------------------------- fox kit with scarf by tree
def fox():
    # tail behind
    blob([(60, -170), (150, -140), (225, -80), (240, -10), (200, -40), (150, -70), (90, -110)], lw=LW)
    curve([(205, -30), (220, -70), (200, -100)], lw=4.5)
    # body
    ell(0, -115, 88, 106)
    ell(0, -120, 48, 74, lw=LW_FINE)
    front_legs(46, -70, -200, 26)
    feet(-208, 48, 36, 22)
    # ears
    for s in (-1, 1):
        poly([(s * 52, 130), (s * 126, 250), (s * 138, 120)], lw=LW)
        poly([(s * 76, 140), (s * 118, 208), (s * 122, 138)], lw=4.5)
    # cheek tufts
    for s in (-1, 1):
        poly([(s * 88, 40), (s * 168, 20), (s * 150, -10), (s * 160, -40), (s * 80, -20)], lw=LW)
    ell(0, 55, 108, 90)
    # white muzzle
    blob([(-60, 30), (-62, -4), (-30, -34), (0, -50), (30, -34), (62, -4), (60, 30), (0, 52)], lw=LW_FINE + 1)
    nose_round(0, -38, 15, 11)
    smile(0, -52, 14) if False else None
    arc(-10, -50, 14, 12, 200, 140, lw=4.5)
    arc(10, -50, 14, 12, 200, 140, lw=4.5)
    line(0, -48, 0, -38, lw=4)
    eyes(0, 70, 48, 12)
    arc(-48, 92, 18, 7, 30, 120, lw=4)
    arc(48, 92, 18, 7, 30, 120, lw=4)
    scarf(0, -42, 170, 90, side=-1)
    # little tree
    tree(185, -245, 220)
    snowflake(-200, 190, 34)
    snow_dots([(-215, 40), (-150, 285), (150, 300), (-215, -90)])


# 8 ------------------------------------------------------------- owlet on snowy branch
def owl():
    # branch
    rrect(-250, -200, 500, 38, r=19, lw=LW)
    line(-190, -190, -130, -178, lw=3.5)
    line(120, -192, 190, -182, lw=3.5)
    curve([(170, -162), (210, -120), (240, -110)], lw=9)
    # snow on branch
    blob([(-250, -202), (-180, -168), (-90, -182), (0, -165), (110, -178), (190, -166), (248, -200)], lw=LW_FINE + 1, fill=False, closed=False)
    # body
    blob([(0, 250), (90, 235), (150, 150), (160, 0), (130, -120), (70, -190), (0, -200),
          (-70, -190), (-130, -120), (-160, 0), (-150, 150), (-90, 235)], lw=LW)
    # ear tufts
    for s in (-1, 1):
        poly([(s * 40, 240), (s * 118, 292), (s * 118, 205)], lw=LW)
    # wings
    for s in (-1, 1):
        blob([(s * 130, 60), (s * 192, -30), (s * 175, -140), (s * 120, -100), (s * 110, -10)], lw=LW)
        curve([(s * 150, -30), (s * 148, -90)], lw=3.5)
        curve([(s * 130, -10), (s * 128, -70)], lw=3.5)
    # chest scallops
    for row, ys in enumerate((-10, -60, -110)):
        n = 3 + row % 2
        for i in range(n):
            x = (i - (n - 1) / 2) * 44
            arc(x, ys, 22, 20, 200, 140, lw=4)
    # eyes
    for s in (-1, 1):
        ell(s * 56, 135, 52, lw=LW)
        ell(s * 56, 135, 24, lw=LW_FINE, fill=False) if False else None
        dot(s * 56, 135, 22)
        white_dot(s * 56 + 8, 135 + 9, 8)
    # beak
    blob([(-18, 94), (0, 100), (18, 94), (0, 62)], lw=5)
    # feet
    for s in (-1, 1):
        for k in (-1, 0, 1):
            ell(s * 52 + k * 20, -192, 11, 17, lw=4.5)
    # beanie
    beanie(0, 238, 130, tilt=0)
    holly(-175, -140, .0001, 0) if False else None
    holly(190, -230, .8, -30)
    snowflake(-215, 200, 32)
    snow_dots([(-220, 80), (215, 130), (200, 285), (-170, 295)])


# 9 ------------------------------------------------------------- hedgehog with ornaments
def hedgehog():
    # spiky back (behind body)
    pts = []
    n = 13
    for i in range(n + 1):
        a = math.radians(200 - i * (220 / n))
        r_out = 175 if i % 2 == 0 else 135
        pts.append((r_out * math.cos(a) * 1.1, -40 + r_out * math.sin(a) * .9))
    poly(pts + [(0, -130)], lw=LW)
    # body base
    ell(0, -120, 150, 110)
    # feet
    for s in (-1, 1):
        ell(s * 70, -215, 40, 22)
        for k in (-1, 1):
            line(s * 70 + k * 12, -219, s * 70 + k * 12, -206, lw=3.5)
    # face (pointing forward): head blob
    blob([(0, 95), (70, 80), (115, 20), (100, -60), (50, -120), (0, -140), (-50, -120), (-100, -60), (-115, 20), (-70, 80)], lw=LW)
    # face mask
    blob([(-85, 10), (-60, 55), (0, 65), (60, 55), (85, 10), (60, -60), (0, -100), (-60, -60)], lw=LW_FINE + 1)
    for s in (-1, 1):
        ell(s * 108, 55, 28, lw=LW)    # ears
        ell(s * 108, 55, 12, lw=3.5)
    eyes(0, 25, 40, 12)
    nose_round(0, -22, 16, 12)
    smile(0, -34, 16)
    cheeks(0, -22, 62, 10)
    # ornaments on spines
    ornament(-115, 160, 26, 0)
    ornament(100, 190, 24, 2)
    ornament(-20, 215, 22, 1)
    holly(165, 95, .8, 30)
    snowflake(-215, 40, 28)
    snow_dots([(-200, 260), (200, 280), (215, -20), (-215, -90)])


# 10 ------------------------------------------------------------ panda with star + hat
def panda():
    # ears
    for s in (-1, 1):
        ell(s * 100, 210, 42, lw=LW)
        ell(s * 100, 210, 20, lw=4)
    # body
    ell(0, -105, 98, 108)
    ell(0, -115, 58, 76, lw=LW_FINE)
    # limbs
    for s in (-1, 1):
        blob([(s * 85, -40), (s * 150, -90), (s * 165, -170), (s * 118, -170), (s * 76, -105)], lw=LW)
        ell(s * 70, -212, 40, 24)
        for k in (-1, 1):
            line(s * 70 + k * 12, -215, s * 70 + k * 12, -202, lw=3.5)
    ell(0, 62, 122, 100)
    # eye patches
    for s in (-1, 1):
        blob([(s * 22, 100), (s * 60, 110), (s * 92, 80), (s * 88, 40), (s * 52, 30), (s * 28, 62)], lw=LW_FINE + 1)
    eyes(0, 78, 52, 12)
    # muzzle
    ell(0, 28, 36, 26, lw=LW_FINE + 1)
    nose_round(0, 38, 13, 9)
    arc(-8, 18, 10, 9, 200, 140, lw=4.5)
    arc(8, 18, 10, 9, 200, 140, lw=4.5)
    line(0, 32, 0, 18, lw=4)
    cheeks(0, 12, 82, 10) if False else None
    santa_hat(0, 148, 150, tilt=10)
    # holds a big star
    star(150, -70, 62, rot=10, lw=LW)
    ell(100, -104, 30, 26)
    snowflake(-205, 170, 34)
    snow_dots([(-215, 40), (215, 230), (-150, 285), (-205, -80)])



def arms(dx=88, top=-55, bot=-170, w=27, tilt=6):
    for sg in (-1, 1):
        ell(sg * dx, (top + bot) / 2, w, (top - bot) / 2, rot=sg * tilt)


# ---- redrawn versions
def puppy_santa():
    curve([(70, -175), (140, -170), (170, -120), (150, -90)], lw=9)
    ell(0, -115, 92, 108)
    ell(-86, -172, 46, 52)
    ell(86, -172, 46, 52)
    arms(80, -50, -165, 26, 5)
    feet(-205, 52)
    blob([(-70, -30), (0, -52), (70, -30), (66, -10), (0, -32), (-66, -10)], lw=5)
    bell(0, -58, 15)
    blob([(-95, 105), (-150, 80), (-172, 10), (-146, -35), (-105, 20)], lw=LW)
    blob([(95, 105), (150, 80), (172, 10), (146, -35), (105, 20)], lw=LW)
    ell(0, 55, 118, 98)
    ell(0, 15, 56, 42)
    nose_round(0, 38, 14, 10)
    line(0, 28, 0, 14, lw=4)
    smile(0, 14, 16, open_mouth=True)
    eyes(0, 80, 46, 13)
    arc(-46, 100, 18, 8, 30, 120, lw=4)
    arc(46, 100, 18, 8, 30, 120, lw=4)
    santa_hat(-6, 130, 150, tilt=-12)
    gift(120, -250, 120, 100)
    snowflake(-200, 140, 34)
    snowflake(200, 215, 26)
    snow_dots([(-215, 40), (-130, 250), (210, 40)])


def reindeer():
    for s in (-1, 1):
        curve([(s * 50, 140), (s * 80, 200), (s * 112, 245), (s * 130, 300)], lw=11)
        curve([(s * 88, 215), (s * 140, 215), (s * 172, 245)], lw=9)
        curve([(s * 110, 250), (s * 90, 285)], lw=9)
    ell(0, -115, 92, 108)
    ell(0, -125, 55, 70, lw=LW_FINE)
    arms(82, -50, -165, 26, 5)
    for s in (-1, 1):
        ell(s * 52, -212, 36, 22)
        line(s * 52, -226, s * 52, -200, lw=4)
    for s in (-1, 1):
        blob([(s * 100, 70), (s * 170, 100), (s * 190, 60), (s * 140, 20), (s * 100, 35)], lw=LW)
        blob([(s * 118, 65), (s * 160, 82), (s * 166, 62), (s * 132, 45)], lw=4)
    ell(0, 55, 112, 98)
    ell(0, 5, 62, 46)
    ell(0, 25, 24, 18, lw=5.5)
    smile(0, -8, 16)
    eyes(0, 80, 46, 13)
    curve([(-12, 148), (0, 168), (12, 148)], lw=5)
    blob([(-74, -28), (0, -50), (74, -28), (70, -8), (0, -30), (-70, -8)], lw=5)
    bell(0, -56, 16)
    snowflake(-200, 190, 36)
    snowflake(210, 100, 30)
    snow_dots([(-215, 60), (215, 230), (-140, 280), (150, 300), (-220, -60)])
    ground(0, -245, 440, 6)
    holly(-170, -215, .8, 15)


def penguin():
    for s in (-1, 1):
        blob([(s * 118, 40), (s * 175, -40), (s * 185, -120), (s * 140, -90), (s * 110, -20)], lw=LW)
    blob([(0, 200), (80, 175), (125, 90), (140, -30), (110, -140), (50, -205), (0, -215),
          (-50, -205), (-110, -140), (-140, -30), (-125, 90), (-80, 175)], lw=LW)
    blob([(0, 85), (60, 30), (88, -50), (66, -150), (0, -190), (-66, -150), (-88, -50), (-60, 30)], lw=LW_FINE + 1)
    for s in (-1, 1):
        blob([(s * 30, -212), (s * 88, -228), (s * 100, -250), (s * 60, -252), (s * 20, -240)], lw=LW)
        line(s * 52, -230, s * 52, -250, lw=3.5)
        line(s * 76, -234, s * 82, -250, lw=3.5)
    # face disc
    blob([(0, 190), (62, 170), (92, 128), (80, 80), (30, 62), (0, 66), (-30, 62), (-80, 80), (-92, 128), (-62, 170)], lw=LW_FINE + 1)
    eyes(0, 138, 36, 13)
    blob([(-22, 110), (0, 124), (22, 110), (0, 86)], lw=5)
    cheeks(0, 100, 62, 9) if False else None
    scarf(0, 10, 175, 95, side=1)
    for dx, dy in ((-30, -70), (30, -90), (0, -130)):
        curve([(dx - 10, dy), (dx, dy - 10), (dx + 10, dy)], lw=3.5)
    snowflake(-210, 190, 34)
    snowflake(205, 215, 28)
    snowflake(215, 60, 22)
    snow_dots([(-225, 80), (-165, 270), (170, 300), (-222, -80)])
    ground(0, -262, 470, 6)


def bunny():
    for s in (-1, 1):
        blob([(s * 45, 130), (s * 85, 215), (s * 90, 300), (s * 55, 325), (s * 22, 270), (s * 18, 160)], lw=LW)
        blob([(s * 55, 175), (s * 72, 230), (s * 68, 285), (s * 52, 280), (s * 40, 215)], lw=4)
    ell(-105, -180, 30, lw=LW)
    ell(0, -115, 92, 108)
    ell(0, -125, 55, 72, lw=LW_FINE)
    for s in (-1, 1):
        ell(s * 78, -215, 52, 26)
        for k in (-1, 0, 1):
            line(s * 78 + k * 16, -222, s * 78 + k * 16, -208, lw=3.5)
    ell(0, 55, 118, 98)
    eyes(0, 80, 46, 13)
    cheeks(0, 38, 68, 12)
    nose_tri(0, 52, 9)
    line(0, 44, 0, 32, lw=4)
    smile(0, 32, 16)
    rrect(-12, -6, 12, 22, r=3, lw=4)
    rrect(0, -6, 12, 22, r=3, lw=4)
    for s in (-1, 1):
        for k in (-1, 1):
            dot(s * 30 + k * 6, 40 + k * 4, 2.8)
    candy_cane(150, -238, 215, lean=0, w=20)
    ell(112, -96, 30, 24, rot=0)
    ell(150, -90, 30, 26)
    ell(150, -138, 30, 26)
    holly(160, -250, .8, 20)
    snowflake(-200, 150, 34)
    snowflake(200, 235, 26)
    snow_dots([(-215, 40), (-160, 280), (215, 30)])


def fox():
    blob([(60, -170), (150, -150), (225, -95), (245, -20), (205, -45), (155, -75), (90, -110)], lw=LW)
    curve([(210, -40), (222, -75), (204, -105)], lw=4.5)
    ell(0, -115, 88, 106)
    ell(0, -120, 48, 74, lw=LW_FINE)
    arms(78, -50, -165, 25, 5)
    feet(-208, 48, 36, 22)
    for s in (-1, 1):
        poly([(s * 55, 125), (s * 112, 225), (s * 128, 115)], lw=LW)
        poly([(s * 76, 135), (s * 108, 195), (s * 114, 133)], lw=4.5)
    for s in (-1, 1):
        poly([(s * 98, 32), (s * 160, -4), (s * 112, -22)], lw=LW)
    ell(0, 50, 112, 86)
    blob([(-40, 38), (-46, 0), (-26, -22), (0, -34), (26, -22), (46, 0), (40, 38), (0, 52)], lw=LW_FINE + 1)
    nose_round(0, -14, 14, 10)
    line(0, -22, 0, -32, lw=4)
    arc(-9, -32, 12, 10, 200, 140, lw=4.5)
    arc(9, -32, 12, 10, 200, 140, lw=4.5)
    eyes(0, 70, 50, 12)
    scarf(0, -50, 165, 85, side=-1)
    tree(-185, -245, 220)
    snowflake(205, 190, 34)
    snow_dots([(215, 60), (150, 285), (-150, 300), (215, -90)])


def hedgehog():
    pts = []
    n = 15
    for i in range(n + 1):
        a = math.radians(205 - i * (230 / n))
        r_out = 205 if i % 2 == 0 else 160
        pts.append((r_out * math.cos(a), -60 + r_out * math.sin(a) * 1.05))
    poly(pts + [(100, -140), (-100, -140)], lw=LW)
    ell(0, -125, 135, 100)
    for s in (-1, 1):
        ell(s * 75, -215, 42, 22)
        for k in (-1, 1):
            line(s * 75 + k * 12, -219, s * 75 + k * 12, -206, lw=3.5)
    arms(100, -60, -150, 24, 12)
    for s in (-1, 1):
        ell(s * 92, 62, 30, lw=LW)
        ell(s * 92, 62, 13, lw=3.5)
    ell(0, -5, 108, 90)
    ell(0, -52, 56, 42, lw=LW_FINE + 1)
    nose_round(0, -36, 15, 11)
    smile(0, -52, 15)
    eyes(0, 18, 44, 13)
    cheeks(0, -25, 78, 11)
    ornament(-130, 190, 26, 0)
    ornament(120, 205, 24, 2)
    ornament(-10, 240, 22, 1)
    holly(165, 120, .8, 30)
    snowflake(-215, 30, 28)
    snow_dots([(-215, 270), (210, 280), (225, -20), (-225, -90)])


def panda():
    for s in (-1, 1):
        ell(s * 100, 205, 40, lw=LW)
        ell(s * 100, 205, 18, lw=4)
    ell(0, -105, 98, 108)
    ell(0, -115, 58, 76, lw=LW_FINE)
    for s in (-1, 1):
        ell(s * 70, -212, 40, 24)
        for k in (-1, 1):
            line(s * 70 + k * 12, -215, s * 70 + k * 12, -202, lw=3.5)
    arms(-88, -50, -160, 27, -6) if False else None
    ell(-92, -105, 27, 58, rot=-6)
    ell(0, 62, 122, 100)
    for s in (-1, 1):
        blob([(s * 22, 100), (s * 60, 110), (s * 92, 80), (s * 88, 40), (s * 52, 30), (s * 28, 62)], lw=LW_FINE + 1)
    eyes(0, 78, 52, 12)
    ell(0, 28, 36, 26, lw=LW_FINE + 1)
    nose_round(0, 38, 13, 9)
    arc(-8, 18, 10, 9, 200, 140, lw=4.5)
    arc(8, 18, 10, 9, 200, 140, lw=4.5)
    line(0, 32, 0, 18, lw=4)
    santa_hat(0, 148, 150, tilt=10)
    star(170, -40, 62, rot=10, lw=LW)
    ell(112, -88, 27, 56, rot=35)
    ell(142, -42, 26, 22)
    snowflake(-205, 170, 34)
    snow_dots([(-215, 40), (215, 230), (-150, 285), (-205, -80)])


SCENES_A = [
    ("Kitten in a Christmas stocking", kitten_stocking),
    ("Puppy in a Santa hat", puppy_santa),
    ("Baby reindeer with jingle bell", reindeer),
    ("Penguin chick with a scarf", penguin),
    ("Bunny with a candy cane", bunny),
    ("Bear cub peeking out of a gift box", bear_gift),
    ("Fox kit by the little tree", fox),
    ("Owlet in a bobble hat", owl),
    ("Hedgehog with ornaments", hedgehog),
    ("Panda cub holding a star", panda),
]
