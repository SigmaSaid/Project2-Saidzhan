# Project 2: Crime at Stanford

Created by Saidzhan Saitov and Afshinkhan Toktonazarov

## Overview

This project uses the Hugging Face dataset stanforddams/daily, a collection of Stanford Daily police blotter articles, to analyze crime reports from Stanford University. It produces two distinct outputs:
1. A nonfiction data analysis (report.md) that identifies recurring crime themes, extracts representative examples, and presents statistics.
2. A data-grounded creative piece (article.md) that dramatizes one of the recurring patterns found in the data, accompanied by a Note on Sources identifying the real incidents that inspired it.

A third file, sources.txt, saves the raw police blotter entries that match each identified crime category for documentation and verification.
The project combines data extraction and natural language analysis to transform police blotter records into both a readable narrative and a rigorous analytical report about crime at Stanford.

The project combines data extraction and natural language analysis to transform police blotter records into a readable narrative about crime at Stanford.

## Repository Contents

- story_from_dataset.py — Python script that loads the dataset, parses HTML police blotter entries, identifies recurring crime themes, extracts representative examples, and generates the final outputs.
- report.md — Generated Markdown data analysis created from the dataset.
- article.md — Generated data-grounded creative piece dramatizing a recurring pattern from the dataset, with a Note on Sources.
- sources.txt — Raw police blotter entries that match the identified crime categories, saved for documentation and verification.
- requirements.txt — Python packages required to run the project.

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
7. Generates a Markdown data analysis (report.md) based on the discovered patterns.
8. Generates a data-grounded creative piece (article.md) dramatizing a recurring pattern, with a Note on Sources citing the real entries that inspired it.
9. Saves all matching raw entries to sources.txt for documentation.

## Output

- report.md — Nonfiction Data Analysis
A statistical overview of crime patterns at Stanford, including crime counts, example incidents, and discussion of trends found in the police blotter data.
- article.md — Data-Grounded Creative Piece
A short narrative dramatizing the recurring pattern of unattended-electronics theft and bicycle theft documented in the dataset. This is not a report on a single real incident, but a fictionalized composite based on multiple documented patterns. A Note on Sources at the end of the piece identifies the specific real patterns and raw entries that inspired the narrative.
- sources.txt — Raw Source Documentation
A plain-text file containing the actual police blotter entries that match each identified crime category, saved for verification and transparency.

## Technologies Used

- Python
- Hugging Face Datasets
- BeautifulSoup
- Markdown

## Project Structure

```
.
.
├── story_from_dataset.py
├── report.md
├── article.md
├── sources.txt
├── requirements.txt
└── README.md
```
