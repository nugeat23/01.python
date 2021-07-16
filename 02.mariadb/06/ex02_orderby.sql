SELECT name, mDate
from usertbl
order by mDate ASC; --ASC 오름차순(디폴트), DESC 내림차순

SELECT name, height
from usertbl
ORDER BY height desc, name asc;

SELECT addr
FROM usertbl
ORDER BY addr;

SELECT distinct addr
from usertbl;

SELECT emp_no, hire_date
FROM employees
ORDER BY hire_date ASC 
limit 5;

SELECT emp_no, hire_date
FROM employees
ORDER BY hire_date ASC 
limit 0,5;      -- limit 5 offset 0과 동일
