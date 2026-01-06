# Write your MySQL query statement below
select distinct a.product_id, ifnull(b.price, 10) as price from Products a left join (
select p.product_id, p.new_price as price from (
select *, rank() over(partition by product_id order by change_date desc) as r from Products where change_date <= '2019-08-16') p where p.r = 1) b on a.product_id = b.product_id;