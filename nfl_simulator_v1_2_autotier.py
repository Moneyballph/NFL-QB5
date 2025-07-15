
import streamlit as st
import math
import matplotlib.pyplot as plt
import itertools
import base64

st.set_page_config(page_title="🏈 Moneyball Phil: NFL Prop Simulator", layout="centered")

def set_background(image_file_path):
    with open(image_file_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
    st.markdown(f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
    ''', unsafe_allow_html=True)

set_background("ChatGPT Image Jul 14, 2025, 09_58_55 AM.png")

st.title("🏈 Moneyball Phil: NFL Prop Simulator (v1.2)")
st.markdown("Simulate **Under 1.5 Passing TDs** and **Alt/Standard Over Passing Yards** props for any QB.")

st.header("📋 Input Player & Matchup Data")
col1, col2 = st.columns(2)
with col1:
    qb_name = st.text_input("Quarterback Name", value="Kenny Picket")
    opponent_team = st.text_input("Opponent Team", value="Texans")

st.subheader("📊 Passing Yards Props")
col3, col4, col5 = st.columns(3)
with col3:
    standard_yds_line = st.number_input("Standard Passing Yards Line", value=210)
with col4:
    odds_over_std = st.number_input("Odds for Over (Standard Line)", value=-115)
with col5:
    odds_under_std = st.number_input("Odds for Under (Standard Line)", value=-105)

col6, col7 = st.columns(2)
with col6:
    alt_yds_line = st.number_input("Alt Over Yards Line", value=199)
with col7:
    odds_alt_over = st.number_input("Odds for Alt Over Line", value=-145)

st.subheader("🎯 Touchdown Props")
col8, col9 = st.columns(2)
with col8:
    td_line = st.number_input("Passing TD Line", value=1.5)
with col9:
    odds_under_tds = st.number_input("Odds for Under TDs", value=100)

st.subheader("📈 QB & Defense Stats")
col10, col11, col12 = st.columns(3)
with col10:
    qb_yards = st.number_input("QB Yards/Game", value=188.0)
with col11:
    qb_td = st.number_input("QB TD/Game", value=0.7)
with col12:
    pass_attempts = st.number_input("Pass Attempts/Game", value=27.6)

col13, col14 = st.columns(2)
with col13:
    def_yds_allowed = st.number_input("Defense Yards Allowed/Game", value=237.0)
with col14:
    def_td_allowed = st.number_input("Defense Pass TDs/Game", value=1.1)

# ✅ Auto-classify Defense Tier
def classify_def_tier(yards_allowed):
    if yards_allowed < 205:
        return "🔴 Tough"
    elif yards_allowed <= 240:
        return "🟡 Average"
    else:
        return "🟢 Easy"

def_pass_rank = classify_def_tier(def_yds_allowed)
st.markdown(f"### 📊 Matchup Risk Tier: **{def_pass_rank}**")
