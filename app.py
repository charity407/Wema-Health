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
}
#MainMenu, footer, header { visibility: hidden; }
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
[data-testid="stSidebar"] .streamlit-expanderContent {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(212,168,67,0.1) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
    padding: 0.4rem 0.5rem 0.6rem 0.5rem !important;
    margin-bottom: 0.5rem !important;
}

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

.wema-card {
    background:var(--white); border-radius:16px; padding:1.6rem 1.8rem;
    box-shadow:var(--shadow); border:1px solid var(--border); margin-bottom:1.2rem;
}
.wema-card h3 { font-family:'Playfair Display',serif; color:var(--rose); margin-top:0; }

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

.badge-green  { background:#d4edda; color:#155724; padding:0.35rem 1.1rem; border-radius:50px; font-weight:600; font-size:0.9rem; border:1.5px solid #c3e6cb; display:inline-block; }
.badge-yellow { background:#fff3cd; color:#856404; padding:0.35rem 1.1rem; border-radius:50px; font-weight:600; font-size:0.9rem; border:1.5px solid #ffeeba; display:inline-block; }
.badge-red    { background:#f8d7da; color:#721c24; padding:0.35rem 1.1rem; border-radius:50px; font-weight:600; font-size:0.9rem; border:1.5px solid #f5c6cb; display:inline-block; }

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

.forum-post {
    background:var(--white); border-radius:14px; padding:1.2rem 1.5rem;
    margin-bottom:1rem; box-shadow:var(--shadow); border-left:4px solid var(--gold);
}
.forum-post .anon-tag { background:var(--rose); color:white; border-radius:50px; padding:0.15rem 0.7rem; font-size:0.75rem; font-weight:600; margin-right:0.5rem; }
.forum-post .time-tag { color:var(--muted); font-size:0.78rem; }
.forum-post .post-body { margin:0.65rem 0 0.5rem 0; font-size:0.95rem; line-height:1.6; color:var(--charcoal); }
.forum-post .reactions { font-size:0.82rem; color:var(--muted); }

.resource-card { background:var(--white); border-radius:16px; padding:1.6rem; box-shadow:var(--shadow); border-top:4px solid var(--gold); margin-bottom:1rem; }
.resource-card h4 { font-family:'Playfair Display',serif; font-size:1.2rem; color:var(--charcoal); margin:0 0 0.5rem 0; }
.resource-card .tag { background:#FDF0D8; color:#8B5E00; border-radius:50px; padding:0.2rem 0.7rem; font-size:0.75rem; font-weight:600; margin-right:0.4rem; display:inline-block; margin-bottom:0.6rem; }
.resource-card p { font-size:0.9rem; line-height:1.65; color:var(--muted); margin:0; }

.stat-tile { background:linear-gradient(135deg,var(--rose),var(--rose-lt)); border-radius:16px; padding:1.4rem 1.5rem; color:white; text-align:center; box-shadow:0 4px 20px rgba(192,57,90,0.25); }
.stat-tile.gold { background:linear-gradient(135deg,#B8860B,var(--gold)); }
.stat-tile.dark { background:linear-gradient(135deg,#1C1C2E,#3D1A30); }
.stat-tile .num   { font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:700; display:block; }
.stat-tile .label { font-size:0.82rem; opacity:0.88; letter-spacing:0.04em; text-transform:uppercase; }

.section-header { font-family:'Playfair Display',serif; font-size:1.9rem; font-weight:700; color:var(--charcoal); margin-bottom:0.2rem; }
.section-sub    { color:var(--muted); font-size:0.95rem; margin-bottom:1.5rem; }
.gold-line      { width:50px; height:4px; background:linear-gradient(90deg,var(--rose),var(--gold)); border-radius:2px; margin:0.4rem 0 1.2rem 0; }

.about-hero { background:linear-gradient(135deg,#1C1C2E 0%,#3D1A30 100%); border-radius:20px; padding:3rem; color:white; margin-bottom:2rem; box-shadow:var(--shadow-lg); }
.about-hero h2 { font-family:'Playfair Display',serif; font-size:2.4rem; color:var(--gold-lt); margin:0 0 0.8rem 0; }
.about-hero p  { font-size:1.05rem; color:rgba(253,246,238,0.82); line-height:1.8; max-width:700px; }
.team-card { background:var(--white); border-radius:16px; padding:1.5rem; text-align:center; box-shadow:var(--shadow); border-bottom:4px solid var(--gold); }
.team-card .avatar { font-size:2.8rem; margin-bottom:0.6rem; }
.team-card h4 { font-family:'Playfair Display',serif; color:var(--charcoal); margin:0; font-size:1.05rem; }
.team-card .role { font-size:0.82rem; color:var(--muted); margin:0.2rem 0 0.6rem 0; }
.team-card p  { font-size:0.84rem; color:var(--muted); line-height:1.55; margin:0; }
.value-pill { display:inline-block; background:linear-gradient(135deg,var(--rose),var(--rose-lt)); color:white; border-radius:50px; padding:0.5rem 1.3rem; font-size:0.88rem; font-weight:600; margin:0.3rem; }

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
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "🏠  Home"
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
    pain      = log.get("pain_scale", 1)
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

    tbl = Table([[Paragraph(f"<b>TRIAGE STATUS: {report['triage_status']}</b>",
        ParagraphStyle("TS", fontSize=12, fontName="Helvetica-Bold",
                       textColor=tfg, alignment=TA_CENTER))]],
        colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), tbg),
        ("TOPPADDING", (0,0), (-1,-1), 12), ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ]))
    story.extend([tbl, Spacer(1, 14)])

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

    story.append(Paragraph("CLINICAL SUMMARY", label_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER_C, spaceAfter=6))
    story.append(Paragraph(report["summary"], body_s))
    story.append(Spacer(1, 12))

    story.append(Paragraph("RECOMMENDED ACTIONS", label_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER_C, spaceAfter=6))
    for line in report["recommendation"].strip().split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), body_s))
    story.append(Spacer(1, 12))

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
            "qualified and licensed healthcare provider. Wema Health © 2025.",
            small_s),
    ])

    doc.build(story)
    return buf.getvalue()


