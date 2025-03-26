# DEV.to Scraper and Analysis

This educational project scrapes popular articles from DEV.to by topic
and trending period, then performs data analysis and visualization
on the collected data. The scraper uses Playwright to handle dynamic 
content (including infinite scrolling), rotates user agents,
and incorporates randomized delays to mimic human browsing behavior.
These measures help reduce detection risk while gathering valuable data
for learning and research purposes.

## Project structure

    data/
        ├── devto_data.csv
    source/
        ├── analysis
        │   ├── analysis.py        # Data analysis functions
        │   └── visualization.py   # Data visualization functions
        ├── scraping
        │   ├── core/
        │   │   ├── config.py      # Configuration and constants
        │   │   ├── scraper.py     # Main scraping logic 
        │   │   └── utils.py       # Helper functions (metadata extraction, comments scraping)
        │   └── main.py            # Entry point for scraping
        ├── LICENSE.txt            # MIT License
        └── requirements.txt       # Package dependencies

## Features

* #### Dynamic content with infinite scrolling:
Uses Playwright to load DEV.to pages with infinite scrolling.

* #### User-agent rotation:
Rotates the user-agent every 20 articles by default to reduce
detection risk.

* #### Human-like behavior:
Introduces random delays to mimic natural browsing behavior,
helping to avoid triggering anti-bot mechanisms.

* #### Modular code:
The project separates scraping and analysis logic into distinct
modules to maximize reusability and facilitate maintenance.

* #### Data output:
The scraped data is stored in a CSV file inside the `/data` module.

## Compliance
This project is implemented in compliance with DEV.to's robots.txt and
terms of use. The scraper respects the website's guidelines for
automated data collection.

## Requirements
This project is built with **Python, Playwright, and pandas**.
All the necessary dependencies are specified in the `requirements.txt` file.

## Usage
### Scraping
Run the main script from the `/source/scraping` directory:

`python main.py`

This command will:
1. Scrape top DEV.to articles by topic and trending period.
2. Export the data to `/data/devto_data_{timestamp}.csv`

## Analysis
Run the main script from the `/source/analysis` directory:
`python main.py`

This command will:
1. Read a CSV data file from `/data` directory.
2. Execute data analysis and visualizations.

## License
This project is released under the MIT license.