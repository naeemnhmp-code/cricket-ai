
import streamlit as st

st.set_page_config(
    page_title="Cricket AI | T20 Intelligence",
    page_icon="🏏",
    layout="wide"
)

# THEME
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

# COLOURS
theme_choice = st.radio(
    "Appearance",
    ["🌙 Dark", "☀️ Light"],
    horizontal=True,
    index=0 if st.session_state.theme == "Dark" else 1
)
st.session_state.theme = "Dark" if "Dark" in theme_choice else "Light"

if st.session_state.theme == "Dark":
    bg, panel = "#0B1422", "#17263A"
    fg, muted = "#F1F5F9", "#A9B8CC"
    accent, border = "#28D99A", "#304158"
else:
    bg, panel = "#F2F6FB", "#FFFFFF"
    fg, muted = "#17263A", "#64748B"
    accent, border = "#087D58", "#D7E0EA"

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg};
    color: {fg};
}}
[data-testid="stHeader"] {{
    background-color: {bg};
}}
h1,h2,h3,p,label,span {{
    color: {fg};
}}
div[data-testid="stMetric"] {{
    background: {panel};
    border: 1px solid {border};
    border-radius: 14px;
    padding: 16px;
}}
div[data-testid="stMetricValue"] {{
    color: {accent};
}}
div.stTabs [data-baseweb="tab-list"] {{
    gap: 8px;
    border-bottom: 2px solid {border};
}}
div.stTabs [data-baseweb="tab"] {{
    background: {panel};
    border-radius: 9px 9px 0 0;
    padding: 12px 15px;
    font-weight: 600;
}}
div.stTabs [aria-selected="true"] {{
    border-bottom: 3px solid {accent};
}}
.cricket-card {{
    background: {panel};
    border: 1px solid {border};
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
}}
.small {{
    color: {muted};
    font-size: 13px;
}}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown(
    f"<h1 style='font-size:38px'>🏏 CRICKET AI</h1>",
    unsafe_allow_html=True
)
st.markdown(
    f"<p class='small'>T20 INTELLIGENCE • LIVE MATCHES • AI PREDICTIONS</p>",
    unsafe_allow_html=True
)

st.divider()

# SIX MAIN NAVIGATION TABS
home, live, predictions, score, teams, history = st.tabs([
    "🏠 Home",
    "📡 Live Matches",
    "🧠 AI Predictions",
    "🎯 Score Predictor",
    "👥 Team Analytics",
    "📊 Match History"
])

# HOME
with home:
    st.title("Cricket Intelligence Centre")
    st.caption("Your central destination for T20 cricket intelligence.")

    a, b, c = st.columns(3)
    a.metric("Historical Matches", "9,181")
    b.metric("Ball-by-ball Records", "2.1M+")
    c.metric("AI Engine", "In Development")

    st.markdown("## 🏟️ Your Match Centre")

    st.markdown("""
    <div class="cricket-card">
        <h2>Welcome to Cricket AI</h2>
        <p class="small">
        Discover live matches, analyse team performance,
        explore historical T20 data and access AI predictions.
        </p>
        <h3>Intelligence Beyond the Scoreboard 🏏</h3>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Live match discovery and automatic score collection "
        "will be activated after connecting verified live data sources."
    )

    st.markdown("### Explore the platform")
    st.write("Select any of the six tabs above to explore its section.")

# LIVE MATCHES
with live:
    st.title("📡 Live Match Centre")
    st.caption("Find and select ongoing T20 matches.")

    st.warning(
        "Live data connection is not active yet. "
        "No sample fixtures are being presented as real live matches."
    )

    st.markdown("### Upcoming development")
    st.write("- Automatic discovery of ongoing T20 matches")
    st.write("- Multiple live score sources")
    st.write("- Match selection by tournament and teams")
    st.write("- Automatic score and timestamp updates")
    st.write("- Feed freshness and connection warnings")

# AI PREDICTIONS
with predictions:
    st.title("🧠 AI Prediction Centre")

    st.info(
        "Predictions will become available after the trained "
        "models and live match data are connected."
    )

    st.markdown("### Prediction modules")
    st.write("- Pre-match winner probability")
    st.write("- Toss-adjusted winner probability")
    st.write("- First innings final score prediction")
    st.write("- Second innings chase probability")
    st.write("- Match outcome probability distribution")
    st.write("- Prediction confidence and model accuracy")

# SCORE PREDICTOR
with score:
    st.title("🎯 T20 Final Score Predictor")

    st.markdown("""
    <div class="cricket-card">
        <h3>Automatic match-based prediction</h3>
        <p class="small">
        Select an ongoing match. Cricket AI will retrieve its
        current score and estimate the final 20-over total.
        You will not need to enter runs, wickets or overs manually.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.warning(
        "Automatic match selection will be activated "
        "when the live score feed is integrated."
    )

    st.markdown("### Planned prediction output")
    st.write("- Expected final score")
    st.write("- Likely score range")
    st.write("- Conservative and aggressive estimates")
    st.write("- Projected scores at 10, 15 and 20 overs")
    st.write("- Expected runs in the remaining overs")

# TEAM ANALYTICS
with teams:
    st.title("👥 Team & Player Analytics")

    team = st.selectbox(
        "Explore a team",
        [
            "Pakistan", "India", "Australia", "England",
            "South Africa", "New Zealand", "Sri Lanka",
            "West Indies", "Bangladesh"
        ]
    )

    st.subheader(f"{team} Analytics Centre")

    st.info(
        "Team and player statistics will be connected "
        "to the historical database."
    )

    st.write("- Recent team form")
    st.write("- Batting and bowling strength")
    st.write("- Player versus player matchups")
    st.write("- Powerplay and death-over records")
    st.write("- Venue-specific performance")

# MATCH HISTORY
with history:
    st.title("📊 Historical T20 Database")

    st.metric("Matches collected", "9,181")
    st.metric("Ball-by-ball records", "2,109,308")

    st.caption("Database coverage: February 2005 – November 2026")

    st.info(
        "The historical database will be connected "
        "for detailed match and player analysis."
    )

    st.write("- Tournament and season filters")
    st.write("- Team and opponent records")
    st.write("- Venue statistics")
    st.write("- Innings and over-by-over analysis")

# FOOTER
st.divider()
st.markdown(
    "<p style='text-align:center'>🏏 CRICKET AI | "
    "INTELLIGENCE BEYOND THE SCOREBOARD</p>",
    unsafe_allow_html=True
)
