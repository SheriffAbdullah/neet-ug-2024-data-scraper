# NEET UG 2024 Data Scraper

## Problem Statement

1. **Objective**: Collate NEET UG 2024 city and centre-wise data from 4750 PDFs into a unified dataset.

## Methodology

1. **Web Scraping**:
   - Utilized BeautifulSoup to scrape 4750 PDF URLs from a total search space of 900,000 URLs.
   - Employed asynchronous multiprocessing to reduce scraping time from 12 hours to under 10 minutes.

2. **Data Parsing**:
   - Implemented a Python parser using PyMuPDF to extract headers (state, city, centre name) and centre-wise marks from PDFs.

## Dataset Creation

- Compiled a dataset with over 2.3 million entries, including distinct `center_id`, `city`, `state`, and `score` columns.

## Dataset Access

[Download the dataset from Kaggle](https://www.kaggle.com/datasets/abdullahshf/neet-ug-2024-results-all-india).

## Data Source

- The data was scraped from the [NTA official website](https://neet.ntaonline.in/frontend/web/common-scorecard/index?-open-reg).

## Disclaimer

- **No Official Affiliation**: This dataset is not officially affiliated with the NTA or any other organization.
- **No Warranty**: Data accuracy is not guaranteed. Use the dataset at your own risk and verify information independently.
