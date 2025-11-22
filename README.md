# Fitness Analytics Project
This project is a focused data-analytics version of the Multi-AI-Agent Fitness Assistant.
It contains synthetic data, analysis scripts, a Streamlit dashboard skeleton, and guidance to extend it.

Contents:
- data/fitness_data.csv : Synthetic user fitness metrics
- notebooks/fitness_analysis.py : A runnable analysis script (can be converted to a notebook)
- app/streamlit_app.py : Streamlit app to visualize KPIs and trends
- sql/fitness_queries.sql : Example SQL queries for aggregations and KPI tables
- requirements.txt : Python package requirements
- README.md : This file

How to run:
1. Create a virtualenv and install requirements: `pip install -r requirements.txt`
2. Explore the data using `python notebooks/fitness_analysis.py` or open it in a notebook.
3. Run the dashboard: `streamlit run app/streamlit_app.py`
