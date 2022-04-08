emp_data = LOAD 'emp_data.txt' using PigStorage(',') as (name:chararray,dept:chararray,salary:int,state:chararray);
emp_details = LOAD 'emp_details.txt' using PigStorage(',') as (name:chararray,age:int,phone:chararray,item:int);

group_data = GROUP emp_data by dept;
cogroup_data = COGROUP emp_data by name,emp_details by name;

inner_join = JOIN emp_data by name,emp_details by name;

left_join = JOIN emp_data by name LEFT OUTER,emp_details by name;

right_join = JOIN emp_data by name RIGHT,emp_details by name;

full_outer_join = JOIN emp_data by name FULL OUTER,emp_details by name;

filter_data = FILTER emp_data by salary > 50000;

distinct_data = DISTINCT emp_data;

order_data = ORDER emp_data by salary;
limit_data = LIMIT emp_data 1;
dump cogroup_data;
dump inner_join;
dump left_join;
dump right_join;
dump full_outer_join;
dump filter_data;
dump distinct_data;
dump order_data;
dump limit_data;