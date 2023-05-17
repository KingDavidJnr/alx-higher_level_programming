-- Displays all the cities inside CA in the database hbtn_0d_usa.
-- Results are ordered in ascending order of cities.id.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	        FROM `states`
	       WHERE `name` = "California")
ORDER BY `id`;
