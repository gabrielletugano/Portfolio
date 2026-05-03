import os
import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="About | Gabrielle Tugano",
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

/* ── Force heading colors ── */
h1, h2, h3, h4, h5, h6,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: var(--ink) !important;
    font-family: 'DM Serif Display', serif !important;
}

/* ── Page header ── */
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

/* ── Section headings ── */
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

/* ── Body text ── */
.body-text {
    font-size: 1rem;
    color: var(--stone);
    line-height: 1.8;
    max-width: 620px;
    margin-bottom: 1rem;
}

/* ── Values cards ── */
.values-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-top: 1rem;
}
.value-card {
    background: var(--white);
    border: 1px solid var(--sand);
    border-radius: 2px;
    padding: 1.5rem;
}
.value-icon { font-size: 1.4rem; margin-bottom: 0.6rem; }
.value-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.05rem;
    color: var(--ink);
    margin-bottom: 0.4rem;
}
.value-desc {
    font-size: 0.82rem;
    color: var(--stone);
    line-height: 1.6;
}

/* ── Hobbies strip ── */
.hobbies-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1rem;
}
.hobby-tag {
    background: var(--sand);
    color: var(--ink);
    font-size: 0.82rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    padding: 0.5rem 1rem;
    border-radius: 2px;
}

/* ── Divider ── */
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
    <div class="page-eyebrow">About Me</div>
    <h1 class="page-title">The person behind<br>the portfolio.</h1>
</div>
""", unsafe_allow_html=True)

# ── Bio ───────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style="padding: 0 2rem;">
        <div class="section-label">Introduction</div>
        <h2 class="section-title">Hi, I'm Gabrielle.</h2>
        <p class="body-text">
            [Intro paragraph]
        </p>
        <p class="body-text">
            [my time at Northeastern,
            your co-op experiences, or what I've learned along the way.]
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    img_path = os.path.join(os.path.dirname(__file__), "..", "assets", "profile.jpeg")
    st.image(img_path, width=300)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ── Values ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem;">
    <div class="section-label">What Drives Me</div>
    <h2 class="section-title">My values.</h2>
    <div class="values-grid">
        <div class="value-card">
            <div class="value-icon">◎</div>
            <div class="value-title">Growth</div>
            <div class="value-desc">[Desc]</div>
        </div>
        <div class="value-card">
            <div class="value-icon">◈</div>
            <div class="value-title">Integrity</div>
            <div class="value-desc">[Desc]</div>
        </div>
        <div class="value-card">
            <div class="value-icon">⟡</div>
            <div class="value-title">Gratitude</div>
            <div class="value-desc">[Desc]</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ── Hobbies ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem;">
    <div class="section-label">Outside of Work</div>
    <h2 class="section-title">A few of my favorite things.</h2>
    <p class="body-text">[Write a sentence or two about what I enjoy outside of school and work]</p>
    <div class="hobbies-strip">
        <span class="hobby-tag">Weightlifting</span>
        <span class="hobby-tag">Running</span>
        <span class="hobby-tag">Hiking</span>
        <span class="hobby-tag">Dancing</span>
        <span class="hobby-tag">Cooking</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ── Career goals ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem;">
    <div class="section-label">Looking Ahead</div>
    <h2 class="section-title">Where I'm headed.</h2>
    <p class="body-text">
        [Short-term career goals — the kind of roles, industries,
        or problems I want to work on after graduation.]
    </p>
    <p class="body-text">
        [Long-term vision — where do I see yourself in 5–10 years?
        What impact do I want to make?]
    </p>
</div>
""", unsafe_allow_html=True)