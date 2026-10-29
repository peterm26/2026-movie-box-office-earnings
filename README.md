# 2026 Movie Box Office Explorer

## Purpose

This Streamlit application lets users explore and compare box office earnings for 20 movies from Box Office Mojo’s 2026 worldwide chart.

## Project Links

- Public Streamlit app: ADD YOUR DEPLOYED APP URL
- GitHub repository: ADD YOUR REPOSITORY URL

## Dataset

The dataset is stored in `movies_2026.csv` and contains the top 20 movies by worldwide earnings on the collection date.

- Source: [Box Office Mojo — 2026 Worldwide Box Office](https://www.boxofficemojo.com/year/world/2026/)
- Collection date: October 28, 2026
- Currency: US dollars

The CSV contains these columns:

| Column | Description |
|---|---|
| `rank` | Worldwide ranking on the collection date |
| `movie` | Movie title |
| `worldwide_usd` | Worldwide box office earnings |
| `domestic` | Domestic box office earnings |
| `international` | International box office earnings |

## Features

- Dropdown to select worldwide, domestic, or international earnings.
- Slider to display between 5 and 20 movies.
- Interactive Plotly bar chart with hover information.
- Data table showing the selected movies and earnings.
- Insights identifying the highest earner and combined earnings of the displayed movies.

## Run Locally

Install Python, then download or clone this repository. Open a terminal in the project folder and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the app:

```bash
python -m streamlit run app.py
```

Open the Local URL displayed in the terminal.

## User Instructions

1. Choose an earnings category from the dropdown.
2. Move the slider to choose how many movies to display.
3. Hover over the chart’s bars to view earnings.
4. Review the matching data table and insights.

The chart, filtered table, and insights update when the controls change.

## Project Files

- `app.py`: Streamlit application, data preparation, controls, chart, and insights.
- `movies_2026.csv`: Movie earnings dataset.
- `requirements.txt`: Required Python packages.
- `README.md`: Project description and instructions.