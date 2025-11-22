# fitness_analysis.py
# Quick analysis script for the Fitness Analytics Project
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('../data/fitness_data.csv')
print('Rows:', len(df))
print(df.head())

# Basic KPI: average steps per user
kpis = df.groupby('user_id').agg({
    'steps':'mean',
    'calories':'mean',
    'duration_min':'mean'
}).rename(columns={'steps':'avg_steps','calories':'avg_calories','duration_min':'avg_duration'})
print('\nSample KPIs per user:\n', kpis.head())

# Time series for a sample user
sample = df[df['user_id']==1].sort_values('date')
plt.plot(pd.to_datetime(sample['date']), sample['steps'])
plt.title('Steps over time (user 1)')
plt.xlabel('date'); plt.ylabel('steps')
plt.tight_layout()
plt.savefig('../data/fitness_user1_steps.png')
print('Saved sample plot to ../data/fitness_user1_steps.png')