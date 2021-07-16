SELECT userid, name
from usertbl
where height BETWEEN 180 and 183;

SELECT name, addr
FROM usertbl
where addr = '경남'
or addr = '전남'
or addr = '경북';

SELECT name, addr
FROM usertbl
where addr in ('경남','전남','경북');

SELECT name, height
FROM usertbl
where name like '김%'; --%는 글자수와 상관없이 아무거나 와도 됨

SELECT name, height
FROM usertbl
where name like '%경%';

SELECT name, height
FROM usertbl
where name like '_종신'; -- _: 한 글자는 아무거나...FROM 

SELECT name, height
FROM usertbl
where name like '%종%';

-- *,-,% --> 와일드카드 문자


SELECT name, height
from usertbl
where height > (
    SELECT height
    from usertbl
    where name ='김경호'

);
-- 서브 쿼리가 1개의 행만 리턴하면 --> 단일행 서브쿼리

SELECT name, height
from usertbl
where height > (
    SELECT height
    from usertbl
    where  addr ='경남'

);
-- 서브 쿼리가 n개의 행을 리턴하면 -->다중행 서브쿼리

select name, height 
from usertbl
where height >= ANY (
    SELECT height
    from usertbl
    where addr = '경남'

);

select name, height 
from usertbl
where height >= all (
    SELECT height
    from usertbl
    where addr = '경남'

);

SELECT height
from usertbl
where addr = '경남';

select first_name from employees;

select first_name as 이름, last_name as 성명
from employees
where emp_no < 10010;

select first_name 이름, last_name 성명
from employees
where emp_no < 10010;

select *
from employees
where first_name='Uri' and last_name='Lenart';

select *
from employees
where emp_no = 10041;

select *
from employees
where birth_date >= '1960-01-01';

select *
from employees
where birth_date >= '1960-01-01'
and birth_date <= '1960-12-31';

select *
from employees
where last_name = 'Lenart'
or last_name = 'Baaz'
or last_name = 'Pillow';

SELECT * 
FROM employees
WHERE last_name IN ('Lenart','Baaz','Pillow') ;