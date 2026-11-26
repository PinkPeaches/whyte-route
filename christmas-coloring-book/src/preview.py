"""Render scenes to a PDF and a contact sheet for visual checking.
usage: preview.py <module> <outprefix> [indices...]"""
import sys, importlib, subprocess, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
import lib

mod = importlib.import_module(sys.argv[1])
out = sys.argv[2]
scenes = [getattr(mod, n) for n in dir(mod) if n.startswith("SCENES")]
allscenes = [s for lst in scenes for s in lst]
idx = [int(a) for a in sys.argv[3:]] or list(range(len(allscenes)))
c = canvas.Canvas(out + ".pdf", pagesize=(612, 792))
for i in idx:
    name, fn = allscenes[i]
    lib.begin(c)
    c.saveState()
    c.translate(306, 396)
    c.scale(0.98, 0.98)
    fn()
    c.restoreState()
    c.showPage()
c.save()
subprocess.run(["pdftoppm", "-r", "50", "-png", out + ".pdf", out + "_pg"], check=True)
