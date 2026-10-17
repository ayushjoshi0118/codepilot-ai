# 🤖 CodePilot AI

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75C2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**CodePilot AI** is an AI-powered developer workspace designed to streamline programming workflows. Powered by Google Gemini and built with Streamlit, it offers an intuitive dark-themed interface for automated source code generation and comprehensive multi-dimensional code reviews.

---

## ✨ Features

- 🏠 **Interactive Dashboard**: Sleek, modern dark-mode workspace with tool highlights and capability metrics.
- ⚡ **AI Code Generator**:
  - Enter natural-language software requirements.
  - Generates complete working code, explanations, example input/output, and key feature summaries.
  - Supports multiple languages: **Python**, **Java**, **C**, **C++**, **JavaScript**, **HTML/CSS**, and **SQL**.
- 🔍 **AI Code Reviewer**:
  - In-depth, 8-section code quality audit:
    1. Language Identification
    2. Code Summary
    3. 🐛 Errors & Bug Detection
    4. 🔐 Security Vulnerability Assessment
    5. ⚡ Performance & Efficiency Analysis
    6. 📋 Code Readability & Maintainability
    7. 💡 Actionable Improvement Suggestions
    8. ✨ Refactored & Improved Source Code
- 🎨 **Modern Cyber Dark UI**: Responsive layout styled with custom CSS cards, gradients, and metrics.

---

## 📁 Project Structure

```text
AI_Code_Generator/
├── .streamlit/
│   ├── secrets.toml.example  # Template for Gemini API key configuration
│   └── secrets.toml          # (Local only, git-ignored) Your actual API key
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules (protects API keys & cache)
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10** or higher
- A **Google Gemini API Key** (Get one for free at [Google AI Studio](https://aistudio.google.com/))

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_Code_Generator.git
cd AI_Code_Generator
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key

1. Inside the `.streamlit/` directory, copy `secrets.toml.example` to `secrets.toml`:
   ```bash
   # On Windows (PowerShell)
   Copy-Item .streamlit/secrets.toml.example .streamlit/secrets.toml

   # On macOS/Linux
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```
2. Open `.streamlit/secrets.toml` and replace `"your_gemini_api_key_here"` with your actual Gemini API key:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key"
   ```

> 🔒 **Security Notice**: `.streamlit/secrets.toml` is included in `.gitignore` to prevent accidentally committing your secret keys to public repositories.

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🌐 Deployment to Streamlit Community Cloud

You can deploy this application directly to [Streamlit Community Cloud](https://streamlit.io/cloud) in just a few clicks:

1. Push your code to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
3. Click **New app**, select your repository, branch (`main`), and set the main file path to `app.py`.
4. In **Advanced settings** > **Secrets**, enter your Gemini API key in TOML format:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key"
   ```
5. Click **Deploy!**

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) - Fast, interactive web app framework for Python
- [Google GenAI SDK](https://github.com/googleapis/python-genai) - Official client library for Google Gemini models

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
