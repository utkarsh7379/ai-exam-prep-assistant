import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Exam Prep Assistant")

topic = st.text_input("Enter Topic")

if st.button("Generate"):
    prompt = f"""
    Topic: {topic}
    
    Generate:
    1. 7-mark answer
    2. 10-mark answer
    3. Short notes
    4. Important questions
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
