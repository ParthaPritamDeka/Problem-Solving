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


### NEW SQL Queries
                      
'''
1. Get the states with more the than 100000 population
2. Count the number of products which sold more than 10 units
3. Get youngest customer who bought atleast 1 product
4. Get the areas from which we have the products sold
1. Second highest salary
2. Top earning person in each department
'''
#1 
select states, population
from tbl
where population > 100000

#2
Select c.customer_id , count(distinct o.product_id) as no_products
from customers c inner join orders o
on customers.customer_id = orders.order_id
group by c.customer_id
having count(distinct o.product_id) > 10

#3
select c.customer_id
from (Select c.customer_id , dense_rank() over(order by 
                                          EXTRACT(epoch from dob)::int /86400)
             as rank
            ,count(distinct o.product_id) as no_products
from customers c inner join orders o
on customers.customer_id = orders.order_id
group by c.customer_id, dense_rank() over(order by 
                                          EXTRACT(epoch from dob)::int /86400)
having count(distinct o.product_id) > 1)c 
where c.rank = 1

#2. Top earning person in each department

select employee_id
from (select employee_id, department_id, sal
             dense_rank() over(partition by department_id order by salary desc) as rank
      from   employee
      order by department_id, sal desc)
where rank = 1
