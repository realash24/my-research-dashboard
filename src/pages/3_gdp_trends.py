import streamlit as st
import plotly.express as px

st.set_page_config(page_title="GDP Trends", layout="wide")

st.title("GDP per Capita Trends")
st.caption("Economic growth across countries and continents")

df = px.data.gapminder()

# Sidebar controls
st.sidebar.header("Controls")

chart_type = st.sidebar.selectbox(
    "Chart type",
    ["Line chart", "Box plot", "Bar chart (latest year)"]
)

continents = df["continent"].unique().tolist()
selected_continents = st.sidebar.multiselect(
    "Filter Continents",
    options=continents,
    default=["Oceania", "Europe", "Americas"]
)

filtered = df[df["continent"].isin(selected_continents)]

# Charts
if chart_type == "Line chart":
    countries = sorted(filtered["country"].unique().tolist())
    selected_countries = st.sidebar.multiselect(
        "Select Countries",
        options=countries,
        default=["Australia", "United Kingdom", "United States"]
    )
    country_df = filtered[filtered["country"].isin(selected_countries)]
    fig = px.line(
        country_df,
        x="year",
        y="gdpPercap",
        color="country",
        markers=True,
        labels={"gdpPercap": "GDP per Capita (USD)", "year": "Year"},
        title="GDP per Capita Over Time"
    )

elif chart_type == "Box plot":
    fig = px.box(
        filtered,
        x="continent",
        y="gdpPercap",
        color="continent",
        log_y=True,
        labels={"gdpPercap": "GDP per Capita (log scale)"},
        title="GDP per Capita Distribution by Continent"
    )

else:
    latest = filtered[filtered["year"] == filtered["year"].max()]
    top = latest.nlargest(20, "gdpPercap")
    fig = px.bar(
        top,
        x="country",
        y="gdpPercap",
        color="continent",
        labels={"gdpPercap": "GDP per Capita (USD)", "country": "Country"},
        title=f"Top 20 Countries by GDP per Capita ({filtered['year'].max()})"
    )
    fig.update_layout(xaxis_tickangle=-45)

fig.update_layout(height=500)
st.plotly_chart(fig, width="stretch")