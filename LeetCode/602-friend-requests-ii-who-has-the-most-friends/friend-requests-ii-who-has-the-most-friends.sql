# Write your MySQL query statement below
select distinct a.requester_id as id, ifnull(b.num, 0) + ifnull(c.num, 0) as num from (
    select distinct requester_id from RequestAccepted
    union
    select distinct accepter_id from RequestAccepted
    ) a
left join (select requester_id, count(accepter_id) as num from RequestAccepted group by requester_id) as b on a.requester_id = b.requester_id
left join (select accepter_id, count(requester_id) as num from RequestAccepted group by accepter_id) as c on a.requester_id = c.accepter_id order by num desc limit 1;

-- select * from RequestAccepted a
-- left join (select requester_id, count(accepter_id) as num from RequestAccepted group by requester_id) as b on a.requester_id = b.requester_id
-- left join (select accepter_id, count(requester_id) as num from RequestAccepted group by accepter_id) as c on a.requester_id = c.accepter_id;