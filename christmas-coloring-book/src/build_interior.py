"""Builds output/interior.pdf  (62 pages, 8.5x11in, black & white, no bleed)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import lib
from lib import *
from animals_a import SCENES_A
from animals_b import SCENES_B
from animals_c import SCENES_C

ALL = SCENES_A + SCENES_B + SCENES_C
assert len(ALL) == 30
OUT = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUT, exist_ok=True)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("DejaVuB", FONT))

W, H = 612, 792


def centered(c, text, y, size):
    c.setFont("DejaVuB", size)
    c.setFillGray(0)
    c.drawCentredString(W / 2, y, text)


def title_page(c):
    lib.begin(c)
    c.setFillGray(0)
    centered(c, "Cute Christmas", 640, 46)
    centered(c, "Animals", 586, 46)
    centered(c, "Coloring Book", 534, 34)
    centered(c, "For Kids Ages 4–8", 486, 24)
    # little decoration
    c.saveState()
    c.translate(W / 2, 330)
    c.scale(0.62, 0.62)
    tree(0, -120, 250)
    gift(-215, -135, 100, 85)
    gift(120, -135, 110, 95, pattern=1)
    snowflake(-170, 140, 36)
    snowflake(175, 150, 30)
    star(-90, 175, 24, lw=5)
    snow_dots([(-215, 40), (215, 55), (-60, 215), (95, 205)])
    c.restoreState()
    lib.begin(c)
    centered(c, "This book belongs to:", 150, 24)
    c.setLineWidth(3)
    c.setStrokeGray(0)
    c.line(150, 100, W - 150, 100)
    c.showPage()


def blank(c):
    c.showPage()


def build(path):
    c = canvas.Canvas(path, pagesize=(W, H), pageCompression=1, initialFontName="DejaVuB", initialFontSize=12)
    c.setTitle("Cute Christmas Animals - Coloring Book for Kids Ages 4-8")
    c.setAuthor("HSBizHub")
    c.setCreator("HSBizHub")
    title_page(c)
    blank(c)
    for name, fn in ALL:
        lib.begin(c)
        c.saveState()
        c.translate(W / 2, H / 2)
        c.scale(0.98, 0.98)
        fn()
        c.restoreState()
        c.showPage()
        blank(c)
    c.save()


if __name__ == "__main__":
    p = os.path.join(OUT, "Cute-Christmas-Animals_interior.pdf")
    build(p)
    print("wrote", p)
