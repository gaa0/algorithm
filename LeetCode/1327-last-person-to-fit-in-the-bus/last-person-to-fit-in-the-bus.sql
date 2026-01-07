# Write your MySQL query statement below
select s.person_name from (
select
    *,
    sum(weight) over(order by turn) as s
from Queue) s where s.s <= 1000 order by s.turn desc limit 1;