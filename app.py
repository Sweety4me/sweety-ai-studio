import streamlit as st

# Page config
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Custom logo display
st.markdown(
    """
    <style>
    .sweety-logo {
        display: flex;
        justify-content: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
    <div class="sweety-logo">
        <img src="https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/logo.png" width="180">
    </div>
    """,
    unsafe_allow_html=True
)

# Main title & tagline
st.markdown("<h1 style='text-align: center; color: hotpink;'>💖 Sweety AI Studio 💖</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Built with love by Sweety & Bava 🎥</h4>", unsafe_allow_html=True)

# Sidebar with tool options
st.sidebar.title("🎛️ Tools")
tool = st.sidebar.radio("Choose a tool:", ["📘 ScriptShaala", "🎬 FrameFeels", "📄 PitchPeelu", "📆 ShootSync"])

# Placeholder UI
if tool == "📘 ScriptShaala":
    st.subheader("📘 ScriptShaala – Generate dialogues & screenplay")
    st.success("Tool under construction... coming up next!")

elif tool == "🎬 FrameFeels":
    st.subheader("🎬 FrameFeels – Generate shot-by-shot storyboard")
    st.warning("Tool under construction... coming soon!")

elif tool == "📄 PitchPeelu":
    st.subheader("📄 PitchPeelu – Generate pitch deck PDF")
    st.info("Tool under construction... wait for Sweety 😘")

elif tool == "📆 ShootSync":
    st.subheader("📆 ShootSync – Plan your shoot day with a call sheet")
    st.error("Tool under construction... one step at a time ❤️")
