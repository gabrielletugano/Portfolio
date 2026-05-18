import streamlit as st
import json
import os
from datetime import datetime

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Blog | Gabrielle Tugano",
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
    margin-bottom: 2rem;
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

/* Force h1 override for Streamlit's default heading styles */
[data-testid="stMarkdownContainer"] h1,
.stMarkdown h1 {
    font-family: 'DM Serif Display', serif !important;
    color: var(--navy) !important;
    font-weight: 400 !important;
}

/* ── Blog cards ── */
.blog-card {
    background: #fff;
    border: 1px solid var(--sand);
    border-radius: 4px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1.25rem;
    transition: border-color 0.2s;
}
.blog-card:hover { border-color: var(--stone); }
.blog-card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem;
    font-weight: 400;
    color: var(--ink);
    margin-bottom: 0.35rem;
}
.blog-card-meta {
    font-size: 12px;
    color: var(--stone);
    margin-bottom: 0.75rem;
    letter-spacing: 0.03em;
}
.blog-card-excerpt {
    font-size: 14px;
    color: #444;
    line-height: 1.65;
    margin-bottom: 0.75rem;
}
.tag-pill {
    display: inline-block;
    background: var(--sand);
    color: var(--stone);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 20px;
    margin-right: 6px;
}

/* ── Full post view ── */
.post-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.2rem;
    font-weight: 400;
    color: var(--ink);
    margin-bottom: 0.5rem;
    line-height: 1.2;
}
.post-meta {
    font-size: 13px;
    color: var(--stone);
    border-bottom: 1px solid var(--sand);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
}
.post-body {
    font-size: 15.5px;
    line-height: 1.8;
    color: #2a2a2a;
    max-width: 680px;
}

