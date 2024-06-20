-- This script lists all cities in database , sort cities.id in
-- ASCENDING ORDER
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id ASC;
