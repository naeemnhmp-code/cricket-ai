import streamlit as st

st.set_page_config(
    page_title="Cricket AI",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 CRICKET AI")
st.subheader("Live Cricket Intelligence & Prediction System")

st.info("Development version — prediction engine will be connected next.")

st.markdown("---")
st.header("Match Selection")

team1 = st.text_input("Team 1", "Pakistan")
team2 = st.text_input("Team 2", "India")

st.markdown("---")
st.header("Live Match Score")

col1, col2 = st.columns(2)

with col1:
    score = st.number_input("Current Runs", min_value=0, value=36)

with col2:
    wickets = st.number_input("Wickets", min_value=0, max_value=10, value=1)

overs = st.number_input(
    "Overs Completed",
    min_value=0.0,
    max_value=20.0,
    value=4.0,
    step=0.1
)

if st.button("Generate Test Prediction"):
    st.success(f"Match: {team1} vs {team2}")
    st.metric("Current Score", f"{score}/{wickets}")
    st.write(f"Scorecard state: {overs} overs")
    st.warning("Prediction engine is not connected yet.")

st.caption("Cricket AI | Private Development Project")
