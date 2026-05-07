import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Gabrielle Tugano | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Root palette ── */
:root {
    --cream:   #F7F3EE;
    --ink:     #1A1A1A;
    --rust:    #2A6CB0;
    --stone:   #8C8070;
    --sand:    #E8DDD0;
    --white:   #FFFFFF;
    --navy:    #0F1F3D;
}

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}

/* ── Force cream on main content only ── */
.stApp, [data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"], section[data-testid="stMainBlockContainer"] {
    background-color: var(--cream) !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: var(--navy) !important;
    border-right: none;
}
[data-testid="stSidebar"] * {
    color: var(--cream) !important;
}
[data-testid="stSidebar"] a:hover {
    color: var(--rust) !important;
}

/* ── Sidebar nav links ── */
[data-testid="stSidebarNav"] a {
    font-family: 'DM Sans', sans-serif;
    font-weight: 400;
    letter-spacing: 0.04em;
    font-size: 0.9rem;
    text-transform: uppercase;
    padding: 0.5rem 1rem;
    transition: color 0.2s ease;
}

/* ── Headings ── */
h1, h2, h3 {
    font-family: 'DM Serif Display', serif;
    font-weight: 400;
}

/* ── Hero section ── */
.hero-wrap {
    padding: 4rem 2rem 3rem;
    max-width: 860px;
}
.hero-eyebrow {
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--rust);
    font-weight: 500;
    margin-bottom: 1rem;
}
.hero-name {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(3rem, 7vw, 5.5rem);
    line-height: 1.05;
    color: var(--rust);
    margin: 0 0 1.2rem;
}
.hero-name em {
    color: var(--rust);
    font-style: italic;
}
.hero-tagline {
    font-size: 1.1rem;
    color: var(--stone);
    font-weight: 300;
    line-height: 1.7;
    max-width: 520px;
    margin-bottom: 2.5rem;
}

/* ── CTA buttons ── */
.cta-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}
.btn-primary {
    background: var(--rust);
    color: var(--white) !important;
    border: none;
    padding: 0.75rem 1.75rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    text-decoration: none !important;
    cursor: pointer;
    transition: background 0.2s ease, transform 0.15s ease;
    display: inline-block;
}
.btn-primary:hover {
    background: #1E5490;
    transform: translateY(-2px);
}
.btn-ghost {
    background: transparent;
    color: var(--ink) !important;
    border: 1.5px solid var(--ink);
    padding: 0.75rem 1.75rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    text-decoration: none !important;
    cursor: pointer;
    transition: border-color 0.2s ease, color 0.2s ease, transform 0.15s ease;
    display: inline-block;
}
.btn-ghost:hover {
    border-color: var(--rust);
    color: var(--rust) !important;
    transform: translateY(-2px);
}

/* ── Divider ── */
.section-divider {
    border: none;
    border-top: 1px solid var(--sand);
    margin: 2.5rem 0;
}

/* ── Stat strip ── */
.stat-strip {
    display: flex;
    gap: 3rem;
    flex-wrap: wrap;
    padding: 2rem 2rem;
    background: var(--sand);
    margin-top: 0;
}
.stat-item { display: flex; flex-direction: column; gap: 0.2rem; }
.stat-number {
    font-family: 'DM Serif Display', serif;
    font-size: 2.2rem;
    color: var(--rust);
    line-height: 1;
}
.stat-label {
    font-size: 0.78rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--stone);
    font-weight: 500;
}

/* ── Quick-nav cards ── */
.nav-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-top: 2.5rem;
}
.nav-card {
    background: var(--white);
    border: 1px solid var(--sand);
    border-radius: 2px;
    padding: 1.8rem 1.5rem;
    cursor: pointer;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    text-decoration: none;
    display: block;
}
.nav-card:hover {
    border-color: var(--rust);
    box-shadow: 0 2px 12px rgba(42,108,176,0.08);
}
.nav-card-icon { font-size: 1.4rem; margin-bottom: 0.8rem; }
.nav-card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.15rem;
    color: var(--ink);
    margin-bottom: 0.3rem;
}
.nav-card-desc {
    font-size: 0.82rem;
    color: var(--stone);
    line-height: 1.5;
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
                    line-height:1.2; color:#F7F3EE;">Gabrielle Tugano</div>
    </div>
    """, unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-eyebrow">Data Science × Business</div>
    <h1 class="hero-name"><span style="color:#2A6CB0;">Gabrielle</span><br><em>Tugano</em></h1>
    <p class="hero-tagline">
        Double major student at Northeastern University combining data science
        and accounting to turn complex data into clear business decisions.
    </p>
    <div class="cta-row">
        <a class="btn-primary" href="#projects">View Projects</a>
        <a class="btn-ghost"   href="#contact">Get in Touch</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Stat strip ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-strip">
    <div class="stat-item">
        <span class="stat-number">1</span>
        <span class="stat-label">Degree in Progress</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">2</span>
        <span class="stat-label">Co-ops Completed</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">NU '27</span>
        <span class="stat-label">Northeastern University</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">F'26</span>
        <span class="stat-label">Boston Beer Co. · Internal Audit</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Quick-nav cards ───────────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

st.markdown("""
<style>
div.stButton > button {
    background: var(--white);
    border: 1px solid var(--sand);
    border-radius: 2px;
    padding: 1.5rem;
    width: 100%;
    height: 160px;
    text-align: left;
    vertical-align: top;
    align-items: flex-start;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    white-space: normal;
    line-height: 1.5;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
div.stButton > button:hover {
    border-color: #2A6CB0 !important;
    box-shadow: 0 2px 12px rgba(42,108,176,0.08);
    background: var(--white) !important;
    color: var(--ink) !important;
}
div.stButton > button p {
    margin: 0;
    text-align: left;
    width: 100%;
}
div.stButton > button:focus {
    box-shadow: none;
    border-color: var(--sand);
}
</style>
""", unsafe_allow_html=True)

pages = [
    ("✦", "About",      "Background, values, what drives me",  "pages/1_about.py"),
    ("◈", "Experience", "Co-ops, internships & work history",       "pages/2_experience.py"),
    ("◎", "Education",  "Northeastern DS + Business Admin",         "pages/3_education.py"),
    ("⟡", "Skills",     "Technical stack & core competencies",      "pages/4_skills.py"),
    ("◇", "Projects",   "Data pipelines, analyses & builds",        "pages/5_projects.py"),
    ("→", "Contact",    "Let's connect",                            "pages/6_contact.py"),
]

row1 = st.columns(3)
row2 = st.columns(3)

for i, (icon, title, desc, path) in enumerate(pages):
    col = row1[i] if i < 3 else row2[i - 3]
    with col:
        if st.button(f"{icon}  {title}\n\n{desc}", key=f"nav_{title}"):
            st.switch_page(path)