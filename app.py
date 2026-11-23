import streamlit as st

st.set_page_config(
    page_title="Cricket AI",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGES = [
    ("Home", "🏠"),
    ("Live Matches", "📡"),
    ("AI Predictions", "🧠"),
    ("Score Predictor", "🎯"),
    ("Team Analytics", "👥"),
    ("Match History", "📊"),
]

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

# Theme
theme = st.sidebar.radio(
    "Theme",
    ["Dark", "Light"],
    index=0 if st.session_state.theme == "Dark" else 1,
    horizontal=True,
)
st.session_state.theme = theme

if theme == "Dark":
    bg = "#0E1B2A"
    panel = "#172B40"
    fg = "#F4F7FA"
    muted = "#B8C7D6"
    border = "#30465B"
    tile_bg = "#1A3047"
    button_bg = "#1A3047"
    button_hover = "#24445E"
else:
    bg = "#F4F7FA"
    panel = "#FFFFFF"
    fg = "#172638"
    muted = "#596B7C"
    border = "#D5DFE8"
    tile_bg = "#FFFFFF"
    button_bg = "#FFFFFF"
    button_hover = "#E7F0F6"

st.markdown(
    f"""
    <style>
    .stApp {{ background: {bg}; }}
    [data-testid="stHeader"] {{ background: {bg}; }}
    [data-testid="stSidebar"] {{ background: {panel}; }}
    h1, h2, h3, p, label {{ color: {fg}; }}
    .brandline {{
        color: {muted};
        font-size: 12px;
        letter-spacing: 1.2px;
        margin-top: -12px;
        margin-bottom: 14px;
    }}
    .section-note {{
        color: {muted};
        font-size: 13px;
        margin-top: -8px;
        margin-bottom: 16px;
    }}

    /* Keep the six navigation tiles in a compact 3-by-2 grid on phones. */
    div[data-testid="stHorizontalBlock"] {{
        flex-wrap: nowrap !important;
        gap: 8px !important;
    }}
    div[data-testid="column"] {{
        min-width: 0 !important;
        width: 33.333% !important;
        flex: 1 1 0 !important;
    }}

    /* Each Streamlit button is the tile: no separate card or extra button. */
    div.stButton > button {{
        width: 100%;
        min-height: 94px;
        height: auto;
        white-space: normal !important;
        overflow-wrap: anywhere;
        padding: 12px 4px;
        border-radius: 13px;
        border: 1px solid {border};
        background: {button_bg};
        color: {fg};
        font-size: 13px;
        font-weight: 650;
        line-height: 1.25;
        box-shadow: none;
    }}
    div.stButton > button:hover {{
        border-color: #35A982;
        background: {button_hover};
        color: {fg};
    }}
    div.stButton > button:focus {{
        border-color: #35A982;
        color: {fg};
        box-shadow: 0 0 0 1px #35A982;
    }}
    [data-testid="stMetric"] {{
        background: {panel};
        border: 1px solid {border};
        border-radius: 12px;
        padding: 10px;
    }}

    @media (max-width: 480px) {{
        .block-container {{
            padding-left: 0.65rem !important;
            padding-right: 0.65rem !important;
            padding-top: 0.8rem !important;
        }}
        div[data-testid="stHorizontalBlock"] {{
            gap: 6px !important;
        }}
        div.stButton > button {{
            min-height: 82px;
            padding: 9px 2px;
            font-size: 11px;
            border-radius: 11px;
        }}
        h1 {{ font-size: 1.65rem !important; }}
        h2 {{ font-size: 1.2rem !important; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

def navigate(page):
    st.session_state.page = page
    st.rerun()

# Sidebar has the same destinations as the homepage.
st.sidebar.markdown("## 🏏 CRICKET AI")
st.sidebar.caption("T20 INTELLIGENCE CENTRE")
st.sidebar.divider()
st.sidebar.markdown("### Navigation")
for page, emoji in PAGES:
    if st.sidebar.button(
        f"{emoji}  {page}",
        key=f"sidebar_{page}",
        use_container_width=True,
        type="primary" if st.session_state.page == page else "secondary",
    ):
        navigate(page)

st.sidebar.divider()
st.sidebar.caption("Private testing version")

# Compact brand header
st.markdown("# 🏏 CRICKET AI")
st.markdown(
    '<div class="brandline">INTELLIGENCE BEYOND THE SCOREBOARD</div>',
    unsafe_allow_html=True,
)

def home_page():
    st.markdown("## Cricket Intelligence Centre")
    st.markdown(
        '<div class="section-note">Choose a section to get started.</div>',
        unsafe_allow_html=True,
    )

    # Six clickable tiles: exactly three columns by two rows.
    for start in (0, 3):
        columns = st.columns(3, gap="small")
        for column, (page, emoji) in zip(columns, PAGES[start:start + 3]):
            with column:
                label = f"{emoji}\\n{page}"
                if st.button(
                    label,
                    key=f"home_tile_{page}",
                    use_container_width=True,
                    disabled=(page == "Home"),
                ):
                    navigate(page)

    st.markdown("---")
    st.markdown("### Database at a glance")
    left, right = st.columns(2)
    left.metric("Historical matches", "9,181")
    right.metric("Ball-by-ball records", "2.1M+")

    st.info(
        "Private prototype: live score feeds and validated prediction models "
        "are not connected yet. No live scores or predictions are being invented."
    )

def live_page():
    st.title("📡 Live Matches")
    st.warning(
        "Live score feeds are not connected yet. This section will list real "
        "ongoing T20 matches when a verified provider is integrated."
    )
    st.write("Planned: automatic match discovery, score refresh, source comparison, and update timestamps.")

def predictions_page():
    st.title("🧠 AI Predictions")
    st.info(
        "Predictions will be enabled after the historical model is trained and "
        "evaluated on matches that were not used for training."
    )
    st.write("Planned: pre-match probability, toss-adjusted probability, innings projections, and chase probability.")

def score_page():
    st.title("🎯 Score Predictor")
    st.write(
        "The intended workflow is automatic: select a live match, retrieve its "
        "latest verified score, and calculate the projected final score. "
        "You will not have to type runs, wickets, or overs."
    )
    st.warning("Automatic live match selection is not connected yet.")
    st.write("Every future prediction will show the exact score state and timestamp used.")

def teams_page():
    st.title("👥 Team Analytics")
    team = st.selectbox(
        "Select a team",
        ["Pakistan", "India", "Australia", "England", "South Africa",
         "New Zealand", "Sri Lanka", "West Indies", "Bangladesh"],
    )
    st.subheader(f"{team} analytics")
    st.info("Team and player analytics will be connected to the historical database.")
    st.write("Planned: recent form, batting and bowling strength, player matchups, and venue records.")

def history_page():
    st.title("📊 Match History")
    left, right = st.columns(2)
    left.metric("Matches", "9,181")
    right.metric("Deliveries", "2,109,308")
    st.caption("Current database coverage: 17 February 2005 – 1 November 2026")
    st.info("Historical filters and detailed match analysis will be connected next.")

page = st.session_state.page
if page == "Home":
    home_page()
elif page == "Live Matches":
    live_page()
elif page == "AI Predictions":
    predictions_page()
elif page == "Score Predictor":
    score_page()
elif page == "Team Analytics":
    teams_page()
elif page == "Match History":
    history_page()

st.markdown("---")
st.caption("🏏 CRICKET AI · PRIVATE TESTING PROTOTYPE")
