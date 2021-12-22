-- 코드를 입력하세요
set @N = -1;

select T.HOUR, ifnull(dayT.C, 0) as COUNT
from
(select @N := @N + 1 as HOUR
from ANIMAL_OUTS
limit 24) as T

left join
(SELECT HOUR(DATETIME) as h, count(HOUR(DATETIME)) as C from ANIMAL_OUTS
group by HOUR(DATETIME)) as dayT
on T.HOUR = dayT.h