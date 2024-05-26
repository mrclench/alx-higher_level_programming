-- Using the same imported data dump ,Find the TOP 3 cities with the highest
-- temperatures in JULY AND AUGUST in descenDING order
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avG_temp DESC LIMIT 3;
