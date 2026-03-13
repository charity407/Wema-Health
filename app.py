"""
Wema Health — Afrocentric Women's Health Navigation Platform
Hackathon MVP · Python + Streamlit · Single-file deployment
PEP8-compliant
"""

import io
import datetime
import random

import numpy as np
import pandas as pd
import streamlit as st

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle,
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Wema Health",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --rose:     #C0395A; --rose-lt: #E8657E;
    --gold:     #D4A843; --gold-lt: #F0C96A;
    --cream:    #FDF6EE; --white:   #FFFFFF;
    --charcoal: #1C1C2E; --muted:   #6B6B80;
    --border:   #F0E4D4;
    --shadow:   0 4px 24px rgba(192,57,90,0.08);
    --shadow-lg:0 8px 40px rgba(192,57,90,0.14);
}
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--cream);
    color: var(--charcoal);

.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

/* ══ SIDEBAR SHELL ══ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1C1C2E 0%, #2A1228 60%, #1C1C2E 100%) !important;
    border-right: 1px solid rgba(212,168,67,0.22) !important;
    transition: width 0.3s ease !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
}
/* All text inside sidebar inherits cream */
[data-testid="stSidebar"] * { color: var(--cream) !important; }
[data-testid="stSidebar"] hr { border-color: rgba(212,168,67,0.28) !important; }

/* ── Radio nav items ── */
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.9rem !important;
    padding: 0.38rem 0.3rem !important;
    letter-spacing: 0.02em !important;
    cursor: pointer !important;
    border-radius: 8px !important;
    transition: background 0.18s !important;
    display: block !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(212,168,67,0.1) !important;
    color: #F0C96A !important;
}

/* ── Expander headers — nav group titles ── */
[data-testid="stSidebar"] .streamlit-expanderHeader {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(212,168,67,0.18) !important;
    border-radius: 10px !important;
    padding: 0.55rem 0.8rem !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
    color: #F0C96A !important;
    margin-bottom: 0.15rem !important;
    transition: background 0.18s !important;
}
[data-testid="stSidebar"] .streamlit-expanderHeader:hover {
    background: rgba(212,168,67,0.12) !important;
}
[data-testid="stSidebar"] .streamlit-expanderHeader svg {
    stroke: #F0C96A !important;
}
/* Expander content area */
[data-testid="stSidebar"] .streamlit-expanderContent {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(212,168,67,0.1) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
    padding: 0.4rem 0.5rem 0.6rem 0.5rem !important;
    margin-bottom: 0.5rem !important;
}

/* ── Nav sub-buttons inside expanders ── */
.sidebar-nav-btn {
    display: block !important;
    width: 100% !important;
    background: transparent !important;
    border: none !important;
    text-align: left !important;
    padding: 0.42rem 0.6rem !important;
    border-radius: 8px !important;
    font-size: 0.88rem !important;
    color: rgba(253,246,238,0.82) !important;
    cursor: pointer !important;
    margin-bottom: 0.1rem !important;
    transition: background 0.18s, color 0.18s !important;
    letter-spacing: 0.01em !important;
}
.sidebar-nav-btn:hover, .sidebar-nav-btn.active {
    background: rgba(212,168,67,0.14) !important;
    color: #F0C96A !important;
}
.sidebar-nav-btn.active {
    border-left: 3px solid #D4A843 !important;
    padding-left: 0.85rem !important;
    font-weight: 600 !important;
}

