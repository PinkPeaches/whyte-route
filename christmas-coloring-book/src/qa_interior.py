"""QA for interior.pdf: colour ops, blanks, margins, stray text, near-duplicates."""
import sys, re, zlib, subprocess, glob, os, itertools
import numpy as np
from PIL import Image, ImageFilter

def binary_dilation(mask, iterations=1):
    im = Image.fromarray((mask * 255).astype('uint8'))
    im = im.filter(ImageFilter.MaxFilter(2 * iterations + 1))
    return np.array(im) > 127

pdf = sys.argv[1]
tmp = sys.argv[2]
os.makedirs(tmp, exist_ok=True)
for f in glob.glob(tmp + "/q-*.png"): os.remove(f)
subprocess.run(["pdftoppm", "-r", "150", "-gray", "-png", pdf, tmp + "/q"], check=True)
files = sorted(glob.glob(tmp + "/q-*.png"))
n = len(files)
print("pages:", n)
# 1) colour operators in content streams
import importlib, build_interior
tmp_unc = tmp + "/uncompressed.pdf"
import reportlab.pdfgen.canvas as _cv
_orig = _cv.Canvas.__init__
def _patched(self, *a, **k):
    k["pageCompression"] = 0
    _orig(self, *a, **k)
_cv.Canvas.__init__ = _patched
build_interior.build(tmp_unc)
_cv.Canvas.__init__ = _orig
raw = open(tmp_unc, "rb").read()
ops = set()
for m in re.finditer(rb"stream\r?\n(.*?)endstream", raw, re.S):
    d = m.group(1)
    for t in re.findall(rb"([\d.\-]+(?: [\d.\-]+){0,2}) (rg|RG|g|G|k|K)\b", d):
        ops.add((t[0], t[1]))
print("colour operators used:", sorted(ops))
bad = [o for o in ops if o[1] in (b"rg", b"RG", b"k", b"K")]
print("RGB/CMYK operators:", len(bad))
# 2) per page
imgs = []
dpi = 150
for i, f in enumerate(files, 1):
    a = np.array(Image.open(f).convert("L"))
    imgs.append(a)
ink = [(a < 128) for a in imgs]
odd_art = [i for i in range(n) if i >= 2 and i % 2 == 0]     # 0-based indexes of art pages
blank_idx = [i for i in range(n) if i not in odd_art and i != 0]
print("art pages:", len(odd_art), " blank pages:", len(blank_idx))
for i in blank_idx:
    if ink[i].any() or imgs[i].min() < 250:
        print("  NOT BLANK: page", i + 1)
H, W = imgs[0].shape
minm = 1e9
for i in odd_art:
    ys, xs = np.where(ink[i])
    m = min(xs.min(), W - 1 - xs.max(), ys.min(), H - 1 - ys.max()) / dpi
    minm = min(minm, m)
    cov = ink[i].mean() * 100
    if m < 0.45 or cov < 1.0 or cov > 14:
        print(f"  page {i+1}: min margin {m:.2f}in, ink coverage {cov:.1f}%")
print(f"smallest margin on any art page: {minm:.2f} in (KDP minimum 0.25 in)")
# non-black/white big areas: count mid-grey pixels not adjacent to black
mid_total = 0
for i in odd_art + [0]:
    a = imgs[i]
    mid = (a > 60) & (a < 200)
    near = np.zeros_like(mid)
    k = ink[i]
    near = binary_dilation(k, iterations=3)
    mid_total += int((mid & ~near).sum())
print("mid-grey pixels away from black lines (should be 0):", mid_total)
# 3) text on art pages
bad_text = []
for i in odd_art:
    t = subprocess.run(["pdftotext", "-f", str(i + 1), "-l", str(i + 1), pdf, "-"], capture_output=True, text=True).stdout.strip()
    if t: bad_text.append((i + 1, t))
print("art pages containing text:", bad_text or "none")
# 4) near-duplicates

sm = []
for i in odd_art:
    k = binary_dilation(ink[i], iterations=6)
    k = k[::6, ::6].astype(float)
    sm.append(k.flatten())
sm = np.array(sm)
pairs = []
for a, b in itertools.combinations(range(len(sm)), 2):
    x, y = sm[a], sm[b]
    iou = (np.minimum(x, y).sum()) / max(np.maximum(x, y).sum(), 1)
    xc = x - x.mean(); yc = y - y.mean()
    ncc = (xc @ yc) / (np.linalg.norm(xc) * np.linalg.norm(yc) + 1e-9)
    pairs.append((ncc, iou, a + 1, b + 1))
pairs.sort(reverse=True)
print("most similar page pairs (coloring-page numbers 1-30)  [ncc, iou]:")
for p in pairs[:6]:
    print(f"   {p[2]:2d} vs {p[3]:2d}   ncc={p[0]:.2f}  iou={p[1]:.2f}")
