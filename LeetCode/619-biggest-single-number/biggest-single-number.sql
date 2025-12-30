# Write your MySQL query statement below
(select num from MyNumbers group by num having count(*) = 1 order by num desc limit 1)
union
(select null as num from MyNumbers) limit 1;