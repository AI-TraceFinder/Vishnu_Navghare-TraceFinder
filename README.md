## Milestone 1 — Dataset Collection & Preprocessing

- Collected scans from 4 scanners: Epson_L3150 (120 images), HP_DeskJet_2130 (100), Canon_MF3010 (110), Brother_DCP (80).
- Created CSV: `data/image_labels.csv` (columns: image_path, category, scanner_model, width, height, format, dpi, file_size_bytes, md5).
- Summary file: `reports/dataset_summary_by_scanner.csv`.
- Tools used: Python, Pillow, pandas.
