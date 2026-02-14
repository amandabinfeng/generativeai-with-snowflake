import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="Portfolio Checkup Assistant", layout="wide")
st.title("Portfolio Checkup Assistant")
st.caption("Beginner example: tickers + weights -> performance, drawdown, contributors")

st.subheader("1) Enter portfolio")
ticker_text = st.text_input("Tickers (comma-separated)", "AAPL,MSFT,VOO")
weights_text = st.text_input("Weights % (comma-separated, same order)", "40,30,30")
period = st.selectbox("History", ["6mo", "1y", "2y", "5y"], index=1)

if st.button("Analyze"):
    tickers = [t.strip().upper() for t in ticker_text.split(",") if t.strip()]

    try:
        weights = [float(x.strip()) for x in weights_text.split(",") if x.strip()]
    except ValueError:
        st.error("Weights must be numbers.")
        st.stop()

    if len(tickers) == 0 or len(weights) == 0 or len(tickers) != len(weights):
        st.error("Please provide same number of tickers and weights.")
        st.stop()

    total = sum(weights)
    if total <= 0:
        st.error("Weights must sum to a positive value.")
        st.stop()

    norm_weights = [w / total for w in weights]
    w_series = pd.Series(norm_weights, index=tickers)

    data = yf.download(tickers, period=period, auto_adjust=True, progress=False)
    if data.empty:
        st.error("No data returned. Try different tickers or period.")
        st.stop()

    prices = data["Close"] if "Close" in data else data
    if isinstance(prices, pd.Series):
        prices = prices.to_frame(name=tickers[0])

    prices = prices.dropna(how="all")
    prices = prices.fillna(method="ffill").dropna()

    if prices.empty:
        st.error("Price history is empty after cleaning.")
        st.stop()

    missing = [t for t in tickers if t not in prices.columns]
    if missing:
        st.error(f"Missing data for: {', '.join(missing)}")
        st.stop()

    returns = prices.pct_change().fillna(0)
    portfolio_returns = (returns * w_series).sum(axis=1)
    portfolio_growth = (1 + portfolio_returns).cumprod()

    peak = portfolio_growth.cummax()
    drawdown = portfolio_growth / peak - 1

    contrib = (returns * w_series).sum().sort_values(ascending=False)

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Total Return", f"{(portfolio_growth.iloc[-1] - 1):.2%}")
    with c2:
        st.metric("Max Drawdown", f"{drawdown.min():.2%}")

    growth_df = portfolio_growth.reset_index()
    growth_df.columns = ["Date", "Growth"]
    fig_growth = px.line(growth_df, x="Date", y="Growth", title="Portfolio Growth")
    st.plotly_chart(fig_growth, use_container_width=True)

    dd_df = drawdown.reset_index()
    dd_df.columns = ["Date", "Drawdown"]
    fig_dd = px.area(dd_df, x="Date", y="Drawdown", title="Drawdown")
    st.plotly_chart(fig_dd, use_container_width=True)

    st.subheader("Contributors")
    st.dataframe((contrib * 100).rename("Contribution %").to_frame())

    best = contrib.index[0]
    worst = contrib.index[-1]
    summary = (
        f"In this period, your portfolio returned {(portfolio_growth.iloc[-1] - 1):.2%}. "
        f"The biggest positive contributor was {best}, while {worst} weighed on performance most. "
        f"Maximum drawdown was {drawdown.min():.2%}."
    )
    st.subheader("Simple Explanation")
    st.write(summary)
