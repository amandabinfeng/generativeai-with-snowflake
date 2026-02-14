# 3 Beginner "Vibe Coding" App Ideas (Data + Analytics + Investment)

If your goal is to learn by building and keep setup minimal, start with **Streamlit**:

```bash
pip install streamlit pandas yfinance plotly
```

Then run apps with:

```bash
streamlit run app.py
```

---

## 1) Portfolio Snapshot Explainer

**What it does**
- You type in a few stock tickers and weights (for example: AAPL 40%, MSFT 30%, VOO 30%).
- The app fetches recent prices.
- It shows simple charts: portfolio value trend, best/worst performer, allocation pie chart.
- It generates a plain-English summary like: “This portfolio was mainly driven by X in the last 30 days.”

**Why this is a good first project**
- Strong overlap with investment and analytics.
- You learn data loading, data transforms, charting, and simple AI text summarization.
- You can start small and add features later (benchmark vs S&P 500, risk stats, etc.).

**Minimal tools**
- Streamlit + pandas + yfinance + plotly.

---

## 2) Earnings Call Sentiment Mini-Dashboard

**What it does**
- You paste short snippets from earnings call transcripts (or news text).
- The app classifies each snippet as positive / neutral / negative.
- It extracts topics (growth, margins, guidance, risk).
- Dashboard shows sentiment counts and topic trends.

**Why this is a good first project**
- Very practical analytics workflow: text -> labels -> insights.
- Great intro to LLM usage without heavy ML training.
- You can begin with manual pasted text (no complex ingestion setup).

**Minimal tools**
- Streamlit + pandas + a simple LLM API call (OpenAI-compatible or Snowflake Cortex if available).

---

## 3) “Explain This Chart” Data Story Assistant

**What it does**
- You upload a CSV (e.g., monthly returns, KPI metrics, sales by segment).
- App auto-generates basic charts.
- You click a chart and the assistant explains what changed, possible drivers, and follow-up questions.
- Optional: ask “what should I investigate next?”

**Why this is a good first project**
- Directly matches data/analytics background.
- Helps learn AI prompting + simple app UX quickly.
- Useful even outside investment use cases.

**Minimal tools**
- Streamlit + pandas + plotly + LLM API.

---

## Which one should you build first?

Start with **#1 Portfolio Snapshot Explainer**.
- It has clear inputs and outputs.
- You can ship a useful version in a single session.
- It teaches the full loop: data fetch -> analytics -> visualization -> AI explanation.

If you want, next step I can generate a **complete starter `app.py`** for idea #1 with beginner-friendly comments.
