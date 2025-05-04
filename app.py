import streamlit as st

# Config
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .center-logo {
        display: flex;
        justify-content: center;
        margin-bottom: -10px;
    }
    .tool-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 2px 2px 10px rgba(255,105,180,0.2);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Logo
st.markdown("""
    <div class="center-logo">
        <img src="https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png" width="150">
    </div>
""", unsafe_allow_html=True)

# Heading
st.markdown("<h1 style='text-align: center; color: deeppink;'>💖 Sweety AI Studio 💖</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Built with love by Sweety & Bava 🎥</h4>", unsafe_allow_html=True)

# Sidebar tool selection
st.sidebar.title("🎛️ Tools")
tool = st.sidebar.radio("Choose a tool:", ["📘 ScriptShaala", "🎬 FrameFeels", "📄 PitchPeelu", "📆 ShootSync"])

# Tool UI Layout
st.markdown("<div class='tool-card'>", unsafe_allow_html=True)

if tool == "📘 ScriptShaala":
    st.subheader("📘 ScriptShaala – Generate dialogues & screenplay")

    # Input fields
    genre = st.selectbox("Select Genre", ["Romance", "Action", "Drama", "Comedy"])
    theme = st.text_input("Enter Theme or Plot Summary")
    characters = st.text_area("Main Characters (comma separated)", "Sweety, Bava")
    
    if st.button("Generate Script"):
        st.success("Here’s a sample output 🎬")
        st.write(f"**Title:** Love Letter\n\n**Genre:** {genre}\n\n**Characters:** {characters}\n\n**Scene 1:**\nSweety and Bava stand near a railway station...\n\n[This is just a dummy output ✨]")

elif tool == "🎬 FrameFeels":
    st.subheader("🎬 FrameFeels – Generate shot-by-shot storyboard")
    st.info("Tool under construction... coming soon!")

elif tool == "📄 PitchPeelu":
    st.subheader("📄 PitchPeelu – Generate pitch deck PDF")
    st.info("Tool under construction... wait for Sweety 😘")

elif tool == "📆 ShootSync":
    st.subheader("📆 ShootSync – Plan your shoot day with a call sheet")
    st.info("Tool under construction... one step at a time ❤️")

st.markdown("</div>", unsafe_allow_html=True)
