import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Education | Gabrielle Tugano",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --cream:  #F7F3EE;
    --ink:    #1A1A1A;
    --navy:   #0F1F3D;
    --blue:   #2A6CB0;
    --stone:  #8C8070;
    --sand:   #E8DDD0;
    --rust:   #C0522A;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}

.stApp,
[data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"],
section[data-testid="stMainBlockContainer"] {
    background-color: var(--cream) !important;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
[data-testid="stSidebarNav"] { display: none; }

[data-testid="stSidebar"] {
    background-color: var(--navy) !important;
    border-right: none;
}
[data-testid="stSidebar"] * { color: var(--cream) !important; }
[data-testid="stSidebar"] a:hover { color: var(--blue) !important; }

/* ── Page header ── */
.page-header {
    border-bottom: 2px solid var(--ink);
    padding-bottom: 1.5rem;
    margin-bottom: 2.5rem;
}
.page-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--stone);
    margin-bottom: 0.5rem;
}
.page-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.8rem;
    font-weight: 400;
    color: var(--navy) !important;
    line-height: 1.1;
    margin: 0;
}

[data-testid="stMarkdownContainer"] h1,
.stMarkdown h1 {
    font-family: 'DM Serif Display', serif !important;
    color: var(--navy) !important;
    font-weight: 400 !important;
}

/* ── Section headings ── */
.section-label {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--stone);
    margin-bottom: 1rem;
    margin-top: 2.5rem;
    display: block;
}

/* ── School block ── */
.school-block {
    margin-bottom: 0.5rem;
}
.school-name {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    font-weight: 400;
    color: var(--navy);
    line-height: 1.2;
}
.school-meta {
    font-size: 13.5px;
    color: var(--stone);
    margin-top: 0.25rem;
}
.degree-line {
    font-size: 15px;
    color: var(--ink);
    margin-top: 0.6rem;
    font-weight: 500;
}

/* ── GPA badge ── */
.gpa-badge {
    display: inline-block;
    background: var(--navy);
    color: #F7F3EE;
    font-size: 13px;
    font-weight: 500;
    padding: 5px 14px;
    border-radius: 3px;
    margin-top: 0.75rem;
    letter-spacing: 0.04em;
}

/* ── Honors badge ── */
.honor-badge {
    display: inline-block;
    background: var(--sand);
    color: var(--ink);
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.05em;
    padding: 4px 12px;
    border-radius: 3px;
    margin-top: 0.5rem;
    margin-right: 6px;
}

/* ── Course pills ── */
.course-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 0.5rem;
}
.course-pill {
    background: #fff;
    border: 1px solid var(--sand);
    color: var(--ink);
    font-size: 13px;
    padding: 6px 14px;
    border-radius: 3px;
}

/* ── Club cards ── */
.club-card {
    background: #fff;
    border: 1px solid var(--sand);
    border-radius: 4px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
}
.club-name {
    font-weight: 500;
    font-size: 15px;
    color: var(--ink);
    margin-bottom: 0.2rem;
}
.club-role {
    font-size: 13px;
    color: var(--stone);
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--sand);
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ✦ Gabrielle Tugano")
    st.markdown("---")
    st.page_link("main.py",               label="Home")
    st.page_link("pages/1_about.py",      label="About")
    st.page_link("pages/2_experience.py", label="Experience")
    st.page_link("pages/3_education.py",  label="Education")
    st.page_link("pages/4_skills.py",     label="Skills")
    st.page_link("pages/5_projects.py",   label="Projects")
    st.page_link("pages/6_contact.py",    label="Contact")
    st.page_link("pages/7_blog.py",       label="Blog")

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-label">Background</div>
    <h1 class="page-title">Education</h1>
</div>
""", unsafe_allow_html=True)

# ── School ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="school-block">
    <div class="school-name">Northeastern University</div>
    <div class="school-meta">Boston, MA &nbsp;·&nbsp; Expected May 2027</div>
    <div class="degree-line">Bachelor of Science — Data Science &amp; Business Administration</div>
    <div class="school-meta" style="margin-top:0.2rem;">Concentration in Accounting</div>
    <div style="margin-top:0.75rem;">
        <span class="gpa-badge">GPA &nbsp;3.83</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── Honors ────────────────────────────────────────────────────────────────────
st.markdown('<span class="section-label">Honors</span>', unsafe_allow_html=True)
st.markdown("""
<div>
    <span class="honor-badge">Dean's List — Freshman Year</span>
    <span class="honor-badge">Dean's List — Sophomore Year</span>
    <span class="honor-badge">Dean's List — Junior Year</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── Relevant Coursework ───────────────────────────────────────────────────────
st.markdown('<span class="section-label">Relevant Coursework</span>', unsafe_allow_html=True)

courses = [
    "Programming with Data (DS2000)",
    "Intermediate Programming with Data (DS2500)",
    "Advanced Data Science (DS3500)",
    "Database Design (CS3200)",
    "Cybersecurity (CY2550)",
    "Financial Accounting (ACCT1201)",
    "Managerial Accounting (ACCT2301)",
    "Financial Reporting and Analysis 1 (ACCT3401)",
]

course_html = "".join(f'<span class="course-pill">{c}</span>' for c in courses)
st.markdown(f'<div class="course-grid">{course_html}</div>', unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── Clubs & Organizations ─────────────────────────────────────────────────────
st.markdown('<span class="section-label">Clubs &amp; Organizations</span>', unsafe_allow_html=True)

clubs = [
    ("Kappa Delta Sorority", "Member"),
    ("Northeastern Women in Business", "Member"),
    ("Barkada — Filipino Student Association", "Member"),
]

for name, role in clubs:
    st.markdown(f"""
    <div class="club-card">
        <div class="club-name">{name}</div>
        <div class="club-role">{role}</div>
    </div>
    """, unsafe_allow_html=True)