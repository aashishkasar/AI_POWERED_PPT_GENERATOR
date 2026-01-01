

---

# 📊 AI PowerPoint Generator using Streamlit & Google Gemini

This project is a **Streamlit-based AI PowerPoint generator** built using **LangChain** and **Google Gemini (gemini-2.5-flash)**.
Users can describe their presentation in natural language, choose slide options, and automatically **generate & download a PowerPoint (`.pptx`) file**.

The app dynamically generates **executable Python code** using **python-pptx**, runs it, and delivers the final presentation to the user.

---

## 📌 Features

* Interactive UI built with **Streamlit**
* Uses **Google Gemini** via **LangChain**
* Natural-language PowerPoint creation
* User-selectable:

  * Number of slides
  * Slide background color
* Secure API key handling with **dotenv**
* Generates real `.pptx` files using **python-pptx**
* One-click **download** of generated PowerPoint
* Supports user API key or `.env` fallback

---

## 🧠 How the Code Works

### 1️⃣ Page Configuration

```python
st.set_page_config(page_title="PowerPoint Generator")
```

* Sets app title and layout
* Improves UI consistency

---

### 2️⃣ Environment Setup

```python
load_dotenv()
```

* Loads environment variables from `.env`
* Keeps API keys **secure** and out of source code

---

### 3️⃣ Sidebar Controls

#### Slide Options

```python
slide_count = st.sidebar.number_input("Number of slides", 1, 20, 5)
slide_color = st.sidebar.color_picker("Slide background color", "#FFFFFF")
```

* Allows users to control:

  * Total slides
  * Background color for all slides

#### API Key Input

```python
user_api_key = st.sidebar.text_input("Paste your Google API Key", type="password")
```

* Users can provide their own **Google Gemini API key**
* Falls back to `.env` key if not provided

---

### 4️⃣ LLM Initialization

```python
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
```

* Uses **Gemini Flash** for fast code generation
* LangChain acts as the **LLM client**
* Gemini acts as the **closed-source LLM server**

---

### 5️⃣ Prompt Engineering (Core Logic)

```python
system_prompt = f"""
You are an AI assistant that generates complete and executable Python code.
...
"""
```

**Strict system rules enforce:**

* Use `python-pptx`
* Create **exactly N slides**
* Apply selected background color
* Save output as `output.pptx`
* Output **ONLY Python code**
* No markdown or explanations

This ensures **valid, executable PPT generation code**.

---

### 6️⃣ PPT Generation Flow

```
User Description
      ↓
System Rules + Prompt
      ↓
Gemini via LangChain
      ↓
Python Code (python-pptx)
      ↓
Saved as app.py
      ↓
Executed Automatically
      ↓
output.pptx Generated
```

---

### 7️⃣ Download PowerPoint

```python
st.download_button(
    label="⬇️ Download PPT",
    data=ppt_file,
    file_name="presentation.pptx"
)
```

* Allows users to **download the generated PowerPoint**
* Uses correct MIME type for `.pptx`

---

## 📦 Dependencies

### `requirements.txt`

```txt
streamlit
langchain
langchain_google_genai
python-dotenv
python-pptx
```

### Why These Dependencies?

| Package                | Purpose                    |
| ---------------------- | -------------------------- |
| streamlit              | Web UI                     |
| langchain              | LLM abstraction            |
| langchain_google_genai | Google Gemini integration  |
| python-dotenv          | Secure API key handling    |
| python-pptx            | PowerPoint file generation |

---

## 🔐 Why Use `dotenv`?

* Keeps API keys **secure**
* Prevents GitHub credential leaks
* Allows different keys for **local / cloud**
* Enables user key override via UI

### Example `.env` File

```env
gak=YOUR_GOOGLE_GEMINI_API_KEY
```

---

## 🚫 Why Use `.gitignore`?

Prevents sensitive or unnecessary files from being pushed.

### `.gitignore`

```gitignore
.env
__pycache__/
venv/
.env.local
output.pptx
```

✅ Protects API keys
✅ Keeps repository clean
✅ Industry standard

---

## 🚀 Run Locally (Step-by-Step)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-ppt-generator.git
cd ai-ppt-generator
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add `.env` File (Optional)

```env
gak=YOUR_GOOGLE_GEMINI_API_KEY
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push project to **GitHub**
2. Open **Streamlit Cloud**
3. Select your repository
4. Add Environment Variable:

   ```
   gak = YOUR_GOOGLE_GEMINI_API_KEY
   ```
5. Deploy 🚀

---

## 📜 MIT License

```text
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

## 📚 Learning Outcomes

* Prompt-driven code generation
* LLM-based automation
* python-pptx integration
* Streamlit UI + sidebar design
* Secure API key handling
* Dynamic code execution
* File generation & download workflows

---

## 🙌 Author

**Aashish**
AI / ML / GenAI Developer

---


