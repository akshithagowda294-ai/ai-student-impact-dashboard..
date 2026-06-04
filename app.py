import streamlit as st
import pandas as pd
from analytics import create_charts
from insights import generate_insights

st.set_page_config(
    page_title="AI Impact Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("🎓 AI Impact on Student Performance")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success(f"Dataset Loaded: {df.shape[0]} Rows")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average GPA",
        round(df["Post_Semester_GPA"].mean(),2)
    )

    col2.metric(
        "Average AI Hours",
        round(df["Weekly_GenAI_Hours"].mean(),2)
    )

    col3.metric(
        "Average Skill Retention",
        round(df["Skill_Retention_Score"].mean(),2)
    )

    st.divider()

    create_charts(df)

    st.divider()

    generate_insights(df)
