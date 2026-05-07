import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Experience | Gabrielle Tugano",
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

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; color: var(--ink); }

.stApp, [data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"], section[data-testid="stMainBlockContainer"] {
    background-color: var(--cream) !important;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

[data-testid="stSidebar"] { background-color: var(--navy) !important; border-right: none; }
[data-testid="stSidebar"] * { color: var(--cream) !important; }
[data-testid="stSidebar"] a:hover { color: var(--blue) !important; }

h1, h2, h3, [data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2, [data-testid="stMarkdownContainer"] h3 {
    color: var(--ink) !important;
    font-family: 'DM Serif Display', serif !important;
}

.page-eyebrow {
    font-size: 0.78rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--blue); font-weight: 500; margin-bottom: 0.8rem; padding-top: 3rem;
}
.page-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2rem, 5vw, 3.5rem);
    color: var(--ink); margin: 0 0 3rem; line-height: 1.1;
}
.timeline-date {
    font-size: 0.75rem; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--blue); font-weight: 500; margin-bottom: 0.3rem;
}
.timeline-role {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem; color: var(--ink); margin-bottom: 0.2rem;
}
.timeline-company {
    font-size: 0.9rem; color: var(--stone); font-weight: 500; margin-bottom: 0.8rem;
}
.timeline-tag {
    display: inline-block; background: var(--sand); color: var(--ink);
    font-size: 0.75rem; font-weight: 500; letter-spacing: 0.04em;
    padding: 0.3rem 0.8rem; border-radius: 2px; margin-right: 0.4rem; margin-top: 0.6rem;
}
.section-divider {
    border: none; border-top: 1px solid var(--sand); margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 2rem 1.5rem 1rem; border-bottom: 1px solid #1E3560;">
        <div style="font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase;
                    color:#2A6CB0; margin-bottom:0.4rem;">Portfolio</div>
        <div style="font-family:'DM Serif Display',serif; font-size:1.3rem;
                    line-height:1.2; color:#F7F3EE;">Gabrielle<br>Tugano</div>
    </div>
    """, unsafe_allow_html=True)

# ── Page header ────────────────────────────────────────────────────────────────
st.markdown('<div class="page-eyebrow" style="padding: 0 2rem;">Work Experience</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title" style="padding: 0 2rem;">Where I\'ve been.</h1>', unsafe_allow_html=True)

# ── Helper function ────────────────────────────────────────────────────────────
def timeline_entry(date, role, company, bullets, tags):
    bullets_html = "".join(f"<li style='margin-bottom:0.4rem; color:#8C8070; font-size:0.9rem; line-height:1.8;'>{b}</li>" for b in bullets)
    tags_html = "".join(f"<span class='timeline-tag'>{t}</span>" for t in tags)
    st.markdown(f"""
    <div style="padding: 0 2rem 0 3rem; border-left: 2px solid #E8DDD0; margin: 0 2rem 2.5rem 2rem; position: relative;">
        <div style="position:absolute; left:-0.45rem; top:0.3rem; width:10px; height:10px;
                    border-radius:50%; background:#2A6CB0; border:2px solid #F7F3EE;
                    box-shadow: 0 0 0 2px #2A6CB0;"></div>
        <div class="timeline-date">{date}</div>
        <div class="timeline-role">{role}</div>
        <div class="timeline-company">{company}</div>
        <ul style="padding-left:1.2rem; margin:0 0 0.5rem;">
            {bullets_html}
        </ul>
        <div>{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Timeline entries ───────────────────────────────────────────────────────────
timeline_entry(
    date="June 2025 — December 2025",
    role="Full-Stack Developer",
    company="Fresenius Medical Care · Lexington, MA",
    bullets=[
        "Developed an end-to-end healthcare web application integrating clinical "
        "reports and patient follow-up data",
        "Implemented and executed 100+ Junit tests for application reliability, "
        "functionality, and quality purposes",
        "Queried large-scale financial datasets (e.g., Expense Lines, "
        "Cost Plans, Budgets) using SQL, enabling month-over-month cost analysis "
        "across 10+ budget categories ",
    ],
    tags=["Full-Stack Development", "SQL & Data Analysis", "Software Testing (Junit)"]
)

timeline_entry(
    date="July 2026 — December 2026",
    role="Internal Audit",
    company="Boston Beer Company · Boston, MA",
    bullets=[
        "[Describe a key responsibility or achievement.]",
        "[Describe a key responsibility or achievement.]",
        "[Describe a key responsibility or achievement.]",
    ],
    tags=["[Skill 1]", "[Skill 2]", "[Skill 3]"]
)