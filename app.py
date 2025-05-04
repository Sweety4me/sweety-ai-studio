import streamlit as st

# Page configuration
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Professional CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .header {
        text-align: center;
        padding: 10px;
    }
    .logo-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 120px;
        margin-bottom: -10px;
    }
    .tool-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        margin-top: 20px;
    }
    .title-text {
        font-size: 30px;
        color: #333333;
        font-weight: 600;
    }
    .subtitle-text {
        font-size: 16px;
        color: #666666;
    }
    </style>
""", unsafe_allow_html=True)

# Logo and Title
st.markdown('<img class="logo-img" src="https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png">', unsafe_allow_html=True)
st.markdown("<div class='header'><div class='title-text'>Sweety AI Studio</div><div class='subtitle-text'>AI Tools for Modern Filmmakers</div></div>", unsafe_allow_html=True)

# Sidebar Tool Navigation
st.sidebar.title("🛠️ AI Tools")
tool = st.sidebar.radio("Select a tool", ["ScriptShaala", "FrameFeels", "PitchPeelu", "ShootSync"])

# Tool UI
st.markdown("<div class='tool-card'>", unsafe_allow_html=True)

if tool == "ScriptShaala":
    st.subheader("🎬 ScriptShaala – Screenplay Generator")
    genre = st.selectbox("Choose Genre", ["Romance", "Action", "Drama", "Thriller"])
    theme = st.text_input("Theme or Summary")
    characters = st.text_area("Main Characters", placeholder="Ex: Aarya, Sita")

    if st.button("Generate Script"):
        st.success("Sample Screenplay Output")
        st.write(f"""**Title:** {theme or "Untitled Project"}  
**Genre:** {genre}  
**Characters:** {characters}  

**Scene 1:**  
INT. TEA SHOP – DAY  
{characters.split(",")[0].strip()} sits alone sipping chai. The city buzzes behind them.  
[Generated screenplay coming soon...]""")

elif tool == "FrameFeels":
    st.subheader("🎞️ FrameFeels – Storyboard Tool")
    st.info("This tool is coming soon.")

elif tool == "PitchPeelu":
    st.subheader("📝 PitchPeelu – Pitch Deck Builder")
    st.info("This tool is under development.")

elif tool == "ShootSync":
    st.subheader("📅 ShootSync – Call Sheet Scheduler")
    st.info("Coming soon with scheduling features.")

st.markdown("</div>", unsafe_allow_html=True)
