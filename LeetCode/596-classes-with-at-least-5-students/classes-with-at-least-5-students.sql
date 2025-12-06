# Write your MySQL query statement below
select class from (
select class, count(*) as cnt from Courses
group by class) as a where a.cnt >= 5;