# ─────────────────────────────────────────────
# TREND DATA & NAV CALLBACK
# ─────────────────────────────────────────────
def make_trend_data() -> pd.DataFrame:
    np.random.seed(42)
    dates   = pd.date_range(end=datetime.date.today(), periods=30)
    pain    = np.clip(np.random.normal(4.5, 1.5, 30).cumsum() % 9 + 1, 1, 10).round(1)
    bloat   = np.clip(np.random.normal(3,   1.2, 30), 1, 10).round(1)
    fatigue = np.clip(np.random.normal(5,   1.4, 30), 1, 10).round(1)
    return pd.DataFrame({"Pelvic Pain": pain, "Bloating": bloat, "Fatigue": fatigue},
                        index=dates)

def nav_to(target: str):
    st.session_state.page = target
    # No st.rerun() here - callbacks handle it instantly

NAV_GROUPS = {
    "main": ["🏠  Home", "ℹ️  About Wema"],
    "symptoms": ["📋  Log Symptoms", "🩺  My Reports"],
    "community": ["💬  Community Forum"],
    "library": ["📚  Resource Library"],
}


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
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

    cur = st.session_state.page

    with st.expander("🏠  Main", expanded=(cur in NAV_GROUPS["main"])):
        # Callbacks ensure no hard reset is needed
        st.button("🏠  Home", on_click=nav_to, args=("🏠  Home",), width="stretch", key="nav_home")
        st.button("ℹ️  About Wema", on_click=nav_to, args=("ℹ️  About Wema",), width="stretch", key="nav_about")

    with st.expander("📋  Log Symptoms", expanded=(cur in NAV_GROUPS["symptoms"])):
        st.markdown("<div style='font-size:0.78rem; color:rgba(253,246,238,0.45); padding:0.3rem 0.2rem 0.5rem 0.2rem;'>Track symptoms & generate reports.</div>", unsafe_allow_html=True)
        st.button("📋  Log Symptoms", on_click=nav_to, args=("📋  Log Symptoms",), width="stretch", key="nav_log")
        st.button("🩺  My Reports", on_click=nav_to, args=("🩺  My Reports",), width="stretch", key="nav_reports")

    with st.expander("🤝  Support Groups", expanded=(cur in NAV_GROUPS["community"])):
        st.button("💬  Community Forum", on_click=nav_to, args=("💬  Community Forum",), width="stretch", key="nav_forum")

    with st.expander("📚  Health Library", expanded=(cur in NAV_GROUPS["library"])):
        st.button("📚  Resource Library", on_click=nav_to, args=("📚  Resource Library",), width="stretch", key="nav_library")

    st.markdown("<hr style='margin:0.9rem 0 0.6rem 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style='padding:0 0.3rem;'>
        <div style='font-size:0.7rem; color:rgba(253,246,238,0.38); letter-spacing:0.07em; text-transform:uppercase; margin-bottom:0.5rem;'>Did You Know?</div>
        <div style='font-size:0.82rem; color:rgba(253,246,238,0.65); line-height:2.1;'>
            🌍 &nbsp;1 in 10 women — endometriosis<br>
            🌸 &nbsp;~20% have fibroids by age 35<br>
            🩺 &nbsp;Avg endo diagnosis: 7–10 yrs
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main Container to ensure clean DOM rendering
main_content = st.container()

# Pre-fill library search
if "library_search" not in st.session_state:
    st.session_state.library_search = ""

# ─────────────────────────────────────────────
# PAGE ROUTING
# ─────────────────────────────────────────────
with main_content:
    page = st.session_state.page

    if page == "🏠  Home":
        st.markdown("""
        <div class="hero-section">
            <div class="hero-badge">🌸 Afrocentric Women's Health · Powered by AI</div>
            <div class="hero-title">Your health story<br><span class="hero-accent">deserves to be heard.</span></div>
            <div class="hero-sub">Wema Health bridges the gap between African women and quality healthcare.</div>
        </div>
        """, unsafe_allow_html=True)

        b1, b2, _ = st.columns([2, 2, 8])
        with b1:
            st.button("📋  Log Your Symptoms →", on_click=nav_to, args=("📋  Log Symptoms",), key="h_log")
        with b2:
            st.button("ℹ️  Learn More About Wema", on_click=nav_to, args=("ℹ️  About Wema",), key="h_about")

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        for col, num, lbl, cls in [(c1, "2,400+", "Women Supported", ""), (c2, "94%", "Better Consults", "gold"), (c3, "3 min", "Avg Log Time", "dark"), (c4, "12+", "Conditions", "")]:
            with col:
                st.markdown(f"<div class='stat-tile {cls}'><span class='num'>{num}</span><span class='label'>{lbl}</span></div>", unsafe_allow_html=True)

        st.markdown("<br><div class='section-header'>Symptom Intelligence Dashboard</div><div class='gold-line'></div>", unsafe_allow_html=True)
        st.line_chart(make_trend_data(), height=280, width="stretch")

    elif page == "📋  Log Symptoms":
        st.markdown("<div class='section-header'>Symptom Log</div><div class='gold-line'></div>", unsafe_allow_html=True)
        with st.form("symptom_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                location = st.selectbox("Anatomical Location", ["Lower abdomen / pelvis", "Upper abdomen", "Lower back", "Entire abdomen", "Right side / ovarian", "Left side / ovarian", "Vaginal / vulvar", "Rectum / bowel region", "Bladder / urinary region"])
                pain_scale = st.slider("Pain Intensity", 1, 10, 4)
                duration = st.selectbox("Duration", ["Less than 1 day", "1 day", "2–3 days", "4–7 days", "More than 1 week", "More than 1 month"])
            with col_b:
                associated = st.multiselect("Associated Symptoms", ["Fever", "Nausea", "Vomiting", "Bloating", "Back pain", "Painful urination", "Painful bowel movements", "Fainting / Dizziness", "Abnormal bleeding", "Pain during intercourse", "Shoulder tip pain", "Fatigue / Exhaustion"])
                menstrual_phase = st.selectbox("Current Menstrual Phase", ["During period", "Before period (luteal phase)", "Mid-cycle (ovulation)", "After period (follicular)", "Not applicable / unsure"])
                notes = st.text_area("Notes", height=110)
            
            submitted = st.form_submit_button("🔍  Generate Clinical Report")

        if submitted:
            log_entry = {"timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "location": location, "pain_scale": pain_scale, "duration": duration, "associated": associated, "menstrual_phase": menstrual_phase, "notes": notes}
            st.session_state.symptom_logs.append(log_entry)
            report = generate_triage_report(log_entry)
            st.markdown(f"""<div class="report-box"><div class="report-title">Wema Health Summary</div><div class="report-section"><strong>Clinical Summary</strong><p>{report['summary']}</p></div></div>""", unsafe_allow_html=True)
            pdf_bytes = build_pdf_report(report, log_entry)
            st.download_button("⬇️  Download PDF Report", data=pdf_bytes, file_name="Wema_Report.pdf", mime="application/pdf")

    elif page == "🩺  My Reports":
        st.markdown("<div class='section-header'>My Health Reports</div><div class='gold-line'></div>", unsafe_allow_html=True)
        st.line_chart(make_trend_data(), height=260, width="stretch")
        if not st.session_state.symptom_logs:
            st.info("No logs found.")
        else:
            for i, log in enumerate(reversed(st.session_state.symptom_logs)):
                with st.expander(f"Log #{len(st.session_state.symptom_logs)-i} | {log['timestamp']}"):
                    st.write(log)

    elif page == "💬  Community Forum":
        st.markdown("<div class='section-header'>Community Forum</div><div class='gold-line'></div>", unsafe_allow_html=True)
        for post in st.session_state.forum_posts:
            st.markdown(f"""<div class="forum-post"><span class="anon-tag">Anonymous</span><div class="post-body">{post['body']}</div></div>""", unsafe_allow_html=True)

    elif page == "📚  Resource Library":
        st.markdown("<div class='section-header'>Resource Library</div><div class='gold-line'></div>", unsafe_allow_html=True)
        st.info("Curated condition guides for African women.")

    elif page == "ℹ️  About Wema":
        st.markdown("<div class='about-hero'><h2>About Wema Health</h2></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'>Our Core Values</div><div class='gold-line'></div>", unsafe_allow_html=True)
        st.markdown("<span class='value-pill'>🌍 Equity</span><span class='value-pill'>🔬 Evidence</span><span class='value-pill'>🤝 Sisterhood</span>", unsafe_allow_html=True)