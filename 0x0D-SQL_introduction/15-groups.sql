-- This script lists the number of records with same score
--the number of records for the score and it should be DESC;
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
