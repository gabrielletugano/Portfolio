import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Skills | Gabrielle Tugano",
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

/* ── Category card ── */
.category-card {
    background: #fff;
    border: 1px solid var(--sand);
    border-radius: 4px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1.25rem;
    height: 100%;
}
.category-title {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--stone);
    margin-bottom: 1.25rem;
    display: block;
}

/* ── Skill row ── */
.skill-row {
    margin-bottom: 1rem;
}
.skill-label-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 5px;
}
.skill-name {
    font-size: 14px;
    font-weight: 500;
    color: var(--ink);
}
.skill-level {
    font-size: 11px;
    color: var(--stone);
    letter-spacing: 0.04em;
}

/* ── Progress bar track ── */
.bar-track {
    background: var(--sand);
    border-radius: 2px;
    height: 5px;
    width: 100%;
}
.bar-fill {
    height: 5px;
    border-radius: 2px;
    background: var(--navy);
    transition: width 0.6s ease;
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--sand);
    margin: 1.5rem 0;
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
    <div class="page-label">What I Work With</div>
    <h1 class="page-title">Skills</h1>
</div>
""", unsafe_allow_html=True)

# ── Skill data ────────────────────────────────────────────────────────────────
# Proficiency levels map to bar widths:
# Expert = 95%, Proficient = 78%, Intermediate = 60%, Familiar = 40%

LEVELS = {
    "Expert":       95,
    "Proficient":   78,
    "Intermediate": 60,
    "Familiar":     40,
}

categories = [
    {
        "title": "Programming Languages",
        "skills": [
            ("Python",      "Expert"),
            ("SQL",         "Proficient"),
            ("R",           "Intermediate"),
            ("Java",        "Familiar"),
            ("HTML / CSS",  "Intermediate"),
        ],
    },
    {
        "title": "Tools & Platforms",
        "skills": [
            ("Git / GitHub",  "Proficient"),
            ("Docker",        "Proficient"),
            ("PyCharm",       "Expert"),
            ("Streamlit",     "Proficient"),
            ("Flask",         "Intermediate"),
            ("VS Code",       "Proficient"),
        ],
    },
    {
        "title": "Data & Analytics",
        "skills": [
            ("Pandas / NumPy",      "Expert"),
            ("Scikit-learn",        "Proficient"),
            ("Matplotlib / Seaborn","Proficient"),
            ("GeoPandas / Folium",  "Intermediate"),
            ("MySQL",               "Proficient"),
            ("SQLite",              "Intermediate"),
        ],
    },
    {
        "title": "Accounting & Finance",
        "skills": [
            ("Financial Reporting",     "Proficient"),
            ("Managerial Accounting",   "Proficient"),
            ("Internal Audit Concepts", "Intermediate"),
            ("Cost & Variance Analysis","Intermediate"),
            ("Microsoft Excel",         "Proficient"),
        ],
    },
    {
        "title": "Soft Skills",
        "skills": [
            ("Communication",      "Expert"),
            ("Problem Solving",    "Expert"),
            ("Collaboration",      "Expert"),
            ("Project Management", "Proficient"),
            ("Attention to Detail","Expert"),
        ],
    },
]

# ── Helper: render one skill bar ──────────────────────────────────────────────
def skill_bar(name, level):
    width = LEVELS.get(level, 50)
    return f"""
    <div class="skill-row">
        <div class="skill-label-row">
            <span class="skill-name">{name}</span>
            <span class="skill-level">{level}</span>
        </div>
        <div class="bar-track">
            <div class="bar-fill" style="width:{width}%"></div>
        </div>
    </div>
    """

# ── Helper: render one category card ─────────────────────────────────────────
def category_card(cat):
    bars = "".join(skill_bar(s, l) for s, l in cat["skills"])
    return f"""
    <div class="category-card">
        <span class="category-title">{cat['title']}</span>
        {bars}
    </div>
    """

# ── Layout: 2 columns ─────────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="large")

left_cats  = categories[:3]   # Programming, Tools, Data
right_cats = categories[3:]   # Accounting, Soft Skills

with col1:
    for cat in left_cats:
        st.markdown(category_card(cat), unsafe_allow_html=True)

with col2:
    for cat in right_cats:
        st.markdown(category_card(cat), unsafe_allow_html=True)