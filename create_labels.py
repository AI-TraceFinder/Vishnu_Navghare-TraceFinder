# scripts/create_labels.py (REPLACE your old file with this)
import os
import hashlib
from PIL import Image
import pandas as pd

# Determine DATA_DIR relative to this script file (works regardless of cwd)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(THIS_DIR, ".."))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
OUTPUT_CSV = os.path.join(DATA_DIR, "image_labels.csv")

# Allowed image file extensions (lowercase)
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".gif", ".webp"}

rows = []

if not os.path.isdir(DATA_DIR):
    print("ERROR: data directory not found at:", DATA_DIR)
    print("Please check that your project folder contains a 'data' folder.")
    raise SystemExit(1)

# List top-level items under data/ for user info
top_level = sorted(os.listdir(DATA_DIR))
print("Found top-level items in data/:", top_level)

# Walk each top-level folder (this will treat each as a category)
for category in top_level:
    category_path = os.path.join(DATA_DIR, category)
    if not os.path.isdir(category_path):
        # skip files directly inside data/
        continue

    # Walk recursively through category_path
    for root, dirs, files in os.walk(category_path):
        # Determine scanner_model:
        # If files are directly in category_path -> scanner_model = "unknown"
        # If files are in category_path/<scanner_model>/... -> scanner_model = first folder name after category_path
        relpath = os.path.relpath(root, category_path)
        parts = relpath.split(os.sep)
        if relpath == ".":
            scanner_model = "unknown"
        else:
            scanner_model = parts[0] if parts[0] else "unknown"

        for fname in files:
            fpath = os.path.join(root, fname)
            # filter by extension
            ext = os.path.splitext(fname)[1].lower()
            if ext not in IMAGE_EXTS:
                # skip non-image files
                continue
            if not os.path.isfile(fpath):
                continue

            # Safely open image metadata
            try:
                with Image.open(fpath) as im:
                    width, height = im.size
                    mode = im.mode
                    fmt = im.format
                    info = im.info
                    dpi = info.get("dpi", (None, None))[0] if isinstance(info.get("dpi", None), tuple) else info.get("dpi", None)
            except Exception as e:
                # if image can't be opened, still record path but with None metadata
                width = height = mode = fmt = dpi = None

            try:
                file_size = os.path.getsize(fpath)
            except Exception:
                file_size = None

            try:
                with open(fpath, "rb") as fbin:
                    checksum = hashlib.md5(fbin.read()).hexdigest()
            except Exception:
                checksum = None

            rows.append({
                "image_path": os.path.abspath(fpath),
                "category": category,
                "scanner_model": scanner_model,
                "file_name": fname,
                "width": width,
                "height": height,
                "channels_or_mode": mode,
                "format": fmt,
                "dpi": dpi,
                "file_size_bytes": file_size,
                "md5": checksum
            })

# Save results
df = pd.DataFrame(rows)
# ensure output folder exists
os.makedirs(DATA_DIR, exist_ok=True)
df.to_csv(OUTPUT_CSV, index=False)
print("\nSaved:", OUTPUT_CSV)
print("Total image rows:", len(df))

# Diagnostics
if len(df) == 0:
    print("\nWARNING: No image files were found by the script.")
    print("Possible causes:")
    print(" - data/ folder empty or contains different folder names.")
    print(" - images use uncommon extensions (not jpg/png/tif/...).")
    print(" - images are stored in a different location.")
    print("\nPlease check the printed top-level list above and make sure your images are inside subfolders.")
else:
    print("\nSample rows:")
    print(df.head(10).to_string(index=False))

    # Print counts per category and per scanner
    print("\nCounts per category:")
    print(df["category"].value_counts())

    print("\nCounts per scanner_model (top 20):")
    print(df["scanner_model"].value_counts().head(20))
