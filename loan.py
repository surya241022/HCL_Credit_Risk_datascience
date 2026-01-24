import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Loan Default Analysis", layout="wide")

st.title("📊 Loan Default Analysis Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload Loan Dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")

    # Show dataset preview
    with st.expander(" Dataset Preview"):
        st.dataframe(df.head())

    target = "default"
    features = [
        "loan_purpose",
        "gender",
        "employment_status",
        "past_defaults"
    ]

    st.subheader("📌 Feature vs Default Analysis")

    for feature in features:
        st.markdown(f"## 🔹 {feature.replace('_', ' ').title()} vs Default")

        col1, col2 = st.columns(2)

        # ---------- Stacked Bar Chart ----------
        grouped = (
            df.groupby([feature, target])
            .size()
            .reset_index(name="count")
        )

        fig_bar = px.bar(
            grouped,
            x=feature,
            y="count",
            color=target,
            barmode="stack",
            title=f"{feature} vs Default (Count)"
        )

        col1.plotly_chart(fig_bar, use_container_width=True)

        # ---------- Pie Chart ----------
        pie_data = (
            df.groupby([feature, target])
            .size()
            .reset_index(name="count")
        )

        fig_pie = px.pie(
            pie_data,
            names=feature,
            values="count",
            color=target,
            title=f"{feature} Distribution by Default"
        )

        col2.plotly_chart(fig_pie, use_container_width=True)

else:
    st.info(" Upload a CSV file to start analysis")

