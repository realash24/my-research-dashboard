import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Life Expectancy Trends", layout="wide")

st.title("Life Expectancy Trends")
st.caption("How life expectancy has changed over time")

df = px.data.gapminder()

# Sidebar controls
st.sidebar.header("Controls")

view_by = st.sidebar.radio(
    "View by",
    options=["Continent (average)", "Individual countries"]
)

continents = df["continent"].unique().tolist()
selected_continents = st.sidebar.multiselect(
    "Filter Continents",
    options=continents,
    default=continents
)

filtered = df[df["continent"].isin(selected_continents)]

# Chart logic
if view_by == "Continent (average)":
    grouped = (
        filtered.groupby(["year", "continent"])["lifeExp"]
        .mean()
        .reset_index()
    )
    fig = px.line(
        grouped,
        x="year",
        y="lifeExp",
        color="continent",
        markers=True,
        labels={
            "year": "Year",
            "lifeExp": "Average Life Expectancy (years)"
        },
        title="Average Life Expectancy by Continent (1952–2007)"
    )
else:
    countries = sorted(filtered["country"].unique().tolist())
    selected_countries = st.sidebar.multiselect(
        "Select Countries",
        options=countries,
        default=["Australia", "United States", "China", "India"]
    )
    country_df = filtered[filtered["country"].isin(selected_countries)]
    fig = px.line(
        country_df,
        x="year",
        y="lifeExp",
        color="country",
        markers=True,
        labels={
            "year": "Year",
            "lifeExp": "Life Expectancy (years)"
        },
        title="Life Expectancy by Country (1952–2007)"
    )

fig.update_layout(height=500)
st.plotly_chart(fig, width="stretch")