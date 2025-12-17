# Write your MySQL query statement below
select
    stu.student_id,
    stu.student_name,
    sub.subject_name,
    count(e.student_id) as attended_exams
from Students stu
cross join Subjects sub
left join Examinations e
on sub.subject_name = e.subject_name and e.student_id = stu.student_id
group by stu.student_id, stu.student_name, sub.subject_name
order by stu.student_id, sub.subject_name;