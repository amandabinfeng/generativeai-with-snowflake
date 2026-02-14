# Beginner AI + Web Apps (Local, Minimal Setup)

These are 3 simple Streamlit apps tailored to data/analytics/investing learning.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install streamlit pandas plotly yfinance numpy
```

## Conda option (update repo environment)

```bash
conda env update -f module-1/environment.yml --prune
conda activate app_environment
```

## Run

```bash
streamlit run beginner_apps/app1_portfolio_checkup.py
streamlit run beginner_apps/app2_earnings_sentiment.py
streamlit run beginner_apps/app3_kpi_anomaly.py
```

## Apps

1. **Portfolio Checkup Assistant**
   - Enter tickers + weights
   - See cumulative return, drawdown, and contributors

2. **Earnings Call Sentiment Tracker**
   - Paste one snippet per line
   - Rule-based sentiment + topic detection

3. **KPI Anomaly Explainer**
   - Upload a CSV with a date column and KPI columns
   - Detect outliers via z-score and summarize anomalies


## What to do next

See the beginner progression guide: `beginner_apps/NEXT_STEPS.md`.

## Deploy to a website

See `DEPLOYMENT.md` for step-by-step deployment on Streamlit Community Cloud and Render.
