/* GetConnections between Users */
SELECT l1.user, l2.user, count(*) as x FROM pm4py.log as l1
INNER JOIN pm4py.log as l2 ON l1.name = l2.name
WHERE l1.user <> l2.user
GROUP BY l1.user, l2.user
ORDER BY x DESC;


/*Get Min max sum avg from users */
SELECT user, min(y), max(y), avg(y), sum(y)
FROM
(SELECT  name, user, count(*) as y
FROM pm4py.log
GROUP BY name, user) as x
GROUP BY user;
