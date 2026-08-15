--1. top 5 funds by AUM
select Scheme_name,aum_crore from fact_performance order by aum_crore desc limit 5;

--2.average NAV per month
select 
strftime('%Y-%m', date) as month,
AVG(nav) as average_nav
from fact_nav
group by month
order by month;

--3.SIP inflow YOY growth
select 
strftime('%Y',transaction_date)  as year,
sum(amount_inr) as total_sip
from fact_transactions
where transaction_type="SIP"
group by year
order by year;

--4.transaction by state
select state,count(*) as total_transactions
from fact_transactions
group by state
order by total_transactions desc;

-- 5.Funds with Expense Ratio < 1%
select scheme_name,expense_ratio_pct
from fact_performance
where expense_ratio_pct < 1;

-- 6.Top 10 Funds by 5-Year Return
select
scheme_name,
return_5yr_pct
from fact_performance
order by return_5yr_pct desc
limit 10;

-- 7. Average Expense Ratio by Category
select
category,
AVG(expense_ratio_pct) as avg_expense_ratio
from fact_performance
group by category;

-- 8. Average AUM by Category
select
category,
AVG(aum_crore) as average_aum
from fact_performance
group by category;

-- 9. Highest NAV Recorded
select
amfi_code,
MAX(nav) as highest_nav
from fact_nav
group by amfi_code
order by highest_nav desc
limit 10;

-- 10. Number of Transactions by Type
select
transaction_type,
COUNT(*) as total
from fact_transactions
group by transaction_type;