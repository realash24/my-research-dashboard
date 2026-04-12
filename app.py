import streamlit as st

st.set_page_config(
    page_title="Research Dashboard",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Global Health & Wealth Research Dashboard")
st.markdown("---")

st.markdown("""
Welcome to the research dashboard. Use the sidebar to navigate between visualisations.

### Pages
- **Gapminder Explorer** — Interactive bubble chart of GDP vs Life Expectancy by year
- **Life Expectancy Trends** — Line chart showing life expectancy over time by continent  
- **GDP Trends** — Compare GDP per capita across countries and continents

### Data Source
All data sourced from the [Gapminder dataset](https://www.gapminder.org/) 
via Plotly Express. Data covers 1952–2007.
""")

st.info("Select a page from the sidebar to get started.")