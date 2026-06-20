# Sentiment Analysis with VADER

This repository contains a sentiment analysis project using the VADER sentiment analysis approach and supporting tools for collecting review data from Google Play Store.

## Repository Structure

```text
project-name/
│
├── README.md
├── vader_sentiment_analysis.ipynb
│
└── scraper/
    ├── README.md
    ├── scrap.ipynb
    └── scrap_tiket_playstore.py
```

## Files

### vader_sentiment_analysis.ipynb

Jupyter Notebook containing the complete sentiment analysis workflow using VADER, including data preprocessing, sentiment scoring, and result evaluation.

### scraper/

Contains scripts and notebooks used to collect review data from Google Play Store.

See `scraper/README.md` for more details.

## Requirements

* Python 3.9+
* Jupyter Notebook

Install required packages:

```bash
pip install pandas nltk vaderSentiment
```

## Usage

1. Collect review data using the tools inside the `scraper` folder.
2. Prepare the dataset for analysis.
3. Run `vader_sentiment_analysis.ipynb` to perform sentiment classification and analysis.

## Notes

This repository is intended for educational and research purposes related to sentiment analysis of user reviews.
