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
            I'm a fourth-year Northeastern University student studying Data Science and 
            Business Administration with a Concentration in Accounting. During my time at Northeastern, 
            I've had the privilege to explore both sides of my combined major through my co-ops at 
            Fresenius Medical Care and The Boston Beer Company.
        </p>
        <p class="body-text">
            At Fresenius, I worked as a full-stack developer, building applications for nurses to 
            manage treatment sheets, end-of-shift reports, and volume hypertension reports. 
            This fall, I'll be joining The Boston Beer Company as an Internal Audit co-op. 
            What I've loved most about both experiences is the freedom to go beyond the job description
             — each team gave me the space to explore the industry on my own terms, and I got to see 
             firsthand how a data science and accounting background can speak to both technical and 
             business needs at once. That intersection is what I find most exciting, and long-term, 
             I hope to use it to help make the audit process smarter and more efficient.
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
            <div class="value-icon">🌳</div>
            <div class="value-title">Growth</div>
            <div class="value-desc">I'd take a hard redirect over empty validation any day. 
            Honest feedback is how I actually get better and being told my process is wrong is far 
            more valuable to me than being left to repeat it. I'd rather someone take the time to 
            correct me than spare my feelings at the expense of my growth.</div>
        </div>
        <div class="value-card">
            <div class="value-icon">👩🏻‍⚖️</div>
            <div class="value-title">Integrity</div>
            <div class="value-desc">Integrity means owning your mistakes before they become 
            someone else's problem. I'd rather raise my hand, admit I got it wrong, and fix it 
            together than let pride get in the way of the team moving forward.</div>
        </div>
        <div class="value-card">
            <div class="value-icon">🕊️</div>
            <div class="value-title">Gratitude</div>
            <div class="value-desc">Not everyone gets to do what they love,
             and I don't take that lightly. Choosing 'I get to' over 'I have to' is how 
             I stay grounded in what actually matters.</div>
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
    <p class="body-text">When I'm not in class or off the clock, I love pursing hobbies that push me 
    both physically and mentally. You might find me hiking a trail in Acadia, attempting a new recipe 
    in the kitchen, or finding a new playlist to move to at the gym. I'm someone who's always looking 
    for the next thing to do, the next place to go, or the next skill to pick up. I think it's safe 
    to say staying still doesn't really suit me.</p>
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
        After graduation, I want to pursue a career in internal auditing, but I don't want to stop there. 
        My data science background gives me a lens that most auditors don't have, and I want to use it. 
        Projects like AuditLens, where I built a tool to flag fraudulent and suspicious transactions, 
        showed me how much room there is to make the audit process smarter and more automated. 
        That's the problem I want to keep working on.
    </p>
    <p class="body-text">
        Five to ten years from now, I'm keeping my options open on purpose. I want to spend my early 
        career exploring the industry, following what excites me, and letting my experiences shape 
        where I end up — rather than locking myself into a plan before I've even fully started. 
        I'd rather stay curious and let the industry surprise me than commit to a path before I've 
        had the chance to truly explore it.
    </p>
</div>
""", unsafe_allow_html=True)