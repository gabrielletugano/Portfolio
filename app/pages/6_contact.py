# about.py
import streamlit as st

# page configuration
st.set_page_config(
    page_title="About Me | Gabrielle Tugano",
    page_icon="👤",
    layout="wide"
)

# sidebar
with st.sidebar:
    st.markdown("## Gabrielle Tugano")
    st.markdown("*Data Science & Business Administration*")
    st.markdown("*Northeastern University*")
    st.markdown("---")
    st.page_link("main.py", label="🏠 Home")
    st.page_link("pages/about.py", label="👤 About Me")
    st.page_link("pages/experience.py", label="💼 Experience")
    st.page_link("pages/education.py", label="🎓 Education")
    st.page_link("pages/skills.py", label="🛠️ Skills")
    st.page_link("pages/projects.py", label="🚀 Projects")
    st.page_link("pages/contact.py", label="📬 Contact")
    st.markdown("---")
    st.markdown("[GitHub](https://github.com) | [LinkedIn](https://linkedin.com)")

# page title
st.title("👤 About Me")
st.markdown("---")

# photo and bio
col1, col2 = st.columns([1, 2])

with col1:
    # replace with your actual photo path
    st.image("app/assets/profile.jpg", width=250)

with col2:
    st.subheader("Hi, I'm Gabrielle 👋")
    st.markdown("""
    # ADD YOUR BIO HERE
    """)

st.markdown("---")

# quick facts
st.subheader("Quick Facts")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("📍 **Location**")
    st.markdown("Boston, MA")

with col2:
    st.markdown("🎓 **University**")
    st.markdown("Northeastern University")

with col3:
    st.markdown("📅 **Expected Graduation**")
    st.markdown("# ADD GRADUATION YEAR")

st.markdown("---")

# interests
st.subheader("Interests")
st.markdown("""
# ADD YOUR INTERESTS HERE
""")