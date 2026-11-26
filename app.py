
import streamlit as st

st.set_page_config(
    page_title="Cricket AI",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGES = [
    ("🏠 Home", "Home"),
    ("📡 Live Matches", "Live Matches"),
    ("🧠 AI Predictions", "AI Predictions"),
    ("🎯 Score Predictor", "Score Predictor"),
    ("👥 Team Analytics", "Team Analytics"),
    ("📊 Match History", "Match History"),
]

PAGE_LABELS = [label for label, _ in PAGES]
PAGE_BY_LABEL = {label: page for label, page in PAGES}
LABEL_BY_PAGE = {page: label for label, page in PAGES}

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

# SIDEBAR BRANDING
st.sidebar.markdown(
    """
    <div style="padding:12px 0 4px 0">
      <div style="font-size:28px;font-weight:800">
        🏏 CRICKET AI
      </div>
      <div style="font-size:13px;opacity:.72;letter-spacing:1px;margin-top:12px">
        CRICKET INTELLIGENCE PLATFORM
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# THEME SELECTOR
st.sidebar.markdown("### Appearance")
st.sidebar.caption("Choose your theme")

theme = st.sidebar.radio(
    "Choose your theme",
    ["Dark", "Light"],
    index=0 if st.session_state.theme == "Dark" else 1,
    horizontal=True,
    label_visibility="collapsed",
    key="sidebar_theme",
)

st.session_state.theme = theme

# SIDEBAR MAIN MENU
st.sidebar.divider()
st.sidebar.caption("MAIN MENU")

current_label = LABEL_BY_PAGE.get(
    st.session_state.page, "🏠 Home"
)

selected_label = st.sidebar.radio(
    "Main menu",
    PAGE_LABELS,
    index=PAGE_LABELS.index(current_label),
    label_visibility="collapsed",
    key="sidebar_main_menu",
)

selected_page = PAGE_BY_LABEL[selected_label]

if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

st.sidebar.divider()

st.sidebar.markdown(
    """
    <div style="opacity:.7;line-height:2">
      CRICKET AI v1.0<br/>
      Intelligent Cricket Analysis
    </div>
    """,
    unsafe_allow_html=True,
)

# THEME COLOURS
if theme == "Dark":
    bg = "#0E1B2A"
    panel = "#172B40"
    fg = "#F4F7FA"
    muted = "#B8C7D6"
    border = "#30465B"
    tile_bg = "#1A3047"
else:
    bg = "#F4F7FA"
    panel = "#FFFFFF"
    fg = "#172638"
    muted = "#596B7C"
    border = "#D5DFE8"
    tile_bg = "#FFFFFF"

# CUSTOM CSS
st.markdown(
    f"""
    <style>

    .stApp {{
        background: {bg};
    }}

    [data-testid="stHeader"] {{
        background: {bg};
    }}

    [data-testid="stSidebar"] {{
        background: {panel};
    }}

    h1, h2, h3, p, label {{
        color: {fg};
    }}

    .brandline {{
        color: {muted};
        font-size: 12px;
        letter-spacing: 1.2px;
        margin-top: -10px;
        margin-bottom: 16px;
    }}

    .section-note {{
        color: {muted};
        font-size: 13px;
        margin-top: -8px;
        margin-bottom: 14px;
    }}

    /* MOBILE-FRIENDLY THREE-COLUMN GRID */

    .st-key-nav_grid {{
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
    }}

    .st-key-nav_grid [data-testid="stHorizontalBlock"] {{
        display: grid !important;
        grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
        gap: 8px !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
    }}

    .st-key-nav_grid [data-testid="column"] {{
        width: auto !important;
        min-width: 0 !important;
        max-width: 100% !important;
        flex: none !important;
        margin: 0 !important;
    }}

    .st-key-nav_grid [data-testid="column"] > div {{
        width: 100% !important;
        min-width: 0 !important;
    }}

    .st-key-nav_grid div.stButton > button {{
        width: 100% !important;
        min-width: 0 !important;
        min-height: 88px;
        height: 88px;
        padding: 8px 3px;
        white-space: pre-line !important;
        overflow-wrap: anywhere !important;
        border-radius: 12px;
        border: 1px solid {border};
        background: {tile_bg};
        color: {fg} !important;
        font-size: 13px;
        font-weight: 650;
        line-height: 1.35;
        box-shadow: none;
    }}

    .st-key-nav_grid div.stButton > button:hover {{
        border-color: #35A982;
        color: {fg} !important;
    }}

    .st-key-nav_grid div.stButton > button:focus {{
        border-color: #35A982;
        color: {fg} !important;
        box-shadow: 0 0 0 1px #35A982;
    }}

    [data-testid="stMetric"] {{
        background: {panel};
        border: 1px solid {border};
        border-radius: 12px;
        padding: 10px;
    }}

    /* PHONE SCREEN ADJUSTMENTS */

    @media (max-width: 600px) {{

        .block-container {{
            padding-left: .7rem !important;
            padding-right: .7rem !important;
            padding-top: .8rem !important;
        }}

        .st-key-nav_grid [data-testid="stHorizontalBlock"] {{
            grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
            gap: 6px !important;
        }}

        .st-key-nav_grid div.stButton > button {{
            min-height: 76px;
            height: 76px;
            padding: 6px 2px;
            font-size: 11px;
            border-radius: 10px;
        }}

        h1 {{
            font-size: 1.65rem !important;
        }}

        h2 {{
            font-size: 1.2rem !important;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True,
)

# MAIN HEADER
st.markdown("# 🏏 CRICKET AI")

st.markdown(
    '<div class="brandline">INTELLIGENCE BEYOND THE SCOREBOARD</div>',
    unsafe_allow_html=True,
)

def navigate(page):
    st.session_state.page = page
    st.rerun()

# HOME PAGE
def home_page():

    st.markdown("## Cricket Intelligence Centre")

    st.markdown(
        '<div class="section-note">Choose a section to get started.</div>',
        unsafe_allow_html=True,
    )

    # SIX CLICKABLE NAVIGATION TILES
    with st.container(key="nav_grid"):

        for start in (0, 3):

            columns = st.columns(3, gap="small")

            for column, (label, page) in zip(
                columns,
                PAGES[start:start + 3]
            ):

                with column:

                    if st.button(
                        label.replace(" ", "\n", 1),
                        key=f"home_tile_{page}",
                        use_container_width=True,
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

# LIVE MATCHES PAGE
def live_page():

    st.title("📡 Live Matches")

    st.warning(
        "Live score feeds are not connected yet. This section will list real "
        "ongoing T20 matches when a verified provider is integrated."
    )

    st.write(
        "Planned: automatic match discovery, score refresh, "
        "source comparison, and update timestamps."
    )

# AI PREDICTIONS PAGE
def predictions_page():

    st.title("🧠 AI Predictions")

    st.info(
        "Predictions will be enabled after the historical model is trained "
        "and evaluated on matches that were not used for training."
    )

    st.write(
        "Planned: pre-match probability, toss-adjusted probability, "
        "innings projections, and chase probability."
    )

# SCORE PREDICTOR PAGE
def score_page():

    st.title("🎯 Score Predictor")

    st.write(
        "The intended workflow is automatic: select a live match, "
        "retrieve its latest verified score, and calculate the projected "
        "final score. You will not have to type runs, wickets, or overs."
    )

    st.warning(
        "Automatic live match selection is not connected yet."
    )

    st.write(
        "Every future prediction will show the exact score state "
        "and timestamp used."
    )

# TEAM ANALYTICS PAGE
def teams_page():

    st.title("👥 Team Analytics")

    team = st.selectbox(
        "Select a team",
        [
            "Pakistan",
            "India",
            "Australia",
            "England",
            "South Africa",
            "New Zealand",
            "Sri Lanka",
            "West Indies",
            "Bangladesh",
        ],
    )

    st.subheader(f"{team} analytics")

    st.info(
        "Team and player analytics will be connected to the historical database."
    )

    st.write(
        "Planned: recent form, batting and bowling strength, "
        "player matchups, and venue records."
    )

# MATCH HISTORY PAGE
def history_page():

    st.title("📊 Match History")

    left, right = st.columns(2)

    left.metric("Matches", "9,181")
    right.metric("Deliveries", "2,109,308")

    st.caption(
        "Current database coverage: 17 February 2005 – 1 November 2026"
    )

    st.info(
        "Historical filters and detailed match analysis will be connected next."
    )

# PAGE ROUTING
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
# TEMPORARY DATASPORTSAPI CONNECTION TEST
import cricket_api

st.divider()
st.subheader("🔌 DataSportsAPI Connection Test")

if st.button("Test API Connection"):
    try:
        data = cricket_api.get_live_cricket_scores()
        st.success("API request completed!")
        st.json(data)
    except Exception as e:
        st.error(f"API connection failed: {e}")
