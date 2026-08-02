-- Fund Dimension
CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT
);

-- Date Dimension
CREATE TABLE dim_date (
    date DATE PRIMARY KEY
);

-- NAV Fact Table
CREATE TABLE fact_nav (
    amfi_code TEXT,
    date DATE,
    nav REAL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

-- Transactions Fact Table
CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    transaction_date DATE,
    transaction_type TEXT,
    amount_inr REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Performance Fact Table
CREATE TABLE fact_performance (
    amfi_code TEXT PRIMARY KEY,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- AUM Fact Table
CREATE TABLE fact_aum (
    amfi_code TEXT PRIMARY KEY,
    aum_crore REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);