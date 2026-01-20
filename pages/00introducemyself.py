import streamlit as st
from datetime import date

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="AMY J | Self Intro",
    page_icon="✨",
    layout="wide",
)

# -----------------------------
# Simple theming (CSS)
# -----------------------------
st.markdown(
    """
    <style>
      .hero {
        padding: 22px 26px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.12);
        background: linear-gradient(135deg, rgba(255,255,255,0.10), rgba(255,255,255,0.03));
      }
      .pill {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        margin: 4px 6px 0 0;
        border: 1px solid rgba(255,255,255,0.14);
        background: rgba(255,255,255,0.06);
        font-size: 0.9rem;
      }
      .card {
        padding: 16px 18px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.12);
        background: rgba(255,255,255,0.04);
        height: 100%;
      }
      .muted {opacity: 0.85;}
      a {text-decoration: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Data (편하게 여기만 수정해도 됨)
# -----------------------------
PROFILE = {
    "name": "AMY J",
    "headline": "문제를 ‘끝까지’ 해결하는 사람",
    "one_liner": "기획-실행-개선까지 연결되는 흐름을 만들고, 사용자 경험을 더 단단하게 다듬습니다.",
    "location": "Seoul, KR (Remote OK)",
    "email": "your.email@example.com",  # TODO: 변경
    "links": {
        "GitHub": "https://github.com/your-id",         # TODO: 변경
        "LinkedIn": "https://www.linkedin.com/in/your-id",  # TODO: 변경
        "Portfolio": "https://your-portfolio.example.com",  # TODO: 변경
    },
    "tags": ["Product", "UX", "Data", "Automation", "AI", "Frontend"],
}

ABOUT = """
안녕하세요, **AMY J**입니다.  
저는 *사용자에게 가치 있는 경험*을 만들기 위해 문제를 구조화하고, 실행 가능한 계획으로 바꾸며, 결과를 측정하고 개선하는 과정을 좋아합니다.

- 불명확한 요구사항을 **명확한 목표/지표/우선순위**로 정리합니다.
- 빠르게 실험하고, 데이터/피드백을 기반으로 **반복 개선**합니다.
- 팀과 협업할 때는 문서화와 커뮤니케이션을 통해 **속도와 품질의 균형**을 잡습니다.
""".strip()

SKILLS = {
    "Core": ["Problem Solving", "Communication", "Product Thinking", "UX Writing"],
    "Tech": ["Python", "SQL", "Streamlit", "APIs", "Git"],
    "Tools": ["Notion", "Figma", "GA4", "Looker Studio"],
}

PROJECTS = [
    {
        "title": "프로젝트 A — 사용자 이탈 감소",
        "period": "2025",
        "summary": "온보딩 플로우를 재설계하고 A/B 테스트로 이탈 지점을 줄였습니다.",
        "highlights": ["핵심 단계 단순화", "마이크로카피 개선", "지표 대시보드 구축"],
        "link": "",
    },
    {
        "title": "프로젝트 B — 업무 자동화",
        "period": "2024",
        "summary": "반복 업무를 자동화해 팀 운영 시간을 절감했습니다.",
        "highlights": ["API 연동", "알림/리포트 자동 생성", "오류 케이스 핸들링"],
        "link": "",
    },
    {
        "title": "프로젝트 C — 데이터 기반 의사결정",
        "period": "2024",
        "summary": "지표 정의부터 추적 설계까지 end-to-end로 정리했습니다.",
        "highlights": ["KPI 정의", "이벤트 설계", "리포트 템플릿 표준화"],
        "link": "",
    },
]

EXPERIENCE = [
    {
        "role": "Role / Title",
        "company": "Company Name",
        "period": "2023 — Present",
        "what": [
            "주요 지표 개선을 위한 실험 설계 및 실행",
            "유관부서 협업 및 요구사항 조율",
            "문서화/프로세스 정비로 운영 효율화",
        ],
    },
    {
        "role": "Role / Title",
        "company": "Company Name",
        "period": "2021 — 2023",
        "what": [
            "사용자 리서치 기반 기능 개선",
            "데이터 파이프라인/대시보드 운영 지원",
        ],
    },
]

FAQ = [
    ("어떤 일을 가장 좋아하나요?", "복잡한 문제를 잘게 쪼개서 빠르게 실험하고, 결과를 다시 제품/프로세스에 반영하는 일을 좋아합니다."),
    ("협업 스타일은 어떤가요?", "목표/지표/우선순위를 문서로 정리하고, 합의된 기준으로 빠르게 실행하는 편입니다."),
    ("지금 찾는 기회는?", "사용자 경험과 성과 지표를 함께 개선하는 제품/프로젝트에 관심이 있습니다."),
]

# -----------------------------
# Sidebar navigation
# -----------------------------
st.sidebar.title("✨ AMY J")
page = st.sidebar.radio(
    "Menu",
    ["Home", "About", "Projects", "Experience", "Contact"],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.caption("Customize: app.py 상단의 PROFILE/ABOUT/PROJECTS 등을 수정하세요.")

# -----------------------------
# Helpers
# -----------------------------
def pills(items):
    return "".join([f"<span class='pill'>{st.escape(i)}</span>" for i in items])

def section_title(title, desc=None):
    st.markdown(f"## {title}")
    if desc:
        st.caption(desc)

# -----------------------------
# Pages
# -----------------------------
if page == "Home":
    left, right = st.columns([1.4, 1.0], gap="large")

    with left:
        st.markdown(
            f"""
            <div class="hero">
              <h1 style="margin:0 0 6px 0;">{PROFILE["name"]}</h1>
              <h3 class="muted" style="margin:0 0 12px 0;">{PROFILE["headline"]}</h3>
              <p style="margin:0 0 14px 0; font-size: 1.05rem;">{PROFILE["one_liner"]}</p>
              <div>{pills(PROFILE["tags"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        section_title("Quick Summary")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='card'><b>Strength</b><br/>문제 구조화 → 실행 → 측정 → 개선</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='card'><b>Focus</b><br/>사용자 경험과 성과 지표를 함께 개선</div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='card'><b>Style</b><br/>문서화, 빠른 실험, 협업 중심</div>", unsafe_allow_html=True)

        st.write("")
        section_title("Featured Projects", "대표 프로젝트 3개를 요약했어요.")
        for p in PROJECTS[:3]:
            with st.container(border=True):
                st.subheader(f"{p['title']}  ·  {p['period']}")
                st.write(p["summary"])
                st.write("— " + " / ".join(p["highlights"]))
                if p.get("link"):
                    st.link_button("View", p["link"])

    with right:
        section_title("Info")
        st.write(f"📍 {PROFILE['location']}")
        st.write(f"✉️ {PROFILE['email']}")
        st.write("")
        section_title("Links")
        for k, v in PROFILE["links"].items():
            if v:
                st.link_button(k, v)

        st.write("")
        section_title("Resume (Optional)")
        st.caption("원하면 아래 텍스트를 PDF로 만든 파일을 업로드/연결해도 좋아요.")
        resume_text = f"""AMY J Resume Snapshot ({date.today().isoformat()})

Headline: {PROFILE["headline"]}
Location: {PROFILE["location"]}
Email: {PROFILE["email"]}

Skills:
- Core: {", ".join(SKILLS["Core"])}
- Tech: {", ".join(SKILLS["Tech"])}
- Tools: {", ".join(SKILLS["Tools"])}

Projects:
- {PROJECTS[0]["title"]}: {PROJECTS[0]["summary"]}
- {PROJECTS[1]["title"]}: {PROJECTS[1]["summary"]}
- {PROJECTS[2]["title"]}: {PROJECTS[2]["summary"]}
"""
        st.download_button(
            "Download resume snapshot (txt)",
            data=resume_text.encode("utf-8"),
            file_name="AMYJ_resume_snapshot.txt",
            mime="text/plain",
        )

elif page == "About":
    section_title("About")
    st.markdown(ABOUT)

    st.write("")
    section_title("Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Core")
        for s in SKILLS["Core"]:
            st.write("• " + s)
    with col2:
        st.markdown("### Tech")
        for s in SKILLS["Tech"]:
            st.write("• " + s)
    with col3:
        st.markdown("### Tools")
        for s in SKILLS["Tools"]:
            st.write("• " + s)

    st.write("")
    section_title("FAQ")
    for q, a in FAQ:
        with st.expander(q):
            st.write(a)

elif page == "Projects":
    section_title("Projects", "프로젝트를 카드 형태로 정리했어요.")
    for p in PROJECTS:
        with st.container(border=True):
            top = st.columns([1.2, 0.5])
            with top[0]:
                st.subheader(p["title"])
                st.caption(p["period"])
            with top[1]:
                if p.get("link"):
                    st.link_button("Open", p["link"])

            st.write(p["summary"])
            st.markdown("**Highlights**")
            st.write("\n".join([f"- {h}" for h in p["highlights"]]))

elif page == "Experience":
    section_title("Experience", "경력/역할을 간단히 요약했어요.")
    for e in EXPERIENCE:
        with st.container(border=True):
            st.subheader(f"{e['role']} — {e['company']}")
            st.caption(e["period"])
            for w in e["what"]:
                st.write("• " + w)

elif page == "Contact":
    section_title("Contact", "연락 채널과 간단한 메시지 폼이에요.")
    st.write(f"✉️ Email: **{PROFILE['email']}**")

    st.write("")
    st.markdown("### Send a message")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        msg = st.text_area("Message", height=140)
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not (name and email and msg):
            st.error("이름/이메일/메시지를 모두 입력해 주세요.")
        else:
            st.success("메시지 내용을 확인했습니다! (데모 폼이라 실제 전송은 되지 않아요)")
            st.info("Streamlit Cloud에서 이메일 전송까지 하려면 SMTP 또는 이메일 API(예: SendGrid)를 연동하면 됩니다.")

# Footer
st.markdown("---")
st.caption("© AMY J · Built
