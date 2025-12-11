# Milestone 1 – Dataset Collection & Preprocessing  
**Week 1 Report**

### ✅ 1. Dataset Collection
For this project, scanned document samples were collected from multiple scanner sources.  
The dataset contains the following categories:

- **Official document scans**
- **Wikipedia document scans**
- **Tampered images**
- **Flatfield images**
- **Original documents**

These files represent scanned outputs from **multiple scanner devices (minimum 3–5 models)** required for forensic scanner identification.

---

### ✅ 2. Labeled Dataset Creation
A Python script (`create_labels.py`) was used to automatically generate a labeled dataset file:

- File name: **`data/image_labels.csv`**
- Columns included:
  - `scanner_model`
  - `file_name`
  - `image_path`
  - `category`
  - `width`, `height`
  - `mode` (color channel)
  - `format`
  - `dpi`
  - `file_size`
  - `md5` checksum

This labeling ensures each scanned document is associated with a specific scanner source.

---

### ✅ 3. Image Property Analysis
Using the script `analyze_images.py`, the dataset was analyzed for basic properties:

- **Total images:** 589  
- **Unique scanner models detected:** 4  
- **Most common resolutions:** e.g., 1240×1754, 2480×3508  
- **Most common formats:** TIFF, PNG, JPEG  
- **Color channels:** mostly RGB  
- **Missing metadata:** small number of missing DPI or corrupted width/height values  

A summary file was generated:

- **`reports/dataset_summary_by_scanner.csv`**

This summary provides counts of images per scanner and average dimensions.

---

### ✅ 4. Conclusion
The dataset for Milestone 1 is successfully collected, labeled, and analyzed.  
All required preprocessing steps for scanner identification have been completed:

✔️ Scanner-wise dataset organized  
✔️ Labeled CSV created  
✔️ Image statistics computed  
✔️ Summary report generated  

This dataset is now ready for **Milestone 2 — Preprocessing, Noise Extraction & Feature Engineering**.

---

*(Replace scanner names or numbers with your real output after running the scripts.)*
