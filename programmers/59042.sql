-- 코드를 입력하세요
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
# SELECT *
from ANIMAL_OUTS left join ANIMAL_INS
on ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
where INTAKE_CONDITION is NULL;