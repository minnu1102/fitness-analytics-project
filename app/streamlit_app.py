# streamlit_app.py - Fitness Analytics Dashboard (skeleton)
import streamlit as st
import pandas as pd
import altair as alt

st.title('Fitness Analytics Dashboard')
df = pd.read_csv('data/fitness_data.csv', parse_dates=['date'])
st.sidebar.write('Data: {} rows'.format(len(df)))

user = st.sidebar.selectbox('Select user', sorted(df['user_id'].unique()))
user_df = df[df['user_id']==user].sort_values('date')

st.header('User KPIs')
kpis = {
    'Average Steps': int(user_df['steps'].mean()),
    'Average Calories': round(user_df['calories'].mean(),1),
    'Average Duration (min)': round(user_df['duration_min'].mean(),1)
}
st.metric('Average Steps', kpis['Average Steps'])
st.metric('Average Calories', kpis['Average Calories'])
st.metric('Average Duration (min)', kpis['Average Duration (min)'])

st.header('Steps Over Time')
chart = alt.Chart(user_df).mark_line().encode(
    x='date:T', y='steps:Q'
)
st.altair_chart(chart, use_container_width=True)

st.header('Activity Type Distribution')
st.bar_chart(user_df['workout_type'].value_counts())
