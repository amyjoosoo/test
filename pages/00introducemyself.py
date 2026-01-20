import streamlit as st

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="AMY J | 소개",
    page_icon="✨",
    layout="wide",
)

# ----------------------------
# Data (여기만 바꾸면 됨)
# ----------------------------
NAME = "AMY J"
HEADLINE = "문제를 끝까지 해결하는 사람"
ONE_LINER = "기획-실행-개선까지 연결되는 흐름을 만들고, 사용자 경험을 더 단단하게 다듬습니다."

LOCATION = "Seoul, KR (Remote OK)"
EMAIL = "your.email@example.com"  # TODO: 본인 이메일로 변경

LINKS = {
    "GitHub": "https://github.com/your-id",          # TODO
    "LinkedIn": "https://www.linkedin.com/in/your-id",  # TODO
    "Portfolio": "https://your-portfolio.example.com",  # TODO
}

TAGS = ["Product", "UX", "Data", "Automation", "AI", "Frontend"]

ABOUT = [
    "안녕하세요, AMY J입니다.",
    "저는 사용자에게 가치 있는 경험을 만들기 위해 문제를 구조화하고, 실행 가능한 계획으로 바꾸며, 결과를 측정하고 개선하는 과정을 좋아합니다.",
    "불명확한 요구사항을 목표/지표/우선순위로 정리하고, 빠르게 실험해 반복 개선하는 편입니다.",
]

PROJECTS = [
    {
        "title": "프로젝트 A — 사용자 이탈 감소",
        "period": "2025",
        "summary": "온보딩 플로우를 재설계하고 간단한 실험으로 이탈 지점을 줄였습니다.",
        "highlights": ["핵심 단계 단순화", "마이크로카피 개선", "지표 대시보드 정리"],
        "link": "",
    },
    {
        "title": "프로젝트 B — 업무 자동화",
        "period": "2024",
        "summary": "반복 업무를 자동화해 운영 시간을 절감했습니다.",
        "highlights": ["API 연동", "알림/리포트 자동 생성", "예외/오류 처리"],
        "link": "",
    },
]

EXPERIENCE = [
    {
        "role": "Role / Title",
        "company": "Company Name",
        "period": "2023 — Present",
        "bullets": [
            "주요 지표 개선을 위한 실험 설계 및 실행",
            "유관부서 협업 및 요구사항 조율",
            "문서화/프로세스 정비로 운영 효율화",
        ],
    },
    {
        "role": "Role / Title",
        "company": "Company Name",
        "period": "2021 — 2023",
        "bullets": [
            "사용자 피드백 기반 기능 개선",
            "데이터 리포트/대시보드 운영 지원",
        ],
    },
]

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("✨ " + NAME)
page = st.sidebar.radio("메뉴", ["Home", "About", "Projects", "Experience", "Contact"], index=0)

st.sidebar.markdown("---")
st.sidebar.caption("커스터마이징: app.py 상단의 데이터만 바꾸면 됩니다.")

# ----------------------------
# Pages
# ----------------------------
if page == "Home":
    col1, col2 = st.columns([1.5, 1.0], gap="large")

    with col1:
        st.title(NAME)
        st.subheader(HEADLINE)
        st.write(ONE_LINER)

        st.write("")
        st.markdown("### Tags")
        st.write(" · ".join(TAGS))

        st.write("")
        st.markdown("### Quick Summary")
        st.info("문제 구조화 → 실행 → 측정 → 개선 흐름을 만드는 데 강점이 있습니다.")

        st.write("")
        st.markdown("### Featured Projects")
        for p in PROJECTS:
            with st.container(border=True):
                st.subheader(p["title"])
                st.caption(p["period"])
                st.write(p["summary"])
                if p["highlights"]:
                    st.write(" / ".join(p["highlights"]))
                if p.get("link"):
                    st.link_button("Open", p["link"])

    with col2:
        st.markdown("### Info")
        st.write("📍 " + LOCATION)
        st.write("✉️ " + EMAIL)

        st.write("")
        st.markdown("### Links")
        for k, v in LINKS.items():
            if v:
                st.link_button(k, v)

elif page == "About":
    st.title("About")
    for line in ABOUT:
        st.write("- " + line)

elif page == "Projects":
    st.title("Projects")
    for p in PROJECTS:
        with st.container(border=True):
            st.subheader(p["title"])
            st.caption(p["period"])
            st.write(p["summary"])
            if p["highlights"]:
                st.markdown("**Highlights**")
                for h in p["highlights"]:
                    st.write("• " + h)
            if p.get("link"):
                st.link_button("Open", p["link"])

elif page == "Experience":
    st.title("Experience")
    for e in EXPERIENCE:
        with st.container(border=True):
            st.subheader(e["role"] + " — " + e["company"])
            st.caption(e["period"])
            for b in e["bullets"]:
                st.write("• " + b)

elif page == "Contact":
    st.title("Contact")
    st.write("✉️ Email: **" + EMAIL + "**")

    st.write("")
    st.markdown("### Message (데모 폼)")
    with st.form("contact_form", clear_on_submit=True):
        your_name = st.text_input("Your name")
        your_email = st.text_input("Your email")
        msg = st.text_area("Message", height=140)
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not your_name or not your_email or not msg:
            st.error("이름/이메일/메시지를 모두 입력해 주세요.")
        else:
            st.success("입력 완료! (이 폼은 데모라 실제 전송은 하지 않습니다.)")

st.markdown("---")
st.caption("© " + NAME + " · Built with Streamlit")
