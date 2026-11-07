# Letty & Sky Learn 123 — original kids' videos

`make_counting_video.py` generates **"Let's Count to 10!"** (~1:30, 1080p) entirely from code:
characters, objects, background music, sound effects and narration are all created by the script,
so there is no third-party copyright in the output.

- `out/letty_sky_count_to_10.mp4` — the finished video
- `out/thumbnail.png` — 1280×720 YouTube thumbnail

Re-render: `python3 make_counting_video.py out` (needs Python with Pillow + numpy, ffmpeg, espeak-ng).

**Natural voices (free, Apache-2.0, OK for monetized YouTube):** the published video uses
[Kokoro](https://github.com/thewh1teagle/kokoro-onnx). To use it:

```bash
pip install kokoro-onnx soundfile
mkdir -p models && cd models
B=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
curl -L -o kokoro.onnx $B/kokoro-v1.0.int8.onnx && curl -L -o voices.bin $B/voices-v1.0.bin
cd .. && KOKORO_DIR=models python3 make_counting_video.py out
```

Without `KOKORO_DIR` the script falls back to the robotic espeak-ng voice.

When uploading to YouTube, set **Audience → "Yes, it's made for kids"** and, under
"Altered or synthetic content", note that the voice is computer-generated.
