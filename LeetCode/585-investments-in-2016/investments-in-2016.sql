# Write your MySQL query statement below
select round(sum(tiv_2016), 2) as tiv_2016 from (
select a.* from Insurance a
left join (select *, count(*) as cnt from Insurance group by lat, lon having cnt = 1) b
on a.lat = b.lat and a.lon = b.lon
left join (select *, count(*) as cnt from Insurance group by tiv_2015 having cnt >= 2) c
on a.tiv_2015 = c.tiv_2015
where b.pid is not null and c.pid is not null
group by a.pid, a.tiv_2015, a.tiv_2016, a.lat, a.lon) d;