'''
SQL questions -
A table schema with tables like employee, department, 
employee_to_projects, projects

1) Select employee from departments where max salary of the 
   department is 40k
2) Select employee assigned to projects
3) Select employee which have the max salary in a 
   given department
4) Select employee with second highest salary
5) Table has two data entries every day for 
# of apples and oranges sold. write a query to get the 
difference between the apples… 
'''

#1)
select b.employee_id
from (select department_id, max(salary) as sal
from department
group by department_id)a inner join employee b
on a.department_id = b.department_id
where a.sal = 40000

#2)
select a.employee_id
from employee_to_projects a inner join projects b
on a.project_id = b. project_id

#3) 
select a.employee_id
from 
(select department_id, employee_id,
       dense_rank() over(partition by department_id 
                         order by salary) as rank
from employee) a  
where a.rank = 1

#4) Select employee with second highest salary:
select employee_id
from
(select employee_id, dense_rank() over(order by sal) as rank
from employee)a
where a.rank = 2

#5) Apple Orange difference in a day

select day,
       abs(max(case when fruit = 'apple' then sold
                else 0 end) -       
       max(case when fruit = 'orange' then sold
                else 0 end)) as apple_orange_diff
from table
group by day
            
                      
