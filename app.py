import streamlit as st
import os
import sys
import subprocess
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.set_page_config(page_title="PowerPoint Generator")

st.title("PowerPoint Generator")

# ---- Sidebar ----
st.sidebar.title("How to use this app")
st.sidebar.markdown(
"""
**1.** Paste your Google API key  
**2.** Select slide options  
**3.** Describe your PowerPoint  
**4.** Click **Download PPT**
"""
)

st.sidebar.divider()
st.sidebar.title("Slide Options")

slide_count = st.sidebar.number_input("Number of slides", 1, 20, 5)
slide_color = st.sidebar.color_picker("Slide background color", "#FFFFFF")

st.sidebar.divider()
st.sidebar.title("API Key")

user_api_key = st.sidebar.text_input("Paste your Google API Key", type="password")

if user_api_key:
    os.environ["GOOGLE_API_KEY"] = user_api_key
else:
    os.environ["GOOGLE_API_KEY"] = os.getenv("gak", "")

# ---- Main UI ----
inp = st.text_area("Describe your PowerPoint content")

if st.button("Generate PPT"):
    if not os.environ["GOOGLE_API_KEY"]:
        st.error("Please provide a Google API key in the sidebar.")
    elif not inp.strip():
        st.error("Please enter PowerPoint content.")
    else:
        with st.spinner("Generating PowerPoint... ⏳"):
            model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

            system_prompt = f"""
You are an AI assistant that generates complete and executable Python code.

Requirements:
- Use python-pptx
- Create exactly {slide_count} slides
- Apply background color {slide_color} to ALL slides
- Always create Presentation()
- Always save the file as output.pptx

Strict rules:
- Output ONLY Python code
- No explanations
- No markdown
- No backticks
"""

            prompt = [
                ("system", system_prompt),
                ("user", inp)
            ]

            result = model.invoke(prompt)

            with open("app.py", "w", encoding="utf-8") as f:
                f.write(result.content.strip())

            subprocess.run([sys.executable, "app.py"])

        st.success("PowerPoint generated successfully!")

        # ---- DOWNLOAD TO USER COMPUTER ----
        with open("output.pptx", "rb") as ppt_file:
            st.download_button(
                label="⬇️ Download PPT",
                data=ppt_file,
                file_name="presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
