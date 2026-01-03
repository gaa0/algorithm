# Write your MySQL query statement below
select
    *,
    (case when (x > y and x > z and x >= y + z)
    or (y > x and y > z and y >= x + z)
    or (z > x and z > y and z >= x + y) then 'No'
    else 'Yes' end)
    as triangle
from Triangle;