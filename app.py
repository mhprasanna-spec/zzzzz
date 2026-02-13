import streamlit as st
import ollama
import base64

st.set_page_config(
    page_title="🌸 LLaMA 3.2 Chatbot",
    page_icon="🦙",
    layout="centered"
)

# --------------------------------------------------
# Background + Overlay
# --------------------------------------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        /* Background */
        .stApp {{
            background:
                linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
                url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Title */
        h1 {{
            color: white;
        }}

        .stCaption {{
            color: #dddddd;
        }}

        /* USER message */
        div[data-testid="stChatMessage"][aria-label="user"] {{
            background-color: #e3f2fd;
            color: #000000;
            border-radius: 14px;
            padding: 14px;
            margin-bottom: 10px;
        }}

        /* ASSISTANT message */
        div[data-testid="stChatMessage"][aria-label="assistant"] {{
            background-color: #ffffff;
            color: #000000;
            border-radius: 14px;
            padding: 14px;
            margin-bottom: 10px;
        }}

        /* Fix text visibility */
        div[data-testid="stMarkdownContainer"] p {{
            color: #000000 !important;
        }}

        /* Chat input bar */
        div[data-testid="stChatInput"] {{
            background-color: rgba(0,0,0,0.85);
            padding: 12px;
            border-radius: 16px;
        }}

        textarea {{
            background-color: #ffffff !important;
            color: #000000 !important;
            border-radius: 12px !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("lily.jpg")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🌸 LLaMA 3.2 Chatbot")
st.caption("Powered by Ollama · llama3.2:latest · Runs locally")

# --------------------------------------------------
# Chat History
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------------------------------------
# Input
# --------------------------------------------------
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        box = st.empty()
        full_response = ""

        stream = ollama.chat(
            model="llama3.2:latest",
            messages=st.session_state.messages,
            stream=True
        )

        for chunk in stream:
            full_response += chunk["message"]["content"]
            box.markdown(full_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )
