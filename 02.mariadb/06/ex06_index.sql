create index idx_employees_first_name
on employees(first_name);

show index from employees;

-- INDEX 삭제
drop index idx_employees_first_name on employees;