/* ── Sidebar collapse button ── */
[data-testid="stSidebarCollapseButton"] {
    background: rgba(212,168,67,0.1) !important;
    border: 1.5px solid rgba(212,168,67,0.4) !important;
    border-radius: 50% !important;
    width: 2rem !important; height: 2rem !important;
    transition: background 0.2s, transform 0.2s !important;
}
[data-testid="stSidebarCollapseButton"]:hover {
    background: rgba(212,168,67,0.25) !important;
    transform: scale(1.08) !important;
}
[data-testid="stSidebarCollapseButton"] svg { stroke: #F0C96A !important; fill: none !important; }

/* ── Collapsed rail ── */
[data-testid="collapsedControl"] {
    background: linear-gradient(180deg, #1C1C2E 0%, #2A1228 100%) !important;
    border-right: 2px solid rgba(212,168,67,0.3) !important;
    display: flex !important; align-items: flex-start !important;
    padding-top: 1rem !important;
}
[data-testid="collapsedControl"] button {
    background: rgba(212,168,67,0.1) !important;
    border: 1.5px solid rgba(212,168,67,0.4) !important;
    border-radius: 50% !important;
    width: 2rem !important; height: 2rem !important;
    margin: 0 auto !important;
    transition: background 0.2s, transform 0.2s !important;
}
[data-testid="collapsedControl"] button:hover {
    background: rgba(212,168,67,0.25) !important;
    transform: scale(1.08) !important;
}
[data-testid="collapsedControl"] svg { stroke: #F0C96A !important; fill: none !important; }

/* ── Cards ── */
.wema-card {
    background:var(--white); border-radius:16px; padding:1.6rem 1.8rem;
    box-shadow:var(--shadow); border:1px solid var(--border); margin-bottom:1.2rem;
}
.wema-card h3 { font-family:'Playfair Display',serif; color:var(--rose); margin-top:0; }

/* ── Hero ── */
.hero-section {
    background:linear-gradient(135deg,#1C1C2E 0%,#3D1A30 55%,#1C1C2E 100%);
    border-radius:20px; padding:3.5rem 3rem; margin-bottom:2rem;
    position:relative; overflow:hidden; box-shadow:var(--shadow-lg);
}
.hero-section::before {
    content:''; position:absolute; top:-60px; right:-60px;
    width:300px; height:300px;
    background:radial-gradient(circle,rgba(212,168,67,0.15) 0%,transparent 70%);
    border-radius:50%;
}
.hero-title {
    font-family:'Playfair Display',serif; font-size:3.2rem; font-weight:700;
    color:var(--white); line-height:1.15; margin:0 0 0.5rem 0;
}
.hero-accent { color:var(--gold-lt); }
.hero-sub {
    font-size:1.15rem; color:rgba(253,246,238,0.78); font-weight:300;
    margin:0.7rem 0 1.8rem 0; max-width:560px; line-height:1.65;
}
.hero-badge {
    display:inline-block; background:rgba(212,168,67,0.18); color:var(--gold-lt);
    border:1px solid rgba(212,168,67,0.35); border-radius:50px;
    padding:0.3rem 1rem; font-size:0.82rem; letter-spacing:0.06em;
    text-transform:uppercase; margin-bottom:1.2rem; font-weight:500;
}

/* ── Step cards ── */
.step-card {
    background:var(--white); border-radius:16px; padding:1.6rem;
    text-align:center; box-shadow:var(--shadow); border-top:4px solid var(--rose); height:100%;
}
.step-icon { font-size:2.4rem; margin-bottom:0.8rem; }
.step-num {
    background:var(--rose); color:white; width:28px; height:28px; border-radius:50%;
    display:inline-flex; align-items:center; justify-content:center;
    font-size:0.85rem; font-weight:700; margin-bottom:0.7rem;
}
.step-card h4 { font-family:'Playfair Display',serif; font-size:1.1rem; color:var(--charcoal); margin:0.4rem 0; }
.step-card p  { font-size:0.88rem; color:var(--muted); line-height:1.55; margin:0; }

/* ── Triage badges ── */
.badge-green  { background:#d4edda; color:#155724; padding:0.35rem 1.1rem; border-radius:50px; font-weight:600; font-size:0.9rem; border:1.5px solid #c3e6cb; display:inline-block; }
.badge-yellow { background:#fff3cd; color:#856404; padding:0.35rem 1.1rem; border-radius:50px; font-weight:600; font-size:0.9rem; border:1.5px solid #ffeeba; display:inline-block; }
.badge-red    { background:#f8d7da; color:#721c24; padding:0.35rem 1.1rem; border-radius:50px; font-weight:600; font-size:0.9rem; border:1.5px solid #f5c6cb; display:inline-block; }

/* ── Report box ── */
.report-box {
    background:linear-gradient(135deg,#FDF6EE,#fff);
    border-left:5px solid var(--rose); border-radius:0 16px 16px 0;
    padding:1.8rem 2rem; box-shadow:var(--shadow); margin-top:1rem;
}
.report-title { font-family:'Playfair Display',serif; font-size:1.5rem; color:var(--rose); margin:0 0 0.3rem 0; }
.report-meta  { font-size:0.83rem; color:var(--muted); margin-bottom:1.2rem; }
.report-section { margin-bottom:1rem; }
.report-section strong { font-size:0.8rem; text-transform:uppercase; letter-spacing:0.07em; color:var(--muted); display:block; margin-bottom:0.3rem; }
.report-section p { font-size:0.97rem; color:var(--charcoal); margin:0; line-height:1.6; }

/* ── Forum ── */
.forum-post {
    background:var(--white); border-radius:14px; padding:1.2rem 1.5rem;
    margin-bottom:1rem; box-shadow:var(--shadow); border-left:4px solid var(--gold);
}
.forum-post .anon-tag { background:var(--rose); color:white; border-radius:50px; padding:0.15rem 0.7rem; font-size:0.75rem; font-weight:600; margin-right:0.5rem; }
.forum-post .time-tag { color:var(--muted); font-size:0.78rem; }
.forum-post .post-body { margin:0.65rem 0 0.5rem 0; font-size:0.95rem; line-height:1.6; color:var(--charcoal); }
.forum-post .reactions { font-size:0.82rem; color:var(--muted); }

/* ── Resources ── */
.resource-card { background:var(--white); border-radius:16px; padding:1.6rem; box-shadow:var(--shadow); border-top:4px solid var(--gold); margin-bottom:1rem; }
.resource-card h4 { font-family:'Playfair Display',serif; font-size:1.2rem; color:var(--charcoal); margin:0 0 0.5rem 0; }
.resource-card .tag { background:#FDF0D8; color:#8B5E00; border-radius:50px; padding:0.2rem 0.7rem; font-size:0.75rem; font-weight:600; margin-right:0.4rem; display:inline-block; margin-bottom:0.6rem; }
.resource-card p { font-size:0.9rem; line-height:1.65; color:var(--muted); margin:0; }

/* ── Stat tiles ── */
.stat-tile { background:linear-gradient(135deg,var(--rose),var(--rose-lt)); border-radius:16px; padding:1.4rem 1.5rem; color:white; text-align:center; box-shadow:0 4px 20px rgba(192,57,90,0.25); }
.stat-tile.gold { background:linear-gradient(135deg,#B8860B,var(--gold)); }
.stat-tile.dark { background:linear-gradient(135deg,#1C1C2E,#3D1A30); }
.stat-tile .num   { font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:700; display:block; }
.stat-tile .label { font-size:0.82rem; opacity:0.88; letter-spacing:0.04em; text-transform:uppercase; }

/* ── Section headers ── */
.section-header { font-family:'Playfair Display',serif; font-size:1.9rem; font-weight:700; color:var(--charcoal); margin-bottom:0.2rem; }
.section-sub    { color:var(--muted); font-size:0.95rem; margin-bottom:1.5rem; }
.gold-line      { width:50px; height:4px; background:linear-gradient(90deg,var(--rose),var(--gold)); border-radius:2px; margin:0.4rem 0 1.2rem 0; }

/* ── About ── */
.about-hero { background:linear-gradient(135deg,#1C1C2E 0%,#3D1A30 100%); border-radius:20px; padding:3rem; color:white; margin-bottom:2rem; box-shadow:var(--shadow-lg); }
.about-hero h2 { font-family:'Playfair Display',serif; font-size:2.4rem; color:var(--gold-lt); margin:0 0 0.8rem 0; }
.about-hero p  { font-size:1.05rem; color:rgba(253,246,238,0.82); line-height:1.8; max-width:700px; }
.team-card { background:var(--white); border-radius:16px; padding:1.5rem; text-align:center; box-shadow:var(--shadow); border-bottom:4px solid var(--gold); }
.team-card .avatar { font-size:2.8rem; margin-bottom:0.6rem; }
.team-card h4 { font-family:'Playfair Display',serif; color:var(--charcoal); margin:0; font-size:1.05rem; }
.team-card .role { font-size:0.82rem; color:var(--muted); margin:0.2rem 0 0.6rem 0; }
.team-card p  { font-size:0.84rem; color:var(--muted); line-height:1.55; margin:0; }
.value-pill { display:inline-block; background:linear-gradient(135deg,var(--rose),var(--rose-lt)); color:white; border-radius:50px; padding:0.5rem 1.3rem; font-size:0.88rem; font-weight:600; margin:0.3rem; }

/* ── Back to Dashboard button (secondary/ghost style) ── */
[data-testid="stButton"] button[kind="secondary"],
div[data-testid="stButton"]:has(button[key="back_from_log"]) button,
div[data-testid="stButton"]:has(button[key="back_from_about"]) button {
    background: transparent !important;
    color: var(--rose) !important;
    border: 1.5px solid var(--rose) !important;
    border-radius: 50px !important;
    padding: 0.4rem 1.2rem !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    box-shadow: none !important;
    letter-spacing: 0.02em !important;
    margin-bottom: 1rem !important;
}
div[data-testid="stButton"]:has(button[key="back_from_log"]) button:hover,
div[data-testid="stButton"]:has(button[key="back_from_about"]) button:hover {
    background: rgba(192,57,90,0.07) !important;
    transform: translateX(-2px) !important;
}
.stButton > button {
    background:linear-gradient(135deg,var(--rose),var(--rose-lt)) !important;
    color:white !important; border:none !important; border-radius:50px !important;
    padding:0.6rem 2rem !important; font-weight:600 !important; font-size:1rem !important;
    box-shadow:0 4px 16px rgba(192,57,90,0.3) !important;
}
.stDownloadButton > button {
    background:linear-gradient(135deg,#1C1C2E,#3D1A30) !important;
    color:var(--gold-lt) !important;
    border:1.5px solid rgba(212,168,67,0.4) !important;
    border-radius:50px !important; padding:0.6rem 2rem !important;
    font-weight:600 !important; font-size:1rem !important;
}
.stSlider > div > div > div > div { background:var(--rose) !important; }
.stSelectbox > div > div, .stTextArea > div > div, .stTextInput > div > div {
    border-radius:10px !important; border-color:var(--border) !important;
}
/* 1. Unhide the specific container for the expand icon */
header[data-testid="stHeader"] {
    display: block !important;
    background: transparent !important;
    visibility: visible !important;
}

/* 2. Hide everything in the header EXCEPT the sidebar toggle button */
header[data-testid="stHeader"] > div:first-child {
    visibility: hidden !important;
}

/* 3. Specifically target and show the collapse/expand button */
[data-testid="stSidebarCollapseButton"] {
    visibility: visible !important;
    background: rgba(212, 168, 67, 0.15) !important; /* Slight gold tint */
    border: 1px solid #D4A843 !important;
    position: fixed !important;
    top: 15px !important;
    left: 15px !important;
    z-index: 999999 !important;
}

/* 4. Ensure the icon inside the button is Gold so you can see it on the dark background */
[data-testid="stSidebarCollapseButton"] svg {
    fill: #D4A843 !important;
    stroke: #D4A843 !important;
}
     [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "🏠  Home"
if "symptom_logs" not in st.session_state:
    st.session_state.symptom_logs = []
if "forum_posts" not in st.session_state:
    st.session_state.forum_posts = [
        {"alias": "Nneka_A",  "time": "2 hours ago",
         "body": "Has anyone been diagnosed with endometriosis after years of being told period pain is 'normal'? I finally got a laparoscopy — stage III. You are not alone. 🌸",
         "replies": 14, "hearts": 38},
        {"alias": "Amara_O",  "time": "5 hours ago",
         "body": "My doctor dismissed my ovarian cyst pain as anxiety. I switched and got proper imaging within a week. Advocating for yourself is not optional — it is survival.",
         "replies": 22, "hearts": 61},
        {"alias": "Zainab_M", "time": "Yesterday",
         "body": "Has anyone found relief from bloating and pelvic pain through diet changes alone? Anti-inflammatory diets for fibroids?",
         "replies": 9,  "hearts": 27},
        {"alias": "Chisom_E", "time": "2 days ago",
         "body": "Wema Health's resource library has the clearest explanation of PCOS I have ever read. Sharing with every woman in my family. 💛",
         "replies": 5,  "hearts": 44},
    ]


# ─────────────────────────────────────────────
# CLINICAL INTELLIGENCE ENGINE
# ─────────────────────────────────────────────
def generate_triage_report(log: dict) -> dict:
    """Transform a raw symptom log into a structured clinical triage report."""
    pain     = log.get("pain_scale", 1)
    duration = log.get("duration", "Less than 1 day")
    symptoms = log.get("associated", [])
    location = log.get("location", "")

    red_hits    = {"Fever", "Vomiting", "Fainting / Dizziness", "Abnormal bleeding"}.intersection(set(symptoms))
    yellow_hits = {"Nausea", "Bloating", "Back pain"}.intersection(set(symptoms))

    if pain >= 8 or red_hits or duration in ("More than 1 week", "More than 1 month"):
        status  = "RED — Urgent"
        emoji   = "🔴"
        colour  = "red"
        urgency = ("Patient presents with HIGH-SEVERITY symptoms. Immediate clinical evaluation "
                   "strongly recommended. Rule out acute PID, ruptured cyst, or ectopic pregnancy.")
        recs = ("• Arrange same-day or emergency appointment.\n"
                "• Conduct pelvic ultrasound and full blood count.\n"
                "• Gynaecological referral within 24–48 hours.\n"
                "• Patient advised to seek ER care if pain escalates acutely.")
    elif pain >= 5 or yellow_hits or duration in ("2–3 days", "4–7 days"):
        status  = "YELLOW — Monitor"
        emoji   = "🟡"
        colour  = "yellow"
        urgency = ("Patient presents with MODERATE symptoms. Clinical review recommended "
                   "within 48–72 hours. Differential includes endometriosis, ovarian cyst, or fibroids.")
        recs = ("• Schedule gynaecological appointment within 72 hours.\n"
                "• Pelvic ultrasound as first-line imaging.\n"
                "• Advise NSAID management if not contraindicated.\n"
                "• Return if pain escalates above reported level.")
    else:
        status  = "GREEN — Routine"
        emoji   = "🟢"
        colour  = "green"
        urgency = ("Patient presents with MILD symptoms. Routine monitoring advised. "
                   "May represent normal menstrual variation or early hormonal changes.")
        recs = ("• Routine gynaecological check-up at next convenient date.\n"
                "• Continue symptom logging via Wema Health.\n"
                "• Anti-inflammatory diet and stress management recommended.\n"
                "• Re-assess if symptoms persist beyond 14 days or worsen.")

    assoc   = ", ".join(symptoms) if symptoms else "None reported"
    summary = (f"Patient reports pain {pain}/10 localised to the {location} region, "
               f"lasting {duration}. Associated symptoms: {assoc}. {urgency}")

    return {"triage_status": f"{emoji} {status}", "colour": colour,
            "summary": summary, "recommendation": recs, "log": log}


# ─────────────────────────────────────────────
# PDF REPORT GENERATOR
# ─────────────────────────────────────────────
def build_pdf_report(report: dict, log: dict) -> bytes:
    """Build a polished A4 PDF clinical report. Returns bytes."""
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm,  bottomMargin=18*mm)

    ROSE       = colors.HexColor("#C0395A")
    GOLD       = colors.HexColor("#D4A843")
    CHARCOAL   = colors.HexColor("#1C1C2E")
    CREAM_C    = colors.HexColor("#FDF6EE")
    MUTED_C    = colors.HexColor("#6B6B80")
    BORDER_C   = colors.HexColor("#F0E4D4")

    triage_map = {
        "green":  (colors.HexColor("#d4edda"), colors.HexColor("#155724")),
        "yellow": (colors.HexColor("#fff3cd"), colors.HexColor("#856404")),
        "red":    (colors.HexColor("#f8d7da"), colors.HexColor("#721c24")),
    }
    tbg, tfg = triage_map[report["colour"]]

    styles = getSampleStyleSheet()
    title_s  = ParagraphStyle("T", fontSize=22, fontName="Helvetica-Bold",
                               textColor=ROSE,    spaceAfter=2,  alignment=TA_LEFT)
    sub_s    = ParagraphStyle("S", fontSize=9,  fontName="Helvetica",
                               textColor=MUTED_C, spaceAfter=1,  alignment=TA_LEFT)
    label_s  = ParagraphStyle("L", fontSize=7.5, fontName="Helvetica-Bold",
                               textColor=MUTED_C, spaceBefore=10, spaceAfter=3,
                               letterSpacing=1.2, alignment=TA_LEFT)
    body_s   = ParagraphStyle("B", fontSize=10, fontName="Helvetica",
                               textColor=CHARCOAL, leading=15, spaceAfter=4, alignment=TA_LEFT)
    small_s  = ParagraphStyle("D", fontSize=7.5, fontName="Helvetica-Oblique",
                               textColor=MUTED_C, alignment=TA_CENTER)

    story = []

    # Header bar
    hdr = Table([[
        Paragraph("<font color='#C0395A' size='16'><b>Wema Health</b></font>", styles["Normal"]),
        Paragraph("<font color='#B0B0C0' size='8'>Afrocentric Women's Health Navigation</font>", styles["Normal"]),
    ]], colWidths=[90*mm, 80*mm])
    hdr.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CHARCOAL),
        ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (0, -1), 14),  ("RIGHTPADDING", (-1, 0), (-1, -1), 14),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (1, 0), (1, -1), "RIGHT"),
    ]))
    story.extend([hdr, Spacer(1, 12)])

    story.append(Paragraph("Clinical Consultation Report", title_s))
    story.append(HRFlowable(width="100%", thickness=2, color=ROSE, spaceAfter=4))
    ts = log.get("timestamp", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    story.append(Paragraph(
        f"Generated: {ts}  |  Menstrual phase: {log.get('menstrual_phase','N/A')}", sub_s))
    story.append(Spacer(1, 10))

    # Triage box
    tbl = Table([[Paragraph(f"<b>TRIAGE STATUS: {report['triage_status']}</b>",
        ParagraphStyle("TS", fontSize=12, fontName="Helvetica-Bold",
                       textColor=tfg, alignment=TA_CENTER))]],
        colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), tbg),
        ("TOPPADDING", (0,0), (-1,-1), 12), ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ]))
    story.extend([tbl, Spacer(1, 14)])

    # Symptom table
    story.append(Paragraph("SYMPTOM SUMMARY", label_s))
    assoc = ", ".join(log.get("associated", [])) or "None reported"
    rows = [
        ("Pain Intensity",      f"{log.get('pain_scale','—')}/10"),
        ("Anatomical Location", log.get("location","—")),
        ("Duration",            log.get("duration","—")),
        ("Associated Symptoms", assoc),
        ("Menstrual Phase",     log.get("menstrual_phase","—")),
    ]
    sym = Table([[Paragraph(f"<b>{r[0]}</b>", body_s), Paragraph(r[1], body_s)] for r in rows],
                colWidths=[60*mm, 110*mm])
    sym.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [CREAM_C, colors.white]),
        ("GRID", (0,0), (-1,-1), 0.4, BORDER_C),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
    ]))
    story.extend([sym, Spacer(1, 14)])

    # Summary
    story.append(Paragraph("CLINICAL SUMMARY", label_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER_C, spaceAfter=6))
    story.append(Paragraph(report["summary"], body_s))
    story.append(Spacer(1, 12))

    # Recommendations
    story.append(Paragraph("RECOMMENDED ACTIONS", label_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER_C, spaceAfter=6))
    for line in report["recommendation"].strip().split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), body_s))
    story.append(Spacer(1, 12))

    # Patient notes
    notes = log.get("notes", "").strip()
    if notes:
        story.append(Paragraph("PATIENT NOTES", label_s))
        story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER_C, spaceAfter=6))
        story.append(Paragraph(notes, body_s))
        story.append(Spacer(1, 12))

    story.extend([
        Spacer(1, 20),
        HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=8),
        Paragraph(
            "This report is generated by the Wema Health digital navigation platform for "
            "informational purposes only. It is not a medical diagnosis. Always consult a "
            "qualified and licensed healthcare provider. Wema Health © 2026.",
            small_s),
    ])

    doc.build(story)
    return buf.getvalue()


