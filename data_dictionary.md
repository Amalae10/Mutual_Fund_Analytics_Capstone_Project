Mutual Fund Analytics – Data Dictionary

1. fund_master.csv
Column	            Data Type	    Description
amfi_code	        Integer	        Unique AMFI scheme identifier
fund_house	        Text	        Asset Management Company (AMC)
scheme_name	        Text	        Name of the mutual fund scheme
category	        Text	        Main fund category
sub_category	    Text	        Specific fund category
plan	            Text            Direct or Regular plan
launch_date	        Date	        Scheme launch date
benchmark	        Text	        Benchmark index used for comparison
expense_ratio_pct	Float	        Annual expense ratio (%)
exit_load_pct	    Float	        Exit load charged on redemption (%)
min_sip_amount	    Float	        Minimum SIP investment amount
min_lumpsum_amount	Float	        Minimum lump sum investment amount
fund_manager	    Text	        Name of the fund manager
risk_category	    Text	        Risk category of the scheme
sebi_category_code	Text	        SEBI category code

Source: data/raw/01_fund_master.csv

2. nav_history.csv
Column	        Data Type	    Description
amfi_code	    Integer	        Mutual fund scheme identifier
date	        Date	        NAV date
nav	            Float	        Net Asset Value

Source: data/raw/02_nav_history.csv

3. 03_aum_by_fund_house.csv
Column	        Data Type	Description
date	        Date	    Reporting date
fund_house	    Text	    Asset Management Company
aum_lakh_crore	Float	    AUM in lakh crore
aum_crore	    Float	    AUM in crore
num_schemes	    Integer	    Number of schemes managed

Source: data/raw/03_aum_by_fund_house.csv

4. monthly_sip_inflows.csv
Column	                    Data Type	    Description
month	                    Date	        Month of record
sip_inflow_crore	        Float	        Monthly SIP inflow (₹ Crore)
active_sip_accounts_crore	Float	        Active SIP accounts (crore)
new_sip_accounts_lakh	    Float	        Newly opened SIP accounts (lakh)
sip_aum_lakh_crore	        Float	        SIP Assets Under Management (lakh crore)
yoy_growth_pct	            Float	        Year-over-Year growth percentage

Source: data/raw/04_monthly_sip_inflows.csv

5. category_inflows.csv
Column	            Data Type	    Description
month	            Date	        Reporting month
category	        Text	        Mutual fund category
net_inflow_crore	Float	        Net inflow/outflow in ₹ Crore

Source: data/raw/05_category_inflows.csv

6. 06_industry_folio_count.csv
Column	            Data Type	    Description
month	            Date	        Reporting month
total_folios_crore	Float	        Total investor folios (crore)
equity_folios_crore	Float	        Equity fund folios (crore)
debt_folios_crore	Float	        Debt fund folios (crore)
hybrid_folios_crore	Float	        Hybrid fund folios (crore)
others_folios_crore	Float	        Other category folios (crore)

Source: data/raw/06_industry_folio_count.csv

7. scheme_performance.csv
Column	            Data Type	    Description
amfi_code	        Integer	        Unique AMFI scheme identifier
scheme_name	        Text	        Mutual fund scheme name
fund_house	        Text	        Asset Management Company
category	        Text	        Fund category
plan	            Text	        Regular or Direct plan
return_1yr_pct	    Float	        1-year return (%)
return_3yr_pct	    Float	        3-year return (%)
return_5yr_pct	    Float	        5-year return (%)
benchmark_3yr_pct	Float	        Benchmark 3-year return (%)
alpha	            Float	        Alpha value
beta	            Float	        Beta value
sharpe_ratio	    Float	        Sharpe Ratio
sortino_ratio	    Float	        Sortino Ratio
std_dev_ann_pct	    Float	        Annualized Standard Deviation (%)
max_drawdown_pct	Float	        Maximum Drawdown (%)
aum_crore	        Float	        Assets Under Management (₹ Crore)
expense_ratio_pct	Float	        Expense Ratio (%)
morningstar_rating	Integer	        Morningstar Rating
risk_grade	        Text	        Risk Grade

Source:(data/raw/07_scheme_performance.csv)

8. investor_transactions.csv
Column	            Data Type	Description
investor_id	        Integer	        Unique investor identifier
transaction_date	Date	        Date of transaction
amfi_code	        Integer     	Mutual fund scheme identifier
transaction_type	Text	        Type of transaction (SIP/Lumpsum/Redemption)
amount_inr	        Float	        Transaction amount in Indian Rupees
state	            Text	        Investor's state
city	            Text	        Investor's city
city_tier	        Text	        City classification (Tier 1/2/3)
age_group	        Text	        Investor age group
gender	            Text	        Investor gender
annual_income_lakh	Float	        Annual income (₹ Lakh)
payment_mode	    Text	        Payment method used
kyc_status	        Text	        KYC verification status

Source: data/raw/08_investor_transactions.csv

9. portfolio_holdings.csv
Column	            Data Type	    Description
amfi_code	        Integer	        Mutual fund scheme identifier
stock_symbol	    Text	        Stock ticker symbol
stock_name	        Text	        Company/stock name
sector	            Text	        Industry sector
weight_pct	        Float	        Portfolio allocation percentage
market_value_cr	    Float	        Market value (₹ Crore)
current_price_inr	Float	        Current stock price (₹)
portfolio_date	    Date	        Portfolio reporting date

Source: data/raw/09_portfolio_holdings.csv

10. benchmark_indices.csv
Column	        Data Type	    Description
date	        Date	        Trading date
index_name	    Text	        Benchmark index name
close_value	    Float	        Closing value of the index

Source: data/raw/10_benchmark_indices.csv