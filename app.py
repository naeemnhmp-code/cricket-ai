import streamlit as st

st.set_page_config(page_title="Cricket AI | T20 Intelligence", page_icon="🏏", layout="wide", initial_sidebar_state="expanded")

PAGES = {
    "Home": "🏠",
    "Live Matches": "📡",
    "AI Predictions": "🧠",
    "Score Predictor": "🎯",
    "Team Analytics": "👥",
    "Match History": "📊",
}

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

theme = st.sidebar.radio("Appearance", ["Dark", "Light"], index=0 if st.session_state.theme == "Dark" else 1, horizontal=True)
st.session_state.theme = theme

if theme == "Dark":
    bg, panel, fg, muted, accent, border = "#101B2B", "#1B2A3D", "#F3F6FA", "#B7C3D0", "#35B58A", "#34465B"
else:
    bg, panel, fg, muted, accent, border = "#F3F6FA", "#FFFFFF", "#172638", "#607080", "#087D58", "#D6E0E9"

st.markdown(f"""
<style>
.stApp {{ background: {bg}; color: {fg}; }}
[data-testid="stHeader"] {{ background: {bg}; }}
h1,h2,h3,h4,p,label,span {{ color: {fg}; }}
[data-testid="stSidebar"] {{ background: {panel}; }}
.brand-subtitle {{ color: {muted}; letter-spacing: 1.5px; }}
.home-card {{ background: {panel}; border: 1px solid {border}; border-radius: 15px; padding: 17px 16px; min-height: 112px; margin-bottom: 7px; }}
.home-card-icon {{ font-size: 27px; margin-bottom: 5px; }}
.home-card-title {{ font-size: 18px; font-weight: 700; }}
.home-card-desc {{ color: {muted}; font-size: 12px; margin-top: 5px; }}
div.stButton > button {{ border-radius: 12px; border: 1px solid {border}; min-height: 48px; font-weight: 650; }}
div[data-testid="stMetric"] {{ background: {panel}; border: 1px solid {border}; border-radius: 13px; padding: 13px; }}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🏏 CRICKET AI")
st.sidebar.caption("T20 INTELLIGENCE CENTRE")
st.sidebar.divider()
st.sidebar.markdown("### Navigation")
for page, emoji in PAGES.items():
    if st.sidebar.button(f"{emoji}  {page}", key=f"side_{page}", use_container_width=True, type="primary" if st.session_state.page == page else "secondary"):
        st.session_state.page = page
        st.rerun()
st.sidebar.divider()
st.sidebar.caption("Private testing version")

st.markdown("# 🏏 CRICKET AI")
st.markdown('<p class="brand-subtitle">T20 INTELLIGENCE • LIVE MATCHES • AI PREDICTIONS</p>', unsafe_allow_html=True)
st.divider()

def go_to(page):
    st.session_state.page = page
    st.rerun()

def show_home():
    st.title("Cricket Intelligence Centre")
    st.caption("Your central destination for T20 cricket intelligence.")
    a, b, c = st.columns(3)
    a.metric("Historical Matches", "9,181")
    b.metric("Ball-by-ball Records", "2.1M+")
    c.metric("AI Engine", "In Development")
    st.markdown("## Explore Cricket AI")
    descriptions = {
        "Home": "Your main dashboard",
        "Live Matches": "Find ongoing T20 matches",
        "AI Predictions": "Match and innings predictions",
        "Score Predictor": "Estimate the final innings score",
        "Team Analytics": "Team and player performance",
        "Match History": "Explore historical T20 data",
    }
    pages = list(PAGES.keys())
    for start in (0, 3):
        cols = st.columns(3)
        for col, page in zip(cols, pages[start:start+3]):
            with col:
                st.markdown(f'<div class="home-card"><div class="home-card-icon">{PAGES[page]}</div><div class="home-card-title">{page}</div><div class="home-card-desc">{descriptions[page]}</div></div>', unsafe_allow_html=True)
                if st.button(f"Open {page}", key=f"card_{page}", use_container_width=True, disabled=(page == "Home")):
                    go_to(page)
    st.info("Live score feeds and trained prediction models are not connected yet. This version does not display invented live matches or unverified predictions.")

def show_live():
    st.title("📡 Live Match Centre")
    st.caption("Find and select ongoing T20 matches.")
    st.warning("Live data is not connected yet. No sample fixtures are being shown as real matches.")
    st.write("- Automatic discovery of ongoing T20 matches")
    st.write("- Multiple score sources and freshness checks")
    st.write("- Automatic score and timestamp updates")
    st.write("- Match selection by tournament and teams")

def show_predictions():
    st.title("🧠 AI Prediction Centre")
    st.info("Predictions will be enabled after the historical model is trained, tested on later matches, and connected to verified match data.")
    st.write("- Pre-match and toss-adjusted winner probability")
    st.write("- First-innings final score prediction")
    st.write("- Second-innings chase probability")
    st.write("- Prediction confidence and model evaluation")

def show_score():
    st.title("🎯 T20 Final Score Predictor")
    st.markdown("### Automatic match-based prediction")
    st.write("The intended workflow is: choose a live match → Cricket AI retrieves the latest score automatically → the model estimates the final score. You will not need to type runs, wickets, or overs.")
    st.warning("Automatic match selection will appear after a reliable live score feed and the first validated prediction model are connected.")
    st.write("- Expected final score and likely range")
    st.write("- Projected score at 6, 10, 15 and 20 overs")
    st.write("- Expected runs in the remaining overs")
    st.caption("Every future prediction will display the score state and update time used.")

def show_teams():
    st.title("👥 Team & Player Analytics")
    team = st.selectbox("Explore a team", ["Pakistan", "India", "Australia", "England", "South Africa", "New Zealand", "Sri Lanka", "West Indies", "Bangladesh"])
    st.subheader(f"{team} Analytics Centre")
    st.info("Detailed analytics will be connected to the historical database.")
    st.write("- Recent team form")
    st.write("- Batting and bowling strength")
    st.write("- Player matchups")
    st.write("- Powerplay and death-over records")
    st.write("- Venue-specific performance")

def show_history():
    st.title("📊 Historical T20 Database")
    a, b = st.columns(2)
    a.metric("Matches collected", "9,181")
    b.metric("Ball-by-ball records", "2,109,308")
    st.caption("Database coverage: 17 February 2005 – 1 November 2026")
    st.info("The historical database will be connected for detailed analysis.")
    st.write("- Tournament and season filters")
    st.write("- Team and opponent records")
    st.write("- Venue statistics")
    st.write("- Innings and over-by-over analysis")

page = st.session_state.page
if page == "Home":
    show_home()
elif page == "Live Matches":
    show_live()
elif page == "AI Predictions":
    show_predictions()
elif page == "Score Predictor":
    show_score()
elif page == "Team Analytics":
    show_teams()
elif page == "Match History":
    show_history()

st.divider()
st.markdown("<div style='text-align:center'>🏏 CRICKET AI | INTELLIGENCE BEYOND THE SCOREBOARD</div>", unsafe_allow_html=True)
    
