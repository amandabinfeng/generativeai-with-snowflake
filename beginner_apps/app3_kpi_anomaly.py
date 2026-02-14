import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="KPI Anomaly Explainer", layout="wide")
st.title("KPI Anomaly Explainer")
st.caption("Beginner example: upload CSV -> detect unusual KPI changes")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.write("Preview")
    st.dataframe(df.head())

    date_candidates = [c for c in df.columns if "date" in c.lower() or "month" in c.lower()]
    date_col = st.selectbox("Date column", df.columns, index=(df.columns.get_loc(date_candidates[0]) if date_candidates else 0))

    numeric_cols = [c for c in df.columns if c != date_col and pd.api.types.is_numeric_dtype(df[c])]
    if not numeric_cols:
        st.error("No numeric KPI columns found.")
        st.stop()

    kpi_col = st.selectbox("KPI column", numeric_cols)

    work = df[[date_col, kpi_col]].copy()
    work[date_col] = pd.to_datetime(work[date_col], errors="coerce")
    work = work.dropna().sort_values(date_col)

    if len(work) < 5:
        st.warning("Need at least 5 rows after cleaning to detect anomalies.")
        st.stop()

    values = work[kpi_col]
    z = (values - values.mean()) / (values.std(ddof=0) + 1e-9)
    work["z_score"] = z
    work["anomaly"] = np.where(np.abs(z) >= 2, "anomaly", "normal")

    fig = px.line(work, x=date_col, y=kpi_col, title=f"{kpi_col} Trend")
    anom = work[work["anomaly"] == "anomaly"]
    if not anom.empty:
        fig.add_scatter(
            x=anom[date_col],
            y=anom[kpi_col],
            mode="markers",
            name="anomaly",
            marker=dict(size=10, color="red"),
        )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detected anomalies")
    st.dataframe(anom[[date_col, kpi_col, "z_score"]])

    st.subheader("Simple Explanation")
    if anom.empty:
        st.write("No major anomalies were detected using |z-score| >= 2.")
    else:
        top = anom.iloc[np.argmax(np.abs(anom["z_score"]))]
        st.write(
            f"Detected {len(anom)} anomaly points. The strongest anomaly occurred on "
            f"{top[date_col].date()} with {kpi_col}={top[kpi_col]:,.2f} (z={top['z_score']:.2f})."
        )
else:
    st.info("Upload a CSV to begin.")
