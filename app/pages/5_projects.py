import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Projects | Gabrielle Tugano",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ────────────────────────────────────────────────────────────────────────
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
.project-tag {
    display: inline-block; background: var(--sand); color: var(--ink);
    font-size: 0.72rem; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase;
    padding: 0.25rem 0.7rem; border-radius: 2px; margin-right: 0.4rem; margin-bottom: 0.4rem;
}
.section-divider {
    border: none; border-top: 1px solid var(--sand); margin: 1.5rem 0;
}

/* ── Expander overrides ── */
[data-testid="stExpander"] {
    background: var(--white) !important;
    border: 1px solid var(--sand) !important;
    border-radius: 2px !important;
    margin-bottom: 1rem !important;
}
[data-testid="stExpander"]:hover {
    border-color: var(--blue) !important;
}
[data-testid="stExpanderToggleIcon"] { color: var(--blue) !important; }
[data-testid="stExpander"] summary {
    color: var(--ink) !important;
}
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] details summary div {
    color: var(--ink) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
}

.detail-label {
    font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--blue); font-weight: 500; margin-bottom: 0.3rem; margin-top: 1rem;
}
.detail-text {
    font-size: 0.9rem; color: var(--stone); line-height: 1.8;
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
st.markdown('<div class="page-eyebrow" style="padding: 0 2rem;">Projects</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title" style="padding: 0 2rem;">Things I\'ve built.</h1>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# ── Project data ───────────────────────────────────────────────────────────────
projects = [
    {
        "title": "AuditLens",
        "blurb": "an anomaly detection tool that analyzes over 284,000 credit card transactions "
                 "to automatically flag suspicious activity, revealing "
                 "the riskiest transactions so they can be reviewed. I built it to explore how "
                 "data science can make the audit process smarter and more scalable.",
        "tags": ["Python", "Data Analysis", "Audit"],
        "github": "https://github.com/gabrielletugano/AuditLens",
        "status": "Complete",
        "overview": "[Detailed overview of the project — what problem it solves, who it's for, and how it works.]",
        "challenges": "[Describe 1–2 challenges you ran into while building this and how you approached them.]",
        "lessons": "[What did you learn from this project? Technical skills, problem-solving approaches, etc.]",
        "next": "[What would you add or improve if you kept working on this?]",
    },
    {
        "title": "Breathe Easy",
        "blurb": "a multi-source data pipeline and interactive dashboard that pulls from five public datasets: "
                 "EPA, NOAA, OpenAQ, CDC, and the US Census — to explore how air quality and weather patterns "
                 "connect to respiratory health outcomes across four major East Coast cities. I built it to "
                 "practice building real-world data pipelines that integrate messy, disparate sources into "
                 "something actually usable and visually digestible.",
        "tags": ["[Tech 1]", "[Tech 2]", "[Tech 3]"],
        "github": "https://github.khoury.northeastern.edu/ilannalam/ds3500_final_project",
        "status": "In Progress",
        "overview": "[Detailed overview of the project.]",
        "challenges": "[Challenges you encountered.]",
        "lessons": "[What you learned.]",
        "next": "[Future improvements.]",
    },
    {
        "title": "[Project 3 Title]",
        "blurb": "[Short description of what this project does and why you built it.]",
        "tags": ["[Tech 1]", "[Tech 2]", "[Tech 3]"],
        "github": "https://github.com/gabrielletugano/[repo]",
        "status": "In Progress",
        "overview": "[Detailed overview of the project.]",
        "challenges": "[Challenges you encountered.]",
        "lessons": "[What you learned.]",
        "next": "[Future improvements.]",
    },
]

# ── Render projects ────────────────────────────────────────────────────────────
for p in projects:
    tags_html = "".join(f'<span class="project-tag">{t}</span>' for t in p["tags"])
    status_color = "#2A6CB0" if p["status"] == "In Progress" else "#5A8A5A"

    with st.expander(f"**{p['title']}** — {p['blurb']}", expanded=False):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f'<div style="margin-bottom:0.8rem;">{tags_html}</div>', unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style="text-align:right; font-size:0.75rem; font-weight:500;
                        color:{status_color}; letter-spacing:0.08em; text-transform:uppercase;">
                ● {p['status']}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

        st.markdown('<div class="detail-label">Overview</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-text">{p["overview"]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="detail-label">Challenges</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-text">{p["challenges"]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="detail-label">Lessons Learned</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-text">{p["lessons"]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="detail-label">What\'s Next</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-text">{p["next"]}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("View on GitHub →", p["github"])

    st.markdown("")