/* ── Section divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--sand);
    margin: 2rem 0;
}

/* ── Form styling ── */
.form-section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--stone);
    margin-bottom: 0.75rem;
    display: block;
}
</style>
""", unsafe_allow_html=True)

# ── Data helpers ───────────────────────────────────────────────────────────────
POSTS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "blog_posts.json")

def load_posts():
    os.makedirs(os.path.dirname(POSTS_FILE), exist_ok=True)
    if not os.path.exists(POSTS_FILE):
        return []
    with open(POSTS_FILE, "r") as f:
        return json.load(f)

def save_posts(posts):
    os.makedirs(os.path.dirname(POSTS_FILE), exist_ok=True)
    with open(POSTS_FILE, "w") as f:
        json.dump(posts, f, indent=2)

def new_id(posts):
    return max((p["id"] for p in posts), default=0) + 1

def excerpt(body, chars=160):
    return body[:chars].rstrip() + "…" if len(body) > chars else body

# ── Session state ──────────────────────────────────────────────────────────────
if "blog_view" not in st.session_state:
    st.session_state.blog_view = "list"   # list | read | write | edit | login
if "active_post_id" not in st.session_state:
    st.session_state.active_post_id = None
if "filter_tag" not in st.session_state:
    st.session_state.filter_tag = "All"
if "is_author" not in st.session_state:
    st.session_state.is_author = False

# ── Sidebar nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ✦ Gabrielle Tugano")
    st.markdown("---")
    st.page_link("main.py",            label="Home")
    st.page_link("pages/1_about.py",   label="About")
    st.page_link("pages/2_experience.py", label="Experience")
    st.page_link("pages/3_education.py",  label="Education")
    st.page_link("pages/4_skills.py",     label="Skills")
    st.page_link("pages/5_projects.py",   label="Projects")
    st.page_link("pages/6_contact.py",    label="Contact")
    st.page_link("pages/7_blog.py",       label="Blog")

# ── Load posts ─────────────────────────────────────────────────────────────────
posts = load_posts()

# ═══════════════════════════════════════════════════════════════════════════════
# VIEW: LIST
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.blog_view == "list":

    # Page header
    st.markdown("""
    <div class="page-header">
        <div class="page-label">Writing</div>
        <h1 class="page-title">Blog</h1>
    </div>
    """, unsafe_allow_html=True)

    # Controls row
    col_filter, col_spacer, col_btn = st.columns([2, 4, 1.2])

    all_tags = sorted({tag for p in posts for tag in p.get("tags", [])})
    tag_options = ["All"] + all_tags

    with col_filter:
        chosen_tag = st.selectbox(
            "Filter by tag",
            tag_options,
            index=tag_options.index(st.session_state.filter_tag)
                  if st.session_state.filter_tag in tag_options else 0,
            label_visibility="collapsed",
        )
        st.session_state.filter_tag = chosen_tag

    with col_btn:
        if st.session_state.is_author:
            if st.button("✦ New Post", use_container_width=True):
                st.session_state.blog_view = "write"
                st.rerun()
        else:
            if st.button("Author Login", use_container_width=True):
                st.session_state.blog_view = "login"
                st.rerun()

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Filter posts
    visible = [
        p for p in sorted(posts, key=lambda x: x["date"], reverse=True)
        if chosen_tag == "All" or chosen_tag in p.get("tags", [])
    ]

    if not visible:
        st.markdown(
            "<p style='color:#8C8070;font-size:15px;margin-top:1rem;'>"
            "No posts yet — hit <strong>✦ New Post</strong> to write your first one.</p>",
            unsafe_allow_html=True,
        )
    else:
        for post in visible:
            tag_html = "".join(
                f'<span class="tag-pill">{t}</span>' for t in post.get("tags", [])
            )
            st.markdown(f"""
            <div class="blog-card">
                <div class="blog-card-title">{post['title']}</div>
                <div class="blog-card-meta">{post['date']}</div>
                <div class="blog-card-excerpt">{excerpt(post['body'])}</div>
                <div>{tag_html}</div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3 = st.columns([1.2, 1.2, 8])
            with c1:
                if st.button("Read →", key=f"read_{post['id']}"):
                    st.session_state.active_post_id = post["id"]
                    st.session_state.blog_view = "read"
                    st.rerun()
            if st.session_state.is_author:
                with c2:
                    if st.button("Edit", key=f"edit_{post['id']}"):
                        st.session_state.active_post_id = post["id"]
                        st.session_state.blog_view = "edit"
                        st.rerun()
                with c3:
                    if st.button("Delete", key=f"del_{post['id']}"):
                        posts = [p for p in posts if p["id"] != post["id"]]
                        save_posts(posts)
                        st.success("Post deleted.")
                        st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# VIEW: READ
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.blog_view == "read":
    post = next((p for p in posts if p["id"] == st.session_state.active_post_id), None)

    if st.button("← Back to Blog"):
        st.session_state.blog_view = "list"
        st.rerun()

    if post:
        tag_html = "".join(
            f'<span class="tag-pill">{t}</span>' for t in post.get("tags", [])
        )
        st.markdown(f"""
        <div style="max-width:720px;margin-top:1.5rem;">
            <h1 class="post-title">{post['title']}</h1>
            <div class="post-meta">{post['date']} &nbsp;·&nbsp; {tag_html}</div>
            <div class="post-body">{post['body'].replace(chr(10), '<br>')}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Post not found.")

# ═══════════════════════════════════════════════════════════════════════════════
# VIEW: WRITE (new post)
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.blog_view == "write":

    st.markdown("""
    <div class="page-header">
        <div class="page-label">Writing</div>
        <h1 class="page-title">New Post</h1>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Cancel"):
        st.session_state.blog_view = "list"
        st.rerun()

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    title = st.text_input("Title", placeholder="Post title")
    tags_raw = st.text_input(
        "Tags",
        placeholder="e.g. data science, internship, python  (comma-separated)",
    )
    body = st.text_area("Content", height=320, placeholder="Write your post here…")

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    if st.button("Publish Post", type="primary"):
        if not title.strip():
            st.warning("Please add a title.")
        elif not body.strip():
            st.warning("Please write some content.")
        else:
            tags = [t.strip() for t in tags_raw.split(",") if t.strip()]
            new_post = {
                "id":    new_id(posts),
                "title": title.strip(),
                "date":  datetime.today().strftime("%B %d, %Y"),
                "tags":  tags,
                "body":  body.strip(),
            }
            posts.append(new_post)
            save_posts(posts)
            st.success("Post published!")
            st.session_state.blog_view = "list"
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# VIEW: EDIT
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.blog_view == "edit":
    post = next((p for p in posts if p["id"] == st.session_state.active_post_id), None)

    st.markdown("""
    <div class="page-header">
        <div class="page-label">Writing</div>
        <h1 class="page-title">Edit Post</h1>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Cancel"):
        st.session_state.blog_view = "list"
        st.rerun()

    if post:
        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

        title = st.text_input("Title", value=post["title"])
        tags_raw = st.text_input("Tags", value=", ".join(post.get("tags", [])))
        body = st.text_area("Content", value=post["body"], height=320)

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        if st.button("Save Changes", type="primary"):
            if not title.strip():
                st.warning("Title can't be empty.")
            elif not body.strip():
                st.warning("Content can't be empty.")
            else:
                tags = [t.strip() for t in tags_raw.split(",") if t.strip()]
                for p in posts:
                    if p["id"] == post["id"]:
                        p["title"] = title.strip()
                        p["tags"]  = tags
                        p["body"]  = body.strip()
                        break
                save_posts(posts)
                st.success("Post updated!")
                st.session_state.blog_view = "list"
                st.rerun()
    else:
        st.error("Post not found.")

# ═══════════════════════════════════════════════════════════════════════════════
# VIEW: LOGIN
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.blog_view == "login":

    st.markdown("""
    <div class="page-header">
        <div class="page-label">Writing</div>
        <h1 class="page-title">Author Login</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='max-width:380px;margin-top:1rem'>", unsafe_allow_html=True)
    pw = st.text_input("Password", type="password")
    col_a, col_b = st.columns([1, 2])
    with col_a:
        if st.button("Log in", type="primary", use_container_width=True):
            if pw == st.secrets["BLOG_PASSWORD"]:
                st.session_state.is_author = True
                st.session_state.blog_view = "list"
                st.rerun()
            else:
                st.error("Incorrect password.")
    with col_b:
        if st.button("← Cancel", use_container_width=True):
            st.session_state.blog_view = "list"
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)