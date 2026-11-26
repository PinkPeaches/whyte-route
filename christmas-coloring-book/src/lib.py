"""Vector line-art primitives for the coloring book.

Everything is drawn with reportlab as true vectors: black strokes, white fills
(white fill is what hides lines behind a shape), no grey, no shading.
Coordinates: y points up. Scenes draw around (0, 0) in "scene units"; the
page code translates/scales them onto the 8.5x11in page.
"""
import math
from reportlab.pdfgen import canvas as _canvas

LW = 6.0     # main outline width (scene units)
LW_FINE = 4.0

C = None     # active canvas, set by begin()
FILL = None  # None = white (interior); (r,g,b) for colour cover
STROKE = None



def begin(c):
    global C
    C = c
    C.setLineJoin(1)
    C.setLineCap(1)
    C.setStrokeGray(0)
    C.setFillGray(1)


def setfill(rgb=None):
    global FILL
    FILL = rgb


def _af():
    """Apply current fill (white gray by default) and stroke (black)."""
    if FILL is None:
        C.setFillGray(1)
    else:
        C.setFillColorRGB(*FILL)
    C.setStrokeGray(0)


# ---------------------------------------------------------------- paths
def _cr(points, closed):
    """Catmull-Rom spline through points -> list of cubic bezier segments."""
    n = len(points)
    segs = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        if closed:
            p0, p1, p2, p3 = points[(i - 1) % n], points[i], points[(i + 1) % n], points[(i + 2) % n]
        else:
            p0 = points[i - 1] if i > 0 else points[i]
            p1 = points[i]
            p2 = points[i + 1]
            p3 = points[i + 2] if i + 2 < n else points[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
        segs.append((p1, c1, c2, p2))
    return segs


def blob(points, fill=True, lw=None, closed=True, stroke=True):
    """Smooth closed shape through points."""
    segs = _cr(points, closed)
    p = C.beginPath()
    p.moveTo(*segs[0][0])
    for _, c1, c2, e in segs:
        p.curveTo(c1[0], c1[1], c2[0], c2[1], e[0], e[1])
    if closed:
        p.close()
    _af()
    C.setLineWidth(lw or LW)
    C.drawPath(p, stroke=1 if stroke else 0, fill=1 if (fill and closed) else 0)


def curve(points, lw=None):
    """Smooth open stroke through points."""
    blob(points, fill=False, lw=lw, closed=False)


def poly(points, fill=True, lw=None, closed=True):
    p = C.beginPath()
    p.moveTo(*points[0])
    for q in points[1:]:
        p.lineTo(*q)
    if closed:
        p.close()
    _af()
    C.setLineWidth(lw or LW)
    C.drawPath(p, stroke=1, fill=1 if (fill and closed) else 0)


def line(x1, y1, x2, y2, lw=None):
    C.setLineWidth(lw or LW)
    C.line(x1, y1, x2, y2)


def ell(cx, cy, rx, ry=None, fill=True, lw=None, rot=0):
    ry = rx if ry is None else ry
    C.saveState()
    C.translate(cx, cy)
    C.rotate(rot)
    _af()
    C.setLineWidth(lw or LW)
    C.ellipse(-rx, -ry, rx, ry, stroke=1, fill=1 if fill else 0)
    C.restoreState()


def rrect(x, y, w, h, r=10, fill=True, lw=None, rot=0, cx=None, cy=None):
    """Rounded rect with lower-left (x,y); optional rotation about (cx,cy)."""
    C.saveState()
    if rot:
        C.translate(cx if cx is not None else x + w / 2, cy if cy is not None else y + h / 2)
        C.rotate(rot)
        C.translate(-(cx if cx is not None else x + w / 2), -(cy if cy is not None else y + h / 2))
    _af()
    C.setLineWidth(lw or LW)
    C.roundRect(x, y, w, h, r, stroke=1, fill=1 if fill else 0)
    C.restoreState()


def arc(cx, cy, rx, ry, start, extent, lw=None):
    """Open elliptical arc (degrees, counter-clockwise from +x)."""
    C.setLineWidth(lw or LW)
    p = C.beginPath()
    p.arc(cx - rx, cy - ry, cx + rx, cy + ry, start, extent)
    C.drawPath(p, stroke=1, fill=0)


def dot(cx, cy, r):
    """Solid black dot."""
    C.saveState()
    C.setFillGray(0)
    C.circle(cx, cy, r, stroke=0, fill=1)
    C.restoreState()


# ---------------------------------------------------------------- faces
def white_dot(cx, cy, r):
    C.saveState()
    C.setFillGray(1)
    C.circle(cx, cy, r, stroke=0, fill=1)
    C.restoreState()


def eye(x, y, r=11, shine=True):
    dot(x, y, r)
    if shine:
        C.saveState()
        C.setFillGray(1)
        C.circle(x + r * 0.32, y + r * 0.34, r * 0.38, stroke=0, fill=1)
        C.restoreState()


def eyes(cx, cy, dx, r=11):
    eye(cx - dx, cy, r)
    eye(cx + dx, cy, r)


def happy_eye(x, y, r=12):
    """Closed, smiling eye (upside-down U arc)."""
    arc(x, y - r * 0.2, r, r * 0.9, 20, 140, lw=LW_FINE + 1)


def smile(cx, cy, w=16, open_mouth=False):
    """Little 'w' smile under the nose at (cx, cy)."""
    if open_mouth:
        blob([(cx - w, cy), (cx - w * .6, cy - w * 1.1), (cx, cy - w * 1.45),
              (cx + w * .6, cy - w * 1.1), (cx + w, cy)], lw=LW_FINE + 1)
        # tongue
        ell(cx, cy - w * 1.0, w * .42, w * .32, lw=LW_FINE - 1)
    else:
        arc(cx - w * .5, cy, w * .5, w * .5, 200, 140, lw=LW_FINE + 1)
        arc(cx + w * .5, cy, w * .5, w * .5, 200, 140, lw=LW_FINE + 1)


def nose_round(cx, cy, w=10, h=7):
    C.saveState()
    C.setFillGray(0)
    C.ellipse(cx - w, cy - h, cx + w, cy + h, stroke=0, fill=1)
    C.restoreState()


def nose_tri(cx, cy, w=9):
    C.saveState()
    C.setFillGray(0)
    p = C.beginPath()
    p.moveTo(cx - w, cy + w * .5)
    p.lineTo(cx + w, cy + w * .5)
    p.lineTo(cx, cy - w * .6)
    p.close()
    C.setLineWidth(3)
    C.drawPath(p, stroke=1, fill=1)
    C.restoreState()


def cheeks(cx, cy, dx, r=10):
    ell(cx - dx, cy, r, r * .75, lw=LW_FINE - 1)
    ell(cx + dx, cy, r, r * .75, lw=LW_FINE - 1)


def whiskers(cx, cy, dx, spread=14, ln=40, drop=0):
    for sgn in (-1, 1):
        for k in (-1, 0, 1):
            x1 = cx + sgn * dx
            y1 = cy + k * 7
            line(x1, y1, x1 + sgn * ln, y1 + k * spread * .6 - drop, lw=3.5)


def toes(x, y, w=14):
    """Two small toe lines on a paw."""
    line(x - w * .3, y - 2, x - w * .3, y + 7, lw=3.5)
    line(x + w * .3, y - 2, x + w * .3, y + 7, lw=3.5)


# ---------------------------------------------------------------- christmas props
def star(cx, cy, r, rot=0, inner=0.45, lw=None):
    pts = []
    for i in range(10):
        a = math.radians(90 + rot + i * 36)
        rr = r if i % 2 == 0 else r * inner
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    poly(pts, lw=lw)


def snowflake(cx, cy, r, lw=4.0):
    for k in range(6):
        a = math.radians(k * 60 + 90)
        ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
        line(cx, cy, ex, ey, lw=lw)
        for t in (0.55,):
            bx, by = cx + r * t * math.cos(a), cy + r * t * math.sin(a)
            for s in (-1, 1):
                b = a + s * math.radians(45)
                line(bx, by, bx + r * .32 * math.cos(b), by + r * .32 * math.sin(b), lw=lw)


def snow_dots(pts, r=7):
    for x, y in pts:
        ell(x, y, r, fill=True, lw=3.5)


def holly(cx, cy, s=1.0, rot=0):
    C.saveState()
    C.translate(cx, cy)
    C.rotate(rot)
    C.scale(s, s)
    for sgn in (-1, 1):
        blob([(0, 0), (sgn * 18, 14), (sgn * 38, 10), (sgn * 52, 0), (sgn * 38, -10), (sgn * 18, -12)], lw=4.5)
        line(0, 0, sgn * 40, 0, lw=3)
    for dx, dy in ((-9, -11), (9, -11), (0, -22)):
        ell(dx, dy, 9, lw=4.5)
    C.restoreState()


def bell(cx, cy, r=14):
    blob([(cx - r, cy - r * .7), (cx - r * .9, cy + r * .5), (cx, cy + r * 1.2),
          (cx + r * .9, cy + r * .5), (cx + r, cy - r * .7)], lw=4.5)
    line(cx - r * 1.1, cy - r * .75, cx + r * 1.1, cy - r * .75, lw=4.5)
    ell(cx, cy - r * 1.0, r * .28, lw=4)


def ornament(cx, cy, r=24, style=0):
    """Hanging bauble. style picks a decoration."""
    rrect(cx - r * .3, cy + r - 2, r * .6, r * .42, r=3, lw=4)
    ell(cx, cy, r, lw=5.5)
    if style == 0:        # stripes
        arc(cx, cy, r * .62, r * .95, 70, 40, lw=3.5)
        arc(cx, cy, r * .62, r * .95, 250, 40, lw=3.5)
        line(cx - r * .86, cy + r * .12, cx + r * .86, cy + r * .12, lw=3.5)
        line(cx - r * .86, cy - r * .22, cx + r * .86, cy - r * .22, lw=3.5)
    elif style == 1:      # star on it
        star(cx, cy, r * .5, lw=3.5)
    else:                 # dots
        for dx, dy in ((-.35, .3), (.35, .3), (0, -.2), (-.35, -.55), (.35, -.55)):
            ell(cx + dx * r, cy + dy * r, r * .13, lw=3)


def gift(x, y, w, h, bow=True, pattern=0):
    """Gift box, lower-left corner (x,y)."""
    rrect(x, y, w, h, r=6, lw=5.5)
    cxm = x + w / 2
    # ribbon vertical
    rrect(cxm - w * .09, y, w * .18, h, r=2, lw=4)
    rrect(x, y + h * .42, w, h * .16, r=2, lw=4)
    if pattern == 1:
        for fx in (.2, .8):
            for fy in (.2, .8):
                ell(x + w * fx, y + h * fy, 5, lw=3)
    if bow:
        by = y + h
        blob([(cxm, by + 2), (cxm - w * .32, by + h * .32), (cxm - w * .38, by + h * .08),
              (cxm - w * .12, by - 2)], lw=4.5)
        blob([(cxm, by + 2), (cxm + w * .32, by + h * .32), (cxm + w * .38, by + h * .08),
              (cxm + w * .12, by - 2)], lw=4.5)
        ell(cxm, by + 4, w * .08, lw=4)


def candy_cane(x, y, h, lean=0, w=17):
    """Candy cane: base at (x,y), straight up h, hook at top to the right."""
    pts = [(x, y), (x + lean * .3, y + h * .55), (x + lean, y + h), (x + lean + w * .9, y + h + w * .75),
           (x + lean + w * 1.9, y + h + w * .1), (x + lean + w * 1.5, y + h - w * .6)]
    C.saveState()
    segs = _cr(pts, False)
    p = C.beginPath()
    p.moveTo(*segs[0][0])
    for _, c1, c2, e in segs:
        p.curveTo(c1[0], c1[1], c2[0], c2[1], e[0], e[1])
    C.setLineCap(0)
    C.setStrokeGray(0)
    C.setLineWidth(w + 10)
    C.drawPath(p, stroke=1, fill=0)
    C.setStrokeGray(1)
    C.setLineWidth(w - 1)
    C.drawPath(p, stroke=1, fill=0)
    C.restoreState()
    # stripes
    for i in range(1, 6):
        t = i / 6.0 * 0.8
        sx = x + lean * .3 * t / .55 if t < .55 else x + lean * .3 + (lean * .7) * (t - .55) / .45
        sy = y + h * t / .8 if False else y + h * t * 1.1
        line(sx - w * .5, sy - w * .35, sx + w * .5, sy + w * .35, lw=4)


def santa_hat(cx, cy, w=110, tilt=0, droop=1):
    """Santa hat sitting with its brim centred at (cx, cy)."""
    C.saveState()
    C.translate(cx, cy)
    C.rotate(tilt)
    hw = w / 2
    # cone + droop
    blob([(-hw * .85, 4), (-hw * .7, hw * .6), (-hw * .2, hw * 1.05),
          (hw * .5 * droop, hw * 1.15), (hw * 1.0 * droop, hw * .85),
          (hw * .85 * droop, hw * .55), (hw * .8, 4)], lw=LW)
    ell(hw * 1.0 * droop + 2, hw * .78, hw * .21, lw=LW - 0.5)       # pompom
    rrect(-hw, -hw * .14, w, hw * .38, r=hw * .19, lw=LW)           # brim
    C.restoreState()


def elf_hat(cx, cy, w=100, tilt=0):
    C.saveState()
    C.translate(cx, cy)
    C.rotate(tilt)
    hw = w / 2
    blob([(-hw * .8, 0), (-hw * .55, hw * .8), (-hw * .1, hw * 1.45), (hw * .6, hw * 1.7),
          (hw * .55, hw * 1.3), (hw * .2, hw * .8), (hw * .8, 0)], lw=LW)
    ell(hw * .6, hw * 1.72, hw * .17, lw=5)
    # zigzag trim
    pts = []
    n = 6
    for i in range(n + 1):
        pts.append((-hw * .9 + i * (hw * 1.8 / n), 0 if i % 2 == 0 else -hw * .26))
    poly([(-hw * .9, 0)] + pts[1:] + [(hw * .9, 0)], lw=LW - 1)
    C.restoreState()


def beanie(cx, cy, w=110, tilt=0):
    """Bobble winter hat with striped cuff."""
    C.saveState()
    C.translate(cx, cy)
    C.rotate(tilt)
    hw = w / 2
    blob([(-hw * .92, 0), (-hw * .85, hw * .55), (-hw * .4, hw * .95), (0, hw * 1.02),
          (hw * .4, hw * .95), (hw * .85, hw * .55), (hw * .92, 0)], lw=LW)
    ell(0, hw * 1.12, hw * .2, lw=5)
    rrect(-hw, -hw * .2, w, hw * .4, r=hw * .18, lw=LW)
    for i in range(-3, 4):
        line(i * hw * .25, -hw * .17, i * hw * .25, hw * .17, lw=3.5)
    C.restoreState()


def scarf(cx, cy, w=110, tail=70, side=1, stripes=True):
    """Scarf band centred at (cx,cy) with a hanging tail on the given side."""
    hw = w / 2
    # band
    blob([(cx - hw, cy + 10), (cx - hw * .5, cy - 14), (cx, cy - 20), (cx + hw * .5, cy - 14),
          (cx + hw, cy + 10), (cx + hw * .5, cy + 24), (cx, cy + 20), (cx - hw * .5, cy + 24)], lw=LW)
    # tail
    tx = cx + side * hw * .55
    rrect(tx - 17, cy - tail - 18, 34, tail + 8, r=7, lw=LW - 0.5, rot=side * -6, cx=tx, cy=cy)
    if stripes:
        for k in range(1, 4):
            yy = cy - 16 - k * (tail / 4.2)
            line(tx - 17, yy, tx + 17, yy, lw=3.5)
    for k in (-1, 0, 1):   # fringe
        line(tx + k * 11, cy - tail - 18, tx + k * 11, cy - tail - 28, lw=4)
    if stripes:
        for k in range(-3, 4):
            line(cx + k * hw * .22, cy - 20 + abs(k) * 1.2, cx + k * hw * .22, cy + 20 - abs(k) * 1.2, lw=3.2)


def stocking(x, y, s=1.0, cuff=True, rot=0):
    """Big Christmas stocking, toe at lower-left; (x,y) is the cuff centre."""
    C.saveState()
    C.translate(x, y)
    C.rotate(rot)
    C.scale(s, s)
    blob([(-55, -10), (55, -10), (58, -95), (80, -150), (60, -190), (10, -195),
          (-30, -170), (-50, -110)], lw=LW + 0.5)
    ell(-5, -178, 28, 14, lw=4)        # toe patch hint
    line(-48, -118, -20, -126, lw=4)   # heel seam
    if cuff:
        rrect(-68, -8, 136, 46, r=18, lw=LW + 0.5)
        for i in range(-2, 3):
            line(i * 24, 0, i * 24, 30, lw=3.5)
    # hanging loop
    arc(46, 22, 14, 18, 0, 280, lw=4)
    C.restoreState()


def tree(cx, cy, h=260, baubles=True, star_top=True):
    """Christmas tree with base at (cx, cy)."""
    w = h * .62
    tiers = 3
    for i in range(tiers):
        ty = cy + h * .12 + i * h * .25
        tw = w * (1 - i * .27)
        th = h * .36
        poly([(cx - tw / 2, ty), (cx - tw * .18, ty + th * .55), (cx - tw * .30, ty + th * .55),
              (cx, ty + th), (cx + tw * .30, ty + th * .55), (cx + tw * .18, ty + th * .55),
              (cx + tw / 2, ty)], lw=LW)
    rrect(cx - h * .06, cy, h * .12, h * .14, r=3, lw=LW)
    if baubles:
        for dx, dy in ((-.16, .2), (.14, .33), (-.08, .5), (.1, .66)):
            ell(cx + dx * h, cy + dy * h, h * .035, lw=4.5)
    if star_top:
        star(cx, cy + h * 1.08, h * .1, lw=5)


def lights(points, bulb=9):
    """String of lights along a smooth curve with bulbs hanging below."""
    curve(points, lw=4)
    for (x, y) in points[1:-1]:
        ell(x, y - bulb - 3, bulb * .75, bulb, lw=4)


def mitten(cx, cy, s=1.0, rot=0):
    C.saveState()
    C.translate(cx, cy)
    C.rotate(rot)
    C.scale(s, s)
    blob([(-28, -40), (-30, 10), (-18, 42), (4, 48), (26, 28), (30, -10), (24, -40)], lw=LW)
    blob([(-28, 0), (-48, 4), (-52, -14), (-34, -22)], lw=5)
    rrect(-30, -62, 60, 28, r=8, lw=5)
    C.restoreState()


def cookie_person(cx, cy, s=1.0):
    """Gingerbread cookie (no face needed besides buttons)."""
    C.saveState()
    C.translate(cx, cy)
    C.scale(s, s)
    blob([(0, 44), (-18, 36), (-30, 28), (-58, 30), (-62, 14), (-36, 6), (-30, -10), (-48, -40),
          (-30, -52), (-8, -26), (8, -26), (30, -52), (48, -40), (30, -10), (36, 6), (62, 14),
          (58, 30), (30, 28), (18, 36)], lw=5.5)
    eye(-9, 22, 4.5, shine=False)
    eye(9, 22, 4.5, shine=False)
    arc(0, 18, 9, 7, 210, 120, lw=3)
    for yy in (4, -10):
        dot(0, yy, 4.5)
    C.restoreState()


def mug(cx, cy, w=110, h=110):
    """Mug whose bottom centre is (cx, cy); handle on the right."""
    hx, hy = cx + w / 2 + 6, cy + h * .5
    ell(hx + 12, hy, 52, 62, lw=LW)
    ell(hx + 12, hy, 26, 36, lw=LW)
    rrect(cx - w / 2, cy, w, h, r=26, lw=LW)
    for i in range(3):
        ell(cx - w * .26 + i * w * .26, cy + h * .2, 6, lw=3.5)


def sled(cx, cy, w=240):
    """Simple sled, runners bottom at cy."""
    hw = w / 2
    # runners
    curve([(cx - hw - 20, cy + 40), (cx - hw - 6, cy + 4), (cx - hw + 30, cy), (cx + hw - 10, cy),
           (cx + hw + 30, cy + 8), (cx + hw + 36, cy + 34)], lw=7)
    # bed
    rrect(cx - hw + 6, cy + 24, w - 12, 36, r=12, lw=LW)
    for xx in (cx - hw * .55, cx + hw * .55):
        line(xx, cy + 4, xx, cy + 26, lw=LW)
    line(cx - hw * .1, cy + 36, cx - hw * .1, cy + 52, lw=4)
    line(cx + hw * .3, cy + 36, cx + hw * .3, cy + 52, lw=4)


def wreath(cx, cy, r=70):
    ell(cx, cy, r, fill=False, lw=LW)
    ell(cx, cy, r * .55, fill=False, lw=LW)
    for k in range(10):
        a = math.radians(k * 36)
        mx, my = cx + r * .78 * math.cos(a), cy + r * .78 * math.sin(a)
        blob([(mx - 9, my), (mx, my + 11), (mx + 9, my), (mx, my - 11)], lw=3.5)
    # bow
    by = cy - r * .8
    blob([(cx, by), (cx - 30, by + 16), (cx - 36, by - 6), (cx - 10, by - 6)], lw=4.5)
    blob([(cx, by), (cx + 30, by + 16), (cx + 36, by - 6), (cx + 10, by - 6)], lw=4.5)
    for dx in (-18, 22):
        dot(cx + dx, cy + r * .78 + dx * 0.1, 5)


def ground(cx, cy, w=420, bumps=5):
    """Wavy snow-ground line."""
    pts = []
    for i in range(bumps + 1):
        x = cx - w / 2 + i * w / bumps
        pts.append((x, cy + (6 if i % 2 else -4)))
    curve(pts, lw=5)


def finish_png_check():
    pass
