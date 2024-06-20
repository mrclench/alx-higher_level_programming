-- import a table dump into database hbtn_0c_0
-- find the avg temp of each cityin DESCENDING ORDER
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
