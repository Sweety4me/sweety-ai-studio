import streamlit as st

# Page config
st.set_page_config(page_title="Sweety AI Studio", page_icon="🎬", layout="wide")

# Logo + Title
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/Sweety4me/sweety-ai-studio/main/assets/Sweety%20logo.png' width='150'>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: darkred;'>🎬 Sweety AI Studio</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #444;'>AI Tools for Modern Filmmakers – By Sweety & Bava</h4>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.title("🎛️ Tools")
tool = st.sidebar.radio("Choose a tool:", [
    "📘 ScriptShaala",
    "📸 Shot Division",
    "🎬 FrameFeels",
    "📄 PitchPeelu",
    "📆 ShootSync"
])

# ScriptShaala Tool
if tool == "📘 ScriptShaala":
    st.subheader("📘 ScriptShaala – Dummy Script Generator")

    st.text_input("🎞️ Genre", value="Romance Drama", key="genre")
    st.text_area("📄 Summary", placeholder="Eg: A lonely man finds love in an unexpected way.")
    st.text_area("🎭 Characters", placeholder="Eg: Raju - a taxi driver, Sweety - a cheerful artist")
    st.text_area("🎬 Scene Description", placeholder="Eg: Raju is driving through the rain-soaked streets when he sees Sweety waiting...")

    if st.button("Generate Dummy Script"):
        st.markdown("### ✨ Generated Script")

        st.markdown("""
        **Scene 1: EXT. BUS STOP – EVENING**

        Rain pours as people hurry past. Raju slows down his taxi and notices Sweety drenched but smiling.

        **RAJU**  
        (rolling down window)  
        Need a ride?

        **SWEETY**  
        Only if you're going somewhere magical.

        **RAJU**  
        Buckle up.

        The taxi pulls away, leaving a splash and a promise behind.

        🔚 *Full story coming soon...*
        """)

# Shot Division Dummy
elif tool == "📸 Shot Division":
    st.subheader("📸 Shot Division – Dummy Output")

    st.write("🎬 Scene: Hero Introduction")
    st.markdown("""
    - Shot 1: Wide shot – City skyline  
    - Shot 2: Mid shot – Hero walking on bridge  
    - Shot 3: Close up – Hero lights cigarette  
    - Shot 4: Drone shot – Zoom out from above  
    """)
    st.success("More shot divisions coming soon...")

# Other tools – placeholders
elif tool == "🎬 FrameFeels":
    st.subheader("🎬 FrameFeels – Storyboard Tool")
    st.info("Tool under construction... stay tuned!")

elif tool == "📄 PitchPeelu":
    st.subheader("📄 PitchPeelu – Pitch Deck Creator")
    st.info("Tool under construction... wait for Sweety 😘")

elif tool == "📆 ShootSync":
    st.subheader("📆 ShootSync – Shoot Planner")
    st.info("Tool under construction... one step at a time ❤️")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>© 2025 Sweety & Bava Productions</p>", unsafe_allow_html=True)
