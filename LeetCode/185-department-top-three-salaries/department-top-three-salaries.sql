# Write your MySQL query statement below
select b.name as Department, a.name as Employee, salary as Salary from (
select *, dense_rank() over(partition by departmentId order by salary desc) as r from Employee) a left join Department b on a.departmentId = b.id where r <= 3;