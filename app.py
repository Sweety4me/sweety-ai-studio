import streamlit as st

# Page config
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Logo and Title
st.markdown("""
    <style>
    .logo {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: -10px;
    }
    .title-block {
        text-align: center;
        padding-top: 10px;
    }
    .main-title {
        font-size: 32px;
        font-weight: bold;
        color: #1f1f1f;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px;
        color: #6f6f6f;
        font-weight: 500;
    }
    .tool-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Show logo from GitHub
st.markdown(
    """
    <div class="logo">
        <img src="https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png" width="130">
    </div>
    """,
    unsafe_allow_html=True
)

# Title block
st.markdown("""
    <div class='title-block'>
        <div class='main-title'>Sweety AI Studio</div>
        <div class='sub-title'>AI Tools for Modern Filmmakers</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar tool navigation
st.sidebar.title("🎛️ AI Tools")
tool = st.sidebar.radio("Select a Tool", ["ScriptShaala", "FrameFeels", "PitchPeelu", "ShootSync"])

# Tool container
st.markdown("<div class='tool-card'>", unsafe_allow_html=True)

if tool == "ScriptShaala":
    st.subheader("🎬 ScriptShaala – Screenplay Generator")
    genre = st.selectbox("🎭 Choose Genre", ["Romance", "Action", "Drama", "Thriller"])
    theme = st.text_input("🧵 Theme or Summary")
    characters = st.text_area("🧑‍🤝‍🧑 Main Characters (comma-separated)", placeholder="Ex: Arjun, Meera")

    if st.button("🚀 Generate Screenplay"):
        st.success("✅ Screenplay Generated")
        first_character = characters.split(",")[0].strip() if characters else "Character"
        st.write(f"""**Title:** {theme or "Untitled Project"}  
**Genre:** {genre}  
**Characters:** {characters or "N/A"}  

**Scene 1:**  
INT. COFFEE SHOP – DAY  
{first_character} sits alone, flipping through an old diary. Raindrops tap on the glass.  
A stranger enters. Their eyes meet. The story begins...  
""")

elif tool == "FrameFeels":
    st.subheader("🖼️ FrameFeels – Storyboard Generator")
    st.info("Coming soon... will help you visualize each scene frame-by-frame!")

elif tool == "PitchPeelu":
    st.subheader("📄 PitchPeelu – PDF Deck Builder")
    st.info("Coming soon... will auto-generate investor & producer pitch decks!")

elif tool == "ShootSync":
    st.subheader("📅 ShootSync – Call Sheet Planner")
    st.info("Coming soon... will manage your shoot day like a pro!")

st.markdown("</div>", unsafe_allow_html=True)
