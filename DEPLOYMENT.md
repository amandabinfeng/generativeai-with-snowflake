# Deployment Guide (Website)

You can deploy this project as a website using either **Streamlit Community Cloud** (easiest) or **Render**.

## Option 1: Streamlit Community Cloud (recommended)

1. Push this repo to GitHub.
2. Go to https://share.streamlit.io
3. Click **New app**.
4. Set:
   - **Repository**: your fork/repo
   - **Branch**: your branch (or main)
   - **Main file path**: `beginner_apps/app1_portfolio_checkup.py` (or app2/app3)
5. Click **Deploy**.

### Requirements used for deployment
This repo includes `requirements.txt` with:
- streamlit
- pandas
- plotly
- yfinance
- numpy

## Option 2: Render

1. Create a new Web Service from this GitHub repo.
2. Use:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run beginner_apps/app1_portfolio_checkup.py --server.port $PORT --server.address 0.0.0.0`
3. Deploy.

## Notes
- If you want one app URL per app, deploy each app file separately.
- If you want one unified website, convert to a proper Streamlit multipage setup under a single entrypoint.
