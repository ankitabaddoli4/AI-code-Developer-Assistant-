import streamlit as st
from core.generator import generate_code
from core.bug_detector import detect_bugs
from core.fixer import fix_code
from utils.helpers import validate_input, detect_language

# 🔥 Page Config
st.set_page_config(
    page_title="AI Code Developer Assistant",
    page_icon="🤖",
    layout="centered"
)

# ✅ TITLE (FIXED - ALWAYS VISIBLE)
st.title("🤖 AI Code Developer Assistant")
st.caption("Generate • Debug • Fix Code using AI")

# 🎯 Feature selection
option = st.selectbox(
    "🚀 Choose Feature",
    ["Generate Code", "Detect Bugs", "Fix Code"]
)

# 🧠 Dynamic Heading
heading = (
    "🧠 Code Generation" if option == "Generate Code"
    else "🐞 Bug Detection" if option == "Detect Bugs"
    else "🛠 Code Fixing"
)

st.markdown(f"### {heading}")

# 📝 Input
user_input = st.text_area(
    "✍️ Enter your input/code here",
    placeholder="Example: Write Python code for factorial"
)

# ▶️ Run Button
if st.button("🚀 Run AI"):

    if not validate_input(user_input):
        st.warning("⚠️ Please enter valid input")
    else:
        with st.spinner("🤖 AI is thinking..."):

            try:
                if option == "Generate Code":
                    result = generate_code(user_input)
                elif option == "Detect Bugs":
                    result = detect_bugs(user_input)
                else:
                    result = fix_code(user_input)

                lang = detect_language(result)

                # ✨ Output
                st.subheader("✨ AI Result")
                st.code(result, language=lang)

                # ⬇️ Download
                st.download_button(
                    "⬇️ Download Code",
                    result,
                    file_name="output.py"
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")