import pandas as pd

risk_map = {
    'Low': ['Low'],
    'Moderate': ['Moderate', 'Moderately High'],
    'High': ['High', 'Very High']
}

def recommend_funds(risk_appetite, scheme_performance):
    grades = risk_map[risk_appetite]

    result = scheme_performance[
        scheme_performance['risk_grade'].isin(grades)
    ]

    return (
        result
        .sort_values('sharpe_ratio', ascending=False)
        .head(3)
    )