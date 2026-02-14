# 3 Simple AI + Web App Ideas to Start Vibe Coding

You said you have limited coding experience and want to learn by examples with minimal setup.
So these ideas are designed to be:
- **Local-first** (runs on your laptop)
- **Simple web UI** (Streamlit)
- **Relevant to data, analytics, and investing**
- **Easy to expand into more advanced versions later**

## Minimal setup (once)

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install streamlit pandas plotly yfinance
```

Run any app with:

```bash
streamlit run app.py
```

---

## Idea 1 (Best first): Portfolio Checkup Assistant

### What the app does
- You enter 3–10 tickers and portfolio weights.
- App downloads price history.
- Shows:
  - Portfolio growth line chart
  - Drawdown chart (how much it dropped from peaks)
  - Best/worst contributor table
- AI-style summary in plain English:
  - “Your portfolio underperformed mainly because X and Y.”

### Why it is good for beginners
- Clear input/output.
- Immediate visual feedback.
- Teaches core analytics skills: cleaning data, combining time series, charting.

### MVP (first version, 60–90 min)
1. Ticker input box (comma-separated).
2. Weight input (simple percentages).
3. Price download with `yfinance`.
4. One line chart + one short written summary.

### Nice upgrades later
- Compare against benchmark (SPY/QQQ).
- Add rolling volatility.
- Add “What changed this week?” AI commentary.

---

## Idea 2: Earnings Call Sentiment Tracker

### What the app does
- You paste earnings-call snippets (or management commentary).
- App labels each snippet as Positive / Neutral / Negative.
- App extracts simple themes (growth, margin, demand, guidance, risk).
- Dashboard shows:
  - Sentiment distribution
  - Theme counts
  - Most concerning statements

### Why it is good for beginners
- Great first NLP workflow without model training.
- You learn table transformations and dashboard views.
- Useful for investment research routines.

### MVP (first version)
1. Text box with one snippet per line.
2. Rule-based sentiment (keyword lists).
3. Bar charts for sentiment + themes.

### AI upgrade later
- Replace rule-based logic with LLM calls for better classification and explanations.

---

## Idea 3: KPI Anomaly Explainer (CSV Upload)

### What the app does
- Upload a CSV with date + KPI columns (revenue, CAC, churn, etc.).
- App auto-detects unusual changes (spikes/drops).
- App explains anomalies in plain language:
  - “Revenue dropped 14% vs last month while CAC increased 9%.”
- App suggests follow-up questions.

### Why it is good for beginners
- Directly aligned with analytics background.
- No external API required for the first version.
- Works with your own real datasets.

### MVP (first version)
1. CSV uploader.
2. Choose KPI from dropdown.
3. Show trend chart.
4. Flag points above/below simple threshold (e.g., z-score).

### Nice upgrades later
- Segment filters (region/product/channel).
- Week-over-week and month-over-month decomposition.
- AI-generated investigation checklist.

---

## What to build first

Start with **Idea 1: Portfolio Checkup Assistant**.

It gives the fastest learning loop:
1. Get data
2. Build charts
3. Add explanation text
4. Share and iterate

If you want, next I can generate a full **beginner-friendly `app.py`** for Idea 1 with comments on every step.
