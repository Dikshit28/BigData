use db;

select count(substring(name,1,1)) as cnt
from t1
group by substring(name,1,1);