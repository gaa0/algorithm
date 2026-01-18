# Write your MySQL query statement below
select salary as SecondHighestSalary from (
select *, DENSE_RANK() over(order by salary desc) as r from Employee) a where r = 2
union
select null limit 1;