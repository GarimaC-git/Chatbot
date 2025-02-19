import streamlit as st
import random

# Set up the page title and layout
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Add typing effect for the title
st.markdown(
    """
    <h1 style='text-align:center;'>
        🤖 <span id='title'></span>
    </h1>
    <script>
        let i = 0;
        let txt = "WELCOME TO AI CHATBOT";
        function typeWriter() {
            if (i < txt.length) {
                document.getElementById('title').innerHTML += txt.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        typeWriter();
    </script>
    """,
    unsafe_allow_html=True
)

st.divider()
st.subheader("Interact with the chatbot from the sidebar")

# Display an AI chatbot image (centered)
st.markdown(
    """
    <style>
        .stImage { display: flex; justify-content: center; }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("https://powermaverick.dev/wp-content/uploads/2021/01/blog-banner.png")

# Fun interaction (Randomized Surprise Feature)
surprise_messages = [
    "🎈 Surprise! Keep exploring AI chatbots!",
    "🚀 You're awesome! Keep innovating with AI!",
    "✨ AI is full of surprises—keep chatting!",
    "🎉 You're one click away from discovering something amazing!"
]

st.subheader("✨ Want a surprise? Click below!")
if st.button("Give me a surprise! 🎉"):
    st.balloons()
    st.success(random.choice(surprise_messages))

# Styling to center the button
st.markdown(
    """
    <style>
        .stButton button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer message
st.markdown(
    "<p style='text-align:center;'>A fun AI experiment by Garima ⭐</p>",
    unsafe_allow_html=True
)
