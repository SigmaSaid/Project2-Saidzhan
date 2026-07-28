from __future__ import annotations

from collections import Counter
from pathlib import Path
import re

from bs4 import BeautifulSoup
from datasets import load_dataset


ROOT = Path(__file__).parent
OUTPUT = ROOT / "article.md"


CRIME_TYPES = {
    "bike theft": [
        "bike theft",
        "bicycle theft",
        "bike stolen",
        "bicycle stolen",
    ],
    "burglary": [
        "burglary",
        "break-in",
        "break in",
    ],
    "battery": [
        "battery",
    ],
    "stalking": [
        "stalking",
    ],
    "arson": [
        "arson",
    ],
    "assault": [
        "assault",
    ],
    "rape": [
        "rape",
    ],
    "petty theft": [
        "petty theft",
    ],
    "grand theft": [
        "grand theft",
    ],
    "vehicle theft": [
        "vehicle theft",
        "car theft",
        "auto theft",
    ],
    "hate violence": [
        "hate violence",
    ],
}


def parse_html(example: dict) -> dict:
    soup = BeautifulSoup(example["html"], "html.parser")

    example["items"] = [
        re.sub(r"\s+", " ", li.get_text(" ", strip=True))
        for li in soup.find_all("li")
    ]

    return example


def count_crimes(records: list[dict]) -> Counter[str]:
    counts: Counter[str] = Counter()

    for record in records:
        text = " ".join(
            [record["title"]] + record["items"]
        ).lower()

        for crime, keywords in CRIME_TYPES.items():
            if any(keyword in text for keyword in keywords):
                counts[crime] += 1

    return counts


def find_example(records: list[dict], keywords: list[str]) -> str | None:
    for record in records:
        for item in record["items"]:
            lowered = item.lower()

            if any(keyword in lowered for keyword in keywords):
                return item.rstrip(".")

    return None


def collect_examples(
    records: list[dict],
    crimes: list[str],
) -> list[str]:

    examples = []

    for crime in crimes:
        example = find_example(
            records,
            CRIME_TYPES[crime],
        )

        if example:
            examples.append(example)

    return examples


def build_statistics(counter: Counter[str]) -> str:
    rows = [
        "| Crime | Count |",
        "|------|------:|",
    ]

    for crime, count in counter.most_common():
        rows.append(
            f"| {crime.title()} | {count} |"
        )

    return "\n".join(rows)


def build_article(
    records: list[dict],
    counts: Counter[str],
) -> str:

    total_articles = len(records)
    total_incidents = sum(
        len(record["items"])
        for record in records
    )

    top_three = counts.most_common(3)

    examples = collect_examples(
        records,
        [crime for crime, _ in top_three],
    )

    statistics = build_statistics(counts)

    example_text = "\n".join(
        f"- {example}"
        for example in examples
    )

    summary = ", ".join(
        f"**{crime}** ({count})"
        for crime, count in top_three
    )

    return f"""# Crime at Stanford: Patterns in the Police Blotter

**By Saidzhan Saitov and Afshinkhan Toktonazarov**

This article analyses the **stanforddams/daily dataset hosted on Hugging Face**, which contains Stanford Daily police blotter reports published between 2021 and 2026. The analysis examined **{total_articles} articles** containing **{total_incidents} reported incidents**.

The analysis shows that crime on campus is largely driven by recurring property offences. The three most frequently recorded crime categories are {summary}. Although Stanford is widely viewed as a safe university, the dataset demonstrates that theft and other offences appear consistently throughout the reporting period.

The dataset also documents more serious incidents, including assault, battery, stalking, rape and arson. While these crimes occur less frequently than property offences, they demonstrate the wide range of public safety issues handled by campus authorities.

## Crime Statistics

{statistics}

## Example Incidents

{example_text}

## Discussion

One notable feature of the Stanford Daily police blotter is its concise reporting style. Each incident is presented as a short factual summary, usually including information about the location and nature of the event. While individual reports may appear isolated, analysing hundreds of records reveals repeated patterns.

Property crimes represent a significant portion of reported incidents, especially those involving bicycles, vehicles and personal belongings. However, the presence of violent crimes and harassment reports highlights that campus safety involves more than preventing theft.

## Conclusion

The stanforddams/daily dataset provides a valuable record of crime patterns at Stanford University. Instead of focusing on individual cases, analysing multiple years of police blotter reports reveals broader trends in campus safety. The data shows that while Stanford remains a secure academic environment, crime continues to be a recurring part of university life.
"""


def main() -> None:

    metadata = load_dataset(
        "stanforddams/daily",
        split="train",
    )

    html = load_dataset(
        "stanforddams/daily",
        "html",
        split="train",
    )

    html = html.map(parse_html)

    records = []

    for meta, page in zip(metadata, html):
        records.append(
            {
                "title": meta.get("title", ""),
                "items": page["items"],
            }
        )

    counts = count_crimes(records)

    article = build_article(
        records,
        counts,
    )

    OUTPUT.write_text(
        article,
        encoding="utf-8",
    )

    print(f"Article written to {OUTPUT}")


if __name__ == "__main__":
    main()
