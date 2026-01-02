# Write your MySQL query statement below
select a.employee_id, ifnull(b.department_id, a.department_id) as department_id
from Employee a
left join Employee b
on a.employee_id = b.employee_id
and b.primary_flag = 'Y'
group by a.employee_id;