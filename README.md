# DummyJSON API Product Tracker

A Python project that fetches product data from the DummyJSON API and exports selected product fields to a CSV file.

## What It Does

- Sends a GET request to the DummyJSON products endpoint
- Parses the JSON response
- Extracts product title, price, stock, and category
- Saves the selected fields to `competitor_prices.csv`

## Project Files

```text
tracker.py
competitor_prices.csv
requirements.txt
README.md
```

## Requirements

- Python 3
- requests

Install the required package with:

```bash
pip install -r requirements.txt
```

## How to Run

Run:

```bash
python tracker.py
```

The script creates:

```text
competitor_prices.csv
```

The CSV contains:

```text
Product Title | Price ($) | Stock | Category
```

## Purpose

This project was built to practice working with REST APIs, JSON responses, Python dictionaries and lists, and CSV export.

## Limitations

- It uses the public DummyJSON demo API rather than a live competitor system.
- It currently performs a single request and does not include retries or pagination.
