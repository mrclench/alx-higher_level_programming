-- script to display mac temp of each state , displaying only top 3 
-- in ascending order by state name
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3;
