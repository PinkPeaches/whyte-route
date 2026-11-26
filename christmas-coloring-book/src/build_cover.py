"""Builds output/wrap-cover.pdf: back + spine + front, 0.125in bleed, sized for 62 pages (white paper).

KDP formula (paperback, white paper): spine = pages * 0.002252in
  width  = 2 * 8.5 + spine + 2 * 0.125
  height = 11 + 2 * 0.125
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
import lib
from lib import *

PAGES = 62
INCH = 72.0
TRIM_W, TRIM_H = 8.5 * INCH, 11 * INCH
BLEED = 0.125 * INCH
SPINE = PAGES * 0.002252 * INCH
WRAP_W = 2 * TRIM_W + SPINE + 2 * BLEED
WRAP_H = TRIM_H + 2 * BLEED
FRONT_X = BLEED + TRIM_W + SPINE      # left edge of front trim box
BACK_X = BLEED                        # left edge of back trim box
Y0 = BLEED

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
pdfmetrics.registerFont(TTFont("DejaVuB", FONT))
pdfmetrics.registerFont(TTFont("DejaVu", FONT_R))

def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))

SKY_TOP, SKY_BOT = rgb("#7CC4F2"), rgb("#D6F0FF")
RED, GREEN, WHITE = rgb("#E5424B"), rgb("#2E9E57"), (1, 1, 1)
ORANGE, CREAM, TAN, BROWN = rgb("#F5A04A"), rgb("#FFE9C7"), rgb("#EBC27E"), rgb("#B97A44")
PINK, GREY, DARK = rgb("#F7A8B8"), rgb("#8FA2B5"), rgb("#2B3A55")
YELLOW, PURPLE, BLUE = rgb("#FFD23F"), rgb("#8F5BE8"), rgb("#2F7BDB")


def F(c):
    lib.setfill(c)


# --------------------------------------------------------------- background
def background(c):
    n = 80
    for i in range(n):
        t = i / (n - 1)
        col = tuple(SKY_TOP[k] * (1 - t) + SKY_BOT[k] * t for k in range(3))
        c.setFillColorRGB(*col)
        y = WRAP_H * (1 - (i + 1) / n)
        c.rect(0, y - 0.5, WRAP_W, WRAP_H / n + 1.5, stroke=0, fill=1)
    # twinkles + snowflakes (white)
    c.setFillColorRGB(1, 1, 1)
    import random
    rnd = random.Random(7)
    for _ in range(90):
        x, y = rnd.uniform(0, WRAP_W), rnd.uniform(WRAP_H * 0.30, WRAP_H)
        c.circle(x, y, rnd.choice((1.6, 2.2, 3.0)), stroke=0, fill=1)
    # snow hills across the whole wrap
    for (cx, cy, rx, ry, col) in ((WRAP_W * .18, 70, 520, 150, "#EAF6FF"), (WRAP_W * .62, 40, 620, 160, "#F6FBFF"),
                                  (WRAP_W * .95, 80, 420, 140, "#EAF6FF")):
        c.setFillColorRGB(*rgb(col))
        c.ellipse(cx - rx, cy - ry, cx + rx, cy + ry, stroke=0, fill=1)


def white_flake(c, x, y, r):
    c.saveState()
    c.setStrokeGray(1)
    lib.begin(c)
    c.setStrokeGray(1)
    c.translate(x, y)
    snowflake(0, 0, r, lw=max(2.5, r * .13))
    c.restoreState()
    lib.begin(c)


# --------------------------------------------------------------- coloured props
def hat(cx, cy, w=110, tilt=0):
    c = lib.C
    c.saveState()
    c.translate(cx, cy)
    c.rotate(tilt)
    hw = w / 2
    F(RED)
    blob([(-hw * .85, 4), (-hw * .7, hw * .6), (-hw * .2, hw * 1.05), (hw * .5, hw * 1.15), (hw * 1.0, hw * .85),
          (hw * .85, hw * .55), (hw * .8, 4)], lw=5)
    F(WHITE)
    ell(hw + 2, hw * .78, hw * .21, lw=4.5)
    rrect(-hw, -hw * .14, w, hw * .38, r=hw * .19, lw=5)
    c.restoreState()


def tree_c(cx, cy, h=260):
    w = h * .62
    F(rgb("#7A4A24"))
    rrect(cx - h * .06, cy, h * .12, h * .14, r=3, lw=5)
    for i in range(3):
        ty = cy + h * .12 + i * h * .25
        tw = w * (1 - i * .27)
        th = h * .36
        F(GREEN if i != 1 else rgb("#3BB56A"))
        poly([(cx - tw / 2, ty), (cx - tw * .18, ty + th * .55), (cx - tw * .30, ty + th * .55),
              (cx, ty + th), (cx + tw * .30, ty + th * .55), (cx + tw * .18, ty + th * .55),
              (cx + tw / 2, ty)], lw=5)
    cols = (RED, YELLOW, PURPLE, BLUE)
    for k, (dx, dy) in enumerate(((-.16, .2), (.14, .33), (-.08, .5), (.1, .66))):
        F(cols[k])
        ell(cx + dx * h, cy + dy * h, h * .035, lw=4)
    F(YELLOW)
    star(cx, cy + h * 1.08, h * .1, lw=4.5)


def gift_c(x, y, w, h, box, rib):
    F(box)
    rrect(x, y, w, h, r=6, lw=5)
    F(rib)
    cxm = x + w / 2
    rrect(cxm - w * .09, y, w * .18, h, r=2, lw=3.5)
    rrect(x, y + h * .42, w, h * .16, r=2, lw=3.5)
    by = y + h
    blob([(cxm, by + 2), (cxm - w * .32, by + h * .32), (cxm - w * .38, by + h * .08), (cxm - w * .12, by - 2)], lw=4)
    blob([(cxm, by + 2), (cxm + w * .32, by + h * .32), (cxm + w * .38, by + h * .08), (cxm + w * .12, by - 2)], lw=4)
    ell(cxm, by + 4, w * .08, lw=3.5)


def scarf_c(cx, cy, w, col, side=1, tail=70):
    hw = w / 2
    F(col)
    blob([(cx - hw, cy + 10), (cx - hw * .5, cy - 14), (cx, cy - 20), (cx + hw * .5, cy - 14),
          (cx + hw, cy + 10), (cx + hw * .5, cy + 24), (cx, cy + 20), (cx - hw * .5, cy + 24)], lw=5)
    tx = cx + side * hw * .55
    rrect(tx - 17, cy - tail - 18, 34, tail + 8, r=7, lw=4.5, rot=side * -6, cx=tx, cy=cy)
    F(WHITE)
    for k in range(1, 4):
        yy = cy - 16 - k * (tail / 4.2)
        line(tx - 17, yy, tx + 17, yy, lw=3.5)


# --------------------------------------------------------------- coloured animals
def arms_c(col, dx=80, top=-50, bot=-165, w=26, tilt=5):
    F(col)
    for sg in (-1, 1):
        ell(sg * dx, (top + bot) / 2, w, (top - bot) / 2, rot=sg * tilt)


def feet_c(col, y=-208, dx=50, rx=38, ry=22):
    F(col)
    for s in (-1, 1):
        ell(s * dx, y, rx, ry)
        for k in (-1, 1):
            line(s * dx + k * 11, y - 4, s * dx + k * 11, y + 9, lw=3.5)


def kitten():
    F(ORANGE); ell(0, -115, 88, 104)
    F(CREAM); ell(0, -122, 50, 70, lw=4)
    arms_c(ORANGE, 82, -50, -165); feet_c(ORANGE, -208, 50)
    curve([(70, -160), (150, -160), (170, -100), (150, -60)], lw=12)   # tail outline
    F(ORANGE)
    for s in (-1, 1):
        poly([(s * 40, 100), (s * 120, 170), (s * 128, 85)], lw=6)
        F(PINK); poly([(s * 64, 106), (s * 106, 142), (s * 108, 100)], lw=4); F(ORANGE)
    ell(0, 55, 122, 96)
    F(CREAM); ell(0, 22, 52, 36, lw=4)
    for dx in (-22, 0, 22):
        line(dx, 148, dx, 126, lw=5)
    eyes(0, 70, 48, 13)
    F(PINK); nose_tri(0, 36, 10)
    lib.C.setFillGray(0)
    smile(0, 14, 14)
    whiskers(0, 28, 70, 14, 46)
    hat(-6, 130, 140, tilt=-10)


def puppy():
    F(TAN); ell(0, -115, 92, 108)
    F(CREAM); ell(0, -122, 52, 70, lw=4)
    F(TAN); ell(-86, -172, 44, 50); ell(86, -172, 44, 50)
    arms_c(TAN, 80, -50, -165); feet_c(TAN, -205, 52)
    F(BROWN)
    for s in (-1, 1):
        blob([(s * 95, 105), (s * 150, 80), (s * 172, 10), (s * 146, -35), (s * 105, 20)], lw=6)
    F(TAN); ell(0, 55, 118, 96)
    F(CREAM); ell(0, 15, 56, 42, lw=4)
    nose_round(0, 38, 14, 10)
    eyes(0, 80, 46, 13)
    smile(0, 14, 15, open_mouth=True)
    F(RED)
    blob([(-70, -30), (0, -52), (70, -30), (66, -10), (0, -32), (-66, -10)], lw=5)
    F(YELLOW); bell(0, -58, 15)
    hat(-6, 128, 140, tilt=-12)


def reindeer():
    F(BROWN)
    for s in (-1, 1):
        curve([(s * 50, 140), (s * 80, 200), (s * 112, 245), (s * 130, 300)], lw=11)
        curve([(s * 88, 215), (s * 140, 215), (s * 172, 245)], lw=9)
        curve([(s * 110, 250), (s * 90, 285)], lw=9)
    F(rgb("#C98A55")); ell(0, -115, 92, 108)
    F(CREAM); ell(0, -125, 55, 70, lw=4)
    arms_c(rgb("#C98A55"), 82, -50, -165)
    F(rgb("#C98A55"))
    for s in (-1, 1):
        ell(s * 52, -212, 36, 22); line(s * 52, -226, s * 52, -200, lw=4)
    for s in (-1, 1):
        F(rgb("#C98A55")); blob([(s * 100, 70), (s * 170, 100), (s * 190, 60), (s * 140, 20), (s * 100, 35)], lw=6)
        F(PINK); blob([(s * 118, 65), (s * 160, 82), (s * 166, 62), (s * 132, 45)], lw=4)
    F(rgb("#C98A55")); ell(0, 55, 112, 98)
    F(CREAM); ell(0, 5, 62, 46, lw=4)
    F(RED); ell(0, 25, 24, 18, lw=5.5)
    eyes(0, 80, 46, 13)
    smile(0, -8, 16)
    F(GREEN)
    blob([(-74, -28), (0, -50), (74, -28), (70, -8), (0, -30), (-70, -8)], lw=5)
    F(YELLOW); bell(0, -56, 16)


def penguin():
    F(DARK)
    for s in (-1, 1):
        blob([(s * 118, 40), (s * 175, -40), (s * 185, -120), (s * 140, -90), (s * 110, -20)], lw=6)
    blob([(0, 200), (80, 175), (125, 90), (140, -30), (110, -140), (50, -205), (0, -215),
          (-50, -205), (-110, -140), (-140, -30), (-125, 90), (-80, 175)], lw=6)
    F(WHITE)
    blob([(0, 85), (60, 30), (88, -50), (66, -150), (0, -190), (-66, -150), (-88, -50), (-60, 30)], lw=5)
    F(ORANGE)
    for s in (-1, 1):
        blob([(s * 30, -212), (s * 88, -228), (s * 100, -250), (s * 60, -252), (s * 20, -240)], lw=6)
    F(WHITE)
    blob([(0, 190), (62, 170), (92, 128), (80, 80), (30, 62), (0, 66), (-30, 62), (-80, 80), (-92, 128), (-62, 170)], lw=5)
    eyes(0, 138, 36, 13)
    F(ORANGE); blob([(-22, 110), (0, 124), (22, 110), (0, 86)], lw=5)
    scarf_c(0, 10, 175, RED, side=1, tail=95)


def bunny():
    F(WHITE)
    for s in (-1, 1):
        blob([(s * 45, 130), (s * 85, 215), (s * 90, 300), (s * 55, 325), (s * 22, 270), (s * 18, 160)], lw=6)
        F(PINK); blob([(s * 55, 175), (s * 72, 230), (s * 68, 285), (s * 52, 280), (s * 40, 215)], lw=4); F(WHITE)
    ell(-105, -180, 30, lw=6)
    ell(0, -115, 92, 108)
    F(rgb("#FFE4EC")); ell(0, -125, 55, 72, lw=4)
    F(WHITE)
    for s in (-1, 1):
        ell(s * 78, -215, 52, 26)
    ell(0, 55, 118, 98)
    eyes(0, 80, 46, 13)
    F(PINK); cheeks(0, 38, 68, 12)
    nose_tri(0, 52, 9)
    smile(0, 32, 15)
    F(WHITE)
    rrect(-12, -6, 12, 22, r=3, lw=4); rrect(0, -6, 12, 22, r=3, lw=4)
    F(GREEN)
    holly(135, -215, 1.0, 20)
    F(RED)
    for dx, dy in ((-9, -11), (9, -11), (0, -22)):
        ell(135 + dx, -215 + dy, 8, lw=3.5)
    F(WHITE)


def place(fn, x, y, s):
    c = lib.C
    c.saveState()
    c.translate(x, y)
    c.scale(s, s)
    fn()
    c.restoreState()


# --------------------------------------------------------------- front cover
def put_text(c, text, x, base, font, size, fill, mode=0, stroke=None, lw=0):
    """Draw text at x (left) with explicit render mode so state never leaks."""
    c.saveState()
    c.setLineJoin(1)
    if stroke is not None:
        c.setStrokeColorRGB(*stroke)
        c.setLineWidth(lw)
    t = c.beginText(x, base)
    t.setFont(font, size)
    t.setFillColorRGB(*fill)
    t.setTextRenderMode(mode)
    t.textOut(text)
    c.drawText(t)
    c.restoreState()


def centered_text(c, text, cx, base, font, size, fill):
    w = stringWidth(text, font, size)
    put_text(c, text, cx - w / 2, base, font, size, fill)


def title_line(c, text, cx, base, size, col, outline1=DARK, outline2=WHITE):
    w = stringWidth(text, "DejaVuB", size)
    x = cx - w / 2
    put_text(c, text, x, base, "DejaVuB", size, col, mode=1, stroke=outline1, lw=size * .30)
    put_text(c, text, x, base, "DejaVuB", size, col, mode=1, stroke=outline2, lw=size * .17)
    put_text(c, text, x, base, "DejaVuB", size, col, mode=0)


def front(c):
    c.saveState()
    c.translate(FRONT_X, Y0)
    W, H = TRIM_W, TRIM_H
    # sparkle snowflakes
    for (x, y, r) in ((60, 700, 24), (555, 735, 20), (40, 520, 16), (575, 470, 22), (540, 590, 14), (90, 600, 14)):
        white_flake(c, x, y, r)
    title_line(c, "Cute", W / 2, 672, 88, RED)
    title_line(c, "Christmas", W / 2, 584, 84, GREEN)
    title_line(c, "Animals", W / 2, 496, 92, PURPLE)
    # subtitle banner
    lib.begin(c)
    F(YELLOW)
    rrect(40, 392, W - 80, 62, r=31, lw=6)
    c.setFillColorRGB(*DARK)
    c.setFont("DejaVuB", 25)
    c.drawCentredString(W / 2, 412, "Coloring Book for Kids Ages 4–8")
    lib.begin(c)
    # background trees
    tree_c(62, 108, 175)
    tree_c(552, 108, 165)
    # animals
    place(kitten, 128, 252, .42)
    place(puppy, 226, 242, .43)
    place(reindeer, 306, 236, .44)
    place(penguin, 402, 242, .41)
    place(bunny, 484, 238, .38)
    # presents in front
    gift_c(150, 18, 62, 52, RED, YELLOW)
    gift_c(228, 14, 52, 44, BLUE, WHITE)
    gift_c(330, 18, 66, 56, GREEN, RED)
    gift_c(420, 14, 54, 46, PURPLE, YELLOW)
    c.restoreState()


# --------------------------------------------------------------- back cover
def back(c):
    c.saveState()
    c.translate(BACK_X, Y0)
    W, H = TRIM_W, TRIM_H
    lib.begin(c)
    # white-ish panel for the text
    F(rgb("#FFFFFF"))
    rrect(44, 330, W - 88, 400, r=34, lw=6)
    for (x, y, r) in ((70, 760, 20), (545, 750, 24), (560, 300, 16)):
        white_flake(c, x, y, r)
    centered_text(c, "30 Cozy Christmas Pages!", W / 2, 672, "DejaVuB", 31, RED)
    lines = [
        "Meet a kitten in a stocking, a puppy in a",
        "Santa hat, a baby reindeer, a snowy penguin",
        "and 26 more sweet little animals, all dressed",
        "up for the holidays and ready for crayons!",
        "",
        "★ 30 different pictures, one per page",
        "★ Big, bold lines that are easy to color",
        "★ Blank page behind every picture so",
        "    markers don’t bleed through",
        "★ Large 8.5″ × 11″ pages",
        "",
        "A fun, screen-free gift for ages 4–8.",
    ]
    y = 628
    for ln in lines:
        if ln.startswith("\u2605") or ln.startswith("    "):
            put_text(c, ln, 92, y, "DejaVu", 17, DARK)
        elif ln:
            centered_text(c, ln, W / 2, y, "DejaVu", 17, DARK)
        y -= 25
    # barcode area (must stay blank white): 2in x 1.2in, bottom right, 0.25in inside trim
    bw, bh = 2.0 * INCH, 1.2 * INCH
    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(*GREY)
    c.setLineWidth(1)
    c.rect(W - 0.25 * INCH - bw, 0.25 * INCH, bw, bh, stroke=1, fill=1)
    # trees + animals peeking along the bottom-left
    tree_c(80, 96, 190)
    place(bunny, 190, 150, .24)
    gift_c(250, 100, 48, 40, RED, YELLOW)
    c.restoreState()


def spine(c):
    c.saveState()
    c.setFillColorRGB(*RED)
    c.rect(BLEED + TRIM_W, 0, SPINE, WRAP_H, stroke=0, fill=1)
    c.restoreState()


def build(path):
    c = canvas.Canvas(path, pagesize=(WRAP_W, WRAP_H), pageCompression=1, initialFontName="DejaVuB", initialFontSize=12)
    c.setTitle("Cute Christmas Animals - full wrap cover (62 pages)")
    c.setAuthor("HSBizHub")
    lib.begin(c)
    background(c)
    spine(c)
    lib.begin(c)
    back(c)
    lib.begin(c)
    front(c)
    c.showPage()
    c.save()


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "output", "Cute-Christmas-Animals_wrap-cover.pdf")
    build(out)
    print("wrote", out)
    print(f"spine {SPINE/INCH:.4f} in; wrap {WRAP_W/INCH:.4f} x {WRAP_H/INCH:.4f} in")
