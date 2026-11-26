# Cute Christmas Animals: KDP coloring book (HSBizHub)

- `output/` print files: interior PDF (62 pages) and wrap-cover PDF
- `LISTING_COPY.md` ready-to-paste KDP listing, price and royalty math
- `UPLOAD_CHECKLIST.md` Amazon-side steps, including the AI-content disclosure
- `PAGE_SPECS.md` what each of the 30 pages shows, and how to regenerate it
- `QA_REPORT.txt` automated checks on the interior
- `src/` the code that draws everything. Rebuild with `cd src && python3 build_interior.py && python3 build_cover.py` (needs `reportlab`).

All art is original vector line art drawn by code; nothing was traced, copied or generated from another book.
