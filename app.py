import streamlit as st
from google import genai

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CodePilot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #111827 50%,
            #0b1120 100%
        );
        color: white;
    }

    /* Header */
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
        background: linear-gradient(
            90deg,
            #38bdf8,
            #818cf8,
            #c084fc
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.15rem;
        margin-bottom: 35px;
    }

    /* Cards */
    .feature-card {
        background: rgba(30, 41, 59, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 18px;
        padding: 25px;
        min-height: 180px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.25);
    }

    .feature-card:hover {
        border-color: #38bdf8;
    }

    .feature-icon {
        font-size: 2.2rem;
    }

    .feature-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 10px;
    }

    .feature-text {
        color: #94a3b8;
        line-height: 1.6;
    }

    /* Section headings */
    .section-title {
        font-size: 1.7rem;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Info box */
    .info-box {
        background: rgba(15, 23, 42, 0.8);
        border-left: 4px solid #38bdf8;
        border-radius: 8px;
        padding: 15px 20px;
        color: #cbd5e1;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        padding: 30px;
        margin-top: 50px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 700;
        padding: 0.6rem 1.5rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0b1120;
        border-right: 1px solid #1e293b;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# GEMINI CONFIGURATION
# =========================================================

# Put your Gemini API key here
API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.5-flash-lite"


# =========================================================
# SESSION STATE
# =========================================================

if "generated_code" not in st.session_state:
    st.session_state.generated_code = ""

if "review_result" not in st.session_state:
    st.session_state.review_result = ""


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 CodePilot AI")

    st.markdown("---")

    st.markdown("### 🛠️ Tools")

    tool = st.radio(
        "Select a tool",
        [
            "🏠 Dashboard",
            "⚡ Code Generator",
            "🔍 Code Reviewer"
        ]
    )

    st.markdown("---")

    st.markdown("### ⚙️ Configuration")

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript",
            "HTML/CSS",
            "SQL"
        ]
    )

    st.markdown("---")

    st.markdown(
        """
        **CodePilot AI**

        AI-powered developer assistant for:

        • Source code generation  
        • Code review  
        • Bug detection  
        • Security analysis  
        • Code improvement
        """
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 CodePilot AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Generate smarter code. Review faster. Build better.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# DASHBOARD
# =========================================================

if tool == "🏠 Dashboard":

    st.markdown(
        '<div class="section-title">🚀 AI Developer Workspace</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        Welcome to <b>CodePilot AI</b> — an AI-powered programming
        assistant that helps developers generate source code and
        review existing code using Google Gemini.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">
                    Code Generator
                </div>
                <div class="feature-text">
                    Describe your programming requirement
                    and generate complete source code using AI.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <div class="feature-title">
                    Code Reviewer
                </div>
                <div class="feature-text">
                    Analyze source code for bugs, security
                    problems, performance issues and quality.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">✨</div>
                <div class="feature-title">
                    Smart Improvements
                </div>
                <div class="feature-text">
                    Receive AI-generated suggestions and
                    improved versions of your source code.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    st.markdown("### 📊 Application Capabilities")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("AI Model", "Gemini")

    with col2:
        st.metric("Languages", "7+")

    with col3:
        st.metric("AI Tools", "2")

    with col4:
        st.metric("Platform", "Python")


# =========================================================
# CODE GENERATOR
# =========================================================

elif tool == "⚡ Code Generator":

    st.markdown(
        '<div class="section-title">⚡ AI Code Generator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        Describe what you want to build. CodePilot will generate
        the source code, explanation and sample input/output.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    requirement = st.text_area(
        "💡 What do you want to build?",
        placeholder=(
            "Example: Create a Python program that checks "
            "whether a number is prime."
        ),
        height=180
    )

    if st.button(
        "⚡ Generate Source Code",
        use_container_width=True
    ):

        if not requirement.strip():

            st.warning(
                "Please enter a programming requirement."
            )

        else:

            prompt = f"""
You are an expert software developer.

Generate source code for the following requirement:

{requirement}

Programming language:
{language}

Provide the response in this format:

## Programming Language

## Source Code

Provide complete working code.

## Explanation

Explain the code in simple language.

## Example Input

## Example Output

## Key Features

List the important features.

Make the solution beginner-friendly and correct.
"""

            try:

                with st.spinner(
                    "🤖 Gemini is generating your code..."
                ):

                    response = client.models.generate_content(
                        model=MODEL,
                        contents=prompt
                    )

                st.session_state.generated_code = response.text

                st.success(
                    "✅ Source code generated successfully!"
                )

            except Exception as e:

                st.error(
                    f"❌ API Error: {e}"
                )

    if st.session_state.generated_code:

        st.markdown("### 🧠 AI Generated Result")

        st.markdown(
            st.session_state.generated_code
        )


# =========================================================
# CODE REVIEWER
# =========================================================

elif tool == "🔍 Code Reviewer":

    st.markdown(
        '<div class="section-title">🔍 AI Code Reviewer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        Paste your source code below. CodePilot will inspect it
        for bugs, security problems, performance issues and
        code-quality improvements.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    code = st.text_area(
        "💻 Paste your source code",
        placeholder="""def add(a, b):
    return a - b

x = input("Enter number: ")
y = input("Enter number: ")

print(add(x, y))
""",
        height=350
    )

    if st.button(
        "🔍 Review My Code",
        use_container_width=True
    ):

        if not code.strip():

            st.warning(
                "Please paste some source code."
            )

        else:

            prompt = f"""
You are an expert software engineer and code reviewer.

Review the following {language} source code:

---------------- CODE ----------------

{code}

-------------- END CODE --------------

Perform a detailed code review.

Use the following structure:

# 1. Programming Language

Identify the language.

# 2. Code Summary

Explain what the code does.

# 3. 🐛 Errors and Bugs

Identify logical and syntax errors.

# 4. 🔐 Security Issues

Identify possible security vulnerabilities.

# 5. ⚡ Performance Issues

Identify inefficient operations.

# 6. 📋 Code Quality

Discuss readability, naming, structure and maintainability.

# 7. 💡 Suggestions

Give practical improvements.

# 8. ✨ Improved Code

Provide a corrected and improved version.

Explain everything in simple language suitable for a
college student.
"""

            try:

                with st.spinner(
                    "🔎 Gemini is reviewing your code..."
                ):

                    response = client.models.generate_content(
                        model=MODEL,
                        contents=prompt
                    )

                st.session_state.review_result = response.text

                st.success(
                    "✅ Code review completed!"
                )

            except Exception as e:

                st.error(
                    f"❌ API Error: {e}"
                )

    if st.session_state.review_result:

        st.markdown("### 📋 Code Review Report")

        st.markdown(
            st.session_state.review_result
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🤖 CodePilot AI &nbsp;•&nbsp;
        Powered by Google Gemini &nbsp;•&nbsp;
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
