from pathlib import Path

import streamlit as st
import pandas as pd

import plotly.express as px

st.set_page_config(page_title="2026 Movie Box Office", layout="wide")

# labeling
st.title("2026 Movie Box Office Explorer")

st.header("Overview")
# read file to be displayed
csv_path = Path(__file__).parent / "movies_2026.csv" 
df = pd.read_csv(csv_path)

# Convert formatted earnings into chart displayed; missing values stay missing.
for column in ["worldwide_usd", "domestic", "international"]:
    df[column] = pd.to_numeric(
        df[column].astype(str).str.replace(",", "", regex=False),
        errors="coerce",
    )

st.header("Data Display")
st.dataframe(df, hide_index=True)

st.caption("Source: https://www.boxofficemojo.com/year/world/2026/")

st.header("Overview")
st.write(
    "Choose an earnings category and to view movies box office earnings. "
    "The chart ranks movies based off 20-movie dataset."
)

earnings_options = {
        "Worldwide": "worldwide_usd",
        "Domestic": "domestic",
        "International": "international"
    }

category = st.selectbox(
        "Which earnings would you like to compare?",
        list(earnings_options)
    )

number_of_movies = st.slider(
        "How many movies wold you like to see?",
        min_value=5,
        max_value=20,
        value=10
    )

selected_column = earnings_options[category]

filtered_df = (
    df.dropna(subset=[selected_column])
    .sort_values(selected_column, ascending=False)
    .head(number_of_movies)
    .copy()
    )

filtered_df["earnings_millions"] = filtered_df[selected_column] / 1_000_000
filtered_df["Category"] = category

fig = px.bar(
    filtered_df,
    x="earnings_millions",
    y="movie",
    color="Category",
    orientation="h",
    title=f"Top {len(filtered_df)} Movies by {category} Earnings",
    labels={
        "earnings_millions": "Box Office Earnings (Millions of USD)",
        "movie": "Movie",
        "Category": "Earnings Category",
    },
    hover_data={selected_column: ":,.0f"},
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"},
    height=max(450, len(filtered_df) * 35)
)

fig.update_xaxes(
    title_text="Box Office Earnings (USD; M = million)",
    tickprefix="$",
    ticksuffix="M",
    tickformat=",.0f",
    showgrid=True,
    gridcolor="rgba(128, 128, 128, 0.35)",
    gridwidth=1,
)

st.plotly_chart(fig, use_container_width=True)

st.header("Data Display")
st.dataframe(
    filtered_df[["movie", selected_column]].rename(
        columns={
            "movie": "Movie",
            selected_column: f"{category} Earnings (USD)"
        }
    ),
    hide_index=True
)

st.header("Insights")

top_movie = filtered_df.iloc[0]
total_earnings = filtered_df[selected_column].sum()

st.write(
    f"**{top_movie['movie']}** has the highest {category.lower()} "
    f"earnings among the displayed movies: "
    f"**${top_movie[selected_column]:,.0f}**."
)

st.metric(
    label=f"Combined {category} Earnings of Displayed Movies",
    value=f"${total_earnings / 1_000_000_000:,.2f} billion",
)

st.info(
    "This dataset contains the top 20 movies by worldwide earnings "
    "on the collection date. Domestic and international rankings apply "
    "only to these movies. Missing earnings are excluded from the "
    "selected category; revenue does not represent profit."
)

st.caption(
    "Source: Box Office Mojo | Collected October 28, 2026 | "
    "https://www.boxofficemojo.com/year/world/2026/"
)