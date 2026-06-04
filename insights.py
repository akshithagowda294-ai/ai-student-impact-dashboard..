import streamlit as st

def generate_insights(df):

    st.subheader("🧠 AI Generated Insights")

    avg_gpa = df["Post_Semester_GPA"].mean()

    high_ai = df[
        df["Weekly_GenAI_Hours"] > 20
    ]["Post_Semester_GPA"].mean()

    low_ai = df[
        df["Weekly_GenAI_Hours"] < 5
    ]["Post_Semester_GPA"].mean()

    burnout = (
        df["Burnout_Risk_Level"]
        .value_counts()
        .idxmax()
    )

    retention = (
        df["Skill_Retention_Score"]
        .mean()
    )

    st.info(
        f"""
        • Average GPA: {avg_gpa:.2f}

        • High AI users GPA: {high_ai:.2f}

        • Low AI users GPA: {low_ai:.2f}

        • Most Common Burnout Level: {burnout}

        • Average Skill Retention: {retention:.2f}
        """
    )

    if high_ai > low_ai:
        st.success(
            "Students using AI extensively show higher academic performance."
        )
    else:
        st.warning(
            "Heavy AI usage does not necessarily improve GPA."
        )
