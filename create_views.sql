CREATE VIEW total_log AS
SELECT TO_CHAR(time,'FMMonth DD, YYYY') AS date, COUNT(*) as log_total
FROM log
GROUP BY date;

CREATE VIEW error_log AS
SELECT TO_CHAR(time,'FMMonth DD, YYYY') AS date, COUNT(*) as error_total
FROM log
WHERE status not like '%200%'
GROUP BY date;