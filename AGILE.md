# Agile Development Notes

## Project Goal

We want to build an interactive Streamlit application that lets users compare movie box office earnings using a CSV dataset, controls, and a Plotly chart.

## User Stories

- As a user, I want to select an earnings category so I can compare worldwide, domestic, and international revenue.
- As a user, I want to choose how many movies appear so I can focus on a smaller or larger selection.
- As a user, I want clear chart labels and insights so I can understand the results.

## Current Task Board

### Done

- Collect 20 movies and their earnings from Box Office Mojo.
- Save the dataset as a CSV.
- Load and clean the dataset in Python.
- Add an earnings dropdown and movie-count slider.
- Create a labeled Plotly bar chart.
- Display the selected data and earnings insights.
- Create requirements.txt.

### In Progress

- Improve the chart’s earnings labels and add vertical grid lines.
- Complete the README and development documentation.

### To Do

- Test every earnings category and the slider limits.
- Check how missing domestic earnings are handled.
- Upload the project to GitHub.
- Deploy to Streamlit Community Cloud.
- Test the public app and add submission links.

## Step-by-Step Development

### Step 1: Dataset and Basic App

Collected the movie earnings, created the CSV, and added a basic Streamlit page. A filename mismatch prevented the CSV from loading. Renaming the file resolved the issue.

### Step 2: Interactivity and Visualization

Added the dropdown, slider, Plotly chart, filtered table, and insights. A missing definition of df caused an error. Loading the dataset before filtering it resolved the issue.

### Step 3: Review and Improvement

Reviewed the running app and identified that the x-axis values could be clearer. The next improvement is to add dollar signs, an M suffix for millions, and vertical grid lines.

### Step 4: Testing and Verification

Tested the worldwide, domestic, and international earnings options and confirmed that the chart, table, and insights updated together. Tested the slider at 5 and 20 movies. Confirmed that missing domestic earnings were excluded without causing an error.

### Step 5: Documentation and GitHub

Completed the README with the app’s purpose, dataset source, and user instructions. Confirmed that requirements.txt listed Streamlit, pandas, and Plotly. Uploaded the application, dataset, and documentation to GitHub.

### Step 6: Deployment and Final Review

Deployed the application publicly using Streamlit Community Cloud. Opened the public URL and tested the dropdown, slider, chart, table, and insights. Added the public app and GitHub repository links to the README and prepared both links for submission.

## Acceptance Checklist

- [x] Each earnings category updates the chart, table, and insights correctly.
- [x] The slider works at both 5 and 20 movies.
- [x] Missing earnings are excluded without causing an error.
- [x] The chart has a readable title, labeled axes, units, and legend.
- [x] The public app loads and its controls work.

## Reflection

Building the app in smaller steps helped isolate problems. Loading the CSV first made it easier to fix the filename issue before adding the chart. Reviewing the visualization also revealed an opportunity to make the earnings scale easier to understand.