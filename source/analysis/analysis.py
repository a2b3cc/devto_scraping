# source/analysis/analysis.py

import os
from pathlib import Path
import pandas as pd

base_dir = Path(__file__).resolve().parent.parent.parent
data_dir = base_dir / "data"
csv_files = sorted(data_dir.glob("devto_data_*.csv"))

if not csv_files:
    print("No CSV files found")
else:
    latest_file = csv_files[-1]
    df = pd.read_csv(latest_file)
    print(df.shape)