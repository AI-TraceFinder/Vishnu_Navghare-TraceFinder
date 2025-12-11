# scripts/analyze_images.py
import pandas as pd
import matplotlib.pyplot as plt

# Load labels generated earlier
df = pd.read_csv("../data/image_labels.csv")

# Quick sanity checks
print("Total images:", len(df))
print("Unique scanners:", df["scanner_model"].nunique())
print(df["scanner_model"].value_counts())

# Resolution distribution
df["resolution"] = df["width"].fillna(0).astype(int).astype(str) + "x" + df["height"].fillna(0).astype(int).astype(str)
res_counts = df["resolution"].value_counts().head(20)
print("\nTop resolutions:\n", res_counts)

# File format distribution
print("\nFormats:\n", df["format"].value_counts())

# Missing data summary
print("\nMissing DPI count:", df["dpi"].isna().sum())
print("Missing width/height:", df[["width","height"]].isna().sum())

# Save a small report CSV with counts
summary = df.groupby(["scanner_model"]).agg(
    images=("image_path","count"),
    avg_width=("width","mean"),
    avg_height=("height","mean"),
    avg_size_bytes=("file_size_bytes","mean")
).reset_index()
summary.to_csv("../reports/dataset_summary_by_scanner.csv", index=False)
print("\nSaved reports/dataset_summary_by_scanner.csv")
