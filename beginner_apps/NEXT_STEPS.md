# What’s Next? (Beginner Roadmap)

Great progress — you now have 3 runnable apps. Here is a simple next path.

## Step 1: Pick one app and make one small change (30–60 min)
Start with `app1_portfolio_checkup.py`.

Ideas:
- Change default tickers to ones you follow.
- Rename chart titles/labels.
- Add one extra metric card (for example: number of trading days).

Goal: become comfortable reading and editing existing code.

## Step 2: Add one analytics feature (1–2 hours)
For app 1, add one of these:
- Benchmark line (SPY) on the same chart.
- Rolling 30-day volatility.
- Best and worst day.

Goal: practice real data analysis logic.

## Step 3: Add one AI feature (1–2 hours)
For app 2 or app 3:
- Keep current rule-based logic as baseline.
- Add optional LLM explanation via API key in env var.
- Show both outputs side-by-side: rule-based vs AI-based.

Goal: learn where AI helps and where deterministic rules are enough.

## Step 4: Combine into one mini product (2–3 hours)
Create a multi-page Streamlit app with pages:
1. Portfolio
2. Sentiment
3. KPI anomalies

Goal: turn separate examples into a coherent analytics assistant.

## Step 5: Polish and share
- Add clear error messages.
- Add sample CSV file for app 3.
- Add screenshots and a short demo GIF.
- Publish repo update and ask for feedback.

---

## Practical “next command” checklist

```bash
# 1) activate env
conda activate app_environment

# 2) run the first app
streamlit run beginner_apps/app1_portfolio_checkup.py

# 3) after making a small change, syntax check
python -m py_compile beginner_apps/app1_portfolio_checkup.py
```

If you want, the next concrete step I can do is: add a **benchmark (SPY) comparison** to app 1.
