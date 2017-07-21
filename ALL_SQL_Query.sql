
/********** apple and Orange sold difference ************/


CREATE table stg.temp_x(Day date, fruit varchar(200), sold int);

INSERT INTO stg.temp_x VALUES
 ('2011-11-04', 'Apple', 5)
,('2011-11-03', 'Apple', 2)
,('2011-11-02', 'Apple', 3)
,('2011-11-01', 'Apple', 4)
,('2011-11-04', 'Orange', 8)
,('2011-11-03', 'Orange', 7)
,('2011-11-02', 'Orange', 9)
,('2011-11-01', 'Orange', 11);


select Day,  abs(max(decode(fruit, 'Apple', sold, null)) - max(decode(fruit, 'Orange', sold, null))) Diff_apple_vs_Orange_sold
from stg.temp_x
group by Day
order by Day;

/*********************************/

/***** Three consecutive wins *******/

CREATE TABLE stg.v_playday (played date, winner varchar(100), looser varchar(100));

insert into stg.v_playday values ('2013-03-03', 'USA', 'China'),
                                 ('2013-03-04', 'USA', 'Belgium'),
                                 ('2013-03-05', 'USA', 'Italy'),
                                 ('2013-03-05', 'USA', 'Russia'),
                                 ('2013-03-03', 'France', 'Germany'),
                                 ('2013-03-09', 'USA', 'Russia'),
                                 ('2013-03-06', 'France', 'Germany'),
                                 ('2013-03-09', 'USA', 'Russia');

/***********************/

select count(*)
from
(select winner,grp, (max(played)-min(played))+1 as no_of_consecutive_wins
from 
(
select winner, (extract(epoch from played) ::int / 86400 
       - row_number() over (partition by winner order by played)) grp, played
from stg.v_playday
order by winner, played)
group by winner,grp)
where winner = 'USA' and no_of_consecutive_wins = 3;


/********************************/

  
#### Delete duplicates from Oracle ####


delete from table a
where table.row_id > Any(select row_id
                         from table b
                         where a.col1 = b.col1
                         and   a.col2 = b.col2)
			   
#### Corelated Subquery display all customer who have no orders ####

select * from customers c
where not exists (select 1 from orders o where c.cust_id = o.cust_id)			   
   

CREATE TEMP TABLE v(id int, visit date);
INSERT INTO v VALUES
 (444631, '2011-11-07')
,(444631, '2011-11-06')
,(444631, '2011-11-05')
,(444631, '2011-11-04')
,(444631, '2011-11-02')
,(444631, '2011-11-01')
,(444632, '2011-12-02')
,(444632, '2011-12-03')
,(444632, '2011-12-05');



SELECT id, max(dur) + 1 AS max_consecutive_days
FROM (
    SELECT id, grp, max(visit) - min(visit) AS dur
    FROM (
      -- subtract an integer representing the number of day from the row_number()
      -- creates a "group number" (grp) for consecutive days
      SELECT id
            ,EXTRACT(epoch from visit)::int / 86400
           - row_number() OVER (PARTITION BY id ORDER BY visit) AS grp
            ,visit
      FROM   v
      ORDER  BY 1,2
      ) x
    GROUP BY 1,2
    ) y
GROUP  BY 1
ORDER  BY 1
LIMIT  1;



/************* Funny Practice ***************/

select id, max(no_consecutive_visits)
from 
(
select id, (no_of_visits +1) as no_consecutive_visits
from (
select id, grp, (max(visit) - min(visit)) no_of_visits
FROM
(
select id, grp, visit
FROM
(

select id,
       extract(epoch from visit) secs_from_epoch , EXTRACT(epoch from visit)::int / 86400 day_from_epoch,
       row_number() over (partition by id order by visit) as rownum,
       (EXTRACT(epoch from visit)::int / 86400 -
       row_number() over (partition by id order by visit)) grp,
       visit
FROM   stg.temp_v
      ORDER  BY 1,2 
)
order by id, grp
)

group by id, grp
)
)
group by id;


/********************* Three / Four consecutive wins with row_num() function***********************/

/*************************Three consecutive *********************************/


CREATE TABLE stg.v_temp_playday (played date, winner varchar(100), looser varchar(100));

insert into stg.v_temp_playday values ('2013-03-03', 'USA', 'China'),
                                 ('2013-03-04', 'USA', 'Belgium'),
                                 ('2013-03-05', 'USA', 'Italy'),
                                 ('2013-03-06', 'USA', 'Russia'),
                                 ('2013-03-07', 'France', 'Germany'),
                                 ('2013-03-08', 'USA', 'Russia'),
                                 ('2013-03-09', 'France', 'Germany'),
                                 ('2013-03-10', 'USA', 'Russia');


analyze stg.v_temp_playday;

--truncate table stg.v_temp_playday;

select winner, no_consecuive_win
from 
(select winner, grp, (days_diff + 1) as no_consecuive_win
from (select winner, grp, (max(played) - min(played)) days_diff
from
(select winner, played, extract(epoch from played) ::int /86400 - row_number() over (partition by winner order by played) grp
from stg.v_temp_playday
order by winner, played)
group by winner, grp
order by winner, grp))
where winner


select 
select count(*) as cnt

select a.*
from
(select c.*, row_number() over(order by played) rn from stg.v_temp_playday c) a
inner join (select c.*, row_number() over(order by played) rn from stg.v_temp_playday c) b on a.winner = b.winner and a.rn = b.rn+1
inner join (select c.*, row_number() over(order by played) rn from stg.v_temp_playday c) d on b.winner = d.winner and b.rn = d.rn+1
inner join (select c.*, row_number() over(order by played) rn from stg.v_temp_playday c) e on d.winner = e.winner and d.rn = e.rn+1
where a.winner = 'USA' ;


/************ Select max value without max function **************/

select ID from
pr where ID not in (select a.ID
from pr a, pr b
where b.ID > a.ID) 


/********************** PSOTGRESQL -Consecutive Ones Query ***********************/

select b.Num
from (select a.Num, a.grp, count(*) as cnt 
      from (select Num, Id, (Id - row_number() over (partition by Num order by Id)) grp
            from one_cons
            order by Num, Id) a
      group by Num, grp) b
where cnt >=3



/********************** MSQL - Consecutive Ones Query *****************/

select 
a.Num
from one_cons a,
     one_cons b,
     one_cons c
where   a.Id = b.Id - 1
    and b.Id = c.Id - 1
    and a.Num = b.Num
    and b.Num = c.Num
