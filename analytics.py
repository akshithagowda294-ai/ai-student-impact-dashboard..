import streamlit as st
import plotly.express as px

def create_charts(df):

    st.subheader("📈 Deep Analytics")

    c1, c2 = st.columns(2)

    with c1:
        fig = px.scatter(
            df,
            x="Weekly_GenAI_Hours",
            y="Post_Semester_GPA",
            color="Major_Category",
            title="AI Usage vs GPA"
        )
        st.plotly_chart(fig,use_container_width=True)

    with c2:
        fig = px.box(
            df,
            x="Burnout_Risk_Level",
            y="Weekly_GenAI_Hours",
            color="Burnout_Risk_Level",
            title="Burnout vs AI Usage"
        )
        st.plotly_chart(fig,use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:
        fig = px.histogram(
            df,
            x="Skill_Retention_Score",
            nbins=30,
            title="Skill Retention Distribution"
        )
        st.plotly_chart(fig,use_container_width=True)

    with c4:
        fig = px.sunburst(
            df,
            path=[
                "Major_Category",
                "Prompt_Engineering_Skill",
                "Burnout_Risk_Level"
            ],
            title="Student Segmentation"
        )
        st.plotly_chart(fig,use_container_width=True)

    heatmap_data = df[
        [
            "Pre_Semester_GPA",
            "Weekly_GenAI_Hours",
            "Traditional_Study_Hours",
            "Perceived_AI_Dependency",
            "Anxiety_Level_During_Exams",
            "Post_Semester_GPA",
            "Skill_Retention_Score"
        ]
    ]

    st.subheader("Correlation Analysis")

    fig = px.imshow(
        heatmap_data.corr(),
        text_auto=True,
        aspect="auto"
    )

    st.plotly_chart(fig,use_container_width=True)
