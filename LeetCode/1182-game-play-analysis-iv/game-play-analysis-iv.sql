# Write your MySQL query statement below
select
    round(count(distinct player_id) / (select count(distinct player_id) from Activity) , 2) as fraction
from (
select
    b.player_id,
    rank() over (partition by a.player_id order by a.event_date) as r
from Activity a
left join Activity b
on
    a.player_id = b.player_id and
    a.event_date + interval 1 day = b.event_date
) c
where c.r = 1;