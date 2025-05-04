import streamlit as st

st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Custom Logo and Title
st.markdown("""
    <div style="text-align:center;">
        <img src="https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png" width="160"/>
        <h1 style='color:darkred; font-size: 40px;'>🎬 Sweety AI Studio</h1>
        <h4 style='color:#555555;'>Tools for modern filmmaking, powered by AI 🎥</h4>
    </div>
    <hr style='margin-top: 10px; margin-bottom: 20px;' />
""", unsafe_allow_html=True)

# Sidebar Tool Selector
st.sidebar.title("🎛️ Tools")
tool = st.sidebar.radio("Choose a tool:", ["📘 ScriptShaala", "🎬 FrameFeels", "📄 PitchPeelu", "📆 ShootSync", "📹 Shot Division"])

# Tool: ScriptShaala
if tool == "📘 ScriptShaala":
    st.subheader("📘 ScriptShaala – Dialogue & Screenplay Generator")
    st.markdown("**Generate your film script structure with genre, summary, characters and a sample scene.**")

    genre = st.selectbox("🎭 Select Genre", ["Romance", "Drama", "Thriller", "Comedy"])
    summary = st.text_area("📝 Enter Story Summary", placeholder="Eg: A taxi driver and a mysterious girl meet on a rainy day...")
    characters = st.text_input("👥 Main Characters", placeholder="Eg: Raju, Sweety")

    if st.button("Generate Dummy Script"):
        st.markdown("### ✨ Generated Script")
        dummy_script = f"""
🎭 Genre: {genre}
📄 Summary: {summary}
👥 Characters: {characters}

---

📽️ Scene 1: EXT. BUS STOP – EVENING

Rain pours as people hurry past. Raju slows down his taxi and notices Sweety drenched but smiling.

RAJU  
(rolling down window)  
Need a ride?

SWEETY  
Only if you're going somewhere magical.

RAJU  
Buckle up.

The taxi pulls away, leaving a splash and a promise behind.

---

🔚 Full story coming soon...
        """

        st.text_area("🎥 Script Output", dummy_script.strip(), height=300)

        # Download as TXT
        st.download_button(
            label="📥 Download Script as .txt",
            data=dummy_script,
            file_name="sweety_script.txt",
            mime="text/plain"
        )

# Tool: FrameFeels
elif tool == "🎬 FrameFeels":
    st.subheader("🎬 FrameFeels – Shot-by-shot storyboard")
    st.info("Tool under construction... coming soon!")

# Tool: PitchPeelu
elif tool == "📄 PitchPeelu":
    st.subheader("📄 PitchPeelu – Create pitch deck")
    st.info("Tool under construction... wait for Sweety 😘")

# Tool: ShootSync
elif tool == "📆 ShootSync":
    st.subheader("📆 ShootSync – Call sheet planner")
    st.info("Tool under construction... one step at a time ❤️")

# Tool: Shot Division
elif tool == "📹 Shot Division":
    st.subheader("📹 Shot Division – Scene Breakdown & Angles")
    st.info("Tool under construction... dummy in place 😇")
