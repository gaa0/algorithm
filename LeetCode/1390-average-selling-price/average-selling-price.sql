# Write your MySQL query statement below
select distinct(lp.product_id), ifnull(average_price, 0) as average_price from Prices lp left join (
select p.product_id, round(sum(price * units) / sum(units), 2) as average_price
from Prices p join UnitsSold u on p.product_id = u.product_id
where start_date <= purchase_date and purchase_date <= end_date
group by product_id) b
on lp.product_id = b.product_id;