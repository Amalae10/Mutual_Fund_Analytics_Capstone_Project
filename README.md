# Bluestock Mutual Fund Analytics Capstone

## 1. Project Overview

The Bluestock Mutual Fund Analytics Capstone is a data analytics project focused on analyzing Indian mutual fund data.

The project covers data ingestion, data cleaning, exploratory data analysis, fund performance analysis, investor analytics, risk metrics, advanced analytics, and an interactive Power BI dashboard.

### Objectives

- Analyze mutual fund performance and risk
- Study SIP and investor transaction trends
- Analyze investor behavior and cohorts
- Calculate Sharpe ratio, Sortino ratio, Alpha and Beta
- Calculate VaR and CVaR
- Analyze sector concentration using HHI
- Build a mutual fund recommendation system
- Create an interactive four-page Power BI dashboard

---

## 2. Data Sources

The project uses the following datasets:

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

## 3. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- SQLite
- Power BI
- Git
- GitHub

---

## 4. Project Structure

Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── check_database.py
│   ├── clean_nav.py
│   ├── clean_performance.py
│   ├── clean_transactions.py
│   ├── data_exploration.py
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── load_database.py
│   ├── run_queries.py
│   └── validate_amfi.py
│
├── Day3_EDA/
├── Day4_Fund_performance/
├── Day5/
├── Day6 _ Advanced Analytics + Risk Metrics/
├── Day7/
│   ├── Bluestock_MF_Presentation.ppt
│   └── Final_Report.pdf
│
├── sql/
├── run_pipeline.py
├── requirements.txt
└── README.md

##  5. Setup Instructions

### a. Install Python

Make sure Python is installed on your system.

### b. Install Dependencies

Open the terminal in the project folder and run:

pip install -r requirements.txt

### c. Open the Project

Open the project folder in VS Code.

### d. Run the ETL Pipeline

python run_pipeline.py


## 6. How to Run the ETL Pipeline

The project contains a master ETL script called `run_pipeline.py`.

The ETL process follows these steps:

Raw Data → Data Ingestion → Data Cleaning → Data Validation → Processed Data → SQLite Database

To run the complete ETL pipeline, open the terminal in the project root folder and run:

python run_pipeline.py
---

##  7. File and Folder Descriptions

### `data/`
Contains the raw and processed mutual fund datasets.

- `raw/` — Original datasets
- `processed/` — Cleaned datasets used for analysis

### `scripts/`
Contains Python scripts used for data processing and database operations.

- `data_ingestion.py` — Loads the raw datasets
- `clean_nav.py` — Cleans NAV data
- `clean_performance.py` — Cleans performance data
- `clean_transactions.py` — Cleans investor transaction data
- `data_exploration.py` — Performs initial data exploration
- `check_database.py` — Checks the SQLite database
- `load_database.py` — Loads processed data into SQLite
- `run_queries.py` — Executes SQL queries
- `live_nav_fetch.py` — Fetches live NAV data
- `validate_amfi.py` — Validates AMFI fund codes

### `Day3_EDA/`
Contains the Exploratory Data Analysis notebook and analysis results.

### `Day4_Fund_performance/`
Contains fund performance and risk metric analysis.

### `Day5/`
Contains the Power BI dashboard, dashboard PDF, and page screenshots.

### `Day6 _ Advanced Analytics + Risk Metrics/`
Contains advanced analytics files such as:

- `Advanced_Analytics.ipynb`
- `var_cvar_report.csv`
- `rolling_sharpe_chart.png`
- `recommender.py`

### `Day7/`
Contains the final project deliverables:

- `Bluestock_MF_Presentation.ppt`
- `Final_Report.pdf`

### `run_pipeline.py`
Master ETL script that runs the data ingestion, cleaning, validation, and database loading steps.

### `requirements.txt`
Contains the Python libraries required to run the project.

### `README.md`
Contains project overview, setup instructions, file descriptions, ETL instructions, and dashboard instructions.

---

##  8. How to Open the Power BI Dashboard

The Power BI dashboard is available in the `Day5/` folder.

### Steps

1. Install **Microsoft Power BI Desktop**.
2. Open the `Day5/` folder.
3. Locate the `.pbix` Power BI dashboard file.
4. Open the `.pbix` file using Power BI Desktop.
5. If prompted, select the appropriate local data source.
6. Click **Refresh** if required.
7. Use the slicers and interactive visuals to explore the dashboard.

### Dashboard Pages

The dashboard contains four interactive pages:

- **Page 1 — Industry Overview**
  - Total AUM
  - SIP Inflows
  - Folio Count
  - Number of Schemes
  - Industry AUM Trend
  - Top Fund Houses

- **Page 2 — Fund Performance**
  - Return vs Risk
  - Fund Scorecard
  - NAV vs Benchmark
  - Fund House, Category and Plan slicers

- **Page 3 — Investor Analytics**
  - Transaction Amount by State
  - SIP vs Lumpsum vs Redemption
  - Age Group Analysis
  - Monthly Transaction Volume

- **Page 4 — SIP & Market Trends**
  - SIP Inflow Trend
  - Nifty 50 Trend
  - Category Inflows
  - SIP Account Growth

  ---

##  9. Advanced Analytics

The Day 6 analysis focuses on advanced risk, performance, and investor analytics.

The advanced analytics files are available in:

`Day6 _ Advanced Analytics + Risk Metrics/`

### Key Analyses

- **VaR (Value at Risk)** — Measures the potential loss of a fund at a selected confidence level.
- **CVaR (Conditional Value at Risk)** — Measures the average loss beyond the VaR threshold.
- **Rolling Sharpe Ratio** — Evaluates risk-adjusted performance over a moving time window.
- **Investor Cohort Analysis** — Compares investment behavior across different investor groups.
- **SIP Continuation Analysis** — Examines investor SIP continuation and investment behavior.
- **Sector Concentration Analysis** — Uses the Herfindahl-Hirschman Index (HHI) to measure portfolio concentration.
- **Fund Recommendation** — Recommends the top funds by Sharpe ratio based on the investor's risk grade.

### Day 6 Files

- `Advanced_Analytics.ipynb` — Advanced analytics notebook
- `var_cvar_report.csv` — VaR and CVaR results
- `rolling_sharpe_chart.png` — Rolling Sharpe ratio visualization
- `recommender.py` — Risk-based fund recommendation logic

## 10. Final Deliverables

### Day 5 — Power BI Dashboard

- Power BI dashboard (`.pbix`)
- Dashboard PDF
- Four dashboard page screenshots

### Day 6 — Advanced Analytics

- `Advanced_Analytics.ipynb`
- `var_cvar_report.csv`
- `rolling_sharpe_chart.png`
- `recommender.py`

### Day 7 — Final Submission

- Clean Python codebase
- `run_pipeline.py`
- `Final_Report.pdf`
- `Bluestock_MF_Presentation.ppt`
- Root `README.md`

---

## 11. Database and GitHub

### SQLite Database

The project uses SQLite for storing and querying the processed mutual fund data.

The database contains the required project tables and can be generated locally through the ETL pipeline.

The SQLite database file is excluded from GitHub using `.gitignore`:

*.db

---

## 12. Author

**Amal AE**

Bluestock Mutual Fund Analytics Capstone Project

This project was developed as part of the Bluestock Mutual Fund Analytics Capstone, covering data engineering, data analysis, risk analytics, investor analytics, and business intelligence dashboard development.