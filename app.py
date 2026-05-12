import streamlit as st
from llm import generate_response

st.set_page_config(page_title="AI Resume Tailor", layout="wide")

st.title("📄 AI Cover Letter & Resume Tailor")

# --- Inputs ---
resume = st.text_area("📄 Paste your Resume", height=200)
job_desc = st.text_area("💼 Paste Job Description", height=200)

if st.button("🚀 Generate"):
    if resume and job_desc:
        prompt = f"""
        You are a professional career assistant.

        Based on the resume and job description below:

        1. Write a tailored cover letter
        2. Suggest improvements to resume bullets

        Resume:
        {resume}

        Job Description:
        {job_desc}
        """

        output = generate_response(prompt)

        st.subheader("✨ Output")
        st.write(output)
    else:
        st.warning("Please fill both fields")