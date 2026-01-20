import streamlit as st
from datetime import datetime
import random

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="✨ MBTI 진로 추천 스튜디오 💼🌈",
    page_icon="🧭",
    layout="wide",
)

# -----------------------
# CSS (화려하게)
# -----------------------
st.markdown("""
<style>
/* 전체 배경 그라데이션 */
.stApp {
  background: radial-gradient(circle at 10% 10%, rgba(255, 0, 128, 0.25), transparent 40%),
              radial-gradient(circle at 90% 20%, rgba(0, 200, 255, 0.22), transparent 40%),
              radial-gradient(circle at 30% 90%, rgba(255, 200, 0, 0.18), transparent 45%),
              linear-gradient(135deg, #0b1020 0%, #140b2d 45%, #061526 100%);
  color: #eaf2ff;
}

/* 기본 텍스트 컬러 */
html, body, [class*="css"]  {
  color: #eaf2ff !important;
}

/* 헤더 글로우 */
.glow-title {
  font-size: 48px;
  font-weight: 900;
  letter-spacing: -1px;
  background: linear-gradient(90deg, #ff4fd8, #59d2ff, #ffe66d, #b6ff7a);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 18px rgba(255, 79, 216, .25),
               0 0 22px rgba(89, 210, 255, .18);
  margin-bottom: 0.2rem;
}
.sub-title {
  font-size: 18px;
  opacity: .9;
  margin-top: 0;
}

/* 카드 */
.card {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.14);
  border-radius: 22px;
  padding: 18px 18px 14px 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.35);
  backdrop-filter: blur(10px);
}

/* 칩(태그) */
.chip {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  margin-right: 8px;
  margin-bottom: 8px;
  font-size: 13px;
  border: 1px solid rgba(255,255,255,0.15);
  background: rgba(255,255,255,0.08);
}

/* 강조 박스 */
.highlight {
  border-left: 6px solid rgba(89, 210, 255, 0.8);
  background: rgba(89, 210, 255, 0.10);
  padding: 14px 16px;
  border-radius: 14px;
}

/* 버튼 느낌 개선 */
.stButton>button {
  border-radius: 14px;
  padding: 0.65rem 1rem;
  font-weight: 800;
  border: 1px solid rgba(255,255,255,0.15);
  background: linear-gradient(90deg, rgba(255,79,216,0.35), rgba(89,210,255,0.25));
  color: #ffffff;
  box-shadow: 0 10px 22px rgba(0,0,0,0.35);
  transition: transform 0.08s ease-in-out;
}
.stButton>button:hover {
  transform: translateY(-1px) scale(1.01);
  border: 1px solid rgba(255,255,255,0.30);
}

/* selectbox, expander 약간 유리 느낌 */
div[data-baseweb="select"] > div {
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
  border-radius: 14px !important;
}
.streamlit-expanderHeader {
  background: rgba(255,255,255,0.06) !important;
  border-radius: 14px !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
}

/* 푸터 */
.footer {
  opacity: 0.7;
  font-size: 13px;
  margin-top: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# DATA
# -----------------------
MBTI_DATA = {
    "INTJ": {
        "nickname": "전략가 🧠♟️",
        "strengths": ["분석력 🔍", "장기 계획 🗺️", "독립성 🧘", "효율 추구 ⚙️"],
        "jobs": [
            ("데이터 사이언티스트 📊", "데이터로 세상을 설계하는 분석가"),
            ("전략 컨설턴트 🧩", "복잡한 문제를 구조화해 해법을 만드는 전문가"),
            ("AI/ML 엔지니어 🤖", "미래 기술을 구현하는 설계자"),
            ("제품 매니저(PM) 🧭", "제품 방향을 설계하고 실행하는 리더"),
        ],
        "fit_env": ["자율성 높은 환경 🧑‍💻", "문제 해결 중심 🔧", "깊이 있는 탐구 📚"],
        "tips": ["포트폴리오를 ‘논리 구조’로 보여주기 🧱", "핵심 가설→검증→결론 흐름 연습 🧪"]
    },
    "INTP": {
        "nickname": "논리 탐험가 🧠🧪",
        "strengths": ["호기심 🧭", "논리적 사고 🧮", "아이디어 발상 💡", "개념화 🧩"],
        "jobs": [
            ("연구원 🔬", "원리를 파고드는 탐구자"),
            ("소프트웨어 엔지니어 💻", "논리를 코드로 구현하는 창작자"),
            ("UX 리서처 🧑‍🔎", "사용자의 진짜 니즈를 발견하는 분석가"),
            ("게임/시뮬레이션 개발자 🎮", "규칙과 세계를 설계하는 메이커"),
        ],
        "fit_env": ["탐구 시간 확보 ⏳", "실험/프로토타입 중심 🧪", "유연한 문화 🌿"],
        "tips": ["아이디어를 ‘작게’ 실험해보기 🧫", "정리/문서화 습관으로 설득력 강화 📝"]
    },
    "ENTJ": {
        "nickname": "지휘관 👑🚀",
        "strengths": ["리더십 🦁", "결단력 ⚡", "목표 지향 🎯", "조직화 🧱"],
        "jobs": [
            ("경영/전략 리더 🏢", "조직을 성장으로 이끄는 리더"),
            ("프로젝트 매니저 📅", "팀을 정렬하고 실행을 밀어붙이는 추진자"),
            ("스타트업 창업가 🚀", "새 판을 짜는 개척자"),
            ("세일즈/비즈니스 개발 🤝", "기회를 발굴하고 확장하는 협상가"),
        ],
        "fit_env": ["성과 중심 🏁", "도전 과제 🔥", "리더십 기회 🌟"],
        "tips": ["듣기/피드백 루프 만들기 👂🔁", "데이터 기반 의사결정 습관 📈"]
    },
    "ENFP": {
        "nickname": "열정 메이커 🌈🔥",
        "strengths": ["창의성 🎨", "공감 🤍", "소통 🗣️", "도전 정신 🧗"],
        "jobs": [
            ("마케터 📣", "사람의 마음을 움직이는 이야기꾼"),
            ("콘텐츠 크리에이터 🎬", "세상을 재밌게 해석하는 제작자"),
            ("교육/코칭 🧑‍🏫", "성장을 돕는 동기부여자"),
            ("브랜드 매니저 🏷️", "브랜드의 성격을 만드는 연출가"),
        ],
        "fit_env": ["자유로운 아이디어 문화 💡", "사람 중심 🤝", "다양한 프로젝트 🧩"],
        "tips": ["아이디어→실행 루틴(체크리스트) 만들기 ✅", "집중 시간 블록으로 산만함 관리 ⏱️"]
    },
    "INFJ": {
        "nickname": "통찰 상담가 🌙🕯️",
        "strengths": ["통찰력 👁️", "공감 🤍", "가치 지향 🌿", "집중력 🎯"],
        "jobs": [
            ("상담사 🧠🤝", "마음과 관계를 돕는 전문가"),
            ("교육 기획자 🧑‍🏫🧩", "배움의 여정을 설계하는 사람"),
            ("작가/에디터 ✍️", "깊은 메시지를 글로 전하는 창작자"),
            ("사회/공공 분야 기획 🌍", "의미 있는 변화를 만드는 설계자"),
        ],
        "fit_env": ["가치/미션 중심 🕊️", "깊은 몰입 🌌", "조용한 협업 🤝"],
        "tips": ["경계를 세우는 연습(에너지 보호) 🛡️", "작은 실천 목표로 번아웃 예방 🌱"]
    },
    "ESTP": {
        "nickname": "현장 해결사 ⚡🧰",
        "strengths": ["순발력 🏃", "실행력 🛠️", "현장 감각 🧭", "대담함 🦅"],
        "jobs": [
            ("세일즈/영업 🧲", "현장에서 기회를 잡는 승부사"),
            ("이벤트/프로덕션 🎤", "현장 운영의 마스터"),
            ("응급/안전/구조 🚑", "즉각적인 판단이 필요한 전문가"),
            ("스포츠/퍼포먼스 코치 🏋️", "몸과 전략을 함께 다루는 지도자"),
        ],
        "fit_env": ["현장 중심 🏟️", "다이나믹한 업무 🌪️", "빠른 피드백 ⚡"],
        "tips": ["장기 목표도 ‘주간 미션’으로 쪼개기 🗓️", "리스크 체크리스트 습관 🧾"]
    },
}

# MBTI 16개 다 채우면 더 좋지만, 일단 예쁘게 동작하는 MVP로 만들고 확장 가능하게 구성
ALL_TYPES = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

DEFAULT_FILL = {
    "nickname": "✨ 멋진 타입 ✨",
    "strengths": ["잠재력 🌟", "성장 가능성 📈", "개성 💎", "학습력 🧠"],
    "jobs": [
        ("직업 탐색가 🧭", "나에게 맞는 길을 실험하며 찾는 사람"),
        ("프로젝트 메이커 🧩", "작은 결과물을 꾸준히 만드는 사람"),
        ("커뮤니케이터 🗣️", "사람과 정보를 연결하는 사람"),
        ("크리에이티브 문제 해결사 🛠️🎨", "새로운 해법을 만들어내는 사람"),
    ],
    "fit_env": ["다양성 🌈", "피드백 문화 🧠", "성장 중심 🌱"],
    "tips": ["한 달에 1개 미니 프로젝트 만들기 🧪", "흥미 분야를 기록하고 패턴 찾기 📝"]
}

# -----------------------
# UI
# -----------------------
st.markdown('<div class="glow-title">✨ MBTI 진로 추천 스튜디오 💼🌈</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">MBTI를 선택하면, 강점에 맞춘 직업 & 학습 팁을 화려하게 추천해줘요! 🎁🧠</div>', unsafe_allow_html=True)
st.write("")

colA, colB = st.columns([1.05, 1], gap="large")

with colA:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 🧭 MBTI 선택하기")
    mbti = st.selectbox("당신의 MBTI는 무엇인가요? ✨", ALL_TYPES, index=ALL_TYPES.index("ENFP"))
    st.markdown("### 🎛️ 추천 스타일")
    vibe = st.radio("어떤 느낌으로 추천 받을래요? 😆", ["밸런스 🌗", "현실 직업 위주 🧱", "꿈/창의 위주 🎨"], horizontal=True)
    st.markdown("### 🧨 오늘의 랜덤 행운 이모지")
    lucky = random.choice(["🍀","🌟","🧿","🦄","💎","🔥","🌈","⚡","🎯","🪄"])
    st.success(f"오늘의 행운: {lucky}  {lucky}  {lucky}")

    if st.button("✨ 추천 결과 보기!"):
        st.session_state["go"] = True
    st.markdown('</div>', unsafe_allow_html=True)

with colB:
    data = MBTI_DATA.get(mbti, DEFAULT_FILL)
    nickname = data["nickname"]
    strengths = data["strengths"]
    jobs = data["jobs"]
    fit_env = data["fit_env"]
    tips = data["tips"]

    if st.session_state.get("go"):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"## {mbti} — {nickname} 💫")
        st.markdown("### 💎 너의 핵심 강점")
        chips = "".join([f'<span class="chip">{s}</span>' for s in strengths])
        st.markdown(chips, unsafe_allow_html=True)

        st.markdown("### 💼 추천 직업 TOP 4")
        # 추천 스타일에 따라 순서를 살짝 바꿔주는 정도의 연출
        if vibe == "현실 직업 위주 🧱":
            jobs_show = jobs[:]  # 그대로
        elif vibe == "꿈/창의 위주 🎨":
            jobs_show = jobs[::-1]
        else:
            jobs_show = jobs

        for (title, desc) in jobs_show:
            st.markdown(f"""
            <div class="highlight">
              <div style="font-size:18px; font-weight:900;">{title}</div>
              <div style="opacity:.9; margin-top:4px;">{desc} ✨</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

        st.markdown("### 🏡 잘 맞는 환경")
        st.write(" / ".join(fit_env))

        st.markdown("### 📚 성장 팁 (교육용)")
        for t in tips:
            st.markdown(f"- {t}")

        with st.expander("🎒 학습 로드맵 추천(샘플) — 클릭해서 펼치기!"):
            st.markdown("""
- 1주차 🗓️: 관심 직업 2개 조사하기(업무/필요 역량/하루 루틴) 🔍  
- 2주차 🧪: 미니 프로젝트 1개 만들기(결과물 남기기) 🧩  
- 3주차 🤝: 현직자/멘토 인터뷰 질문 5개 준비 & 1명에게 메시지 보내기 💬  
- 4주차 🗂️: 포트폴리오 정리 + 다음 달 목표 설정 🎯  
            """)

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("## 👀 아직 결과를 안 눌렀어요!")
        st.markdown("왼쪽에서 **✨ 추천 결과 보기!** 버튼을 눌러줘 😎🎉")
        st.markdown("### 🎇 미리보기")
        st.markdown("- MBTI별 직업 추천 💼")
        st.markdown("- 강점 태그(칩) 💎")
        st.markdown("- 학습 로드맵 🎒")
        st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.markdown(f'<div class="footer">🕰️ {datetime.now().strftime("%Y-%m-%d %H:%M")} · 교육용 데모 · Made with Streamlit 💙</div>', unsafe_allow_html=True)

# 사이드바에 약간의 장식
with st.sidebar:
    st.markdown("## 🪩 메뉴")
    st.markdown("### 🌟 오늘의 미션")
    st.markdown("- 관심 직업 1개 선택 🎯")
    st.markdown("- 필요한 역량 3개 적기 🧠")
    st.markdown("- 이번 주에 할 ‘작은 행동’ 1개 정하기 ✅")
    st.markdown("---")
    st.markdown("### 🎨 꾸미기 팁")
    st.markdown("이 앱은 CSS로 화려하게 꾸몄어요 ✨")
