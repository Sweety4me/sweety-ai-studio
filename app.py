import streamlit as st

# Page config
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Logo + Title + Tagline
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png' width='150'>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #222;'>🎬 Sweety AI Studio</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #555;'>AI Tools for Modern Filmmakers</h4>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.title("🎛️ Tools")
tool = st.sidebar.radio("Choose a tool:", [
    "📘 ScriptShaala",
    "🎬 FrameFeels",
    "📄 PitchPeelu",
    "📆 ShootSync",
    "📸 Shot Division"
])

# Tools
if tool == "📘 ScriptShaala":
    st.subheader("📘 ScriptShaala – Generate dialogues & screenplay")
    st.write("Enter a scene description and get dummy script output.")
    scene = st.text_area("Scene Description", placeholder="Eg: A boy meets girl on a rainy day...")
    if st.button("Generate Dummy Script"):
        st.markdown("#### 📝 Output Script")
        st.markdown("""
        **Scene 1: INT. COFFEE SHOP – EVENING**

        A boy sits alone near the window, raindrops tracing the glass.  
        A girl enters, looking around. Their eyes meet.

        **BOY**  
        Is this seat taken?

        **GIRL**  
        Not anymore.

        **[Story continues...]**

        🔜 *Full story coming soon...*
        """)

elif tool == "🎬 FrameFeels":
    st.subheader("🎬 FrameFeels – Generate shot-by-shot storyboard")
    st.info("Tool under construction... coming soon!")

elif tool == "📄 PitchPeelu":
    st.subheader("📄 PitchPeelu – Generate pitch deck PDF")
    st.info("Tool under construction... wait for Sweety 😘")

elif tool == "📆 ShootSync":
    st.subheader("📆 ShootSync – Plan your shoot day with a call sheet")
    st.info("Tool under construction... one step at a time ❤️")

elif tool == "📸 Shot Division":
    st.subheader("📸 Shot Division – Scene-wise shot breakdown")
    st.write("**Scene:** Opening Scene – Hero Introduction")
    st.write("""
        1. Wide shot – City view  
        2. Mid shot – Hero walking  
        3. Close up – Hero face reveal  
        4. Tracking shot – Following hero  
    """)
    st.success("Dummy output generated. Full tool coming soon!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Built with ❤️ by Sweety & Bava | © 2025</p>", unsafe_allow_html=True)
