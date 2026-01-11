# Write your MySQL query statement below
(select u.name as results from MovieRating m left join Users u on m.user_id = u.user_id
group by m.user_id order by count(rating) desc, u.name limit 1)
union all
(select title as results from MovieRating r left join Movies m on r.movie_id = m.movie_id
group by r.movie_id
order by avg(case when created_at >= '2020-02-01' and created_at < '2020-03-01' then rating end) desc, title
limit 1);