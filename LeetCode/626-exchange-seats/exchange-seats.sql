# Write your MySQL query statement below
select
    a.id,
    ifnull(b.student, a.student) as student
from Seat a
left join
    (select (case when id % 2 = 1 then id + 1 else id - 1 end) as id, student from Seat) b
on a.id = b.id
order by a.id;