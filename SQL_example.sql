-- Selecting all columns from a table
select * from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE" limit 10;

-- Count the number of rows
select count(*) from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE";  --1500


-- Joining two tables with explicit table names
select * from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE" 
JOIN "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF100TCL"."DATE_DIM"
ON "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE"."S_REC_END_DATE" 
= "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF100TCL"."DATE_DIM"."D_DATE"
;

-- Joining two tables with table referrence name
CREATE DATABASE DBS_TEST;
USE DATABASE DBS_TEST;
CREATE TABLE DBS_EXAMPLE_TABLE
AS
select A.*, B.D_DAY_NAME from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE"  A
JOIN "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF100TCL"."DATE_DIM" B
ON A."S_REC_END_DATE" = B."D_DATE"
;

-- Multiple where clauses - be careful of the logic
SELECT * FROM "DBS_TEST"."PUBLIC"."DBS_EXAMPLE_TABLE"
where (S_STORE_ID = 'AAAAAAAAEAAAAAAA' and S_STORE_SK = 4)
or (S_STORE_ID = 'AAAAAAAAKAAAAAAA' and S_STORE_SK = 10) 
;

-- Create my own column using concatanate PIPE |
SELECT S_STORE_ID||'-'||S_STORE_NAME as DBS_STORE_ID
       ,a.*  
FROM "DBS_TEST"."PUBLIC"."DBS_EXAMPLE_TABLE" a
where S_STORE_ID = 'AAAAAAAAKAAAAAAA' ;


-- Check for primay key
SELECT count(*) as total_rows, 
       count(distinct S_STORE_ID) as distinct_Stores,
       count(distinct S_STORE_ID||'-'||S_STORE_SK) as distinct_DBS_idea
FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE";


-- FUCKING MASSIVE
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE_SALES" limit 10;


-- Find all the stores that have indeed closed
create table  stores_that_closed
as
select * 
from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE"
where S_CLOSED_DATE_SK  is not NULL;


-- Only the sales on te day the store closed
-- SUBQUERY 46.23s
-- We used the Partition (or cluster) here so we limited the number of partitions we ad to read
select * from
  (select * 
  from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE"
  where S_CLOSED_DATE_SK  is not NULL) dbs
inner join "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE_SALES" item
on dbs.S_CLOSED_DATE_SK = item.SS_SOLD_DATE_SK
and (S_STORE_ID = 'AAAAAAAAEAAAAAAA' and S_STORE_SK = 4);



-- Aggregations
SELECT sum(SS_NET_PROFIT) as total_profit,
       max(SS_NET_PROFIT) as max_profit
FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE_SALES" 
where SS_SOLD_DATE_SK = 2451126 ;



-- Find the number of sales that were profitable
select profit_yn,
       count(*)
from
(
select SS_NET_PROFIT,
       case when SS_NET_PROFIT >0 then 1 else 0 end as profit_yn
FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE_SALES" a
where SS_SOLD_DATE_SK = 2451126)
group by profit_yn;


-- Find the number of sales that were profitable
select sum(case when SS_NET_PROFIT >0 then 1 else 0 end)
from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE_SALES"
where SS_SOLD_DATE_SK = 2451126;


-- We could create this as a new table if we plan to use this flag moving forwards
create table "STORE_SALES_PROFIT_FLAG" 
as
select a.*
       case when SS_NET_PROFIT >0 then 1 else 0 end as profit_yn
FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."STORE_SALES" a

"STORE_SALES" = 1.3T 
"STORE_SALES_PROFIT_FLAG" = 1.3T+

//check your new table BEFORE YOU DROP!!!!
//drop "STORE_SALES"

//~ TILDA



;

--long comments
/* TIHG
JFTG
JHBGTJHG
*/


