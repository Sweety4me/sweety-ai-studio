import streamlit as st

# Page config
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Logo from GitHub
st.markdown(
    """
    <div style="text-align: center; padding-top: 10px;">
        <img src="https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/logo.png" width="180">
    </div>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align: center; color: pink;'>💖 Sweety AI Studio 💖</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Built with love by Sweety & Bava 🎥</h4>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎛️ Tools")
tool = st.sidebar.radio("Choose a tool:", ["📘 ScriptShaala", "🎬 FrameFeels", "📄 PitchPeelu", "📆 ShootSync"])

# Placeholder UI for each tool
if tool == "📘 ScriptShaala":
    st.subheader("📘 ScriptShaala – Generate dialogues & screenplay")
    st.info("Tool under construction... coming up next!")

elif tool == "🎬 FrameFeels":
    st.subheader("🎬 FrameFeels – Generate shot-by-shot storyboard")
    st.info("Tool under construction... coming soon!")

elif tool == "📄 PitchPeelu":
    st.subheader("📄 PitchPeelu – Generate pitch deck PDF")
    st.info("Tool under construction... wait for Sweety 😘")

elif tool == "📆 ShootSync":
    st.subheader("📆 ShootSync – Plan your shoot day with a call sheet")
    st.info("Tool under construction... one step at a time ❤️")