# ─────────────────────────────────────────────
# TREND DATA
# ─────────────────────────────────────────────
def make_trend_data() -> pd.DataFrame:
    """Return a plausible 30-day symptom intensity DataFrame."""
    np.random.seed(42)
    dates   = pd.date_range(end=datetime.date.today(), periods=30)
    pain    = np.clip(np.random.normal(4.5, 1.5, 30).cumsum() % 9 + 1, 1, 10).round(1)
    bloat   = np.clip(np.random.normal(3,   1.2, 30), 1, 10).round(1)
    fatigue = np.clip(np.random.normal(5,   1.4, 30), 1, 10).round(1)
    return pd.DataFrame({"Pelvic Pain": pain, "Bloating": bloat, "Fatigue": fatigue},
                        index=dates)


# ─────────────────────────────────────────────
# NAVIGATION HELPER
# ─────────────────────────────────────────────
def nav_to(target: str):
    """Switch page via session state and rerun."""
    st.session_state.page = target
    st.rerun()


NAV_OPTIONS = [
    "🏠  Home",
    "📋  Log Symptoms",
    "🩺  My Reports",
    "💬  Community Forum",
    "📚  Resource Library",
    "ℹ️  About Wema",
]

# Pages that belong to each collapsible group
NAV_GROUPS = {
    "main": ["🏠  Home", "ℹ️  About Wema"],
    "symptoms": ["📋  Log Symptoms", "🩺  My Reports"],
    "community": ["💬  Community Forum"],
    "library": ["📚  Resource Library"],
}


