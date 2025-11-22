-- Example SQL to create KPI aggregated table for fitness data
CREATE TABLE fitness_kpis AS
SELECT
  user_id,
  COUNT(*) AS total_sessions,
  AVG(steps) AS avg_steps,
  AVG(calories) AS avg_calories,
  AVG(duration_min) AS avg_duration
FROM fitness_data
GROUP BY user_id;

-- Weekly aggregation
SELECT
  user_id,
  DATE_TRUNC('week', date) AS week,
  AVG(steps) AS avg_steps_week
FROM fitness_data
GROUP BY user_id, DATE_TRUNC('week', date)
ORDER BY user_id, week;
