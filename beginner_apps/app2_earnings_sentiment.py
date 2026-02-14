import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Earnings Call Sentiment Tracker", layout="wide")
st.title("Earnings Call Sentiment Tracker")
st.caption("Beginner example: pasted snippets -> sentiment + topics")

positive_words = {"strong", "growth", "improved", "beat", "upside", "healthy", "record", "expanded"}
negative_words = {"weak", "decline", "miss", "pressure", "risk", "downside", "soft", "uncertain"}

themes = {
    "growth": {"growth", "demand", "volume", "pipeline"},
    "margin": {"margin", "cost", "efficiency", "profitability"},
    "guidance": {"guidance", "outlook", "forecast"},
    "risk": {"risk", "uncertain", "volatility", "headwind"},
}

text = st.text_area(
    "Paste snippets (one per line)",
    "Demand remained strong in enterprise clients.\nWe see margin pressure due to higher logistics costs.",
    height=180,
)


def classify_sentiment(line: str) -> str:
    tokens = set(line.lower().replace(",", " ").replace(".", " ").split())
    pos = len(tokens & positive_words)
    neg = len(tokens & negative_words)
    if pos > neg:
        return "Positive"
    if neg > pos:
        return "Negative"
    return "Neutral"


def detect_theme(line: str) -> str:
    tokens = set(line.lower().replace(",", " ").replace(".", " ").split())
    matches = {k: len(tokens & v) for k, v in themes.items()}
    best = max(matches, key=matches.get)
    return best if matches[best] > 0 else "other"


if st.button("Analyze snippets"):
    lines = [x.strip() for x in text.split("\n") if x.strip()]
    if not lines:
        st.warning("Please paste at least one snippet.")
        st.stop()

    df = pd.DataFrame({"snippet": lines})
    df["sentiment"] = df["snippet"].apply(classify_sentiment)
    df["theme"] = df["snippet"].apply(detect_theme)

    c1, c2 = st.columns(2)
    with c1:
        sent_counts = df["sentiment"].value_counts().reset_index()
        sent_counts.columns = ["sentiment", "count"]
        fig1 = px.bar(sent_counts, x="sentiment", y="count", title="Sentiment Distribution")
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        theme_counts = df["theme"].value_counts().reset_index()
        theme_counts.columns = ["theme", "count"]
        fig2 = px.bar(theme_counts, x="theme", y="count", title="Theme Counts")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Labeled snippets")
    st.dataframe(df)

    negatives = df[df["sentiment"] == "Negative"]["snippet"].tolist()
    st.subheader("Quick takeaway")
    if negatives:
        st.write(f"Found {len(negatives)} negative snippets. Review these first for risk signals.")
    else:
        st.write("No clearly negative snippets were found with the current rules.")