# ─────────────────────────────────────────────
# SIDEBAR — grouped collapsible navigation
# ─────────────────────────────────────────────
with st.sidebar:

    # ── Brand header ──
    st.markdown("""
    <div style='text-align:center; padding:1.4rem 0 0.8rem 0;'>
        <div style='font-size:2.2rem; margin-bottom:0.2rem;'>🌸</div>
        <div style='font-family:"Playfair Display",serif; font-size:1.6rem;
                    color:#F0C96A; font-weight:700; letter-spacing:0.03em;
                    line-height:1.1;'>
            Wema Health
        </div>
        <div style='font-size:0.7rem; color:rgba(253,246,238,0.42);
                    letter-spacing:0.1em; text-transform:uppercase;
                    margin-top:0.3rem;'>
            Women's Health Navigation
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin:0.5rem 0 0.8rem 0;'>", unsafe_allow_html=True)

    cur = st.session_state.page  # shorthand

    # ── Helper: render a nav button that sets page on click ──
    def _nav_btn(label: str, key: str):
        is_active = (cur == label)
        cls = "sidebar-nav-btn active" if is_active else "sidebar-nav-btn"
        # Use a real st.button but override its look via CSS target
        clicked = st.button(label, key=key, use_container_width=True)
        if clicked:
            st.session_state.page = label
            st.rerun()

    # ── GROUP 1: Main ──
    with st.expander("🏠  Main", expanded=(cur in NAV_GROUPS["main"])):
        _nav_btn("🏠  Home",        key="nav_home")
        _nav_btn("ℹ️  About Wema",  key="nav_about")

    # ── GROUP 2: Symptom Tools ──
    with st.expander("📋  Log Symptoms", expanded=(cur in NAV_GROUPS["symptoms"])):
        st.markdown("""
        <div style='font-size:0.78rem; color:rgba(253,246,238,0.45);
                    line-height:1.6; padding:0.3rem 0.2rem 0.5rem 0.2rem;'>
            Track your pain, duration &amp; associated symptoms.
            Generate a clinical triage report &amp; PDF for your doctor.
        </div>
        """, unsafe_allow_html=True)
        _nav_btn("📋  Log Symptoms", key="nav_log")
        _nav_btn("🩺  My Reports",   key="nav_reports")

    # ── GROUP 3: Support Groups ──
    with st.expander("🤝  Support Groups", expanded=(cur in NAV_GROUPS["community"])):
        st.markdown("""
        <div style='font-size:0.78rem; color:rgba(253,246,238,0.45);
                    line-height:1.6; padding:0.3rem 0.2rem 0.5rem 0.2rem;'>
            Connect anonymously with women who share your experience.
            Ask questions, share stories, offer encouragement.
        </div>
        """, unsafe_allow_html=True)
        _nav_btn("💬  Community Forum", key="nav_forum")
        # Sub-group tags shown as decorative chips
        st.markdown("""
        <div style='margin-top:0.4rem; line-height:2.2;'>
            <span style='background:rgba(192,57,90,0.22);color:#F0C96A;
                         border-radius:50px;padding:0.18rem 0.65rem;
                         font-size:0.72rem;margin-right:0.3rem;'>
                #endometriosis
            </span>
            <span style='background:rgba(192,57,90,0.22);color:#F0C96A;
                         border-radius:50px;padding:0.18rem 0.65rem;
                         font-size:0.72rem;margin-right:0.3rem;'>
                #fibroids
            </span>
            <span style='background:rgba(192,57,90,0.22);color:#F0C96A;
                         border-radius:50px;padding:0.18rem 0.65rem;
                         font-size:0.72rem;margin-right:0.3rem;'>
                #PCOS
            </span>
            <span style='background:rgba(192,57,90,0.22);color:#F0C96A;
                         border-radius:50px;padding:0.18rem 0.65rem;
                         font-size:0.72rem;'>
                #fertility
            </span>
        </div>
        """, unsafe_allow_html=True)

    # ── GROUP 4: Health Library ──
    with st.expander("📚  Health Library", expanded=(cur in NAV_GROUPS["library"])):
        st.markdown("""
        <div style='font-size:0.78rem; color:rgba(253,246,238,0.45);
                    line-height:1.6; padding:0.3rem 0.2rem 0.5rem 0.2rem;'>
            Learn about women's health conditions —
            endometriosis, PCOS, fibroids, PID and more.
        </div>
        """, unsafe_allow_html=True)
        _nav_btn("📚  Resource Library", key="nav_library")
        # Condition quick-links (decorative — all route to library)
        conditions = [
            ("🔴", "Endometriosis"),
            ("🟡", "Ovarian Cysts"),
            ("🟠", "Fibroids"),
            ("🟣", "PCOS"),
            ("🔵", "PID"),
        ]
        for dot, name in conditions:
            col_a, col_b = st.columns([1, 6])
            with col_a:
                st.markdown(f"<div style='font-size:0.7rem;padding-top:0.35rem;'>{dot}</div>",
                            unsafe_allow_html=True)
            with col_b:
                if st.button(name, key=f"cond_{name}", use_container_width=True):
                    st.session_state.page = "📚  Resource Library"
                    st.session_state.library_search = name
                    st.rerun()

    st.markdown("<hr style='margin:0.9rem 0 0.6rem 0;'>", unsafe_allow_html=True)

    # ── Quick Facts ──
    st.markdown("""
    <div style='padding:0 0.3rem;'>
        <div style='font-size:0.7rem; color:rgba(253,246,238,0.38);
                    letter-spacing:0.07em; text-transform:uppercase;
                    margin-bottom:0.5rem;'>
            Did You Know?
        </div>
        <div style='font-size:0.82rem; color:rgba(253,246,238,0.65); line-height:2.1;'>
            🌍 &nbsp;1 in 10 women — endometriosis<br>
            🌸 &nbsp;~20% have fibroids by age 35<br>
            💛 &nbsp;PCOS affects ~13% globally<br>
            ❤️ &nbsp;70% receive a late diagnosis<br>
            🩺 &nbsp;Avg endo diagnosis: 7–10 yrs
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin:0.7rem 0 0.5rem 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center; font-size:0.68rem;
                color:rgba(253,246,238,0.25); padding-bottom:0.6rem;'>
        © 2025 Wema Health · Built with 💛<br>For demo purposes only
    </div>
    """, unsafe_allow_html=True)

# Active page (read after sidebar interaction)
page = st.session_state.page

# Pre-fill library search if routed from sidebar condition chips
if "library_search" not in st.session_state:
    st.session_state.library_search = ""


# ══════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════
if page == "🏠  Home":

    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">🌸 Afrocentric Women's Health · Powered by AI</div>
        <div class="hero-title">
            Your health story<br><span class="hero-accent">deserves to be heard.</span>
        </div>
        <div class="hero-sub">
            Wema Health bridges the gap between African women and quality healthcare —
            through intelligent symptom navigation, clinical reporting, and a community
            built on sisterhood.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA Buttons — real Streamlit buttons styled to match the hero
    b1, b2, _spacer = st.columns([2, 2, 8])
    with b1:
        if st.button("📋  Log Your Symptoms →", key="hero_log"):
            nav_to("📋  Log Symptoms")
    with b2:
        if st.button("ℹ️  Learn More About Wema", key="hero_about"):
            nav_to("ℹ️  About Wema")

    st.markdown("<br>", unsafe_allow_html=True)

    # Stats
    c1, c2, c3, c4 = st.columns(4)
    for col, num, label, cls in [
        (c1, "2,400+", "Women Supported",            ""),
        (c2, "94%",    "Report Better Consultations", "gold"),
        (c3, "3 min",  "Average Log Time",            "dark"),
        (c4, "12+",    "Conditions Tracked",          ""),
    ]:
        with col:
            st.markdown(f"<div class='stat-tile {cls}'>"
                        f"<span class='num'>{num}</span>"
                        f"<span class='label'>{label}</span></div>",
                        unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How It Works
    st.markdown("""
    <div class='section-header'>How It Works</div>
    <div class='gold-line'></div>
    <div class='section-sub'>From symptom to consultation report in under five minutes.</div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    steps = [
        ("📝","1","Log Your Symptoms",
         "Record pain, location, duration, and associated symptoms using our guided form."),
        ("🧠","2","AI Triage Engine",
         "Our clinical logic engine analyses your inputs and generates a structured triage report."),
        ("🩺","3","Doctor-Ready PDF",
         "Download a formatted PDF consultation summary your doctor can act on immediately."),
        ("🤝","4","Community & Learn",
         "Connect anonymously with other women and access curated health education resources."),
    ]
    for col, (icon, num, title, desc) in zip(cols, steps):
        with col:
            st.markdown(f"<div class='step-card'><div class='step-icon'>{icon}</div>"
                        f"<div class='step-num'>{num}</div><h4>{title}</h4><p>{desc}</p></div>",
                        unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Trend chart
    st.markdown("""
    <div class='section-header'>Symptom Intelligence Dashboard</div>
    <div class='gold-line'></div>
    <div class='section-sub'>Visualise your 30-day symptom trends to share with your care team.</div>
    """, unsafe_allow_html=True)
    st.line_chart(make_trend_data(), height=280, use_container_width=True)
    st.markdown("<div style='font-size:0.82rem;color:#6B6B80;margin-top:-0.5rem;text-align:center;'>"
                "📊 Sample 30-day trend — log daily for personalised insights</div><br>",
                unsafe_allow_html=True)

    # Mission
    st.markdown("""
    <div class='wema-card'>
        <h3>Our Mission</h3>
        <p style='font-size:1rem;line-height:1.8;color:#1C1C2E;'>
            African women are <strong>3× more likely</strong> to have their pain dismissed.
            <em>Wema</em> — meaning <strong>"good" in Swahili</strong> — reflects our commitment
            to good health, good data, and good outcomes for every woman we serve.<br><br>
            We translate lived experience into clinical language — so no woman ever has to leave
            a doctor's office feeling unheard again.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PAGE: LOG SYMPTOMS
# ══════════════════════════════════════════════
elif page == "📋  Log Symptoms":

    # ── Back to Dashboard ──
    back_col, _ = st.columns([2, 10])
    with back_col:
        if st.button("← Back to Dashboard", key="back_from_log"):
            nav_to("🏠  Home")

    st.markdown("""
    <div class='section-header'>Symptom Log</div>
    <div class='gold-line'></div>
    <div class='section-sub'>Complete the form below to generate your clinical triage report and downloadable PDF.</div>
    """, unsafe_allow_html=True)

    with st.form("symptom_form", clear_on_submit=False):
        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("#### 📍 Location & Severity")
            location = st.selectbox("Anatomical Location", [
                "Lower abdomen / pelvis", "Upper abdomen", "Lower back",
                "Entire abdomen", "Right side / ovarian", "Left side / ovarian",
                "Vaginal / vulvar", "Rectum / bowel region", "Bladder / urinary region",
            ])
            pain_scale = st.slider("Pain Intensity (1 = mild, 10 = unbearable)",
                                   min_value=1, max_value=10, value=4)
            duration = st.selectbox("Duration of symptoms", [
                "Less than 1 day", "1 day", "2–3 days",
                "4–7 days", "More than 1 week", "More than 1 month",
            ])

        with col_b:
            st.markdown("#### 🩺 Associated Symptoms")
            associated = st.multiselect("Select all that apply", [
                "Fever", "Nausea", "Vomiting", "Bloating", "Back pain",
                "Painful urination", "Painful bowel movements",
                "Fainting / Dizziness", "Abnormal bleeding",
                "Pain during intercourse", "Shoulder tip pain", "Fatigue / Exhaustion",
            ])
            menstrual_phase = st.selectbox("Current Menstrual Phase", [
                "During period", "Before period (luteal phase)",
                "Mid-cycle (ovulation)", "After period (follicular)",
                "Not applicable / unsure",
            ])
            notes = st.text_area("Additional notes (optional)",
                                 placeholder="Describe anything else your doctor should know…",
                                 height=110)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔍  Generate Clinical Report")

    if submitted:
        log_entry = {
            "timestamp":       datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "location":        location, "pain_scale": pain_scale,
            "duration":        duration, "associated": associated,
            "menstrual_phase": menstrual_phase, "notes": notes,
        }
        st.session_state.symptom_logs.append(log_entry)
        report = generate_triage_report(log_entry)

        badge_map = {
            "red":    f"<span class='badge-red'>{report['triage_status']}</span>",
            "yellow": f"<span class='badge-yellow'>{report['triage_status']}</span>",
            "green":  f"<span class='badge-green'>{report['triage_status']}</span>",
        }

        st.markdown("---")
        st.markdown("### 📄 Clinical Triage Report")
        st.markdown(f"""
        <div class="report-box">
            <div class="report-title">Wema Health — Consultation Summary</div>
            <div class="report-meta">Generated: {log_entry['timestamp']} &nbsp;|&nbsp; Phase: {menstrual_phase}</div>
            <div class="report-section">
                <strong>Triage Status</strong>{badge_map[report['colour']]}
            </div>
            <div class="report-section">
                <strong>Clinical Summary</strong><p>{report['summary']}</p>
            </div>
            <div class="report-section">
                <strong>Recommended Actions</strong>
                <p style='white-space:pre-line;'>{report['recommendation']}</p>
            </div>
            {'<div class="report-section"><strong>Patient Notes</strong><p>' + notes + '</p></div>' if notes else ''}
            <div style='margin-top:1rem;font-size:0.75rem;color:#9999aa;'>
                ⚠️ Informational only. Always consult a qualified healthcare provider.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if report["colour"] == "red":
            st.error("⚠️ Urgent symptoms detected. Please contact a healthcare provider today "
                     "or visit your nearest emergency facility.")
        elif report["colour"] == "yellow":
            st.warning("📅 Recommend booking a doctor's appointment within 72 hours.")
        else:
            st.success("✅ Symptoms appear mild. Continue logging and schedule a routine check-up.")

        # PDF download
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 📥 Download Your Doctor's Report")
        pdf_bytes = build_pdf_report(report, log_entry)
        fname = ("Wema_Report_"
                 + log_entry["timestamp"].replace(":", "-").replace(" ", "_")
                 + ".pdf")
        st.download_button(
            label="⬇️  Download PDF Report",
            data=pdf_bytes,
            file_name=fname,
            mime="application/pdf",
            help="A formatted A4 clinical PDF ready to share with your doctor",
        )


# ══════════════════════════════════════════════
# PAGE: MY REPORTS
# ══════════════════════════════════════════════
elif page == "🩺  My Reports":

    st.markdown("""
    <div class='section-header'>My Health Reports</div>
    <div class='gold-line'></div>
    <div class='section-sub'>Your symptom history and 30-day trend analysis.</div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📈 30-Day Symptom Trend")
    st.line_chart(make_trend_data(), height=260, use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### 🗂️ Logged Symptom History (This Session)")
    if not st.session_state.symptom_logs:
        st.info("No symptoms logged yet. Head to **📋 Log Symptoms** to create your first entry.")
    else:
        for i, log in enumerate(reversed(st.session_state.symptom_logs)):
            report  = generate_triage_report(log)
            badge   = {"red":    "<span class='badge-red'>🔴 Urgent</span>",
                       "yellow": "<span class='badge-yellow'>🟡 Monitor</span>",
                       "green":  "<span class='badge-green'>🟢 Routine</span>"}[report["colour"]]
            num     = len(st.session_state.symptom_logs) - i

            with st.expander(f"Log #{num}  |  {log['timestamp']}  |  "
                             f"Pain: {log['pain_scale']}/10  |  {log['location']}"):
                st.markdown(
                    f"<div style='display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:0.8rem;'>"
                    f"<div>Triage: {badge}</div>"
                    f"<div style='color:#6B6B80;'>Duration: {log['duration']}</div>"
                    f"<div style='color:#6B6B80;'>Phase: {log['menstrual_phase']}</div></div>",
                    unsafe_allow_html=True,
                )
                if log.get("associated"):
                    st.markdown(f"**Associated symptoms:** {', '.join(log['associated'])}")
                if log.get("notes"):
                    st.markdown(f"**Notes:** {log['notes']}")
                st.markdown(f"**Recommendations:**\n\n{report['recommendation']}")
                st.download_button(
                    label="⬇️  Download PDF Report",
                    data=build_pdf_report(report, log),
                    file_name=f"Wema_Report_Log_{num}.pdf",
                    mime="application/pdf",
                    key=f"pdf_{i}",
                )


# ══════════════════════════════════════════════
# PAGE: COMMUNITY FORUM
# ══════════════════════════════════════════════
elif page == "💬  Community Forum":

    st.markdown("""
    <div class='section-header'>Community Forum</div>
    <div class='gold-line'></div>
    <div class='section-sub'>A safe, anonymous space to share, ask, and support. You are never alone. 🌸</div>
    """, unsafe_allow_html=True)

    with st.expander("✍️  Share something with the community (anonymous)", expanded=False):
        new_post = st.text_area("Your message",
                                placeholder="Ask a question, share your experience, or offer encouragement…",
                                height=110, label_visibility="collapsed")
        if st.button("Post Anonymously"):
            if new_post.strip():
                aliases = ["Adaeze_U","Folake_B","Yemi_C","Ngozi_D","Amaka_F",
                           "Kemi_P","Temi_R","Bisi_S","Chidinma_T","Obiageli_W"]
                st.session_state.forum_posts.insert(0, {
                    "alias": random.choice(aliases), "time": "Just now",
                    "body": new_post.strip(), "replies": 0, "hearts": 1,
                })
                st.success("✅ Your message has been shared anonymously.")
            else:
                st.warning("Please write something before posting.")

    st.markdown("<br>", unsafe_allow_html=True)
    for post in st.session_state.forum_posts:
        st.markdown(f"""
        <div class="forum-post">
            <span class="anon-tag">Anonymous</span>
            <span class="time-tag">{post['time']}</span>
            <div class="post-body">{post['body']}</div>
            <div class="reactions">💬 {post['replies']} replies &nbsp;&nbsp; 🤍 {post['hearts']} hearts &nbsp;&nbsp; 🔗 Share</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='text-align:center;color:#9999aa;font-size:0.8rem;margin-top:1.5rem;'>"
                "🔒 All posts are fully anonymous. Moderated for safety and kindness.</div>",
                unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PAGE: RESOURCE LIBRARY
# ══════════════════════════════════════════════
elif page == "📚  Resource Library":

    st.markdown("""
    <div class='section-header'>Resource Library</div>
    <div class='gold-line'></div>
    <div class='section-sub'>Evidence-based education written for and by African women.</div>
    """, unsafe_allow_html=True)

    RESOURCES = [
        {"title": "Understanding Endometriosis",
         "tags": ["Endometriosis","Chronic Pain","Fertility"],
         "summary": "Affects ~1 in 10 women globally yet takes 7–10 years to diagnose on average. "
                    "Symptoms include severe pelvic pain, painful periods, and infertility.",
         "detail": ("**Missed in Black women:** Significantly underdiagnosed due to systemic biases — "
                    "pain is routinely dismissed as 'normal'.\n\n"
                    "**Treatments:** Hormonal therapy, laparoscopic surgery, anti-inflammatory diet.\n\n"
                    "**When to act:** Any pelvic pain that disrupts daily life deserves investigation.")},
        {"title": "Ovarian Cysts: What You Need to Know",
         "tags": ["Ovarian Cysts","Hormones","Ultrasound"],
         "summary": "Most are functional and self-resolving. Complex or persistent cysts require monitoring.",
         "detail": ("**Types:** Follicular, corpus luteum, dermoid, endometriomas (chocolate cysts), PCOS.\n\n"
                    "**Symptoms:** Pelvic pain, bloating, pain during intercourse or exercise.\n\n"
                    "**Red flag:** Sudden severe pain + fever = possible rupture or torsion. Seek emergency care.")},
        {"title": "Uterine Fibroids & African Women",
         "tags": ["Fibroids","Uterus","African Women"],
         "summary": "African-descent women are 2–3× more likely to develop fibroids, younger, with worse symptoms.",
         "detail": ("**Why the disparity?** Genetics, Vitamin D deficiency, estrogen sensitivity, "
                    "systemic underdiagnosis.\n\n"
                    "**Treatment:** Watchful waiting, medication, uterine fibroid embolisation, or surgery.")},
        {"title": "PCOS: Polycystic Ovary Syndrome",
         "tags": ["PCOS","Hormones","Insulin Resistance"],
         "summary": "The most common endocrine condition in reproductive-age women — affects ~13% globally.",
         "detail": ("**Symptoms:** Irregular periods, acne, excess hair, weight changes, fertility challenges.\n\n"
                    "**Lean PCOS:** Many Black women with PCOS are not overweight and are frequently misdiagnosed.\n\n"
                    "**Management:** Low-GI diet, exercise, metformin, or hormonal therapy.")},
        {"title": "Pelvic Inflammatory Disease (PID)",
         "tags": ["PID","Infection","Fertility"],
         "summary": "Infection of the reproductive organs — untreated PID is a leading cause of infertility.",
         "detail": ("**Symptoms:** Lower abdominal pain, unusual discharge, fever, pain during intercourse.\n\n"
                    "**Treatment:** Antibiotics — early treatment dramatically reduces long-term complications.")},
    ]

    # Pre-fill from sidebar condition chip click
    default_search = st.session_state.get("library_search", "")
    search = st.text_input("🔍  Search resources",
                           value=default_search,
                           placeholder="e.g. fibroid, PCOS, pain…")
    # Clear the pre-fill after using it so it doesn't persist forever
    if default_search:
        st.session_state.library_search = ""

    filtered = [r for r in RESOURCES if not search
                or search.lower() in r["title"].lower()
                or any(search.lower() in t.lower() for t in r["tags"])
                or search.lower() in r["summary"].lower()]

    if not filtered:
        st.info("No resources match your search. Try a different term.")
    for res in filtered:
        tag_html = "".join(f"<span class='tag'>{t}</span>" for t in res["tags"])
        auto_open = bool(search and (
            search.lower() in res["title"].lower()
            or any(search.lower() in t.lower() for t in res["tags"])
        ))
        with st.expander(f"📖  {res['title']}", expanded=auto_open):
            st.markdown(f"<div class='resource-card'><h4>{res['title']}</h4>"
                        f"{tag_html}<p>{res['summary']}</p></div>",
                        unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(res["detail"])
            st.markdown("<div style='font-size:0.78rem;color:#9999aa;margin-top:0.5rem;'>"
                        "📌 Sourced from WHO, NICE, and peer-reviewed gynaecological literature. "
                        "Always consult your healthcare provider.</div>",
                        unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PAGE: ABOUT WEMA
# ══════════════════════════════════════════════
elif page == "ℹ️  About Wema":

    # ── Back to Dashboard ──
    back_col, _ = st.columns([2, 10])
    with back_col:
        if st.button("← Back to Dashboard", key="back_from_about"):
            nav_to("🏠  Home")

    st.markdown("""
    <div class="about-hero">
        <h2>About Wema Health</h2>
        <p>
            <em>Wema</em> means <strong>"good"</strong> in Swahili — and that is exactly what we are
            building: good health access, good clinical data, and good outcomes for every African woman
            navigating a healthcare system that was not designed with her in mind.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # The Problem
    st.markdown("<div class='section-header'>The Problem We're Solving</div>"
                "<div class='gold-line'></div>", unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)
    for col, icon, title, desc in [
        (p1, "😔", "Pain Dismissed",
         "African women are 3× more likely to have chronic pelvic pain dismissed as 'normal' or stress-related."),
        (p2, "⏳", "Diagnostic Delay",
         "Average time from first symptom to endometriosis diagnosis: 7–10 years. Often longer for Black women."),
        (p3, "📋", "No Clinical Voice",
         "Women arrive at consultations without structured data. Decisions are made on incomplete, verbal accounts."),
    ]:
        with col:
            st.markdown(f"<div class='wema-card' style='border-top:4px solid var(--rose);'>"
                        f"<div style='font-size:2rem;'>{icon}</div>"
                        f"<h3 style='font-size:1.05rem;margin:0.5rem 0 0.4rem;'>{title}</h3>"
                        f"<p style='font-size:0.88rem;color:#6B6B80;line-height:1.6;margin:0;'>{desc}</p></div>",
                        unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How Wema Helps
    st.markdown("<div class='section-header'>How Wema Health Helps</div>"
                "<div class='gold-line'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='wema-card'>
        <p style='font-size:1rem;line-height:1.9;color:#1C1C2E;'>
            Wema Health is a <strong>women's health navigation platform</strong> that transforms
            subjective symptom experiences into structured, clinical-grade documentation — in under
            five minutes.<br><br>
            Our <strong>Clinical Intelligence Engine</strong> analyses pain intensity, symptom patterns,
            and menstrual context to produce a colour-coded triage report (Green / Yellow / Red) a doctor
            can act on immediately — and a <strong>downloadable A4 PDF</strong> ready to take to any
            consultation.<br><br>
            The <strong>Symptom Trend Dashboard</strong> gives clinicians a 30-day longitudinal view of
            a patient's health trajectory — turning anecdote into evidence.<br><br>
            Our <strong>Community Forum</strong> provides anonymous peer support, reducing isolation and
            increasing health-seeking behaviour. Our <strong>Resource Library</strong> delivers culturally
            contextualised education addressing how conditions like fibroids and PCOS disproportionately
            affect women of African descent.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Values
    st.markdown("<div class='section-header'>Our Core Values</div>"
                "<div class='gold-line'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <span class='value-pill'>🌍 Equity</span>
        <span class='value-pill'>🔬 Evidence</span>
        <span class='value-pill'>🤝 Sisterhood</span>
        <span class='value-pill'>🔒 Privacy First</span>
        <span class='value-pill'>💛 Dignity</span>
        <span class='value-pill'>📊 Data-Driven</span>
    </div>
    """, unsafe_allow_html=True)

    # Team
    st.markdown("<div class='section-header'>The Team</div>"
                "<div class='gold-line'></div>", unsafe_allow_html=True)
    t1, t2, t3, t4 = st.columns(4)
    team = [
        ("👩🏾‍⚕️","Dr. Amaka Osei",  "Chief Medical Officer",
         "Gynaecologist with 12 years of experience in reproductive health across West Africa."),
        ("👩🏿‍💻","Zainab Musa",      "CTO & Co-Founder",
         "Full-stack engineer and health-tech innovator. Former senior engineer at a leading telehealth startup."),
        ("👩🏽‍🎨","Chisom Eze",       "Head of Design",
         "UX designer specialising in accessible, culturally-informed health interfaces."),
        ("👩🏾‍💼","Folake Adeyemi",   "CEO & Co-Founder",
         "Public health advocate and serial entrepreneur on a mission to close the health equity gap."),
    ]
    for col, (av, name, role, bio) in zip([t1, t2, t3, t4], team):
        with col:
            st.markdown(f"<div class='team-card'><div class='avatar'>{av}</div>"
                        f"<h4>{name}</h4><div class='role'>{role}</div><p>{bio}</p></div>",
                        unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Traction & Roadmap
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("""
        <div class='wema-card'>
            <h3>Traction & Milestones</h3>
            <ul style='line-height:2.2;font-size:0.95rem;color:#1C1C2E;'>
                <li>✅ MVP built and demo-ready</li>
                <li>✅ 2,400+ women onboarded (beta)</li>
                <li>✅ Clinical Intelligence Engine validated</li>
                <li>✅ Partnerships with 3 women's clinics in Lagos</li>
                <li>🔄 IRB ethics approval in progress</li>
                <li>🎯 Seed round target: $500K</li>
            </ul>
        </div>""", unsafe_allow_html=True)
    with r2:
        st.markdown("""
        <div class='wema-card'>
            <h3>Roadmap 2025–2026</h3>
            <ul style='line-height:2.2;font-size:0.95rem;color:#1C1C2E;'>
                <li>📱 Native iOS & Android apps</li>
                <li>🩺 Direct clinic & GP integration</li>
                <li>🤖 LLM-powered symptom analysis</li>
                <li>🌍 Expand to 5 African countries</li>
                <li>📊 Population-level health insights API</li>
                <li>💊 Medication & appointment reminders</li>
            </ul>
        </div>""", unsafe_allow_html=True)

    # Contact
    st.markdown("""
    <div class='wema-card' style='text-align:center;background:linear-gradient(135deg,#1C1C2E,#3D1A30);border:none;'>
        <h3 style='color:#F0C96A;'>Get Involved</h3>
        <p style='color:rgba(253,246,238,0.78);font-size:1rem;line-height:1.8;'>
            Are you a clinician, investor, or health advocate who believes in what we're building?<br>
            <strong style='color:#F0C96A;'>hello@wemahealth.com</strong>
            &nbsp;|&nbsp;
            <strong style='color:#F0C96A;'>@WemaHealth</strong> on LinkedIn & X
        </p>
    </div>
    """, unsafe_allow_html=True)