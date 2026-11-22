
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cricket AI | Intelligence Centre",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- THEME ----------------

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

st.sidebar.markdown("# 🏏 CRICKET AI")
st.sidebar.caption("CRICKET INTELLIGENCE PLATFORM")

st.sidebar.markdown("### Appearance")
theme = st.sidebar.radio(
    "Choose your theme",
    ["Dark", "Light"],
    index=0 if st.session_state.theme == "Dark" else 1,
    horizontal=True
)
st.session_state.theme = theme

if theme == "Dark":
    bg = "#0B1220"
    panel = "#162235"
    text = "#F1F5F9"
    muted = "#A5B4C7"
    accent = "#36D399"
    border = "#29384D"
else:
    bg = "#F3F6FA"
    panel = "#FFFFFF"
    text = "#142033"
    muted = "#64748B"
    accent = "#07865B"
    border = "#DCE4ED"

st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: {text};
}}
[data-testid="stSidebar"] {{
    background: {panel};
    border-right: 1px solid {border};
}}
h1, h2, h3, p, label {{
    color: {text} !important;
}}
div[data-testid="stMetric"] {{
    background: {panel};
    border: 1px solid {border};
    padding: 17px;
    border-radius: 14px;
}}
div[data-testid="stMetricValue"] {{
    color: {accent};
}}
.cricket-card {{
    background: {panel};
    border: 1px solid {border};
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 12px;
}}
.small-note {{
    color: {muted};
    font-size: 13px;
}}
.stButton button {{
    border-radius: 10px;
    border: 1px solid {accent};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "MAIN MENU",
    [
        "🏠 Home",
        "📡 Live Matches",
        "🧠 AI Predictions",
        "🎯 Score Predictor",
        "👥 Team Analytics",
        "📊 Match History"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("CRICKET AI v1.0")
st.sidebar.caption("Intelligent Cricket Analysis")

# ---------------- HEADER ----------------

st.markdown(
    f"<h1 style='font-size:34px'>🏏 CRICKET AI</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='color:" + muted +
    "'>LIVE CRICKET INTELLIGENCE • ANALYTICS • PREDICTIONS</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- HOME ----------------

if page == "🏠 Home":

    st.title("Cricket Intelligence Centre")
    st.caption("Your central hub for T20 cricket analysis.")

    st.info(
        "DEVELOPMENT MODE — Live score feeds and trained prediction "
        "models will be connected in upcoming stages."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Historical Matches", "9,181")

    with c2:
        st.metric("Historical Deliveries", "2.1M+")

    with c3:
        st.metric("Prediction Engine", "In Development")

    st.markdown("## 🏟️ Match Centre")

    st.markdown("""
    <div class="cricket-card">
        <p class="small-note">FEATURED MATCH • DEMO DISPLAY</p>
        <h2 style="text-align:center">🇵🇰 PAKISTAN</h2>
        <h3 style="text-align:center">VS</h3>
        <h2 style="text-align:center">🇮🇳 INDIA</h2>
        <p class="small-note" style="text-align:center">
            Sample match card — not a live score
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## ⚡ Explore Cricket AI")

    a, b = st.columns(2)

    with a:
        st.markdown("### 🧠 AI Predictions")
        st.write("Explore match-winning probabilities and forecasts.")

        st.markdown("### 🎯 Score Predictor")
        st.write("Estimate innings totals and scoring patterns.")

    with b:
        st.markdown("### 👥 Team Analytics")
        st.write("Study team performance and player statistics.")

        st.markdown("### 📊 Match History")
        st.write("Explore historical T20 cricket data.")

# ---------------- LIVE MATCHES ----------------

elif page == "📡 Live Matches":

    st.title("📡 Live Match Centre")

    st.info(
        "Automatic live score collection is not connected yet. "
        "We will integrate verified score sources in a later stage."
    )

    st.markdown("### Match Information")

    col1, col2 = st.columns(2)

    with col1:
        team1 = st.selectbox(
            "Team 1",
            ["Pakistan", "India", "Australia", "England",
             "South Africa", "New Zealand", "Sri Lanka"]
        )

    with col2:
        team2 = st.selectbox(
            "Team 2",
            ["India", "Pakistan", "England", "Australia",
             "New Zealand", "West Indies", "Bangladesh"]
        )

    st.markdown("### Score Entry")

    col1, col2, col3 = st.columns(3)

    with col1:
        runs = st.number_input("Runs", 0, 300, 36)

    with col2:
        wickets = st.number_input("Wickets", 0, 10, 1)

    with col3:
        overs = st.number_input(
            "Overs",
            min_value=0.0,
            max_value=20.0,
            value=4.0,
            step=0.1
        )

    st.markdown(
        f"<div class='cricket-card'><h2>{team1} vs {team2}</h2>"
        f"<h1>{runs}/{wickets}</h1>"
        f"<p class='small-note'>{overs} overs • Manually entered sample score</p>"
        "</div>",
        unsafe_allow_html=True
    )

# ---------------- AI PREDICTIONS ----------------

elif page == "🧠 AI Predictions":

    st.title("🧠 AI Match Predictions")

    st.info(
        "The machine-learning prediction engine is not connected yet. "
        "No winning probabilities are being presented as real predictions."
    )

    st.markdown("### Prediction Modules")

    st.markdown("""
    - Pre-match winner probability
    - Toss-adjusted winner probability
    - First innings score projection
    - Second innings chase probability
    - Final score probability distribution
    - Player and bowler matchup analysis
    """)

    st.warning("Prediction models will be trained and tested before publication.")

# ---------------- SCORE PREDICTOR ----------------

elif page == "🎯 Score Predictor":

    st.title("🎯 T20 Score Predictor")

    st.caption("Enter a match situation to prepare a score projection.")

    col1, col2 = st.columns(2)

    with col1:
        current_runs = st.number_input("Current runs", 0, 300, 50)

    with col2:
        current_wickets = st.number_input("Wickets lost", 0, 10, 1)

    current_overs = st.number_input(
        "Overs completed",
        min_value=0.0,
        max_value=20.0,
        value=6.0,
        step=0.1
    )

    if st.button("Calculate basic run-rate estimate", type="primary"):

        if current_overs <= 0:
            st.warning("Enter at least one completed over.")
        elif current_overs > 20:
            st.warning("Overs cannot exceed 20.")
        else:
            run_rate = current_runs / current_overs
            remaining = max(0, 20 - current_overs)
            estimate = round(current_runs + run_rate * remaining)

            st.metric("Current Run Rate", f"{run_rate:.2f}")
            st.metric("Basic Score Estimate", estimate)

            st.caption(
                "Simple run-rate extrapolation only — not an AI prediction."
            )

# ---------------- TEAM ANALYTICS ----------------

elif page == "👥 Team Analytics":

    st.title("👥 Team Analytics")

    team = st.selectbox(
        "Select a team",
        ["Pakistan", "India", "Australia", "England",
         "South Africa", "New Zealand", "Sri Lanka",
         "West Indies", "Bangladesh"]
    )

    st.markdown(f"### {team} Performance Centre")

    st.info(
        "Team statistics, player form, batting depth, "
        "bowling resources and matchups will be connected to the database."
    )

    st.markdown("### Planned Analytics")

    st.write("- Recent T20 performance")
    st.write("- Batting and bowling strength")
    st.write("- Powerplay and death-over performance")
    st.write("- Player versus player matchups")
    st.write("- Venue-specific performance")

# ---------------- HISTORY ----------------

elif page == "📊 Match History":

    st.title("📊 Historical Cricket Database")

    st.metric("Matches in Database", "9,181")
    st.metric("Ball-by-ball Deliveries", "2,109,308")

    st.caption("Historical database coverage: 2005–2026")

    st.info(
        "The historical SQLite database will be connected "
        "for tournament, team, player and venue analysis."
    )

    st.markdown("### Planned Filters")

    st.write("- Tournament and season")
    st.write("- Team and opponent")
    st.write("- Venue and match date")
    st.write("- Innings and over-by-over analysis")

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<p style='text-align:center;color:" + muted +
    "'>🏏 CRICKET AI • INTELLIGENCE BEYOND THE SCOREBOARD</p>",
    unsafe_allow_html=True
)
