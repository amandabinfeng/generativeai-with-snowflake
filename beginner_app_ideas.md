# 3 Simple AI + Web App Ideas to Start Vibe Coding

If you want to learn by doing with minimal setup, use the runnable examples in `beginner_apps/`.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install streamlit pandas plotly yfinance numpy
```

Run examples:

```bash
streamlit run beginner_apps/app1_portfolio_checkup.py
streamlit run beginner_apps/app2_earnings_sentiment.py
streamlit run beginner_apps/app3_kpi_anomaly.py
```

## 1) Portfolio Checkup Assistant
- Input: ticker list + weights.
- Output: growth chart, drawdown, contributor table, and a plain-English summary.
- Best first project for investment-focused learning.

## 2) Earnings Call Sentiment Tracker
- Input: pasted earnings-call snippets.
- Output: positive/neutral/negative labels plus theme counts (growth, margin, guidance, risk).
- Great intro to NLP workflows without model training.

## 3) KPI Anomaly Explainer
- Input: your CSV with date + KPI columns.
- Output: trend chart, anomaly flags (z-score), and a short explanation.
- Strong fit for analytics/data storytelling.

## Suggested learning path
1. Run app 1 and modify labels/layout.
2. Add one metric to app 1 (benchmark or volatility).
3. Try app 2 and tune sentiment keywords.
4. Use your own CSV in app 3.

When you are ready, I can also provide a single "combined" multi-page Streamlit app.
