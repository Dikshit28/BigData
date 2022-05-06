employee_info = LOAD 'employee.txt' using PigStorage(',') as (emp_id:int,emp_name:chararray,emp_salary:int,emp_rating:int);
emp_expenses = LOAD 'expenses.txt' using PigStorage('\t') AS (emp_id:int, expense:int);

emp_details_LEFTJOIN = JOIN employee_info BY emp_id LEFT OUTER, emp_expenses BY emp_id;
JOIN_details = FILTER emp_details_LEFTJOIN BY emp_expenses::emp_id IS NULL;
emp_details = FOREACH JOIN_details GENERATE employee_info::emp_id, employee_info::emp_name;
DUMP emp_details;   
