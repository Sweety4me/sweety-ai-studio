import streamlit as st

# Page settings
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Title + Logo + Tagline
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png' width='150'>
        <h1 style='font-size: 40px; margin-top: 10px; margin-bottom: 0; color: #222;'>Sweety AI Studio</h1>
        <p style='font-size: 18px; color: #666;'>AI Tools for Modern Filmmakers</p>
    </div>
""", unsafe_allow_html=True)

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

# Tool Logic
if tool == "📘 ScriptShaala":
    st.subheader("📘 ScriptShaala – Generate dialogues & screenplay")
    st.text_area("Enter scene description", placeholder="Eg: A boy meets girl on a rainy day...")
    st.button("Generate Script")
    st.markdown("#### 📝 Output")
    st.info("Scene 1: INT. COFFEE SHOP – EVENING\n\nA boy sits alone... [Story continues here]\n\n🔜 Full story coming soon...")

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
