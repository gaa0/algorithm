# Write your MySQL query statement below
select
    a.reports_to as employee_id,
    b.name,
    count(a.reports_to) as reports_count,
    round(avg(a.age), 0) as average_age
from Employees a
left join Employees b
on a.reports_to = b.employee_id
where a.reports_to is not null
group by a.reports_to
order by a.reports_to;