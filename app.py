import streamlit as st
from groq import Groq

st.set_page_config(page_title="SA Banking Support AI", page_icon="🏦")
st.title("🏦 SA Banking Support AI")

api_key = st.text_input("Enter your Groq API Key:", type="password")

question = st.text_input("Ask a banking question:")

if st.button("Ask"):
    if api_key and question:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a professional South African banking support assistant. Branch hours are Monday to Friday 08:00 to 15:30 and Saturdays 08:00 to 11:00. Emergency line is 0800 123 456. Always be professional and helpful."},
                {"role": "user", "content": question}
            ],
            temperature=0
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter both API key and question!") 
