# Quantium Virtual Experience – Task 3

## Overview
This project is part of the Quantium Software Engineering Virtual Experience.
The goal of Task 3 was to create an interactive Dash application to visualize
Pink Morsel sales over time.

## Objective
To answer the business question:
**Were sales higher before or after the Pink Morsel price increase?**

## How it works
- Raw sales data is processed using `data_processing.py`
- Daily total sales are aggregated and saved as `processed_data.csv`
- A Dash app (`app.py`) visualizes total sales over time using a line chart

## How to run
```bash
pip install pandas dash plotly
python data_processing.py
python app.py

