import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Gapminder Explorer", layout="wide")

st.title("Gapminder Explorer")
st.caption("GDP per capita vs Life Expectancy — bubble size = population")

df = px.data.gapminder()

# Sidebar controls
st.sidebar.header("Controls")

available_years = sorted(df["year"].unique().tolist())
year = st.sidebar.select_slider(
    "Select Year",
    options=available_years,
    value=available_years[-1]
)

continents = df["continent"].unique().tolist()
selected_continents = st.sidebar.multiselect(
    "Filter by Continent",
    options=continents,
    default=continents
)

# Filter data
filtered = df[
    (df["year"] == year) &
    (df["continent"].isin(selected_continents))
]

# Metrics row
col1, col2, col3 = st.columns(3)
col1.metric("Countries shown", len(filtered))
col2.metric("Avg Life Expectancy", f"{filtered['lifeExp'].mean():.1f} yrs")
col3.metric("Avg GDP per Capita", f"${filtered['gdpPercap'].mean():,.0f}")

# Chart
fig = px.scatter(
    filtered,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    labels={
        "gdpPercap": "GDP per Capita (log scale)",
        "lifeExp": "Life Expectancy (years)",
        "pop": "Population"
    },
    title=f"Life Expectancy vs GDP per Capita ({year})"
)

fig.update_layout(height=550)
st.plotly_chart(fig, width="stretch")