# Project 2: Crime at Stanford

Created by Saidzhan Saitov and Afshinkhan Toktonazarov

## Overview

This project uses the Hugging Face dataset `stanforddams/daily`, a collection of Stanford Daily police blotter articles, to analyze crime reports from Stanford University and generate a short article based on recurring patterns found in the data.

The project combines data extraction and natural language analysis to transform police blotter records into a readable narrative about crime at Stanford.

## Repository Contents

- `story_from_dataset.py` — Python script that loads the dataset, parses HTML police blotter entries, identifies recurring crime themes, extracts representative examples, and generates the final article.
- `article.md` — Generated Markdown article created from the dataset.
- `requirements.txt` — Python packages required to run the project.

## Dataset

**Dataset:** `stanforddams/daily`  
**Platform:** Hugging Face  
**Source:** The Stanford Daily police blotter archive  

The project uses two parts of the dataset:

- **Metadata split** — used for article titles and report information.
- **HTML split** — used to extract the full content of police blotter entries.

## How To Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python story_from_dataset.py
```

The script regenerates `article.md`.

## Approach

The project follows these steps:

1. Loads the Stanford Daily crime dataset from Hugging Face.
2. Parses HTML police blotter pages using BeautifulSoup.
3. Extracts incident descriptions from the reports.
4. Searches the dataset for recurring crime categories such as bike theft, burglary, assault, stalking, and other offences.
5. Counts crime patterns across the collected reports.
6. Selects representative examples from actual police blotter entries.
7. Generates a Markdown article based on the discovered patterns.

## Output

The final output is a Markdown article generated from real Stanford Daily police blotter data.

The article combines data analysis with storytelling to describe recurring patterns of crime at Stanford. It is based on incidents and themes found in the dataset rather than a single fictional event.

## Technologies Used

- Python
- Hugging Face Datasets
- BeautifulSoup
- Markdown

## Project Structure

```
.
├── story_from_dataset.py
├── article.md
├── requirements.txt
└── README.md
```
