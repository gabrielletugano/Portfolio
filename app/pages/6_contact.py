import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Contact | Gabrielle Tugano",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --cream:   #F7F3EE;
    --ink:     #1A1A1A;
    --blue:    #2A6CB0;
    --stone:   #8C8070;
    --sand:    #E8DDD0;
    --white:   #FFFFFF;
    --navy:    #0F1F3D;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}

.stApp, [data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"], section[data-testid="stMainBlockContainer"] {
    background-color: var(--cream) !important;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

[data-testid="stSidebar"] {
    background-color: var(--navy) !important;
    border-right: none;
}
[data-testid="stSidebar"] * { color: var(--cream) !important; }
[data-testid="stSidebar"] a:hover { color: var(--blue) !important; }

h1, h2, h3, h4, h5, h6,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: var(--ink) !important;
    font-family: 'DM Serif Display', serif !important;
}

.page-eyebrow {
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--blue);
    font-weight: 500;
    margin-bottom: 0.8rem;
    padding-top: 3rem;
}
.page-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2rem, 5vw, 3.5rem);
    color: var(--ink);
    margin: 0 0 2.5rem;
    line-height: 1.1;
}

.section-label {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--blue);
    font-weight: 500;
    margin-bottom: 0.6rem;
}
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    color: var(--ink);
    margin: 0 0 1rem;
}

.body-text {
    font-size: 1rem;
    color: var(--stone);
    line-height: 1.8;
    max-width: 620px;
    margin-bottom: 1rem;
}

.contact-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-top: 1rem;
}
.contact-card {
    background: var(--white);
    border: 1px solid var(--sand);
    border-radius: 2px;
    padding: 1.5rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.contact-card:hover {
    border-color: var(--blue);
    box-shadow: 0 2px 12px rgba(42,108,176,0.08);
}
.contact-icon { font-size: 1.4rem; margin-bottom: 0.6rem; }
.contact-label {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--stone);
    font-weight: 500;
    margin-bottom: 0.4rem;
}
.contact-value {
    font-family: 'DM Serif Display', serif;
    font-size: 1.05rem;
    color: var(--ink);
}
.contact-value a {
    color: var(--ink) !important;
    text-decoration: none;
}
.contact-value a:hover {
    color: var(--blue) !important;
}

.section-divider {
    border: none;
    border-top: 1px solid var(--sand);
    margin: 3rem 0;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar brand mark ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 2rem 1.5rem 1rem; border-bottom: 1px solid #1E3560;">
        <div style="font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase;
                    color:#2A6CB0; margin-bottom:0.4rem;">Portfolio</div>
        <div style="font-family:'DM Serif Display',serif; font-size:1.3rem;
                    line-height:1.2; color:#F7F3EE;">Gabrielle<br>Tugano</div>
    </div>
    """, unsafe_allow_html=True)

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem;">
    <div class="page-eyebrow">Get In Touch</div>
    <h1 class="page-title">Let's connect.</h1>
</div>
""", unsafe_allow_html=True)

# ── Intro ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem;">
    <div class="section-label">Reach Out</div>
    <h2 class="section-title">I'd love to hear from you.</h2>
    <p class="body-text">
        Whether it's about a role, a project, or just to connect — don't hesitate to reach out.
        I'm always open to new conversations.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ── Contact cards ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem;">
    <div class="section-label">Where to Find Me</div>
    <div class="contact-grid">
        <div class="contact-card">
            <div class="contact-icon">📧</div>
            <div class="contact-label">Email</div>
            <div class="contact-value">
                <a href="mailto:gabbytugan0@gmail.com">gabbytugan0@gmail.com</a>
            </div>
        </div>
        <div class="contact-card">
            <div class="contact-icon">💼</div>
            <div class="contact-label">LinkedIn</div>
            <div class="contact-value">
                <a href="https://www.linkedin.com/in/gabrielle-tugano-b35982276/" target="_blank">Gabrielle Tugano</a>
            </div>
        </div>
        <div class="contact-card">
            <div class="contact-icon">🐋</div>
            <div class="contact-label">GitHub</div>
            <div class="contact-value">
                <a href="https://github.com/gabrielletugano" target="_blank">gabrielletugano</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ── Location ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem;">
    <div class="section-label">Based In</div>
    <h2 class="section-title">Boston, MA.</h2>
    <p class="body-text">Currently studying at Northeastern University. I'm open to remote and 
    in-person opportunities.</p>
</div>
""", unsafe_allow_html=True)