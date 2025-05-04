import streamlit as st

# Page Configuration
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Load Logo and Styles
st.markdown("""
    <style>
    .logo {
        display: flex;
        justify-content: center;
        margin-top: -20px;
        margin-bottom: 10px;
    }
    .title-block {
        text-align: center;
        margin-bottom: 20px;
    }
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #222222;
    }
    .sub-title {
        font-size: 20px;
        font-weight: 500;
        color: #555555;
    }
    .tool-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    }
    </style>
""", unsafe_allow_html=True)

# Show Logo
st.markdown("""
    <div class="logo">
        <img src="https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png" width="150">
    </div>
""", unsafe_allow_html=True)

# Title & Tagline
st.markdown("""
    <div class="title-block">
        <div class="main-title">Sweety AI Studio</div>
        <div class="sub-title">AI Tools for Modern Filmmakers</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🎛️ AI Tools")
tool = st.sidebar.radio("Select a Tool", [
    "ScriptShaala", 
    "FrameFeels", 
    "PitchPeelu", 
    "ShootSync",
    "ShotDivision"  # New Tool added
])

# Main Tool Display
st.markdown("<div class='tool-card'>", unsafe_allow_html=True)

if tool == "ScriptShaala":
    st.subheader("🎬 ScriptShaala – Screenplay Generator")
    genre = st.selectbox("🎭 Choose Genre", ["Romance", "Action", "Drama", "Thriller"])
    theme = st.text_input("🧵 Theme or Summary")
    characters = st.text_area("👥 Characters (comma-separated)", placeholder="Ex: Arjun, Meera")

    if st.button("🚀 Generate Script"):
        st.success("✅ Screenplay Generated")
        first_char = characters.split(",")[0].strip() if characters else "Character"
        st.markdown(f"""
        **🎞️ Title:** *{theme or 'Untitled Project'}*  
        **🎭 Genre:** {genre}  
        **👥 Characters:** {characters or 'Not Provided'}  
        
        ---
        **📍 Scene 1**  
        INT. COFFEE SHOP – DAY  
        {first_char} sits alone, flipping through an old diary. Raindrops tap the glass.  
        A stranger enters. Their eyes meet. The story begins...

        📌 *Full story coming soon... stay tuned!*
        """)

elif tool == "FrameFeels":
    st.subheader("🖼️ FrameFeels – Storyboard Generator")
    st.info("Coming soon... visualize each scene frame-by-frame!")

elif tool == "PitchPeelu":
    st.subheader("📄 PitchPeelu – PDF Deck Builder")
    st.info("Coming soon... auto-generate producer & investor pitch decks!")

elif tool == "ShootSync":
    st.subheader("📅 ShootSync – Call Sheet Planner")
    st.info("Coming soon... manage your shoot day like a pro!")

elif tool == "ShotDivision":
    st.subheader("🎞️ ShotDivision – Scene Breakdown & Shot Planning")
    st.info("Coming soon... will help you split scenes into shots with angles and camera notes!")

st.markdown("</div>", unsafe_allow_html=True)
