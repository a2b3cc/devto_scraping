# source/scraping/main.py

import os
from pathlib import Path
import pandas as pd
from datetime import datetime
from core.scraper import scrape_top_articles
from core.config import TOPICS, TRENDING_PERIODS

def main():
    df_list = []
    for topic in TOPICS:
        for trending_period in TRENDING_PERIODS:
            df_topic = scrape_top_articles(topic, trending_period, 15)
            df_list.append(df_topic)

    df = pd.concat(df_list, ignore_index=True)
    now = datetime.now().strftime("%Y%m%dT%H%M%S")
    base_dir = Path(__file__).resolve().parent.parent.parent
    print(base_dir)
    filename = os.path.join(base_dir, "data", f"devto_data_{now}.csv")
    # Export as CSV to /data/
    df.to_csv(filename, index=False)
    print("DEV.to scraped data exported to CSV")


if __name__ == "__main__":
    main()