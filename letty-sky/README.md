# Letty & Sky Learn 123 — original kids' videos

`make_counting_video.py` generates **"Let's Count to 10!"** (~1:45, 1080p) entirely from code:
characters, objects, background music, sound effects and narration are all created by the script,
so there is no third-party copyright in the output.

- `out/letty_sky_count_to_10.mp4` — the finished video
- `out/thumbnail.png` — 1280×720 YouTube thumbnail

Re-render: `python3 make_counting_video.py out` (needs Python with Pillow + numpy, ffmpeg, espeak-ng).

When uploading to YouTube, set **Audience → "Yes, it's made for kids"** and, under
"Altered or synthetic content", note that the voice is computer-generated.
