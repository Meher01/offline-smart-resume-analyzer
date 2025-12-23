# analyzer.py
import streamlit as st
import PyPDF2
import io
import re
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="📝 AI Resume Analyzer",
    page_icon="📝",
    layout="centered"
)

# --- CSS / UI ---
st.markdown(
    """
    <style>
    body { font-family: 'Segoe UI', sans-serif; }

    /* Header */
    .header { 
        display:flex; 
        align-items:center; 
        justify-content:space-between; 
        padding: 10px 20px; 
        background: linear-gradient(90deg, #4f46e5, #3b82f6); 
        border-radius: 12px; 
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        animation: fadeIn 1s ease-in-out;
    }
    .header h1 {
        font-size: 26px; 
        margin: 0; 
    }
    .header-date {
        font-size: 16px;
        font-weight: 500;
    }

    /* Card style */
    .card {
        border-radius:12px; 
        padding:20px; 
        background:#1e1e2f; 
        color:#f5f5f5;
        box-shadow:0 4px 20px rgba(0,0,0,0.25); 
        margin-bottom:20px;
        animation: slideUp 0.6s ease;
    }

    /* Pills */
    .pill {
        display:inline-block;
        background:#3b82f6;
        color:white;
        padding:4px 12px;
        border-radius:999px;
        margin:4px 4px 4px 0;
        font-size:14px;
        transition: transform 0.2s ease;
    }
    .pill:hover { transform: scale(1.08); }

    /* Score pill */
    .score-pill {
        font-weight:700; 
        font-size:20px; 
        padding:10px 18px; 
        border-radius:999px; 
        background:white; 
        color:#111; 
        display:inline-block;
        margin-bottom:10px;
    }

    /* Progress bar */
    .progress-wrap { 
        width:100%; 
        background:#333; 
        border-radius:999px; 
        height:18px; 
        overflow:hidden; 
        margin-top:6px;
    }
    .progress-bar { 
        height:18px; 
        border-radius:999px; 
        transition: width 0.6s ease; 
    }

    pre { 
        background:#2a2a3d; 
        padding:12px; 
        border-radius:8px; 
        color:#e5e5e5;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity:0; transform:translateY(-10px); }
        to { opacity:1; transform:translateY(0); }
    }
    @keyframes slideUp {
        from { opacity:0; transform:translateY(20px); }
        to { opacity:1; transform:translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Example Resume ---
example_resume_text = """
John Doe
Email: john.doe@email.com | LinkedIn: linkedin.com/in/johndoe

Summary:
Results-driven Backend Engineer with 3+ years of experience in building scalable REST APIs 
and cloud-native applications. Strong background in Java, Spring Boot, Python, and SQL.

Technical Skills:
- Programming: Java, Python, SQL, HTML, CSS, JavaScript
- Frameworks: Spring Boot, Flask, React
- Databases: MySQL, PostgreSQL, MongoDB
- DevOps: Docker, Kubernetes, AWS, GitHub Actions
- Testing: JUnit, Pytest

Experience:
Software Engineer, XYZ Corp (2021–Present)
- Developed RESTful APIs using Spring Boot for a microservices architecture.
- Deployed scalable applications on AWS with CI/CD pipelines.
- Improved SQL query performance by 30%.

Intern, ABC Ltd (2020)
- Built data processing scripts in Python and automated ETL pipelines.
- Assisted in deploying containerized apps with Docker.

Projects:
- Personal Finance Tracker: React + Flask app to track budgets.
- Open-source contributor to a Python data library on GitHub.

Education:
Bachelor of Technology in Computer Science, University of Somewhere (2016–2020)

Certifications:
AWS Certified Developer - Associate
Certified Kubernetes Application Developer (CKAD)
"""

# --- Text extraction ---
def extract_from_pdf(pdf_bytes):
    reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    return "\n".join([page.extract_text() or "" for page in reader.pages])

def extract_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_from_pdf(uploaded_file.read())
    else:
        return uploaded_file.read().decode("utf-8")

# --- Clean excerpt ---
def get_clean_excerpt(text, char_limit=700, max_extend=300):
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) <= char_limit: return text
    end_punc = ['.', '!', '?']
    candidates = [text.rfind(p, 0, char_limit) for p in end_punc]
    best_before = max(candidates)
    if best_before != -1 and best_before >= int(char_limit*0.5):
        return text[:best_before+1].strip()
    lookahead = text[char_limit:min(len(text), char_limit+max_extend)]
    next_pos = [lookahead.find(p) for p in end_punc if lookahead.find(p)!=-1]
    if next_pos: return text[:char_limit + min(next_pos)+1].strip()
    last_space = text.rfind(' ', 0, char_limit)
    return text[:last_space].strip() + "..." if last_space != -1 else text[:char_limit]+"..."

# --- Skills ---
technical_skills = ["python","java","c++","c#","javascript","typescript","html","css","sql","react","docker","aws","flask","spring boot"]
non_technical_signals = ["communication","leadership","teamwork","problem solving","critical thinking"]
extra_signals = ["certification","degree","internship","volunteer","hackathon"]

# --- Analyze Resume ---
def analyze_resume(content, job_role):
    content_lower = content.lower()
    found_tech = sorted({s for s in technical_skills if s in content_lower})
    found_nontech = sorted({s for s in non_technical_signals if s in content_lower})
    found_extra = sorted({s for s in extra_signals if s in content_lower})

    has_experience = "experience" in content_lower or "worked as" in content_lower
    has_projects = "project" in content_lower or "projects" in content_lower

    score_breakdown = {
        "job_role": 15 if job_role.lower() in content_lower else 0,
        "technical": min(35, len(found_tech)*4),
        "non_technical": min(15, len(found_nontech)*3),
        "experience_projects": min(20, (10 if has_experience else 0)+(7 if has_projects else 0)),
        "extras": min(15, len(found_extra)*3)
    }
    total_score = sum(score_breakdown.values())

    suggestions = []
    if score_breakdown["job_role"]<10 and job_role:
        suggestions.append(f"Include '{job_role}' in summary/bullets.")
    if score_breakdown["technical"]<20:
        suggestions.append("Add more technical keywords & frameworks.")
    if score_breakdown["non_technical"]<6:
        suggestions.append("Highlight leadership/communication skills.")
    if score_breakdown["experience_projects"]<10:
        suggestions.append("Add projects with measurable impact.")
    if score_breakdown["extras"]<6:
        suggestions.append("Include certifications, education, or open-source work.")
    if not suggestions: suggestions.append("Resume looks good! Consider quantifying impact.")

    excerpt = get_clean_excerpt(content)
    return {"found_tech": found_tech, "found_nontech": found_nontech, "found_extra": found_extra,
            "score": total_score, "breakdown": score_breakdown, "suggestions": suggestions,
            "raw_text_excerpt": excerpt}

def score_color(score):
    if score >= 80: return "#16a34a"
    if score >= 60: return "#f59e0b"
    return "#44efa8"

# --- Header ---
st.markdown(
    f"""
    <div class="header">
        <h1>🚀 AI Resume Analyzer Offline</h1>
        <div class="header-date">{datetime.utcnow().date()}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Inputs ---
uploaded_file = st.file_uploader("Upload the resume (PDF or TXT)", type=["pdf","txt"])
job_role = st.text_input("Target Job Role (optional):", placeholder="e.g., Backend Engineer")
col_demo, col_analyze = st.columns([0.4,0.6])
use_demo = col_demo.button("📄 Use Example Resume")
analyze = col_analyze.button("🔍 Analyze Resume", type="primary")

# --- Main action ---
if (analyze and uploaded_file) or use_demo:
    content = example_resume_text if use_demo else extract_from_file(uploaded_file)
    res = analyze_resume(content, job_role)

    # --- Highlights ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✨ Resume Highlights")
    st.markdown("Technical Skills:")
    st.markdown(" ".join([f'<span class="pill">{s}</span>' for s in res['found_tech']]), unsafe_allow_html=True)
    st.markdown("Non-Technical Skills:")
    st.markdown(" ".join([f'<span class="pill">{s}</span>' for s in res['found_nontech']]), unsafe_allow_html=True)
    st.markdown("Extras:")
    st.markdown(" ".join([f'<span class="pill">{s}</span>' for s in res['found_extra']]), unsafe_allow_html=True)
    st.markdown("Resume Excerpt:")
    with st.expander("📖 View excerpt"):
        st.write(res["raw_text_excerpt"])
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Score ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💯 Estimated Fit Score")
    color = score_color(res["score"])
    st.markdown(f'<div class="score-pill" style="background:{color}; color:white;">{res["score"]}/100</div>', unsafe_allow_html=True)

    st.markdown("Score Breakdown")
    max_scores = {
        "job_role": 15,
        "technical": 35,
        "non_technical": 15,
        "experience_projects": 20,
        "extras": 15
    }
    for k,v in res["breakdown"].items():
        max_val = max_scores[k]
        percent = int((v / max_val) * 100)
        st.markdown(f"""
            {k.replace('_',' ').title()}: {v}/{max_val}
            <div class="progress-wrap">
                <div class="progress-bar" style="width:{percent}%; background:{color};"></div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Suggestions ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🛠 Suggestions for Improvement")
    for s in res["suggestions"]:
        st.markdown(f"- {s}")
    st.markdown('</div>', unsafe_allow_html=True)  